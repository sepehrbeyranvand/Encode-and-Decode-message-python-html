from stegano import lsb
secret = lsb.hide("Iran.png", "SepehrBeiranvand!")
secret.save("Name.png")