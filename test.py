"""Simple sandbox. Can be overwritten any time"""

from scipy.sparse import lil_matrix

m = lil_matrix((4, 4), dtype=bool)
m[1,2]=True
m[2,1]=True
m[2,3]=True
m[3,2]=True

graph = m.tocsr()

for i in range(4):
    # Use a dict for fast lookup of non-zero entries in row i
    row_start = graph.indptr[i]
    row_end = graph.indptr[i + 1]
    cols = graph.indices[row_start:row_end]
    data = graph.data[row_start:row_end]
    row_dict = dict(zip(cols, data))

    # Write values from i+1 to end of row (upper triangle only)
    for j in range(i + 1, 4):
        cost = int(row_dict.get(j, 9999))
