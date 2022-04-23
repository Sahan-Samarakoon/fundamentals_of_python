from pathlib import Path

path = Path('PSL')
print(path.exists())
path.mkdir()
path.rmdir()
path = path.rename('Psl')

# returns a generator object of all files and diretories in this path
print(path.iterdir())
for x in path.iterdir():
    print(x)

# if there's no million files, convert to list
path_list = [x for x in path.iterdir() if x.is_dir()]
print(path_list)

# searching by a pattern
path.glob('*.*')  # search for all files: returns a generator object
py_files = [x for x in path.glob('*.py')]

# search recursively
path.glob('**/*.py')
# returns all python files in child folders as well
all_files = [x for x in path.rglob('*.py')]
