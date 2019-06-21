from baseball_dataframe import BaseballDataFrame

class PeopleDataFrame(BaseballDataFrame):

    def __init__(self):
        super().__init__('people.csv')
        print(super().memory_usage())
        self['birthYear'] = self['birthYear'].fillna(value=0).astype('int')
        self['birthMonth'] = self['birthMonth'].fillna(value=0).astype('int')
        self['birthDay'] = self['birthDay'].fillna(value=0).astype('int')
        self['birthCountry'] = self['birthCountry'].fillna(value='Unknown').astype('category')
        print(super().memory_usage())


if __name__ == '__main__':
    p = PeopleDataFrame()
    print(p.head())