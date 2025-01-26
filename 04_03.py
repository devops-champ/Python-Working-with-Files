import tarfile


def read_tarfile():
    '''
    read contents of tar archive.
    '''
    
    #compression modes for tar:
    # gz for gzip compression
    # bz for bzip2 compression
    # xz for lzma compression 
    with tarfile.open('archive.tar.gz', 'r:gz') as tar:
        print(tar.getnames())
        #get infromation about a specific file
        files = tar.getmember('descriptions/description01.txt')
        print(files.name)
        print(files.size)
        print(files.mode)
        
        #get infromation about all files using for loop
        for i in tar.getmembers():
            print(i.name)
            print(i.mode)
            print(i.size)
        
def access_content_tar_file():
    '''
    read the file that are inside the tar archive
    '''
    with tarfile.open('archive.tar.gz', 'r:gz') as tar:
        #extract file will only extact the file for reading and writing. It will not extract the file permanently
        with tar.extractfile('descriptions/description02.txt') as file:
            print(file.read())       
        
if __name__ == "__main__":
    #read_tarfile()
    access_content_tar_file()        