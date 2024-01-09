import random

print('*'*30)
print("Welcome to the 2048 game.")
print('*'*30)

def generateRandNums(size):
    x= random.randint(0,size)
    y = random.randint(0, size)
    p = random.randint(0, size)
    q = random.randint(0, size)
    return  x,y,p,q

def generateInitialMatrix(size):
   arr = [[0 for i in range(size)] for  j in range(size)]
   #x,y,p,q = generateRandNums(size-1)
   if arr[0][0] == 0 and arr[0][1]==0:

       arr[0][1]=2

       arr[0][2] = 2
       arr[1][3] = 2
       arr[1][0] = 2
   return arr

def addValuesMatrix(arr,state):
    if state =='a':
        for i,row in enumerate(arr):
            for j in range(len(arr)):
              if row[i][j] == row[i][j+1]:
                  row[i][j] *= 2
    return  arr



arr=generateInitialMatrix(4)
#updateArr=addValuesMatrix(arr,'a')
# for i in arr:
#     print(i)
def addLeft(arr):
    for i in range(4):
        idces=[]
        for j in range(4):
            if arr[i][j] != 0:
                idces.append(j)
        if len(idces)>=2:
            print(idces)
            for k in range(len(idces)):
              if arr[i][idces[k-1]] == arr[i][idces[k]]:
                     arr[i][idces[k]] *=2
                     arr[i][idces[k-1]] =0
    x,y,_,_=generateRandNums(3)
    if arr[x][y] == 0:
        arr[x][y] =2


    return  arr

newarr=addLeft(arr)

newarr[0][2] = 2
newarr[0][3]=2
newarr1 = newarr[:]
newarr1=addLeft(newarr1)
# newarr2=addLeft(newarr1)





for i in arr:
    print(i)
print("\n")
for i in newarr:
    print(i)
# # print("\n")
# for i in newarr2:
#     print(i)
    