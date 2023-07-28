from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('C:\\Users') if isfile(join('C:\\Users', f))]
