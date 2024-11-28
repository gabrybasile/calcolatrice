def somma(operando1, operando2):
    return operando1 + operando2


def differenza(minuendo, sottraendo):
    return minuendo - sottraendo

def moltiplicazione(moltiplicando, moltiplicatore): 
     return moltiplicando * moltiplicatore

def divisione(dividendo , divisore):
    
    return dividendo / divisore


print("1. somma")
print("2. differenza")
print("3. moltiplicazione")
print("4. divisione")

scelta = int(input())

print("inserisci il primo valore")
valore1 = int(input())
print("inserisci il secondo valore")
valore2 = int(input())

risultato = 0
if scelta == 1:
    risultato = somma(valore1, valore2)
elif scelta == 2:
    risultato = differenza(valore1 , valore2)
elif scelta == 3:
    risultato = moltiplicazione(valore1 , valore2)
elif scelta == 4:
    risultato = divisione(valore1 , valore2)  

print(risultato)

