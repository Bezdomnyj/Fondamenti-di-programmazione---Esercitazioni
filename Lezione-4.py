from numbers import Number

'''
1. prec(g1, m1, a1, g2, m2, a2) ritorna True se la data g1, m1, a1 (giorno, mese, anno) è precedente
   o uguale alla data g2, m2, a2 .
   Esempi
   prec(13, 11, 2012,  2,  3, 2013)	ritorna	True
   prec(13, 11, 2012, 27, 12, 2011)	ritorna	False
   prec( 1, 10, 2013,  1, 11, 2013)	ritorna	True
'''

def prec(gg1, mm1, aa1, gg2 = 1, mm2 = 1, aa2 = 1970):
    
    monthsMapper = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
    if not (isinstance(mm1, Number)) or not (isinstance(mm2, Number)):
        print('Inserire un valore numerico per i mesi')
        return None
    
    if not (isinstance(gg1, Number)) or not (isinstance(gg2, Number)):
        print('Inserire un valore numerico per i giorni')
        return None
    
    if not (isinstance(aa1, Number)) or not (isinstance(aa2, Number)):
        print('Inserire un valore numerico per gli anni')
        return None
    
    if not (1 <= mm1 <= 12) or not (1 <= mm2 <= 12):
        print('Inserire un valore compreso tra 1 e 12 per il mese')
        return None
    
    if not (1 <= gg1 <= 31) or not (1 <= gg2 <= 31):
        print('Inserire un valore compreso tra 1 e 31 per il giorno')
        return None
    
    if not (gg1 <= monthsMapper[mm1 - 1]) or not (gg2 <= monthsMapper[mm2 - 1]):
        print('Inserire un giorno valido per il mese')
        return None
    
    return (aa2, mm2, gg2) > (aa1, mm1, gg1)
   
'''
2. l2d(lst) che, presa in input una lista lst i cui elementi sono numeri da 0 a 9 espressi in lettere
   ( 'zero' , 'uno' , …, 'nove' ), ritorna una nuova lista i cui elementi sono la traduzione in numeri degli
   elementi di lst . Esempio
   l2d(['nove','due','due','tre'])	ritorna	[9,2,2,3]
'''

def l2d(lst = ['zero', 'uno', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'otto', 'nove']):
    if not type(lst) == list:
        print('Inserire una lista valida')
        return None
    return [lst[i] for i in range(len(lst) - 1, -1, -1)]

'''
3. distinct(lst) ritorna una nuova lista che contiene gli stessi elementi di lst ma senza le eventuali
   ripetizioni.
   Esempi
   distinct([3,1,3,2,6,6])		ritorna	[3, 1, 2, 6]
   distinct(['a','ab','a','ab'])	ritorna	['a', 'ab']
'''

def distinct(lst = []):
    
    if not type(lst) == list:
        print('Inserire una lista valida')
        return None
    
    result = []
    for x in lst:
        if not x in result:
            result += [x]

    return result

'''
4. search(lst, andc, orc, notc) ritorna una nuova lista di stringhe che contiene le stringhe s della lista
   lst tali che tutte le stringhe della lista andc sono sottostringhe di s, almeno una delle stringhe della
   lista orc (se orc non è vuota) è una sottostringa di s e nessuna delle stringhe della lista notc è una
   sottostringa di s. 
   Esempi, sia lst = ['mela','pera','melo']
   search(lst,['el','a'],['ra','pe','m'],['tt','lo'])	ritorna ['mela']
   search(lst,[],['ra','pe','m'],['tt','lo'])		ritorna ['mela','pera']
   search(lst,['el','a'],[],['tt''lo'])			ritorna ['mela']
   search(lst,[],['ra','pe','m'],[])			ritorna ['mela','pera','melo']
'''

def search(lst, andc, orc, notc):
    result = []
    for label in lst:
        
        isValid = False
        
        # Controllo seconda lista
        
        for oc in orc:
            isValid = isValid or oc in label
            if isValid:
                break
        
        if not isValid and len(orc) > 0:
            continue
            
        isValid = True
        
        # Controllo prima lista
        for ac in andc:
            isValid = isValid and ac in label
            if not isValid:
                break
        
        if not isValid:
            continue
        
        # Controllo terza lista
        for nc in notc:
            isValid = isValid and not (nc in label)
            if not isValid:
                break
        
        if isValid:
            result += [label]
            
    return result