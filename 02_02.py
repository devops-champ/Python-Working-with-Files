def display_as_list():
    with open("spell.txt", encoding="utf-8") as r:
        line = r.readlines()
        print(line)
        
def display_one_line():
    with open("spell.txt", encoding="utf-8") as r:
        line_value = r.readline()
        print(line_value)
        # while line_value != '':
        #     print(line_value)
        #     line_value = r.readline()      
        
if __name__ == "__main__":
    #display_as_list()
    display_one_line()     