from os import walk

def GetChar(path):
    files= []
    for _,__,images in walk(path):
        for image in images:
            dir = path +'\\'+ image
            files.append(dir)
    return files
