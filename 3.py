
import glob
import os

os.chdir('C:\ProgramData\Jenkins\.jenkins\workspace\Demo3')
my_files = glob.glob('*.py')
print(my_files)
    
