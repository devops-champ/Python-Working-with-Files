import json

def generate_dict(id_num, department, name, title):
    '''
    converts the data into dictionary object
    '''
    return {'id_num': id_num, 'department': department, 'name': name, 'title': title}

def dict_to_json(dict_data):
    '''
    write dict objects into json file
    '''
    with open('dict-to-json.json', 'w', encoding='utf-8') as f:
        json.dump(dict_data, f)
    


if __name__ == "__main__":
    employee1 = generate_dict('234', 'sales', 'darshan', 'sales engineer')
    employee2 = generate_dict('456', 'marketing', 'vivek', 'marketing manager')
    dict_to_json([employee1, employee2])