from sys import argv
from os import rename
from glob import glob
from os.path import splitext

for i, f in enumerate(glob("%s/*.*" % argv[1])):
	rename(f, "%s/%d%s" % (argv[1], i + 1, splitext(f)[1]))