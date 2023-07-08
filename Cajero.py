#APLICACION CAJERO AUTOMATICO
caja = {100:3, 50:6, 20:10, 10:20, 1:50}

def contar_disponible(caja):
    contar = 0
    for k,v in caja.items():
        contar += k * v
    return contar

def peticion():
    peticion = int(input('INGRESE LA CANTIDAD QUE QUIERE RETIRAR: '))
    return peticion


def validar_peticion(peticion,disponible):
    if peticion > disponible:
        print('saldo insuficiente')
    else:
         print('Iniciando transaccion')


def contar_retiro(monto):
    count = 0  
    for k,v in caja.items():
        if v == 0 :
            continue

        while count < monto and v > 0 and count + k <= monto:
            count += k
            v -= 1
            caja[k] = v

        if count == monto:
            break
    return 'Transaccion finalizada'

def inicio():
    while True:
        cantidad = peticion()
        disponible = contar_disponible(caja)
        validar_peticion(cantidad,disponible)
        retiro = contar_retiro(cantidad)
        print(retiro)
        print('Cantidad restante en caja...')
        print(caja)
        if disponible < cantidad:
            print('No mas Transacciones: Se acabo la plata!!!')
            break

if __name__ == '__main__' :
    inicio()



    


            
            
            
       
   







