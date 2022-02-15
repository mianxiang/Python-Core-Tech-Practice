from importlib.resources import files
from msilib.schema import File
import os.path

teststr = '2.9 Definition'


with open('test.txt', 'r', encoding='UTF-8') as fread:
    if teststr in fread.readlines():
        print('{} exists in this document'.format(teststr))
    else:
        print('{} does not exists in this document'.format(teststr))