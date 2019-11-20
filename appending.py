import os

dir_name = "bbox_txt/" # Edit as needed


for parent, dirnames, filenames in os.walk(dir_name): 
    for fn in filenames:
        #print(fn)
        f = open(os.path.join(parent, fn), 'a')
        f.write("0 0.5355 0.5583333333333333 0.065 0.02")
        f.close()
#with open(fn, 'a') as f:
        #    f.write("0 0.536 0.545 0.062 0.02")
