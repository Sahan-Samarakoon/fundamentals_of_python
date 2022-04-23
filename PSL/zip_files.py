from pathlib import Path
from zipfile import ZipFile

zip = ZipFile('files.zip', 'w')  # creates the given file in our current folder
# 'w' indicates that we want to write to the zip file
zip.close()

# or
with ZipFile('files.zip', 'w') as zip:
    for path in Path('PSL').rglob('*.*'):
        zip.write(path)

# open for reading
with ZipFile('files.zip') as zip:
    print(zip.namelist())  # retunrs a list of all files in the zip file
    info = zip.getinfo('PSL\\directories.py')  # returns info object
    print(info.file_size)
    print(info.compress_size)
    # can specify a directory to extract files into
    zip.extractall('ecommerce')
    # the relevant directory will be created if it is not there
