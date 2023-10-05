# Wyznaczanie liczby PI metodą Monte Carlo
# dla koła o promieniu 1, środku w (0,0) i kwadratu na nim opisanego o polu 4

import random

l_prob = 1000000
trafione = 0

# generowanie współrzędnych w kwadracie
for i in range(l_prob):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    
    # zliczanie punktów należących do koła
    if (x*x+y*y<=1):
        trafione += 1

# PI jest równe polu koła
pi = 4*(trafione/l_prob)
