import sys

from . import guideline

if __name__ == '__main__':
    dirname = sys.argv[1]
    guideline.create(dirname).create_resources()