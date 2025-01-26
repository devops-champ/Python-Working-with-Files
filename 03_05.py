import csv
# import openpyxl


def write_csv():
    with open('protocols','w', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Category", "Name", "Quantity", "Price"])
        writer.writerow(["69", "Kitchen", "Spoon", "30", "10"])


# def read_and_write_csv():
#     '''
#     read excel file and tranform it into csv using openpyxl
#     '''
#     workbook = openpyxl.load_workbook('list.xlsx')
#     sheet = workbook.active
    
#     with open('book','w', encoding="utf-8") as file:
#         writer = csv.writer(file)
        
        
#         for row in sheet.iter_rows(values_only=True):
#             writer.writerow(row)


def write_csv_dict():
    '''
    if your data is stroed as dic, csv module provides DictWriter method to write it out to csv
    '''
    with open('dict-to-csv.csv', 'w', encoding='utf-8') as f: #f is the file object here
        headers = ['first_name', 'last_name']
        values = csv.DictWriter(f, fieldnames=headers)
        
         #this method writes the headers row in the csv file using the fieldname
        values.writeheader()
        
        values.writerow({'first_name': 'darshan', 'last_name': 'thugadeep'})
        values.writerow({'first_name': 'Kichha', 'last_name': 'sudeep'})

        
if __name__ == '__main__':
    #write_csv()
    write_csv_dict()



   