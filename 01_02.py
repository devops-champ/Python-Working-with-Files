import os

def display_cwd():
    '''
    display the current working directory
    '''
    cwd = os.getcwd()
    print("The current working directory is", cwd)
    
# def previous_dir():
#     '''
#     Changes the current working directory to the parent directory.
#     '''
#     os.chdir("../") # it just changes the current working directory, but doesn't print it.


def get_list_of_files(directory):
    '''
    get the list of files in a directory
    '''
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)
    
if __name__ == "__main__":
    display_cwd()
    # previous_dir()
    display_cwd()
    get_list_of_files("images/")