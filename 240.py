import time
begintime=time.time()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
y=len(matrix)
def search(line,row):
    if line>y-1 or row<0:
        return False
    if matrix[line][row]==target:
        return True
    else:
        if matrix[line][row]>target:
            return search(line,row-1)
        else:
            return search(line+1,row)
print(search(0,len(matrix[0])-1))
endtime=time.time()
print(endtime-begintime)
