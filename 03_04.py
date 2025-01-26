import os
from pathlib import Path
import shutil

def delete_file():
    '''
    delete a file using os module
    '''
    os.remove('backup/monster01.png')
    
def delete_using_pathlib():
    '''
    delete using pathlib module
    '''
    folder = Path('backup/monster02.png')
    folder.unlink()
    
def delete_dir():
    '''
    delete an empty directory. Ensure that directory empty. Orelse it will throw an error
    '''
    os.rmdir('logs/')
    
    
def delete_dir_using_patlib():
    '''
    delete an empty directory using pathlib. Ensure that directory empty. Orelse it will throw an error
    '''
    del_folder = Path('logs/')
    del_folder.rmdir()  
            
def delete_dir_and_contents():
    '''
    delete a directory even when it's not empty.
    '''
    shutil.rmtree('output/')
    





#if __name__ == "__main__":
    #delete_file()
    #delete_using_pathlib()
    #delete_dir()
    #delete_dir_using_patlib()
    #delete_dir_and_contents()