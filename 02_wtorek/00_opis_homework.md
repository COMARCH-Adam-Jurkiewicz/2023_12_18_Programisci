"""
Wykonaj funkcję z precondition i postcondition
Niech funkcja ma trzy parametry wejściowe (miesięczna wpłata ubezpieczenia, procent premii miesięcznej ,
początkowa data wpłaty) i to trzeba w precondition zawrzeć

funkcja powinna liczyć, ile kapitału uzbiera ubezpieczona osoba w takim czasie (do ostatniego pełnego miesiąca)
wg daty systemowej w komputerze.
np. dla 5 miesięcy i składki 100 zł i 0.05%
1 miesiąc = 100 + 0.05 = 100.05
2 miesiąc + 100 = 200.05 + 10.0025 = 200.05
3 miesiąc + 100 = 300.05 + 15.0025 = 315.05
4 miesiąc + 100 = 415.05 + 20.75 = 435.80
5 miesiąc + 100 = 535.80 + 26.79 = 562.59

w postcondition trzeba sprawdzić, czy wartość końcowa jest większa niż (miesięczna składka * ilość miesięcy) * procent
oraz czy zwracana wartość jest typu float
"""