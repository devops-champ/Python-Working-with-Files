import os
from pathlib import Path
import shutil


def rename_file_os():
    '''Rename the file name using os.rename'''
    os.rename('images/monster01.png', 'images/god01.png')
    
    

    
def rename_file_pathlib():
    '''Rename the file using pathlib module'''
    file = Path('images/monster02.png')
    file.rename('images/god02.png')
    
def move_files():
    '''Move single file or all files in a folder using shutil module'''
    shutil.move('images/', '/pn')
        
    
    
if __name__ == "__main__":
    rename_file_os()
    rename_file_pathlib()    