import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

st = ""
for i in range(m):
    for j in range(n):
        st += matrix[j][i]
st = re.sub(r"(?<=\w)\W+(?=\w+)"," ",st)
print(st)
