# Client-Server
Projeto 2 para a matéria de Camada Física da Computação. Utilizando uma transmissão serial UART, uma imagem de uma máquina (client) deve ser enviada para outra máquina (server). A segunda aplicação deve receber a imagem e retornar ao cliente um número correspondente ao tamanho do arquivo de imagem transmitido (número de bytes). Assim que o cliente receber a resposta, deverá verificar se o tamanho recebido condiz com o tamanho real da imagem. O tempo de transmissão deve ser cronometrado, com o intuito de obter a maior taxa de bytes por segundo possível

Para a execução, ambas as aplicações client e server devem ser rodadas independentemente com a utilização de dois arduinos ou um simulador de portas em loopback.

------------------

Assignment 2 for the Camada Física da Computação (Physical Layer of Computer Science) class. Utilizing a UART serial communication protocol, a machine (client) must send an image (chosen by the user) to another machine (server). The second application must receive the image and return a number that represents the size of the transmitted file (amount of bytes) to the client. As soon as the client receives the response, it will verify if the size received corresponds to the real image's size. The time of the transmission shall be calculated, with the intention of obtaining the highest bytes per second rate possible. 

In order to run the program, both the client and server applications must be run independently, along with the using of either two arduinos or a serial port simulator in loopback configuration. 
