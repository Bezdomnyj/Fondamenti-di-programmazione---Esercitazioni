'''
Scrivere le funzioni seguenti.
1. occ(lst, v) ritorna una lista contenente gli indici delle occorrenze di v nella lista lst . 
   Esempi, sia	lst = ['red','blue','red','gray','yellow','red']
	occ(lst, 'red')		ritorna [0,2,5]
	occ(lst, 'green')	ritorna []
'''
def occ(lst, v):  
    return [ i for i, x in enumerate(lst) if x == v ]

'''
2. rep(lst, k) ritorna una lista, senza ripetizioni, che contiene i valori che nella lista lst occorrono
   almeno k volte. 
   Esempi, sia lst = [1,2,1,5,3,4,2,1,3,5,6]

	rep(lst, 2)	ritorna [1,2,5,3]
	rep(lst, 3)	ritorna [1]
	rep(lst, 4)	ritorna []
'''

def rep(lst, k):
    uniques = []
    for x in lst:
        if not x in uniques:
            uniques.append(x)
    return [ e for e in uniques if lst.count(e) >= k ]

'''
3. lastfirst(lst) presa in input una lista lst di parole, ritorna la prima parola che inizia con un
   carattere diverso dall'ultimo carattere della parola precedente, se non c'è ritorna None . 
   Esempi
	lastfirst(['sole','elmo','orco','alba','asta'])		ritorna 'alba'
	lastfirst(['sky','you','use','ear','right'])		ritorna None
'''

def lastfirst(lst):
    result = None
    for i, label in enumerate(lst):
        if i == len(lst) - 1:
            break
        if lst[i][-1] == lst[i + 1][0]:
            continue
        else:
            result = lst[i + 1]
            break
    return result

'''
4. groupd(lst) presa in input una lista lst di interi tale che i primi tre rappresentano una data, 
   i secondi tre un'altra data, i successivi tre un'altra data e così via, 
   modifica la lista lst raggruppando ogni tripla in una stringa separando i numeri con il carattere '/' . 
   Si assume che la lista lst abbia una lunghezza multipla di 3. 
   Esempio
>>> lst = [1, 2, 2013, 23, 9, 2011, 10, 11, 2000]
>>> groupd(lst)
>>> lst
['1/2/2013', '23/9/2011', '10/11/2000']
'''

def groupd(lst):
    groupMultiplier = 3
    if len(lst) % groupMultiplier != 0:
        print('La lunghezza della lista deve essere multipla di {}'.format(groupMultiplier))
        return None
    return ['{}/{}/{}'.format(lst[i], lst[i + 1], lst[i + 2]) for i in list(range(0, len(lst) - groupMultiplier + 1, groupMultiplier )) ]