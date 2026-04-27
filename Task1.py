import os
import shutil
import functools

from pathlib import Path
from sys import argv as args, exit

def io_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IOError as e:
            print(f'Error reading or writing {e.filename}')
    return wrapper

@io_decorator
def recursive_copy(source: Path, dest: Path):
    if(source.name.startswith('.') or source == dest): return 
    if source.is_dir():
        for p in source.iterdir():
            recursive_copy(p, dest)
    else:
        _, extension = os.path.splitext(source.name)
        destination = Path(dest/extension[1:])

        if not destination.exists():
            os.makedirs(destination)
        
        print(f'Copying from {source} to {destination}')
        shutil.copy(source.absolute(), Path(destination/source.name))


def main(source, dest):
    DEFAULT_DEST = './dest'
    if dest == None:
        dest = DEFAULT_DEST
    recursive_copy(Path(source), Path(dest))

if __name__ == '__main__':
    source = ''
    dest = ''
    if len(args) == 1:
        print("Usage: Task1.py {source_folder} {destination_folder}")
        exit(-1)
    elif len(args) > 1:
        source = args[1]
    if len(args) > 2:
        dest = args[2]
    print(args)
    main(source, dest)