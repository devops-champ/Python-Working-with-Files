import zipfile


def read_zip_contents():
    '''
    read the zip file contents as a list
    '''
    with zipfile.ZipFile('archive_files.zip', 'r') as read:
        print(read.namelist())
        

def zip_file_information_all_files():
    '''
    get more information about all the zipped files
    '''
    with zipfile.ZipFile('archive_files.zip', 'r') as read:
        for file_name in read.namelist():
            file_info = read.getinfo(file_name)
            print(file_info)


def zip_file_information():
    '''
    get more infromation about a zip file
    '''
    with zipfile.ZipFile('archive_files.zip', 'r') as read:
        file_info = read.getinfo('value.dita')
        print(file_info)                

def read_zip_file():
    '''
    read a zip file
    '''
    with zipfile.ZipFile('archive_files.zip', 'r') as read:
        with read.open('value.dita') as file:
            print(file.read())
            
            
def extract_all():            
    '''
    extract all the zip files
    '''
    with zipfile.ZipFile('archive_files.zip', 'r') as read:
        read.extractall("extracted")
        
        
if __name__ == "__main__":
    #read_zip() 
    #zip_file_information()
    #read_zip_file()  
    extract_all()    