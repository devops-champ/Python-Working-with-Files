from pathlib import Path

#it provides oops interface to the file system

def dir_contents():
    
    entries = Path.cwd()
    #entries = Path("artwork/")
    for entry in entries.iterdir():
        print(entry.name)
        print(entry.parent)
        print(entry.parent.parent)
        print(entry.stem)
        print(entry.suffix)
        print(entry.stat())
        print()
    


if __name__ == "__main__":
   dir_contents()     
    
    
