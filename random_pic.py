from os import listdir
from os.path import isfile, join
import random

def getRandomPic(directory) :
    allFiles = [f for f in listdir(directory) if isfile(directory + "//" + f) and f.endswith(('.jpg', '.png'))]
    file = directory + "//" + random.choice(allFiles)
    return file

def getRandomCat() :
    return getRandomPic("cats")

def getRandomLeague() :
    return getRandomPic("league")

#x = getRandomCat()
#print(x)
