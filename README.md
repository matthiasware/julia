# Julia Set in Python

![image](julia_set.png)

## Timings
**5000x5000**


|  version |  time | file  |
|---|---|---|
| serial  | 57.5   | julia_serial.py  |
| serial + numpy  | 49.8   | julia_numpy.py |
| multiproc x2  | 31.8  | julia_parallel.py  |
| multiproc x4  |18.9   | julia_parallel.py  |
| multiproc x8  |14.3   | julia_parallel.py |
| numba  | 5.1  | julia_numba.py  |
| multiproc x8 + numba  |3.9   | julia_parallel_numba.py  |
| numba + parange  |3.2  | julia_numba_parallel.py  |
| multiproc + shm + numba  |3.0   | julia_fast.py  |


**10000x10000**

|  version |  time | file  |
|---|---|---|
| numba  | 21.23  | julia_numba.py  |
| multiproc x8 + numba  |3.9   | julia_parallel_numba.py  |
| numba + parange  |13.56  | julia_numba_parallel.py  |
| multiproc + shm + numba  |9.40   | julia_fast.py|