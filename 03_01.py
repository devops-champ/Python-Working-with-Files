

def write_to_file():
    '''
    write to a file using .write method
    '''
    with open('num.txt', 'w', encoding='utf-8') as w:
        for i in range(0,51):
            values = f'{i}\n' #converting the int to string using formatted string
            w.write(values)
            
def append_content():
    '''
    append the content
    '''
    with open('num.txt', 'a', encoding='utf-8') as w:
        for i in range(58,79):
            values = f'{i}\n' #converting the int to string using f-string
            w.write(values)               
            

if __name__ == "__main__":
    write_to_file() 
    append_content()                      