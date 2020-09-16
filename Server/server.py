#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação Server
####################################################

from enlace import *
import time

def main():
    try:
        com2 = enlace('COM8') #Arduino 2
        # com2 = enlace('COM3') #Virtual
        com2.enable() 

        #recebe tamanho da imagem
        print("Esperando tamanho")
        tamanho, nRx = com2.getData(4)
        tamanho = int.from_bytes(tamanho, byteorder='big')
        print(tamanho)

        #recebe imagem
        print("Esperando imagem")
        rxBufferServer, nRxServer = com2.getData(tamanho)
        sizeServer = nRxServer
        sizeServerBytes = nRxServer.to_bytes(4, byteorder='big')

        #manda o número de bytes pro client
        com2.sendData(sizeServerBytes)
        time.sleep(0.1)

        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com2.disable()  
    except:
        print("ops! :-\\")
        com2.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
