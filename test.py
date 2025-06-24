"""Simple sandbox. Can be overwritten any time"""

import os

my_list = []
print(";".join(my_list))


exit(0)
from scipy.sparse import lil_matrix

m = lil_matrix((4, 4), dtype=bool)
m[1,2]=True
m[2,1]=True
m[2,3]=True
m[3,2]=True

graph_coo = m.tocoo()   # Coo format is used to efficiently retrieve upper triangle

# Filter for upper triangle (i <= j)
mask = graph_coo.row <= graph_coo.col
row = graph_coo.row[mask]
col = graph_coo.col[mask]

print(row)
print(col)

a = zip(row, col)
b = zip(col, row)

for x,y in a:
    print(x,y)

for x,y in b:
    print(x,y)



print(m.shape)
