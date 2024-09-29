from numbers import Number

'''
1. Scrivere una funzione media(vals) che prende in input una lista vals (i cui valori si assume siano
   numeri) e ritorna la media dei suoi valori.
'''

def media(vals = []):
    
    if not (type(vals) == list):
        print('Inserire una lista di valori')
        return False
    
    return sum(vals) / len(vals) if len(vals) > 0 else 0

'''
2. Scrivere una funzione space(s, k) che prende in input una stringa s e un intero k e ritorna una nuova
   stringa che ha i caratteri di s separati da k spazi. Ad esempio
   space('ciao ciao', 1) ritorna la stringa
   'c i a o   c i a o'

'''

def space(s, k = 0):
    
    if not (type(s) == str):
        print('Inserire una stringa valida')
        return False
    
    if not (isinstance(k, Number)):
        print('Inserire un intero valido')
        return False

    return (' ' * k).join(s)


'''
3. Scrivere una funzione crossing_over(m, f) che prese in input due liste m e f (che si assume abbiano
   la stessa lunghezza), ritorna una nuova lista che contiene l'incrocio delle due liste come illustrato dal
   seguente esempio (prendendo alternativamente un elemento dalla prima lista, poi dalla seconda, poi dalla prima ...):
   crossing_over([1, 3, 5], [2, 4, 6]) 
   ritorna la lista [1, 2, 3, 4, 5, 6]
'''

def crossing_over(m = [], f = []):
    
    if (type(m) != list or type(f) != list):
        print('Inseire una lista valida')
        return False
    
    if len(m) != len(f):
        print('la lunghezza delle liste deve essere uguale')
        return False
    
    for i, y in enumerate(f):
        m[2 * i + 1:2 * i + 1] = [y]
    
    return m
    