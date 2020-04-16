from main import *
from N import *
from Z import *

class Q():
    def __init__(self, num, denum = N(1) ):
        if isinstance( num, N ):
            self.num = num.toZ()
        elif isinstance( num, Z):
            self.num = Z( num.toN )
        else:
            self.num = Z( num )

        if isinstance( denum, Z ):
            if denum.sign:
                #self.num = mul_zm_z( self.num )
                self.num = self*Z(-1)
            self.denum = abs(denum).toN()
        elif isinstance( denum, N):
            self.denum = denum
        else:
            self.denum = N( denum )

        #self.num = num # Числитель.
        #self.denum = denum  # Знаменатель.
        if not self.denum == N(0) :
            raise ZeroDivisionError("Divided by zero")
    def __str__(self):
        res = str(self.num) + ( str(self.denum) != '1' and "/{}".format(self.denum) or "" ) #если знаменатель == 1, не пишется
        #res = "{}/{}".format(self.num, self.denum)
        return res

    def red(self):
        gcd = self.denum.gcd(abs(self.num).toN())
        self.num = self.num / gcd
        self.denum = self.denum / gcd
        return self

    def ifZ(self):
        if self.num % self.denum == Z(0):
            return True
        else:
            return False

    def toN(self):
        if (self.ifZ and (self.num//self.denum>Z(0))):
            return N(int(str(self.num//self.denum)))
        else:
            raise RuntimeError("Z", str(self), "cannot be presented as N.")

    def toZ(self):
        if (self.ifZ):
            return Z(int(str(self.num//self.denum)))
        else:
            raise RuntimeError("Z", str(self), "cannot be presented as N.")

    def toPoly(self):
        return poly(self)

    def tryReverseOp(a, b, op):
        crutch = {type(N(0)): 1,
                  type(Z(0)): 2,
                  type(Q(0)): 3,
                  type(poly(0)): 4
                  }
        if type(a) != type(b):
            if crutch[type(a)] < crutch[type(b)]:
                eval(type(b)(a) + op + b)
            else:
                eval(a + op + type(a)(b))

    def __add__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '+')

        denum = self.denum * other.denum
        num = self.num*other.denum + self.denum * other.num
        return Q(num, denum)

    def __sub__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '-')

        denum = self.denum * other.denum
        num = self.num * other.denum + self.denum * other.num
        return Q(num, denum)

    def __mul__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '*')
        num = self.num * other.num
        denum = self.denum * self.denum
        return Q(num, denum)

    def __truediv__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '*')
        num = self.num * other.denum
        denum = self.denum * other.num
        return Q(num, denum)

    def __floordiv__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '//')
        tmp = self / other
        res = tmp.num // tmp.denum
        return res

    def __mod__(self,other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '%')
        mod=self-(self//other)
        return mod

    def __lt__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '<')
        return self.num*other.denum < other.num*self.denum
    def __le__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '<=')
        return self.num*other.denum <= other.num*self.denum
    def __eq__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '==')
        return self.num*other.denum == other.num*self.denum
    def __ne__(self, other):
        return not self == other
    def __gt__(self, other):
        return not self <= other
    def __ge__(self, other):
        return not self < other