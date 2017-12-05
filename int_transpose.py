#!/usr/bin/env python3

import numpy as np
from sys import argv
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# create send & recv arrays
sendarr = np.zeros(mat_sz)
recvarr = np.zeros(mat_sz)

# fill send array
for i in range(0, sendarr.size):
    sendarr[i] = rank * size + i

if rank == 0:
    print("Before send:")
    
# print send array
print("Process", rank, sendarr)

# send and rearrange the data
comm.Alltoall(sendarr, recvarr)

if rank == 0:
    print("After recv:")

# print recv array
print("Process", rank, recvarr)


