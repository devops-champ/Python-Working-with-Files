import os

def list_all_files_in_dir():
    '''
    os.walk module will recursively list all files in a directory
    '''
    for dirpath, dirnames, filename in os.walk('artwork/'):
        print("Directory:", dirpath)
        
        print("Includes these directories:")
        for dirname in dirnames:
            print(dirname)
                  
                  
        print("Includes these files:")    
        for file in filename:
            print(file)    





if __name__ == '__main__':
    list_all_files_in_dir()