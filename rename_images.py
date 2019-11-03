import os

#for dirname in os.listdir("images/"):
dirname = "images/"
if os.path.isdir(dirname):
    idx = 275
    for i, filename in enumerate(os.listdir(dirname)):
        #if filename.endswith(".bmp"):
        os.rename(dirname + "/" + filename, dirname + "/" + "{:04d}".format(idx) + ".jpg")
        idx += 1
