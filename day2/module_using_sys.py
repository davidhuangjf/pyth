# __author : david
# date:  2018/10/14
__version__='0.1'

import sys,os

print('The commaU) nd line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nTHe PYTHONPATH is',sys.path)
for i in sys.path:
    print(i)
print(os.getcwd())