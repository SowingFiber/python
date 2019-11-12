import glob2
from datetime import datetime

# find three files, in the filse directory
files = glob2.glob('files/*.txt')
print(files)

# write a new file with current timestamp and combine contents from all files
filepath = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"
with open(filepath, 'w') as newfile:
    for file in files:
        with open(file) as content:
            newfile.write(content.read() + '\n')
