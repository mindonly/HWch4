#!/usr/bin/env python3

# HW ch. 4 Practical
# Rob Sanchez
# CIS 677, F2017

import numpy as np
from sys import argv
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

send_arr = []
recv_arr = []

# matrix size from command-line; 
# must equal mpirun '-np' argument!
n = int(argv[1])

# fill send array
for j in range(1, n+1):
    send_arr.append(tuple([rank+1, j]))

# ensure proper order for printing
if rank != 0:
    comm.send(send_arr, dest=0)

comm.Barrier()

# print send array (ordered)
if rank == 0:
    print("Before send:")
    print("-----------")
    print("Process", rank, send_arr)
    for node in range(1, n):
        recv_arr = comm.recv(source=node)
        print("Process", node, recv_arr) 

# send and rearrange the data
recv_arr = comm.alltoall(send_arr)

# ensure proper order for printing
if rank != 0:
    comm.send(recv_arr, dest=0)

comm.Barrier()

# print recv array (ordered)
if rank == 0:
    print("After recv:")
    print("----------")
    print("Process", rank, recv_arr)
    for node in range(1, n):
        recv_arr = comm.recv(source=node)
        print("Process", node, recv_arr)

