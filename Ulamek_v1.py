import math

class Ułamek:
    def __init__(self, licznik, mianownik):
        assert mianownik != 0, "Mianownik nie może być zerem."
        gcd = math.gcd(licznik, mianownik)
        self.m = abs(mianownik)//gcd
        self.l = licznik//gcd if mianownik >= 0 else -licznik//gcd

    # konwersje do napisów
    def __str__(self):
        if self.m == 1:
            return str(self.l)
        else:            
            return str(self.l) + '/' + str(self.m)
        
    __repr__ = __str__
    
    # operatory porównań
    def __eq__(lhs, rhs):
        return lhs.l == rhs.l and lhs.m == rhs.m
    
    def __ne__(lhs, rhs):
        return not lhs == rhs     

    def __lt__(lhs, rhs):
        lcm = math.lcm(lhs.m, rhs.m)
        return (lhs.l * lcm / lhs.m) < (rhs.l * lcm / rhs.m)
    
    def __le__(lhs, rhs):
        return lhs == rhs or lhs < rhs
    
    def __gt__(lhs, rhs):
        return not lhs <= rhs
    
    def __ge__(lhs, rhs):
        return not lhs < rhs

    # operatory arytmetryczne
    def __add__(lhs, rhs):
        lcm = math.lcm(lhs.m, rhs.m)
        return Ułamek((lhs.l * lcm // lhs.m) + (rhs.l * lcm // rhs.m), lcm)
    
    def __sub__(lhs, rhs):
        lcm = math.lcm(lhs.m, rhs.m)
        return Ułamek((lhs.l * lcm // lhs.m) - (rhs.l * lcm // rhs.m), lcm)
    
    def __mul__(lhs, rhs):
        return Ułamek(lhs.l * rhs.l, lhs.m * rhs.m)
    
    def __truediv__(lhs, rhs):
        return Ułamek(lhs.l * rhs.m, lhs.m * rhs.l)

u1 = Ułamek(3,4)
u2 = Ułamek(5,-6)
print(f"{u1 = } oraz {u2 = }")
print(f"{u1 == u2 = }")
print(f"{u1 != u2 = }")
print(f"{u1 < u2 = }")
print(f"{u1 <= u2 = }")
print(f"{u1 > u2 = }")
print(f"{u1 >= u2 = }")
print(f"{u1 + u2 = }")
print(f"{u1 - u2 = }")
print(f"{u1 * u2 = }")
print(f"{u1 / u2 = }")