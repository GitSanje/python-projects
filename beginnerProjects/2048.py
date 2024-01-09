import random

print('*'*30)
print("Welcome to the 2048 game.")
print('*'*30)
#put 2 on random cell on matrix
def generateRandNums(arr,size,value):
    x= random.randint(0,size)
    y = random.randint(0, size)
    while (arr[x][y] != 0):
        x= random.randint(0, size)
        y= random.randint(0, size)
    arr[x][y] =value
def generateMatrx(size):
    arr = [[0 for i in range(size)] for j in range(size)]
    return arr
def generateInitialMatrix(size):
   arr = generateMatrx(size)
   generateRandNums(arr,size-1,2)
   generateRandNums(arr,size-1,2)
   return arr

def addLeft(arr,addarr,idxsarr,size):

    for i in range(size):
        for j in range(size):
            #print(j% 3, (j%3)+1)# 0 1 1 2 2 3 0 1
            if j == 0:
                  if addarr[i][0] == addarr[i][1] and addarr[i][0] != 0 and addarr[i][1] != 0:
                        print(f"1: , {addarr[i][0]}:{i,0},{addarr[i][1]}:{i,1}")
                        c1 =idxsarr[i][0]
                        c2 = idxsarr[i][1]
                        arr[i][c1] *= 2
                        arr[i][c2] = 0

            elif (j%3== 0 and j!=0):
                continue
            else:
               if addarr[i][j % 3] == addarr[i][j % 3+ 1] and addarr[i][j % 3] != 0 and addarr[i][j % 3 +1] != 0 :
                    print(f"3: ,{addarr[i][j % 3]}:{i,j % 3},{addarr[i][j % 3+1]}:{i,j % 3+1}")
                    c1 = idxsarr[i][j % 3]
                    c2 = idxsarr[i][j % 3+1]
                    arr[i][c1] *= 2
                    arr[i][c2] = 0
    return arr
def addTwoValues(arr,size):
    valuearr= generateMatrx(4)
    idxarr = generateMatrx(4)
    for i in range(size):
        count=0
        for j in range(size):
            if arr[i][j] != 0:
                valuearr[i][count] = arr[i][j]
                idxarr[i][count] =j
                count+=1
            if count < size:
              idxarr[i][count] = -1

    return valuearr,idxarr
# arr=generateInitialMatrix(4)
# generateRandNums(arr,3,2)
# generateRandNums(arr,3,3)
arr = generateMatrx(4)
arr[0][0]=8
arr[0][1]=0
arr[0][2]=6
arr[0][3]=8
for i in arr:
    print(i)
print("\n")
newarr,idxarr= addTwoValues(arr,4)
for i in newarr:
    print(i)

arr= addLeft(arr,newarr,idxarr, 4)
# print("\n")
for i in idxarr:
    print(i)
print("\n")
for i in arr:
    print(i)


