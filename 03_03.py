import shutil

def copy_file():
    '''copy file from location to another location. It copies only file's content and permissions'''
    shutil.copy('artwork/PNG/monster01.png', 'output')
    
def copy_file_metadata():
    '''copies file's content and permissions as well as metadata such as creation time etc'''   
    shutil.copy2('artwork/PNG/monster01_tn.png', 'output')
    
def copy_directory():
    '''copy complete directory with files. Note that destination direcotry cannot exist'''
    shutil.copytree('artwork/PNG/', 'backup/')        
    
    
if __name__ == "__main__":
    copy_file()
    copy_file_metadata()
    copy_directory()