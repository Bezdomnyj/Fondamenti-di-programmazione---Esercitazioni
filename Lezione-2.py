import numbers

'''
1. Scrivere una funzione 'scontato' che prende in input un importo e una percentuale di sconto e ritorna
   l'importo scontato. Ad esempio, se l'importo è 1000 e lo sconto è 20 , la funzione ritorna 800 .
'''

def scontato(importo, percentualeSconto = 0):
    
    if not isinstance(percentualeSconto, numbers.Number):
        print('inserire una percentuale numerica')
        return False
    
    if not (0 <= percentualeSconto <= 100):
        print('la percentuale deve essere compresa tra 0 e 100')
        return False
    
    if not isinstance(importo, numbers.Number):
        print('inserire un importo numerico')
        return False
    
    return importo - importo * percentualeSconto / 100
        

'''
2. Scrivere una funzione 'secondi' che prende in input un lasso di tempo espresso tramite numero di ore
   hh , numero di minuti mm e numero secondi ss e ritorna l'equivalente numero di secondi. Ad esempio,
   se hh = 2 , mm = 1 e ss = 11 , la funzione ritorna 7271 .
'''

def secondi(hh = 0, mm = 0, ss = 0):
        
    if not isinstance(hh, numbers.Number):
        print('Inserire un valore numerico per le ore')
        return False
    
    if not isinstance(mm, numbers.Number):
        print('Inserire un valore numerico per i minuti')
        return False
    
    if not isinstance(ss, numbers.Number):
        print('Inserire un valore numerico per i secondi')
        return False
    
    return hh * 3600 + mm * 60 + ss

'''
3. Scrivere una funzione 'invest' che prende in input un capitale C , un interesse annuale i e un numero di
   anni n e ritorna come intero il capitale maturato dopo un investimento di n anni all'interesse i .
   (usando la formula     maturato = capitale * (1+interesse/100)**anni )
   Ad esempio, se gli argomenti sono  C = 1000 , i = 10 e n = 2 , la funzione ritorna 1210 .
'''

def invest(C, i = 0, n = 0):
        
    if not isinstance(C, numbers.Number):
        print('Inserire un valore numerico per il capitale')
        return False
    
    if not isinstance(i, numbers.Number):
        print('Inserire un valore numerico per il tasso di interesse')
        return False
    
    if not type(n) == int:
        print('Inserire un valore di anni intero')
        return False
    
    if n < 0:
        print('Inserire un di anni positivo')
        return False
    
    return round(C * (1 + i / 100) ** n, 3) if n > 0 else C