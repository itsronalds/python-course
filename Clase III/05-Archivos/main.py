import os
from pathlib import Path

# read all the file
# print(file.read())

# print(Path.cwd())
# print(Path.home())

# print(os.path.dirname(__file__))

dirname = os.path.dirname(__file__)

file = open(f'{dirname}/text.txt', 'r')

# read all the file
# print(file.read())

print('-------------------')

# read line by line
# print(file.readline())
# print(file.readline())

print('-------------------')

# close the file
# file.close()

print('-------------------')

# Iterate file with for loop

# for line in file:
#     print(line)

file.close()

print('-------------------')

# Auto close file with with
with open(f'{dirname}/text.txt', 'a', encoding='utf-8') as file:
    file.write('Hello World')
