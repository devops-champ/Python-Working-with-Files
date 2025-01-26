import shutil
import zipfile

def create_zip_shutil(dir_path):
    '''
    zip nested files and folders using shutil library
    '''
    shutil.make_archive('archive', 'zip', dir_path)
    
def create_zip_of_files(files_list):
    '''
    create zip of individual files
    '''
    with zipfile.ZipFile('archive_files.zip', 'w') as archive:
        for f in files_list:
            archive.write(f)
            
    
if __name__ == "__main__":
    #create_zip_shutil('Nutanix.pdf')
    files_list = ['object.txt', 'num.txt']
    create_zip_of_files(files_list)