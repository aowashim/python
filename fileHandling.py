# with open('text_1.txt','w') as f:
#     n = input('Enter no. of points : ')
#     f.write(f'{n}\n')
#     for i in range(int(n)):
#         tPOint = input('Enter a point : ')
#         f.write(f'{tPOint}\n')

# # pointList = []
# with open('text_1.txt','r') as f:
#     n = int(f.readline())
#     for i in range(1,n):
#         pointList = f.read().splitlines()
#         #pointList.append(tuple(f.readline()))
# print(pointList)

arr = []       
with open('input.txt', 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        arr.append(list(map(int, f.readline().split())))

print(arr)