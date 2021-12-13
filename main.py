"""1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
"""
szam = int(input('Kérek egy számot! '))
if szam % 2 == 0  : 
  print('A megadott szám páros! ')
elif szam % 2 != 0 :
  print('A megadott szám páratlan! ')
print('és')
if szam > 0 :
  print('pozitív! ')
elif szam < 0 :
  print('negatív! ')