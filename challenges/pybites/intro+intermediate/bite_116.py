"""
Bite 116. List and filter files in a directory 

https://codechalleng.es/bites/116
"""
import os
from tempfile import TemporaryDirectory

ONE_KB = 1024


def get_files_list(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    big_enough_files = []
    dir_entries = os.scandir(dirname)
    for de in dir_entries:
        if not de.is_dir():
            stat = de.stat()
            if stat.st_size >= size_in_kb * ONE_KB:
                big_enough_files.append(de.name)
    return big_enough_files
        
                

def get_files(dirname, size_in_kb):
    """Generate files in dirname that are >= size_in_kb"""
    dir_entries = os.scandir(dirname)
    for de in dir_entries:
        if not de.is_dir():
            stat = de.stat()
            if stat.st_size >= size_in_kb * ONE_KB:
                yield de.name

import pytest


TMP = '/tmp'


def _create_files(dirname):
    for i in range(1, 4):
        for j in range(1, 11):
            file_size = i * j * ONE_KB
            filename = f'{file_size}.txt'
            path = os.path.join(dirname, filename)
            _create_file(path, file_size)


def _create_file(path, size):
    with open(path, 'wb') as f:
        f.write(os.urandom(size))


@pytest.mark.parametrize("size", [
    1, 3, 6, 9, 12, 20, 25,
])
def test_get_files(size):
    with TemporaryDirectory(dir=TMP) as dirname:
        test_size_in_kb = size * ONE_KB
        _create_files(dirname)

        files = list(get_files(dirname, test_size_in_kb))
        filenames = [os.path.splitext(os.path.basename(f))[0] for f in files]

        assert all(int(fn) >= test_size_in_kb for fn in filenames)


    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          