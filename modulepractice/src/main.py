from utils.mat_mul import mat_mul
from proto.mat import Matrix

a = Matrix([[1, 2], [3, 4]])
b = Matrix([[5, 6], [7, 8]])

print(mat_mul(a, b).data)