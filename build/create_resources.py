import sys

from .guideline.guideline import Guideline

if __name__ == '__main__':
    dirname = sys.argv[1]
    print("Creating guideline: "+dirname)
    gl = Guideline.create(dirname)
    gl.create_resources()