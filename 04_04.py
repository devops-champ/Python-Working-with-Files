import tarfile


def create_tar():
    '''
    create a tar achieve using files and folders
    '''
    with tarfile.open('python_tar.gz', 'w:gz') as tar:
        for file in ['backup/']: #specify a file or folder
            tar.add(file)
            

def append_tar():
    '''
    append a file to a tar archive
    '''
    with tarfile.open('python_tar.gz', 'w:gz') as tar:
        tar.add('list.xlsx')          
            


def extract_tar():
    '''
    extract all file from tar archive
    '''  
    with tarfile.open('python_tar.gz', 'w:gz') as tar:
        tar.extractall('extracted_from_python')          
            
if __name__ == "__main__":
    #create_tar()
    #append_tar()
    extract_tar()          