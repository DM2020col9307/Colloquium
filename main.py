from N import *
from Z import *
from Q import *
from poly import *

def tryReverseOp(a, b, op):
    crutch = {type(N(0))   :1,
              type(Z(0))   :2,
              type(Q(0))   :3,
              type(poly(0)):4
              }

    if crutch[type(a)] < crutch[type(b)]:
        return eval(type(b)(a) + op + b)
    else:
        return eval(a + op + type(a)(b))


print(N(12)+N(12))

