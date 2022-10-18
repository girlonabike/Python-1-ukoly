from operator import truediv

cislo = str (input ("Zadejte telefonní číslo: "))


def overeni_delky (cislo):
    format = len (cislo)

    if format == 13 and cislo[0:4]=="+420":
        return ("True")       
    elif format == 9:
        return ("True")
    else:
        return ("False")
    
if overeni_delky(cislo) == "False":
    exit()
    
zprava = input ("Zadejte zprávu: ")

from math import ceil

def cena_sms (zprava):
    cena = 3
    znaky = ceil (len (zprava)/180)
    return znaky *3
print (f" Cena Vaší sms je {cena_sms (zprava)} Kč.")