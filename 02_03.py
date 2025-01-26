import json

def json_operation():
    '''
    fetch the json data based on key.
    '''
    with open("file.json", encoding="utf=8") as f:
        content_json = json.load(f)
        #formatted_json = json.dumps(content_json, sort_keys=True, indent=4)
        
        for item in content_json['content']:
            title = item.get('title', [])
            table_contents = item.get('values', [])
            
            print(title)
            print(json.dumps(table_contents, indent=4))

def load_json():
    '''
    load a json file
    '''
    with open("monster.json", encoding="utf=8") as f:
        json_con = json.load(f)
        print(json_con['monsterName'])


if __name__ == "__main__":
    json_operation()
    load_json()