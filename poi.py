import pickle

import os
#how many poi exist?


poi_names = open("../final_project/poi_names.txt", 'rb')
fr=poi_names.readlines()
length=len(fr[2:])
print(length)
poi_names.close()

# print poi_names.read()

