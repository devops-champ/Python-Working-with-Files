import tempfile


def create_temp_file():
    '''
    create a temp file in the memory. The temp file is automatically deleted once the file is closed.
    '''
    with tempfile.TemporaryFile('w+') as tf:
        tf.write('hellp world python')
        tf.seek(0)
        print(tf.read())
        print(tempfile.gettempdir())
        
        
        
if __name__ == "__main__":
    
    create_temp_file()
        
        