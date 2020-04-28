#Регулярные выражения, для парсера строки.
#Авторство модулей можно посмотреть в файле README
import re
def parse(s):
    """Парсер входных данных"""
    def forN(s):
        return 'N(' + s[0] + ')'

    def forx(s):
        return 'poly({1:' + (s[0][:-1] and s[0][:-1] or '1') + '})'

    def fordx(s):
        return 'poly({' + s[3] + ':' + str(s[1] and s[1] or 1) + '})'

    s = s.replace(' ', '')
    s = s.lower()

    patforn = '(?:(?<!x\^)(?<!\d))\d+(?![xX0-9])'  # поиск всех не-коэффициентов х
    patforx = '\d*x'  # для х без степени
    patfordx = '(?<![x0-9])(\d*)(x\^)(\d+)'  # для х со степенью

    s = re.sub(patforn, forN, s)
    s = re.sub(patfordx, fordx, s)
    s = re.sub(patforx, forx, s)
    return s


def tryReverseOp(a, b, op):
    """ Cтабилизация типа -- приводит действие к более "старшему" типу в порядке N -> Z -> Q -> poly."""
    crutch = {type(N(0)): 1,
              type(Z(0)): 2,
              type(Q(0)): 3,
              type(poly(0)): 4
              }
    try:  # Пытаемся сравнить типы по "старшинству".
        if crutch[type(a)] < crutch[type(b)]:
            return eval('type(b)(a)' + op + 'b')  # Если "a" -- "младше", то приводим "a" к типу "b".
        else:
            return eval("a" + op + 'type(a)(b)')  # Если "b" -- "младше", то приводим "b" к типу "a".
    except:
        print(a, op, b, ": ", type(a), type(b))
        raise RuntimeError(
            "Impossible to compare those types")  # Если ошибка при сравнении всё-таки произошла, то сообщаем об этом, вызывая исключение.


def gcd(*args):
    """Общая vararg-функция вызова всех GCD() аргументов по цепи"""
    args, arglist, mustBePoly, outgcd = list(args), [], False, None

    if len(args) < 2:  # Если слишком мало аргументов -- возбуждаем ошибку.
        raise RuntimeError("There's too few arguments for GCD()")

    for i in args:  # Формируем список из аргументов, попутно проверяя, нет ли ошибок в исходных данных и должен ли результат быть полиномом.
        if isinstance(i, (poly)):
            mustBePoly = True  # Если в аргументах есть хотя бы один poly(), то результат уже должен быть того же типа.
            arglist.append(i)
        elif isinstance(i, (Z)):
            arglist.append(abs(i).toN())  # GCD() и LCM() игнорируют знаки, так что все Z() превращаются в N().
        elif isinstance(i, (N)):
            arglist.append(i)
        else:
            print(i)
            raise RuntimeError("Object is not a N-digit, Z-digit or polynom")

    if mustBePoly:  # Здесь приводим все не-poly() объекты к poly() и говорим, что результат -- тоже полином.
        if not isinstance(arglist[0], (poly)):
            arglist[0] = arglist[0].toPoly()
        outgcd = arglist[0]

        for i in range(1, len(arglist)):
            if not isinstance(arglist[i], (poly)):
                arglist[i] = arglist[i].toPoly()
            outgcd = outgcd.gcd(arglist[i])  # Цепной вызов GCD() текущего объекта с предыдущим (начиная со второго).
    else:  # Если же в агрументов не попалось ни одного полинома, то просто вызываем this.GCD( prev ) у всех объектов подряд, кроме первого.
        outgcd = arglist[0]
        for i in range(1, len(arglist)):
            outgcd = outgcd.gcd(arglist[i])

    return outgcd


def lcm(*args):
    """Общая vararg-функция вызова всех LCM() аргументов по цепи."""
    args, arglist, outlcm = list(args), [], None

    if len(args) < 2:  # Если слишком мало аргументов -- возбуждаем ошибку.
        raise RuntimeError("There's too few arguments for LCM()")
    for i in args:  # Формируем список из N() из аргументов, попутно проверяя, нет ли ошибок в исходных данных.
        if isinstance(i, (Z)):
            arglist.append(abs(i).toN())
        elif isinstance(i, (N)):
            arglist.append(i)
        else:
            print(i)
            raise RuntimeError("Object is not a N-digit or Z-digit")

    outlcm = arglist[0]
    for i in range(1, len(arglist)):
        outlcm = outlcm.lcm(arglist[i])  # Цепной вызов GCD() текущего объекта с предыдущим (начиная со второго).
    return outlcm

#Ниже представлены функции, которые вызывают необходимые методы для разнообразия ввода исходных данных
def derivative(arg): return der(arg)

def der(arg):
    if (isinstance(arg, (N, Z, Q))):
        return N(0)
    elif (isinstance(arg, (poly))):
        return arg.der()
    else:
        print(arg)
        raise RuntimeError("Can't convert to digit or polynom")


def degree(arg): return deg(arg)

def deg(arg):
    if (isinstance(arg, (N, Z, Q))):
        return N(0)
    elif (isinstance(arg, (poly))):
        return arg.deg()
    else:
        print(arg)
        raise RuntimeError("Can't convert to digit or polynom")


def lead(arg): return leadcoef(arg)


def leading(arg): return leadcoef(arg)


def leadingcoef(arg): return leadcoef(arg)


def leadcoef(arg):
    if (isinstance(arg, (N, Z, Q))):
        return arg
    elif (isinstance(arg, (poly))):
        return arg.lead()
    else:
        print(arg)
        raise RuntimeError("Can't convert to digit or polynom")


def redq(arg): return reduceq(arg)


def red(arg): return reduceq(arg)


def reduce(arg): return reduceq(arg)


def reducefrac(arg): return reduceq(arg)


def redfrac(arg): return reduceq(arg)


def rdc(arg): return reduceq(arg)


def reducefraction(arg): return reduceq(arg)


def defrac(arg): return reduceq(arg)


def reduceq(arg):
    if (isinstance(arg, (N, Z))):
        return arg
    elif (isinstance(arg, (Q))):
        return arg.red()
    else:
        print(arg)
        raise RuntimeError("Can't reduce fraction")


def factorize(arg): factor(arg)


def factorp(arg): factor(arg)


def factor(arg):
    if (isinstance(arg, (N, Z, Q))):
        return arg
    elif (isinstance(arg, (poly))):
        return arg.factor_P()
    else:
        print(arg)
        raise RuntimeError("Can't convert to digit or polynom")


def nmr(arg):
    """Превращает кратные корни в простые"""
    if (isinstance(arg, (N, Z, Q))):
        return N(0)
    elif (isinstance(arg, (poly))):
        return arg.nmr()
    else:
        print(arg)
        raise RuntimeError("Can't convert to digit or polynom")


class N():
    """ Инициализация класса.
        Здесь: списку "N.digits" присваивается значение первого аргумента (тип: int).
        Пример: "N( 75044 )" создаст объект класса "N()" с "digits = [7, 5, 0, 4, 4]"""
    def __init__(self, digit):
        self.digits = []
        try:
            digit = str(int(str(digit).replace('[', '').replace(']', '').replace(' ', '').replace(',', '')))
            self.digits = [int(i) for i in digit]
        except:
            raise RuntimeError("Digit can't be presented as integer > 0")

    # Что возвращается при вызове через "print()", "format()" и им подобное.
    def __str__(self):
        return str(''.join(map(str, self.digits)))

    # Теперь вызов "len( N() )" даст длину не объекта, а длину списка цифр внутри него.
    def __len__(self):
        return len(self.digits)

    # Перенос текущего числа класса N() в классы Z(), Q() и poly() соответственно.
    def toZ(self):
        return Z(self.digits)

    def toQ(self):
        return Q(self, 1)

    def toPoly(self):
        return poly(self)

    # Перегрузка операторов.

    def __neg__(self):
        return Z(-1) * self

    # "Less than", "<"
    def __lt__(self, other):
        if type(self) != type(other):  # Отправляем в обменную централь, если типы разнятся.
            return tryReverseOp(self, other, '<')
        if (len(self) < len(other)):
            return True
        elif (len(self) > len(other) or (self.digits == [0] and other.digits == [0])):
            return False
        else:  # Последовательное сравнение всех цифр, если длины оказались одинаковыми.
            for i in range(len(self)):
                if self.digits[i] < other.digits[i]:
                    return True
                elif self.digits[i] > other.digits[i]:
                    return False
            return False

    # "Less or equal", "<=" (комментарии те же, что в "<")
    def __le__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '<=')
        if (len(self) < len(other) or (self.digits == [0] and other.digits == [0])):
            return True
        elif (len(self) > len(other)):
            return False
        else:
            for i in range(len(self)):
                if self.digits[i] < other.digits[i]:
                    return True
                elif self.digits[i] > other.digits[i]:
                    return False
            return True

    # "==", то же.
    def __eq__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '==')
        if (len(self) != len(other)):
            return False
        else:
            for i in range(len(self)):
                if self.digits[i] != other.digits[i]:
                    return False
            return True

    # "!=", как "не 'равно'".
    def __ne__(self, other):
        return not self == other

    # ">", то же.
    def __gt__(self, other):
        return not self <= other

    # ">=", то же.
    def __ge__(self, other):
        return not self < other

    # Переопределение сложения.
    def __add__(self, other):
        if type(self) != type(other):  # Отправляем в обменную централь, если типы разнятся.
            return tryReverseOp(self, other, '+')

        # Дополняем списки цифр до одинаковой длины.
        while (len(self) < len(other)):
            self.digits.insert(0, 0)
        while (len(self) > len(other)):
            other.digits.insert(0, 0)

        # Забиваем массив "out" нулями по обновлённой длине "self".
        out = [0] * len(self)

        for i in range(len(self) - 1, -1, -1):  # Складываем все цифры, начиная с младшей.
            out[i] += self.digits[i] + other.digits[i]
            if (out[i] > 9):  # Если сумма текущей позиции больше девяти, то переносим единицу в следующий разряд.
                if (i == 0):
                    out.insert(0, out[i] // 10)
                    out[i + 1] %= 10
                else:
                    out[i - 1] = out[i] // 10
                out[i] %= 10

        return N(''.join(map(str, out)))

    # Перегрузка "-"
    def __sub__(self, other):
        if type(self) != type(other):  # Отправляем в обменную централь, если типы разнятся.
            return tryReverseOp(self, other, '-')
        signMustExist = False

        if (self < other):  # Говорим, что знак в результате будет, если левое число меньше правого.
            self, other = other, self
            signMustExist = True

        # Дополняем до одинакового количества.
        while (len(self) < len(other)):
            self.digits.insert(0, 0)
        while (len(self) > len(other)):
            other.digits.insert(0, 0)

        # Забиваем массив "out" нулями по обновлённой длине "self".
        out = [0] * (len(self) + 1)

        for i in range(len(self), 0, -1):  # Вычитаем, начиная с последней цифры.
            if (self.digits[i - 1] - other.digits[i - 1] < 0 and i != 1):
                self.digits[i - 2] -= 1
                self.digits[i - 1] += 10
            out[i] += self.digits[i - 1] - other.digits[i - 1]

        while (out and out[0] == 0):
            out.pop(0)  # Убираем нули, если они вдруг появились.

        if (not out):  # Если всё -- нули, то возвращаем "0".
            return N(0)
        elif (signMustExist):  # Если должен быть знак, то возвращаем Z( out ).
            newz = Z(out)
            newz.sign = True
            return newz
        else:  # Остальные случаи.
            return N(''.join(map(str, out)))

    def muld(self, d):
        t = 0
        lst = []
        lst += self.digits
        for i in range(1, len(self) + 1):
            lst[-i] *= d
            lst[-i] += t
            t = lst[-i] // 10
            lst[-i] %= 10
        if t:
            lst.insert(0, t)
        return N(lst)

    def mulk(self, k):
        return N(self.digits + [0] * k)  # Изящное умножение в реалиях коллоквиума...

    # "Перегрузка умножения"
    def __mul__(self, other):
        if type(self) != type(other):  # Отправляем в обменную централь, если типы разнятся.
            return tryReverseOp(self, other, '*')
        lst = []
        for i in range(len(other)):
            lst.append(self.muld(other.digits[-i - 1]).mulk(i))
        n = N(0)
        for i in lst:
            n = i + n
        return n

    def nzer(self):
        if self.digits[0] == 0:
            return False
        return True

    # степень частного с первой цифрой
    def divdk(self, other):
        k = 0
        while self >= other.mulk(k):
            k += 1

        k -= 1
        res = 9

        while self < other.muld(res).mulk(k):
            res -= 1
        return res * 10 ** k

    # Перегрузка целочисленного деления
    def __floordiv__(self, other):
        if (other==N(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):  # Отправляем в обменную централь, если типы разнятся.
            return tryReverseOp(self, other, '//')
        lst = []
        lst += self.digits
        tmp = N(lst)
        n = N(0)
        while tmp >= other:
            n = n + N(tmp.divdk(other))
            if tmp < N(tmp.divdk(other)) * other:
                break
            tmp = tmp - N(tmp.divdk(other)) * other
        return n

    # Перегрузка остатка от деления
    def __mod__(self, other):
        if (other == N(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):  # Отправляем в обменную централь, если типы разнятся.
            return tryReverseOp(self, other, '%')
        n = self // other
        n = n * other
        n = self - n
        return n

    # Перегрузка деления с остатком
    def __truediv__(self, other):  # Обёртка для "//" -- по-идее, просто передача управления туда.
        if (other == N(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):  # Отправляем в обменную централь, если типы разнятся.
            return tryReverseOp(self, other, '//')
        if (self % other == N(0)):
            return self // other
        else:
            return Q(self, other)

    # Поиска НОДА чисел
    def gcd(self, other):
        # в этом варианте self не будет изменен
        lst1 = []
        lst2 = []
        lst1 += self.digits
        lst2 += other.digits
        tmp1 = N(lst1)
        tmp2 = N(lst2)
        while tmp2 != N(0):  # Стандартный алгоритм нахождения НОД. Алгоиртм Евклида.
            tmp1 = tmp1 % tmp2
            tmp1, tmp2 = tmp2, tmp1
        return tmp1

    # Нахожление НОКА чисео
    def lcm(self, other):  # НОК( a, b ) == ( a * b )/НОД( a, b ).
        res = self * other
        res = res / self.gcd(other)
        return res


class Z():
    """
    Инициализация класса.
    Здесь: списку "Z.digits" присваивается значение первого аргумента (тип: int).
    Пример: "Z( -1234 )" создаст объект класса "Z()" с "digits = [1, 2, 3, 4]" и "sign = True".
    """
    def __init__(self, digit):
        try:
            digit = str(
                int(str(digit).replace('[', '').replace(']', '').replace(' ', '').replace(',', '').replace('\'', "")))
            self.sign = False
            if (digit[0] == '-'):
                self.sign = True
                digit = digit[1:]
            self.digits = [int(i) for i in digit]
            if self.sign and self.digits[0] == 0:
                self.sign = False
        except:
            print(digit)
            raise RuntimeError("Digit can't be presented as integer")

    # Что возвращается при вызове через "print()", "format()" и им подобное.
    def __str__(self):
        out = self.sign and '-' or ""
        out += str(''.join(map(str, self.digits)))
        return out

    # "len( Z() )", наследованный от N()::__len__() возвращает количество цифр в числе, знак не учитывается.
    def __len__(self):
        return len(self.digits)

    #Модуль числа. Отсекание знака
    def __abs__(self):
        return Z(self.digits)
    #Конвертация в N,Q,Poly соответственно
    def toN(self):
        if (self.sign):
            raise RuntimeError("Z", str(self), "Digit Can't be presented as Natural.")
        return N(str(self))

    def toQ(self):
        return Q(self)

    def toPoly(self):
        return poly(self)

    # Перегрузка операторов. Аналогично тому, как это было сделано в N

    def __neg__(self):
        return Z(-1) * self

    def __gt__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '>')
        if self.sign and other.sign:
            return abs(self).toN() < abs(other).toN()
        elif not (self.sign or other.sign):
            return abs(self).toN() > abs(other).toN()
        elif self.sign:
            return False
        else:
            return True

    def __lt__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '<')
        if self.sign and other.sign:
            return abs(self).toN() > abs(other).toN()
        elif not (self.sign or other.sign):
            return abs(self).toN() < abs(other).toN()
        elif self.sign:
            return True
        else:
            return False

    def __le__(self, other):
        return not (self > other)

    def __ge__(self, other):
        return not (self < other)

    def __eq__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '==')
        if self.sign == other.sign:
            return abs(self).toN() == abs(other).toN()
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, "+")
        if self.sign and other.sign: #Рассматриваем различные ситуации - когда оба отрицательных, положительных и разных знаков
            return Z('-' + str(abs(self).toN() + abs(other).toN()))
        if not (self.sign or other.sign):
            return Z(self.toN() + other.toN())
        elif self.sign:
            return Z(other.toN() - abs(self).toN())
        else:
            return Z(self.toN() - abs(other).toN())

    def __mul__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, "*")
        return Z(("-" if self.sign ^ other.sign else "") + str(abs(self).toN() * abs(other).toN())) #Проверяем знаки и добавлем при ниобходимости

    def __floordiv__(self, other):
        if (other == Z(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):
            return tryReverseOp(self, other, "//")
        res = abs(self).toN() // abs(other).toN()
        m = abs(self).toN() % abs(other).toN()
        if self.sign and m != N(0):
            res = res + N(1)
        return Z(("-" if self.sign ^ other.sign else "") + str(res))

    def __truediv__(self, other):
        if (other == Z(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):
            return tryReverseOp(self, other, "/")
        if (self % other == Z(0)):
            return self // other
        else:
            return Q(self, other)

    def __mod__(self, other):
        if (other == Z(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):
            return tryReverseOp(self, other, "%")
        return self - self // other * other

    def __sub__(self, other):
        if type(self) != type(other):
            tryReverseOp(self, other, "-")
        other = other * Z(-1)
        return self + other

    def gcd(self, other):
        return N(self.digits).GCD(N(other.digits))

    def lcm(self, other):
        return N(self.digits).LCM(N(other.digits))


class Q():
    """ Инициализация класса.
            Здесь: списку "N.num" присваивается значение первого аргумента, а спику "N.denum" - второго аргумента
            Пример: "N(5,3)" создаст объект класса "N()" с "num=[5], denum=[3]"""
    def __init__(self, num, denum=N(1)):
        if isinstance(num, N):
            self.num = num.toZ()
        elif isinstance(num, Z):
            self.num = num
        else:
            self.num = Z(num)

        if isinstance(denum, Z):
            if denum.sign:
                self.num = self.num * Z(-1)
            self.denum = abs(denum).toN()
        elif isinstance(denum, N):
            self.denum = denum
        else:
            self.denum = N(denum)

        # self.num = num # Числитель.
        # self.denum = denum  # Знаменатель.
        if self.denum == N(0):
            raise RuntimeError("Second number can't be equal to the zero")

    def __str__(self):
        res = str(self.num) + (
                str(self.denum) != '1' and "/{}".format(self.denum) or "")  # если знаменатель == 1, не пишется
        return res

    def red(self):
        """Функция сокращения дроби"""
        gcd = self.denum.gcd(abs(self.num).toN())
        num = self.num / gcd
        denum = self.denum / gcd
        return Q(num, denum)

    def ifZ(self):
        if self.num % self.denum == Z(0):
            return True
        else:
            return False

    def toN(self):
        if (self.ifZ and (self.num // self.denum >= Z(0))):
            return N(str(self.num // self.denum))
        else:
            raise RuntimeError("Z", str(self), "Digit can't be presented as Natural")

    def toZ(self):
        if (self.ifZ):
            return Z(str(self.num // self.denum))
        else:
            raise RuntimeError("Z", str(self), "Digit can't be presented as Natural")

    def toPoly(self):
        return poly(self)

    # Перегрузка операторов.

    def __neg__(self):
        return Z(-1) * self

    def __add__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '+')

        denum = self.denum * other.denum
        num = self.num * other.denum + self.denum * other.num
        return Q(num, denum).red()

    def __sub__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '-')

        denum = self.denum * other.denum
        tmp = self.num * other.denum
        tmp2 = self.denum * other.num
        num = tmp - tmp2
        return Q(num, denum).red()

    def __mul__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '*')
        num = self.num * other.num
        denum = self.denum * other.denum
        return Q(num, denum).red()

    def __truediv__(self, other):
        if (other == Q(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):
            return tryReverseOp(self, other, '/')
        num = self.num * other.denum
        denum = self.denum * other.num
        return Q(num, denum).red()

    def __floordiv__(self, other):
        if (other == Q(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):
            return tryReverseOp(self, other, '//')
        tmp = self / other
        res = tmp.num // tmp.denum
        return res

    def __mod__(self, other):
        if (other == Q(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):
            return tryReverseOp(self, other, '%')
        tmp = self / other
        mod = tmp.num % tmp.denum
        return mod

    def __lt__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '<')
        return self.num * other.denum < other.num * self.denum

    def __le__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '<=')
        return self.num * other.denum <= other.num * self.denum

    def __eq__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '==')
        return self.num * other.denum == other.num * self.denum

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other


class poly():
    """
    Здесь: poly() имеет в себе одну переменную-словарь "coef", в которой хранятся
    значения по шаблону { <степень>: <Q-объект>, ... }.
    Пример: poly( {23: Q( 3, 4 ), 7: Q( -4 )} ) будет выглядеть как "3/4 * x^23 - 4 * x^7".
    """
    def __init__(self, coeflist):
        self.coef = {}

        if isinstance(coeflist, list):
            for i in range(len(coeflist)):
                if not isinstance(i, Q):
                    self.coef.update({i: Q(coeflist[i])})
                else:
                    self.coef.update({i: coeflist[i]})
        elif isinstance(coeflist, dict):
            for i in coeflist:
                if isinstance(coeflist[i], Q):
                    self.coef.update({i: coeflist[i]})
                else:
                    self.coef.update({i: Q(coeflist[i])})

        elif isinstance(coeflist, (Z, N)):
            self.coef = {0: coeflist.toQ()}
        elif isinstance(coeflist, Q):
            self.coef = {0: coeflist}
        elif isinstance(coeflist, str):
            lst = coeflist.split(' ')
            for i in range(len(lst)):
                self.coef.update({i: Q(lst[-i - 1])})
        coeflist = self.coef.copy()
        for i in self.coef.keys():
            if str(self.coef[i]) == "0":
                coeflist.pop(i)
        self.coef = coeflist.copy()

        if len(self.coef) == 0:
            self.coef.update({0: Q(0)})

    def __str__(self):
        coef, out = self.coef, ""
        if self.lead() == Q(0):  # Not "self.deg()" (see "poly({ 0: Q( 1 ) })").
            out = "0"
        else:
            key = sorted(list(coef.keys()))[::-1]

            for i in key:
                if coef[i].num.sign == False:
                    out += '+'
                if coef[i] == Q(1) and i != 0:
                    pass
                elif coef[i] == Q(-1) and i != 0:
                    out += '-'
                else:
                    out += str(coef[i])
                if i > 1:
                    out += 'x^{}'.format(i)
                elif i == 1:
                    out += 'x'

            if out[0] == '+':
                out = out[1:]
        return out

    # Степень и длина списка коэффициентов многочлена.
    def __len__(self):
        return len(list(self.coef.keys()))

    def deg(self):
        return max(list(self.coef.keys()))

    # Ведущий (старший) коэффициент.
    def lead(self):
        return self.coef[self.deg()]

    # Перегрузка операторов.
    def __neg__(self):
        return Z(-1) * self

    def __add__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '+')
        tmp = {}
        tmp.update(self.coef)
        for i in other.coef:
            if i in tmp:
                tmp[i] = tmp[i] + other.coef[i]
            else:
                tmp.update({i: other.coef[i]})
        return poly(tmp)

    def __sub__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '-')
        tmp = {}
        tmp.update(self.coef)
        for i in other.coef:
            if i in tmp:
                tmp[i] = tmp[i] - other.coef[i]
            else:
                tmp.update({i: Z(-1) * other.coef[i]})
        return poly(tmp)

    def mulq(self, q):
        out = poly(self.coef)
        for i in out.coef:
            out.coef[i] = out.coef[i] * q
        return out

    def mulqx(self, q, k):
        key = self.coef.keys()
        out = {}
        for i in key:
            out[i + k] = self.coef[i] * q
        return poly(out)

    def __mul__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '*')
        if deg(self) < deg(other):
            self, other = other, self
        out = poly(0)
        for i in other.coef.keys():
            out = out + self.mulqx(other.coef[i], i)
        return out

    def factor_P(self):
        a = poly(self.coef)
        g = abs(a.coef[0].num).toN().gcd(abs(a.coef[0].num).toN())
        l = a.coef[0].denum.lcm(a.coef[0].denum)
        for i in range(1, len(a.coef)):
            g = g.gcd(abs(a.coef[0].num))
            l = l.lcm(a.coef[i].denum)
        return Q(g, l)

    # вернет целую часть
    def __truediv__(self, other):
        if (other == poly(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):
            return tryReverseOp(self, other, '/')
        p1 = poly(self.coef)
        p2 = poly(other.coef)
        res = poly(0)
        while (p1.deg() >= p2.deg() and p1.deg()):
            dif = p1.deg() - p2.deg()
            q = p1.lead() / p2.lead()
            res = res + poly({dif: q})
            p1 = p1 - p2.mulqx(q, dif)
        r = p1
        return res

    def __mod__(self, other):
        if (other == poly(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):
            return tryReverseOp(self, other, '%')
        p1 = poly(self.coef)
        p2 = poly(other.coef)
        res = poly(0)
        while (p1.deg() >= p2.deg() and p1.deg()):
            dif = p1.deg() - p2.deg()
            q = p1.lead() / p2.lead()
            res = res + poly({dif: q})
            p1 = p1 - p2.mulqx(q, dif)
        return p1

    def __floordiv__(self, other):
        if (other == poly(0)):
            raise RuntimeError("Second number can't be equal to the zero")
        if type(self) != type(other):
            return tryReverseOp(self, other, '//')
        return self / other

    def gcd(self, other):
        poly1 = poly(self.coef)
        poly2 = poly(other.coef)
        while poly2.deg() > 0:
            poly1 = poly1 % poly2
            poly1, poly2 = poly2, poly1
        if self % poly1 == Q(0):
            poly1 = poly1.mulq(Q(1) / poly1.lead())
            return poly1
        else:
            return 1

    # Производная многочлена.
    def der(self):
        poly_derivative = poly(0)
        pol = poly(self.coef)
        for i in pol.coef:
            if i:
                poly_derivative = poly_derivative + poly({i - 1: Q(i) * pol.coef[i]})
        return poly_derivative

    # Кратные корни в простые.
    def nmr(self):
        der = self.der()
        gcd = self.gcd(der)
        res = self / gcd
        return res

