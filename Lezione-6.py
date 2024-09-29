'''
1. firstline(t, s) ritorna la prima linea della stringa t che contiene la stringa s , mentre se s non occorre in t ritorna None . 
	Esempio
>>> t = \'''Quant’è bella giovinezza
che si fugge tuttavia!
Chi vuol esser lieto, sia:
del doman non c’è certezza.\'''
	firstline(t, 'non')		ritorna		'del doman non c’è certezza.'
'''

def firstline(t, s):
    for line in t.split('\n'):
        if s in line:
            return line
    return None

'''
2. countw(t, w) ritorna il numero di occorrenze della parola w nella stringa t . 
	Esempio
	t = 'le cose non sono solo cose, ma anche cosette'
	countw(t, 'cose') 		ritorna		2
'''

def countw(t, w):
    return [ ''.join([ a for a in e if a.isalpha() ]) for e in t.split(' ') ].count(w)

'''
3. digits(t) ritorna la lista delle sequenze numeriche contenute nella stringa t . 
   Per sequenza numerica intendiamo una sequenza di cifre (caratteri 0 , 1 ,…, 9 ) di lunghezza massimale. 
	Esempio
	t = 'via Po n.23, tel. 06 7867555 - cell. 345 675665676 (cc 34565)'
	digits(t) 			ritorna 	['23', '06', '7867555', '345', '675665676', '34565']
'''

def digits(t):
    res = [ ''.join([ a for a in e if a.isnumeric() ]) for e in t.split(' ') ]
    return [ x for x in res if x ]

'''
4. column(table, k) ritorna una lista che contiene i valori della colonna k della tabella table . 
   La tabella è rappresentata in modo che ogni linea di table contiene una riga e i valori delle colonne sono separati
   dal carattere ';' . Se table ha n colonne, allora ogni linea di table conterrà esattamente n-1 caratteri ';' .
	Esempio
	table = \'''Milano;12;23
Roma;16;25
Napoli;15;27
Firenze;11;20\'''
	column(table, 1)		ritorna		['12', '16', '15', '11']
'''

def column(table, k):
    return [ row.split(';')[k] for row in table.split('\n') ]