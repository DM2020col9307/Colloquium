#
# [McM]: Не забыть перевести кодировку FAR'а в UTF-8!!!
#

class Z():
    # Инициализация класса.
    # Здесь: списку "Z.digits" присваивается значение первого аргумента (тип: int).
    #Пример: "Z( -1234 )" создаст объект класса "Z()" с "digits = [1, 2, 3, 4]" и "sign = True".
    def __init__(self, digit):
        digit = str(int(str(digit).replace('[', '').replace(']', '').replace(' ', '').replace(',', '')))
        try:
            self.sign = False
            if (digit[0] == '-'):
                self.sign = True
                digit = digit[1:]
            self.digits = [int(i) for i in digit]
        except:
            raise RuntimeError("Digit cannot be presented as integer.")

    # Что возвращается при вызове через "print()", "format()" и им подобное.
    def __str__(self):
        out = self.sign and '-' or ""
        out += str(''.join( map( str, self.digits )))
        return out

    # "len( Z() )" возвращает количество цифр в числе, знак не учитывается.
    def __len__( self ):
        return len( self.digits )

    def __abs__( self ):
        return Z( list( map( abs, self.digits ) ) )

    def toN( self ):
        if ( self < Z( 0 ) ):
            raise RuntimeError( "Z", str( self ), "cannot be presented as N." )
        return N( int( str( self ) ) )

    def __lt__( self, other ):
        if ( not self.sign and not other.sign ):
            if ( len( self ) < len( other ) ):
                return True
            elif ( len( self ) > len( other ) ):
                return False
            else:
                # Long check must be here...
                return True
        elif ( self.sign and other.sign ):
            if ( len( self ) < len( other ) ):
                return False
            elif ( len( self ) > len( other ) ):
                return True
            else:
                # Long check must be here...
                return False
        else:
            if self.sign:
                return True
            else:
                return False
    def __gt__( self, other ):
        if ( not self.sign and not other.sign ):
            if ( len( self ) < len( other ) ):
                return False
            elif ( len( self ) > len( other ) ):
                return True
            else:
                # Long check must be here...
                return False
        elif ( self.sign and other.sign ):
            if ( len( self ) < len( other ) ):
                return True
            elif ( len( self ) > len( other ) ):
                return False
            else:
                # Long check must be here...
                return True
        else:
            if self.sign:
                return False
            else:
                return True

    def __add__( self, other ):
        if self > Z(0) and other > Z(0):
            print('1')
            out = str( other.toN() + self.toN() )
            return Z( int( out ) )
        elif self < Z(0) and other < Z(0):
            print('2')
            out = '-' + str( abs(other).toN() + abs(self).toN() )
            return Z(int(out))
        elif self > Z(0) and other < Z(0):
            print('3')
            if (abs(self) > abs(other)):
                out = str( self.toN() - abs( other ).toN() )
            else:
                out = '-' + str( abs( other ).toN() - self.toN() )
        else:
            print('4')
            if (abs(other) > abs(self)):
                out = str( other.toN() - abs( self ).toN() )
            else:
                out = '-' + str( abs( self ).toN() - other.toN() )
        return Z( int( out ) )
print( Z( 33 ) + Z( -108 ) )
