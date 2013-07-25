from os.path import splitext
from glob import glob
from PIL import Image
from sys import argv

folder, width, height, addname = argv[1], int(argv[2]), int(argv[3]), argv[4]

for f in glob("%s/*.*" % folder):
	i, n = Image.open(f), splitext(f)
	s, (w, h) = (width, height), i.size

	if h > w:
		s = (height, width)

	i.resize(s, Image.ANTIALIAS).save("%s%s%s" % (n[0], addname, n[1]))