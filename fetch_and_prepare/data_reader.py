from os import path, getcwd
import csv

class DataReader():
    path = getcwd() + '/baseball-data/core/'
    def __init__(self, filename):
        self.path = ''
