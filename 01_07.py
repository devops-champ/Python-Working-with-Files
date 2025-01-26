import os

from pathlib import Path

def create_dir():
    '''
    create a directory in the absolute path using os module
    '''
    
    try:
        os.mkdir("logs/")
    except FileExistsError:
        print("Logs directory already exists")     


def make_dir():
    '''
    create a directory using Pathlib module
    '''
    
    dir_path = Path("output/")
    # instead of using try expect block we can make use of path module with exisit_ok parameter.
    dir_path.mkdir(exist_ok=True)
       

if __name__ == "__main__":
    create_dir()
    make_dir() 
    
    
    