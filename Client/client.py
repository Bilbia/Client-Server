#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação Client
####################################################

from enlace import *
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    try:
        com1 = enlace('COM7') #Arduino 1 
        # com1 = enlace('COM2') #Virtual
        com1.enable()

        #Pede para o usuário selecionar uma imagem para ser transmitida
        print('\nPor favor escolha uma imagem:\n')
        Tk().withdraw()
        filename = askopenfilename(filetypes=[("Image files", ".png .jpg .jpeg")])
        print("Arquivo selecionado: {}\n".format(filename))

        #imagem a ser transmitida
        imageR = filename

        #carrega imagem
        print("Carregando imagem pra transmissão\n")
        print("-----------------------------------\n")
        txBufferClient = open(imageR, 'rb').read()
        sizeReal = len(txBufferClient)
        txSizeClient = len(txBufferClient).to_bytes(4, byteorder='big') #esse método é mais rápido do que o getStatus()
        startTime = time.time()

        #manda tamanho da imagem
        com1.sendData(txSizeClient)
        time.sleep(0.1)
        com1.sendData(txBufferClient) #manda imagem pro arduino 1
        time.sleep(0.1)
      
        #bytes recebidos pelo client
        rxBufferClient, nRxClient = com1.getData(4)
        sizeServer = int.from_bytes(rxBufferClient, byteorder='big')
        print("Tamanho da imagem: {}\n".format(sizeServer))

        if sizeServer == sizeReal:
            endTime = time.time()
            print("Transferência de dados bem sucedida\n")
            totalTime = endTime - startTime
            taxa = totalTime/sizeReal
            print("Tempo Total: {}".format(totalTime))
            print("Taxa de transmissão: {} bytes por segundo\n".format(taxa))
        
        else:
            endTime = time.time()
            print("Ocorreu um erro na transferência de dados\n")
    
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
    except:
        print("ops! :-\\")
        com1.disable()

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
    