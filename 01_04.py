import glob

def display_pngs():
    for file in glob.glob('**/*.png', recursive=True):
        print(file)

    


if __name__ == "__main__":
   display_pngs()