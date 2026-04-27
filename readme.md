
100 samples:

| Algorithm       | Time Passed     |
|-----------------|------------------|
| Merge Sort      | 0:00:00.000077   |
| Insertion Sort  | 0:00:00.000055   |
| Tim Sort        | 0:00:00.000002   |


1000 samples:

| Algorithm       | Time Passed     |
|-----------------|------------------|
| Merge Sort      | 0:00:00.000729   |
| Insertion Sort  | 0:00:00.008524   |
| Tim Sort        | 0:00:00.000007   |

100,000 sampes:

| Algorithm       | Time Passed     |
|-----------------|------------------|
| Merge Sort      | 0:00:00.114445   |
| Insertion Sort  | 0:01:28.012174   |
| Tim Sort        | 0:00:00.000302   |


Results of benchmark between Insertion, Merge and TimSort shows that Insertion is least effective, showing minutes in execution. Most efficient is Tim Sort.

Insertion sort time heavily depends on samples count, and it has complexity O(n^2)
Merge sort and Tim sort are more effective for any size of input data, showing complexity of O(n Log n). Tim Sort is little more effective than Merge sort because it uses hybrid approach, based on input data state.


Remark:
Comparing embedded functions and ones implemented in python is not accurate, because embedded are created in low level language (C) and will perform better by definition.


