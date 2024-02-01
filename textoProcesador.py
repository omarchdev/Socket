
def dividir_texto(texto):
    subcadenas = texto.split("$")
    return subcadenas




def verificar_prefijo(cadena):
    if cadena.startswith("+ACK:"): 
        cadena.replace("+ACK:","")
    if cadena.startswith("+RESP:"):
        cadena.replace("+RESP:","") 
    if cadena.startswith("+BUFF"):
        cadena.replace("+BUFF","")  




def verificar_prefijo_cadena(cadena):
    if cadena.startswith("+ACK:") or cadena.startswith("+RESP:") or cadena.startswith("+BUFF"):
        return True
    else:
        return False




