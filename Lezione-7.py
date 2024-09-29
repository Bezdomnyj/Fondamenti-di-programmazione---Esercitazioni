'''
1. Definite la funzione triangolo(N) che torna una matrice triangolare di N*N/2 elementi, 
   contenente solo la parte in basso a sinistra della matrice dei prodotti (tabelline).
   Il risultato quindi dev'essere una lista di N liste di lunghezza crescente da 1 a N.
   Esempio:
>>> triangolo(4)
[[1],
 [2, 4],
 [3, 6, 9],
 [4, 8, 12, 16]] 
'''
def triangolo(N):
    return [ [el * (x + 1) for x in range(el)] for el in range(1, N + 1) ]

'''
2. Definite la funzione potenze_crescenti(lista) che produce come risultato una lista
   in cui ciascun elemento è ottenuto come la potenza i-esima del corrispondente elemento
   in posizione i della lista passata come argomento.
   Esempio:
>>> potenze_crescenti([2, 3, 4, 5, 6])
[1, 3, 16, 125, 1296]
'''
def potenze_crescenti(lst):
    return [ el ** i for i, el in enumerate(lst) ]


'''
3. Definite la funzione non_divisibili(N, divisori) che trova tutti i numeri tra 1 e N (compresi)
   che non sono divisibili per nessuno dei valori presenti nella lista di divisori (interi).
   Esempio:
>>> non_divisibili(10, [2, 3])
[1, 5, 7]
'''
def non_divisibili(N, lst):
    return [ el for el in range(1, N + 1) if el % 3 != 0 and el % 2 != 0 ]

'''
4.  Definite la funzione doppio_dado() che stampa una successione di estrazioni casuali di due dadi a 6 facce 
    e che conta e torna come risultato quante ne sono state necessarie prima di ottenere un doppio 6.
    Esempio:
>>> doppio_dado()
3 5
2 2
1 6
6 4
3 1
5 4
6 6
7
'''
import random

def doppio_dado_rec(d = 6, last = 0):
    times = last
    
    x = random.randint(0, d)
    y = random.randint(0, d)    
    
    print(x, y)
    
    times += 1
    
    if x == d and y == d:
        return times
    else:
        return doppio_dado_rec(d, times)
        
        
def doppio_dado(d = 6):
    x = random.randint(0, d)
    y = random.randint(0, d)  
    print(x, y)  
    times = 0
    while x != d or y != d:
        times += 1
        print(x, y)
        x = random.randint(0, d)
        y = random.randint(0, d) 

    times += 1
    print(x, y)
    return times
