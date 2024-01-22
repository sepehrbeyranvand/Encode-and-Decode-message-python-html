from stegano import lsb #Import stegano library
secret = lsb.hide("Iran.png", "SepehrBeiranvand!") #choose your image and your text
secret.save("Name.png") #set a name or your new image file which contains a secret message

#SepehrBeiranvand
#https://www.sepehrbey.ir