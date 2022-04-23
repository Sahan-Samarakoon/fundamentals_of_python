from pathlib import Path

path = Path()
print(path.parent)  # gives relative value
print(path.absolute())  # gives absolute value of path


path0 = Path(r'c:\Users\monika\Code')
path = Path() / 'work.py'
path2 = Path() / Path('work.py')
path1 = Path()  # represents pwd: the directory that contains the file
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)  # shows what is at the end of it
print(path.stem)
print(path.suffix)
print(path.parent)  # the path without the 'name'(gives parent folder)

path = path.with_name('worky.py')
path = path.with_suffix('.txt')
