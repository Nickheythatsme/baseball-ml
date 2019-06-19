'''
the headers for each CSV file can be read about here:
https://github.com/chadwickbureau/baseballdatabank/blob/master/core/readme2014.txt
'''
from os import path, getcwd
import csv

class DataReader():
    default_path = getcwd() + '/baseball-data/core/'
    def __init__(self, filename):
        self.filepath = DataReader.default_path + filename
        self.headers()
    
    def headers(self):
        if not path.exists(self.filepath):
            raise RuntimeError('file does not exist: ' + self.filepath)
        with open(self.filepath, 'r') as fin:
            return fin.readline().replace('\n', '').split(',')

    
if __name__ == '__main__':
    d = DataReader('Teams.csv')