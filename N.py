#
# [McM]: Не забыть перевести кодировку FAR'а в UTF-8!!!
#

class N:
    # Инициализация класса.
    # Здесь: списку "N.digits" присваивается значение первого аргумента (тип: int).
    #Пример: "N( 75044 )" создаст объект класса "N()" с "digits = [7, 5, 0, 4, 4]".
    def __init__(self, digit):
        self.digits = []
        try:
            digit = str(int(str(digit).replace('[', '').replace(']', '').replace(' ', '').replace(',', '')))
            self.digits = [int(i) for i in digit]
        except:
            raise RuntimeError( "Digit cannot be presented as integer > 0." )

    # Что возвращается при вызове через "print()", "format()" и им подобное.
    def __str__(self):
        return str(''.join(map(str, self.digits)))

    # Теперь вызов "len( N() )" даст длину не объекта, а длину списка цифр внутри него.
    def __len__( self ):
        return len( self.digits )

    # Проверка на возможность перевести запрос на более высокий уровень.
    def tryReverseOp( self, other, operator ):
        if ( isinstance( other, Z ) ):
            return eval( str( self.toZ() ) + operator + str( other ) )
        #if ( isinstance( other, Q ) ):
        #    return eval( str( self.toZ().toQ() ) + operator + str( other ) )
        return "NoRev"

    def toZ( self ):
        return Z( self.digits )


    # "Less than", "<="
    def __lt__( self, other ):
        if ( len( self ) < len( other ) ):
            return True
        elif ( len( self ) > len( other ) or ( self.digits == [ 0 ] and other.digits == [ 0 ] ) ):
            return False
        else:
            for i in range( len( self ), -1, -1 ):
                if self.digits[ i ] < other.digits[ i ]:
                    return True
                elif self.digits[ i ] > other.digits[ i ]:
                    return False
            return True


    # Переопределение сложения.
    def __add__( self, other ):
        out = self.tryReverseOp( other, "+" )
        if ( str( out ) != "noRev" ):
            return out

        if isinstance(other, int):
            other = N( other )
        elif not isinstance(other, N):
            raise RuntimeError( "Digit cannot be presented as integer > 0." )

        while ( len( self ) < len( other ) ):
            self.digits.insert( 0, 0 )
        while ( len( self ) > len( other ) ):
            other.digits.insert( 0, 0 )

        out = [ 0 ] * len( self )
        #print( self.digits, "+", other.digits, "; ", out, '\n' ) # 4debug.

        for i in range( len( self ) - 1, -1, -1 ):
            out[ i ] += self.digits[ i ] + other.digits[ i ]
            if ( out[ i ] > 9 ):
                if ( i == 0 ):
                    out.insert( 0, out[ i ] // 10 )
                else:
                    out[ i - 1 ] = out[ i ] // 10
                out[ i ] %= 10

        return N( int( str(''.join(map(str, out))) ) )
    
    # Переопределение умножения.
    '''def __mul__(self, other):
        self.tryReverseOp(other, "*")
        out=[]
        if (int(str(other))>=0 and int(str(self))>=0):
            for i in range(int(str(other))):
                out += self
            out = list(str(out))
            return N(int(str(''.join(map(str, out)))))
        else:
            raise RuntimeError("Some of these digits is not N class")'''
    
    # Перегрузка "!="
    def __ne__(self, other):
        if((self.sign and other.sign) or (self.sign==False and other.sign==False)):
            if ((abs(self)-abs(other))==0):
                return False
            else:
                return True
        else:
            return True
            
    # Перегрузка "=="
    def __eq__(self, other):
        return not (self!=other)

    # Перегрузка "/"
    def __truediv__(self, other):
        self.tryReverseOp(other, "/")
        out=0
        if (int(str(other)) >= 0 and int(str(self)) >= 0):
            for i in range(int(str(other))):
                out -= self.digits[ i ]
                if (out < 0 and i != 0):
                    out += self.digits[ i ]
                    break
                else:
                    out = 0
            out = list(str(out))
            return N(int(str(''.join(map(str, out)))))
        else:
            raise RuntimeError("Some of these digits is not N class")

    # Перегрузка "//"
    def __floordiv__( self, other ):
        return self / other

    # Перегрузка "-"
    def __sub__(self, other):
        self.tryReverseOp(other, "-")
    
        signMustExist = False
        
        if ( self < other ):
            self, other = other, self
            signMustExist = True

        while (len(self) < len(other)):
            self.digits.insert(0, 0)
        while (len(self) > len(other)):
            other.digits.insert(0, 0)

        out = [0] * ( len(self) + 1 )
        #print( self.digits, "-", other.digits, "; ", out, '\n' ) # 4debug.

        for i in range( len( self ), 0, -1 ):
            if ( self.digits[ i - 1 ] - other.digits[ i - 1 ] < 0 and i != 1 ):
                self.digits[ i - 2 ] -= 1
                self.digits[ i - 1 ] += 10
            out[ i ] += self.digits[ i - 1 ] - other.digits[ i - 1 ]
            #print( str( self.digits ), "-", str( other.digits ), "=", str( out ), ": (", out[ i ], "=", self.digits[i-1], "-", other.digits[i-1], ")" )
        
        while ( out and out[ 0 ] == 0 ):
            out.pop( 0 )

        if ( not out ):
            return N( 0 )
        elif ( signMustExist ):
            newz = Z( out )
            newz.sign = True
            return newz
        else:
            return N(int(str(''.join(map(str, out)))))
            '''if (out[i] < 0):
                #print( )
                #out[ i ] += 10 - ( self.digits[ i ] - other.digits[ i ] )
                if (i == 0):
                    #out = list( str( N( out ).toZ() )[ i ] for i in range( len( str ) ) )
                    #out.toZ()
                    #outZ = self.toZ()
                    out[ i ] = -out[ i ]
                    #mustBeZ = Zsign = True
                else:
                    for k in range (i-1,-1,-1):
                        if (out[k]!=0):
                            self.digits[k]-=1
                            out[i]+=10
                            #print( i, out[ i ])
                            #if out[ i ] < 0:
                            #    out[ i ] += 10
                        if (k==0):
                            mustBeZ = Zsign = True
                            #out[ i ]
                            #outZ = self.toZ()
                            #outZ.sign=True
        if (type(out)!=Z):
            return N(int(str(''.join(map(str, out)))))
        else:
            return Z(int(str(''.join(map(str, out)))))'''

    '''def gcd(n1, n2):
        while N('0') < n1 and N('0') < n2:
            if(n1 < n2):
                n2 = n2 % n1
            else:
                n1 = n1 % n2
            return n1 + n2
    
    def lcm(n1, n2):
        return n1 * n2 // gcd(n1, n2)'''

