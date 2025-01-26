def open_file():
    '''
    without with statement to open a file
    '''
    file = open('sample.txt', 'r', encoding="utf=8")
    content = file.read()
    print(content)
    file.close()


def open_file_with():
    '''
    using with statment to open a file
    '''
    with open('sample.txt', 'r', encoding="utf=8") as r:
        content = r.read()
        print(content)
        

#unmanaged stream or resource
        
def write_to_file():
    '''
    write to a file ie replace the existing text with new text'''
    with open('spell.txt', 'w', encoding="utf=8") as w:
        w.write("Devops Margadarshan")      
        
        
if __name__ == "__main__":
    #open_file()
    write_to_file() 