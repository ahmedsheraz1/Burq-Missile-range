Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from ctypes import *
TenIntegers = c_int * 10
ii = TenIntegers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ii)
<__main__.c_int_Array_10 object at 0x10d6e8440>
for i in ii: print(i, end=" ")

1 2 3 4 5 6 7 8 9 10 
