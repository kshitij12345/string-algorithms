import timeit
from DC3 import *
from suffix_array import *

a = [2,1]*1000


print (timeit.timeit(lambda:build_suffix_array("GA"*1000+"$"),number = 5))
print (timeit.timeit(lambda:DC_3(a),number = 5))
