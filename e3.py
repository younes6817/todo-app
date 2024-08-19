import glob

my_files = glob.glob(".venv/date/*.txt")

for file_name in my_files:
    with open(file_name, "r") as file:
        print(file.read())
        file.close()
