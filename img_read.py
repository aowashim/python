# with open('watch.jpg','rb') as f:
    # rd1 = f.read()
    # btList = list(rd1)
# print(len(btList))
#print(btList)
with open('testStr.txt', 'r+') as f:
    for line in f:
        li = list(line.rstrip('\n').split())
        print(li)