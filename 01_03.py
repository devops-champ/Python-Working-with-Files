from datetime import datetime, timezone
import os


def format_datetime(timestamp):
    utc_timestamp = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    formated_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formated_date

def file_creation(directory):
    '''
    when the file was created
    '''
    with os.scandir(directory) as entries:
        for entry in entries:
            print("Name: ", entry.name)
            info = entry.stat()
            print("creation time: ", format_datetime(info.st_birthtime))
            
def last_accessed(directory):
    '''
    when the file was last accessed
    '''
    with os.scandir(directory) as entries:
        for entry in entries:
            print("Name: ", entry.name)
            info = entry.stat()
            print("last accesses time: ", format_datetime(info.st_atime))
            
def file_size(directory):
    '''
    size of the file
    '''
    with os.scandir(directory) as entries:
        for entry in entries:
            print("Name: ", entry.name)
            info = entry.stat()
            print("file size: ", info.st_size)
            
def display_directory(directory):
    '''
    display the directory
    '''
    
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print("Direcotry name: ", entry.name)


def display_file(directory):
    '''
    display the files
    '''
    
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print("File name: ", entry.name)                                


if __name__ == "__main__":
    file_creation("images/")
    print("- - - - - - -")
    last_accessed("images/")
    print("- - - - - - -")
    file_size("artwork/")
    print("- - - - - - -")
    display_directory("artwork/")
    print("- - - - - - -") 
    display_file("artwork/")   
    
    