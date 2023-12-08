# /usr/bin/time -v python3 wersja1.py 2>&1 1>/dev/null | grep  -E "wall|Max"
# perl -p -e "s/# Wersja2 //" wersja1.py > wersja2.py

import math

class Ułamek:
    # Wersja2 __slots__ = ['m', 'l']

    def __init__(self, licznik, mianownik):
        assert mianownik != 0, "Mianownik nie może być zerem."
        gcd = math.gcd(licznik, mianownik)
        self.m = abs(mianownik)//gcd
        self.l = licznik//gcd if mianownik >= 0 else -licznik//gcd

    def __str__(self):
        if self.m == 1:
            return str(self.l)
        else:            
            return str(self.l) + '/' + str(self.m)
        
    __repr__ = __str__
    
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

# metoda testująca, gdzie:
# n - liczba stworzonych obiektów klasy Ułamek
# k - liczba wykonanych operacji
def test(n, k):
    # Inicjalizacja n ułamków
    tab = []
    n_pół = n // 2
    for i in range(1, n+1):
        tab.append(Ułamek(k * (n % i) + 1, i % 50 + 1))

    # Operacje na ułamkach
    for j in range(k):
        match j%4:
            case 0:
                tab[j] + tab[j+1]
            case 1:
                tab[j] - tab[j+1]
            case 2:
                tab[j] * tab[j+1]
            case 3:
                tab[j] / tab[j+1]

test(1000000, 1000000)