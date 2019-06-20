'''
the headers for each CSV file can be read about here:
https://github.com/chadwickbureau/baseballdatabank/blob/master/core/readme2014.txt
'''
from os import path, getcwd
import logging
from pandas import DataFrame, read_csv

class BaseballDataFrame(DataFrame):

    @staticmethod
    def _create_df(filename):
        filename = getcwd() + '/baseball-data/core/' + filename
        if not path.exists(filename):
            raise RuntimeError('file "{}" does not exist'.format(filename))
        return read_csv(filename)

    def __init__(self, filename):
        DataFrame.__init__(self, data=BaseballDataFrame._create_df(filename))
        self.filepath = getcwd() + '/baseball-data/core/' + filename

    
if __name__ == '__main__':
    d = BaseballDataFrame('Batting.csv')
    print(d.head())
