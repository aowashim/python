import random

with open('test_image.jpg','rb') as img1:
    f1 = img1.read()
    #print(f1)
    byte_list = list(bytearray(f1))
    #print(byte_list)

with open('copy_test_image.jpg','wb') as img2:
    for i in range(len(byte_list)):
        img2.write(byte_list[i].to_bytes(1,'big'))

with open('copy_test_image.jpg','rb') as img2:
    f2 = img2.read()
    #print(f2)


new_byte_list = [((bt * random.randint(0,9)) % 255) for bt in byte_list]
#print(new_byte_list)

for i in range(400):
    new_byte_list[i] = byte_list[i]

with open('modified_test_image.jpg','wb') as img3:
    for i in range(len(new_byte_list)):
        img3.write(new_byte_list[i].to_bytes(1,'big'))

with open('modified_test_image.jpg','rb') as img3:
    f3 = img3.read()
    #print(f3)