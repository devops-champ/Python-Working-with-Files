import csv


def load_csv():
    '''
    read a .csv file. It will print all the monsters name
    '''
    with open('monsters.csv', encoding='utf-8') as f:
        read = csv.reader(f, delimiter=',')
        for row in read:
            print(row)


def load_csv_dictreader():
    '''
    here we use dictReader attribute
    '''
    with open('monsters.csv', encoding='utf-8') as f:
        dictreader = csv.DictReader(f, delimiter=',')
        
        for row in dictreader:
            print(row["monsterName"] + "is priced at " + row["price"])
            
            
if __name__ == "__main__":
    load_csv()
    load_csv_dictreader()           