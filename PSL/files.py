from pathlib import Path
import shutil

path = Path('PSL\\path.py')
print(path.exists())
path.rename('paths.py')
path.unlink()  # deletes file
print(path.stat())  # in book

path.read_bytes()  # returns content of file as a bytes object for representing binary data
path.read_text()  # returns the content of file as a string

# above method is easier than below as they take care of opening and closing the file
with open('PSL\\path.py') as file:
    pass

path.write_bytes()
path.write_text()

# do not use path objects to copy a file
source = Path('PSL\\path.py')
target = Path('help.py')
target.write_text(source.read_text())

# instead, do this
shutil.copy(source, target)
