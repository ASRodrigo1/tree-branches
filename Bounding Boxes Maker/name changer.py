"OpenCV was not working with images containing ' ' and '´'"
"So i had to modify the images names"
import os

path = 'C://Users//Rodrigo//Documents//Project//trees//images//tree-branches'

images = os.listdir(path)

for name in images:
    name1 = name
    name1 = name1.replace(' ', '')
    name1 = name1.replace('á', 'a')
    print(name + " " + name1)
    os.rename(path + '//' + name, path + '//' + name1)
    
