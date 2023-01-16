import sys

from .guideline import Guideline

if __name__ == '__main__':
    dirname = sys.argv[1]
    gl = Guideline.create(dirname)
    gl.create_resources()