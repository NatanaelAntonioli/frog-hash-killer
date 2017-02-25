import itertools
import hashlib
import os
import hashlib,binascii


composicao = True
tamanho = True
continuar = True
continuar2 = True
continuargeral = True
chrs = ""
criptografia: ""
codehash = ""

quadro = """

----------------------------
|   blake2s   | sha3_256   |            
|   sha512    | sha256     |            
|   sha3_512  | sha256     |            
|   sha224    | sha512     |            
|   sha384    | md5        |            
|   sha3_384  | blake2b    |            
|   sha1      | ntlm       |            
----------------------------

"""
logo = """                     

  ______ _____   ____   _____      _    _           _____ _    _       _  _______ _      _      ______ _____  
 |  ____|  __ \ / __ \ / ____|    | |  | |   /\    / ____| |  | |     | |/ /_   _| |    | |    |  ____|  __ \ 
 | |__  | |__) | |  | | |  __     | |__| |  /  \  | (___ | |__| |     | ' /  | | | |    | |    | |__  | |__) |
 |  __| |  _  /| |  | | | |_ |    |  __  | / /\ \  \___ \|  __  |     |  <   | | | |    | |    |  __| |  _  / 
 | |    | | \ \| |__| | |__| |    | |  | |/ ____ \ ____) | |  | |     | . \ _| |_| |____| |____| |____| | \ \ 
 |_|    |_|  \_\\_____/ \_____|    |_|  |_/_/    \_\_____/|_|  |_|     |_|\_\_____|______|______|______|_|  \_\ 

                            _____________________________________  CODADO POR: NATANAEL ANTONIOLI
  _.__-'@_    _------____/    ===  =============================   INSCREVA-SE: FÁBRICA DE NOOBS
 /     '--)  |               ________________/                     #MORTE AO MIOJO
/  >__<<_/   |      ___--_/(_)                  
 \\=x  \=x    |___---                                


 
"""

intro = """

1 - Identificar HASH (HashID)
2 - Realizar ataque de força bruta
3 - Realizar ataque de wordlist

"""

wordlistquadro = """

|-----------------------------------------------------------------------------------------------------------|
| palavrasptbr | Lista de palavras em Português do Brasil, retiradas do Dicionário Aurélio.                 |
| palavrasen   | Lista com mais de 400 mil palavras em Inglês                                               |
| nomesbr      | Mais de 25 mil nomes do Brasil                                                             |
| nomesint     | Nomes em inglês                                                                            |
| datas        | Todas as datas possíveis desde 1900 até 2100, no formado ddmmaaaa                          |
| datasint     | Todas as datas possíveis desde 1900 até 2100, no formado mmddaaaa                          |
| 10milhoesen  | 10 milhões de senhas mais utilizadas, em Inglês                                            |
| cinema       | Mais de 41 mil palavras envolvendo filmes, personagens e atores                            |
|-----------------------------------------------------------------------------------------------------------|


"""

################################## AQUI COMEÇA O CÓDIGO DE VERDADE ###############################


print(logo)
print(intro)


while continuargeral == True:
    menuprincipal = int(input("O que deseja fazer?"))
    
    if menuprincipal ==1:
        
        from sys import executable
        from subprocess import Popen, CREATE_NEW_CONSOLE

        Popen([executable, 'hashid.py'], creationflags=CREATE_NEW_CONSOLE)

        input('Pressione enter para retornar ao programa.')
        

    if (menuprincipal == 2) or (menuprincipal == 3):
        
        print(quadro)

        print("")   
        menu2 = str(input ("Qual algorítmo de hash deseja testar? Escreva o nome como mostrado no quadro."))
        print("")   

        hashcomp = str(input("Insira a hash."))
        print("")   

        criptografia = menu2

        codehash = "hashcerto = hashlib."
        codehash += criptografia
        codehash += "(senha6.encode())"
            
        if menuprincipal == 2:

            print ("")   
            print ("Componha sua amostragem utilizando os comandos abaixo:")
            print ("")   
            print ("1 - Caracteres a-z")
            print ("2 - Caracteres A-Z")
            print ("3 - Caracteres 0-9")
            print ("4 - Caracteres especiais !@#$%&*() ")
            print ("")
            print ("5 - Zerar padrões")
            print ("6 - Prosseguir")
            print ("")

            while composicao == True:
                
                menu1 = int(input("O que deseja fazer?"))
                print("")   
                if menu1 ==1: 
                    chrs += "abcdefghijklmnopqrstuvwxyz"
                if menu1==2:
                    chrs += "ABCDEFGHIJLKMNOPQRSTUVWXYZ"
                if menu1==3:
                    chrs += "0123456789"
                if menu1==4:
                    chrs += "!@#$%&*()"
                if menu1==5:
                    chrs = ""
                if menu1==6:
                    composicao = False


                    
            print("")
            minimo = int(input("Qual o mínimo de caracteres que deseja testar?"))
            print("")   
            maximo = int(input("Qual o máximo de caracteres que deseja testar?"))
            print("")
    
                
            for n in range(minimo, maximo+1):
                for xs in itertools.product(chrs, repeat=n):
                    if continuar == True:
                        if criptografia == "ntlm":
                            xs = str(xs)
                            xs = str(xs)
                            senha1 = (xs.replace("'", ""))
                            senha2 = (senha1.replace("(", ""))
                            senha3 = (senha2.replace(")", ""))
                            senha4 = (senha3.replace("'", ""))
                            senha5 = (senha4.replace(" ", ""))
                            senha6 = (senha5.replace(",", ""))
                            hash = hashlib.new('md4', xs.encode('utf-16le')).digest()
                            hashok = str((binascii.hexlify(hash)))
                            hashfinal = str(hashok.replace("'",""))
                            hashfinal = hashfinal[1:]
                            if hashfinal == hashcomp:
                                print ("")
                                print ("-------------------------------------------------------------")
                                print ("SUCESSO! A senha correspondente à hash é", senha6, "!")
                                wait = input("PRESSIONE ENTER PARA SAIR")
                                continuar = False
                                
                            else:
                                print ("A senha", senha6, "não corresponde. Sua hash é: ", hashfinal)
                        else:
                            
                            xs = str(xs)
                            senha1 = (xs.replace("'", ""))
                            senha2 = (senha1.replace("(", ""))
                            senha3 = (senha2.replace(")", ""))
                            senha4 = (senha3.replace("'", ""))
                            senha5 = (senha4.replace(" ", ""))
                            senha6 = (senha5.replace(",", ""))
                            exec(codehash)
                            hex_dig = hashcerto.hexdigest()
                            if hex_dig == hashcomp:
                                print ("")
                                print ("-------------------------------------------------------------")
                                print ("SUCESSO! A senha correspondente à hash é", senha6, "!")
                                wait = input("PRESSIONE ENTER PARA SAIR")
                                continuar = False
                                
                            else:
                                print ("A senha", senha6, "não corresponde. Sua hash é: ", hex_dig)

                    else:
                        a=0

        if menuprincipal ==3 :
            
            print (wordlistquadro)
            listauso = str(input("Escreva o nome da wordlist que deseja utilizar, exatamente como está no quadro. Caso possua uma wordlist personalizada em .txt, trasnfiara-a para o diretório do programa e insira  seu nome, sem extensão."))
            listauso += ".txt"
            with open (listauso, "r") as myfile:
                data= str(myfile.readlines())
                
            novo = data.split()

            for elem in novo:
                    palavra = (elem.replace("'", ""))
                    palavra = palavra[:-3] 
                    if continuar2 == True:
                        if criptografia == "ntlm":
                            palavra = str(palavra)
                            senha1 = (palavra.replace("'", ""))
                            senha2 = (senha1.replace("(", ""))
                            senha3 = (senha2.replace(")", ""))
                            senha4 = (senha3.replace("'", ""))
                            senha5 = (senha4.replace(" ", ""))
                            senha6 = (senha5.replace(",", ""))
                            hash = hashlib.new('md4', palavra.encode('utf-16le')).digest()
                            hashok = str((binascii.hexlify(hash)))
                            hashfinal = str(hashok.replace("'",""))
                            hashfinal = hashfinal[1:]
                            if hashfinal == hashcomp:
                                print ("")
                                print ("-------------------------------------------------------------")
                                print ("SUCESSO! A senha correspondente à hash é", senha6, "!")
                                print ("")
                                wait = input("PRESSIONE ENTER PARA SAIR")
                                continuar2 = False                                
                            else:
                                print ("A senha", senha6, "não corresponde. Sua hash é: ", hashfinal)                            
                        else:
                            xs = str(palavra)
                            senha1 = (xs.replace("'", ""))
                            senha2 = (senha1.replace("(", ""))
                            senha3 = (senha2.replace(")", ""))
                            senha4 = (senha3.replace("'", ""))
                            senha5 = (senha4.replace(" ", ""))
                            senha6 = (senha5.replace(",", ""))
                            exec(codehash)
                            hex_dig = hashcerto.hexdigest()
                            if hex_dig == hashcomp:
                                print ("")
                                print ("-------------------------------------------------------------")
                                print ("SUCESSO! A senha correspondente à hash é", senha6, "!")
                                print ("")
                                wait = input("PRESSIONE ENTER PARA SAIR")
                                continuar2 = False
                                                    
                            else:
                                print ("A senha", senha6, "não corresponde. Sua hash é: ", hex_dig)
                    else:
                        a = 0
        
