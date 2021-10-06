import mypackage
from mypackage.extras import mul
res = mypackage.MyPackage().spam()
print(res)
########################################

import mypackage.extras.mul as ml
res = ml.multiply(4, 2)
print(res)
###################
import mypackage.extras 
res = mul.multiply(2, 3)
print(res)