class Matrix:
    def __init__(self, mat):
        self.my_mat = mat
        
        
    def __str__(self):
        res = ''
        for i in self.my_mat:
            res += ' '.join([chr(j + 48) for j in i]) + '\n'
        return res
    
    
    def __add__(self, mat):
        res = self.my_mat
        if len(mat.my_mat) < len(res):
            height = len(mat.my_mat)
        else:
            height = len(res)
        if len(mat.my_mat[0]) < len(res[0]):
            width = len(mat.my_mat[0])
        else:
            width = len(res[0])
        for i in range(height):
            for j in range(width):
                res[i][j] += mat.my_mat[i][j]
        return Matrix(res)
    
    
mat = Matrix([[1,1,1],[1,1,1],[2,3,2]])
dif_mat = Matrix([[4,2],[5,6]])
print(mat)
print(mat + dif_mat)