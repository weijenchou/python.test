import numpy as np
a= [1, 2, 3, 4]
matrix_a=np.array(a)
print(a,type(a), matrix_a, type(matrix_a))

b=[
  [1,2],
  [3,4]
  ]
matrix_b= np.array(b)
#print(matrix_b)

zeros_matrix=np.zeros((2,3)) #2,3是直2寬3
print(zeros_matrix)

ones_matrix=np.ones((3,3)) 
print(ones_matrix)

muti_ones_matrix= np.ones((3,2,2))
print(muti_ones_matrix)

range_matrix= np.arange(0,16,3)
print(range_matrix)

random_matrix=np.random.rand(3,2)
print(random_matrix)

random_int_matrix=np.random.randint(1,10, size=(3,2))
print(random_int_matrix)

def coin_simu(count):
    coin_random= np.random.randint(0, 2, size=(count,))
    print(coin_random)
    front= np.sum(coin_random)
    back= 10 - front
    print(f'正面有 {front}次,反面有{back}次')

coin_simu(8)

"""
基本操作
"""

#1.訪問元素(跟list操作一樣)
matrix= np.array([10,20,30,40])
print(matrix[0])
print(matrix[-1])

matrix2= np.array([[10,20],
                   [30,40]])
print(matrix2[0][1])
print(matrix2[-1][-1])

#2.切片操作

matrix3= np.array([10, 20, 30, 40, 50])
print(matrix[1:4]) #獲取第2到第4個元素
print(matrix[::-1]) #倒著數元素切片 矩陣整個反過來

#3.矩陣間的加減乘除
matrix = np.array([10,20,30,40])
matrix1= np.array([1,2,3,4])
print(matrix + matrix1)
print(matrix - matrix1)
print(matrix * matrix1)
print(matrix / matrix1)
print(matrix % matrix1)
print(matrix ** matrix1)

#矩陣間的加減乘除
matrix = np.array([[10,20],
                   [30,40]])
matrix1= np.array([[1,2],
                   [3,4]])
#print(matrix + matrix1)
#print(matrix - matrix1)
print(matrix * matrix1)
#print(matrix / matrix1)
#print(matrix % matrix1)
#print(matrix ** matrix1)

result= np.dot(matrix1, matrix2)
print(result)
result2= matrix1 @ matrix2
print(result2)

"""
矩陣的屬性指令
"""

#1. 形狀(shape)
matrix_2x3=np.array([[1,2,3],
                     [4,5,6]])
#print(matrix_2x3.shape) #輸出(2,3)

#改變矩陣形狀

matrix_1x6= matrix_2x3.reshape(6,)
print(matrix_1x6)

x,y = matrix_2x3.shape #(2,3) 拆包給x,y
matrix_1x6 = matrix_2x3.reshape(x*y)
#print(matrix_1x6)

matrix_1x6=matrix_2x3.reshape(-1)
#print(matrix_1x6)

"""
合併與分割矩陣
"""

#1.合併矩陣
##使用 np.concatenate

matrix1= np.array([[1,2],[3,4]])
matrix2= np.array([[5,6]])
combined_matrix= np.concatenate((matrix1, matrix2), axis=0) #沿行1
print(combined_matrix)

combined_matrix= np.concatenate((matrix1, matrix2.T), axis=1)
print(combined_matrix)

"""
#T是矩陣旋轉的意思
|5 6| => |5|
         |6|
"""

#分割矩陣
##使用np.split

matrix= np.array([1,2,3,4,5,6])
split_matrix = np.split(matrix, 2)
#print(split_matrix, type(split_matrix))

##使用np.vsplit 與 np.hsplit 

#垂直分割：行方向切割，看起來很像-水平線分割
matrix= np.array([[1,2,3],[4,5,6],[7,8,9]])
v_split= np.vsplit(matrix, 3)
print(v_split)

#水平分割:列方向分割，看起來很像-垂直線分割
h_split= np.hsplit(matrix, 3)
print(h_split)

word= 'ajpcjpvjspfaavjvoicddkiwk'
print(word.split('j'))




