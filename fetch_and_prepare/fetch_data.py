from requests import get
from zipfile import ZipFile, BadZipFile
import logging
from os import path, rename, remove

class FetchData():
    # from http://www.seanlahman.com/baseball-archive/statistics/
    download_url = 'https://github.com/chadwickbureau/baseballdatabank/archive/v2019.2.zip'

    def __init__(self, url=download_url, output_dir='baseball-data'):
        self.zip_path = output_dir + '.zip'
        self.output_dir = output_dir
        self.url = url 
        self.logger = logging.getLogger('FetchData')

        self._download()
        self._unzip()

    def _download(self):
        if path.exists(self.zip_path):
            return
        with open(self.zip_path, 'wb') as zipfile:
            r = get(self.url, stream=True)
            if 'content-length' in r.headers:
                filesize = float(r.headers['content-length'])/1000000
            else:
                filesize = 0
            current_filesize = 0.0
            self.logger.info('starting zipfile download: {:2.2} MB'.format(filesize))
            if r.status_code >= 300 or r.status_code < 200:
                self.logger.error('Got bad status code ({}) from url: {} '.format(
                        str(r.status_code), self.url))
                raise RuntimeError('Got bad status code: ' + str(r.status_code))
            for chunk in r.iter_content(chunk_size=512):
                progress = (current_filesize/filesize) * 100
                print('{:8.2f}%       '.format(progress), end='\r')
                current_filesize += (zipfile.write(chunk) / 1000000)
            self.logger.info('finished downloading file: {}'.format(self.zip_path))
    
    def _unzip(self):
        if path.exists(self.output_dir):
            return
        if not path.exists(self.zip_path):
            raise RuntimeError('Zip file ({}) does not exist.'.format(self.zip_path))
        try:
            with ZipFile(self.zip_path, 'r') as zip_file:
                unzip_path = zip_file.namelist()[0]
                zip_file.extractall()
                rename(unzip_path, self.output_dir)
        except BadZipFile:
            self.logger.error('Bad zip file. Redownloading file.')
            remove(self.zip_path)
            self._download()
            self._unzip()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    f = FetchData()
