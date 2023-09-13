
def crypting(message):
    ''' Definujte funkci 'crypting', která na vstupu přijímá zprávu.'''
    alphabet= "abcdefghijklmnopqrstuvwxyz" 
            # Definujte abecedu jako string
              #0123456789  
    code = ""
    # Inicializujte prázdný string nazvaný "code", do kterého se uloží zašifrovaná/dešifrovaná zpráva.
    for x in message: # Iterujte každý znak 'x' ve vstupní zprávě.
        if(x!= " "): # kontrola zda neni znak mezera 
            place = alphabet.index(x) 
            #najde index v alpabete pro dany znak 
            if encrypting == True:  # zda globalni variable pro vybirani uzivatelskeho modu plati 
                newLetter = alphabet[(place + key)%26]
            if decrypting == True: 
                newLetter = alphabet[(place - (key-1))%26]
                #Vypočítejte novou pozici v abecedě pomocí klíče a v případě potřeby použijte modul pro obtékání.
            code = code + newLetter
            
        else:
            code = code + " "
    return code

      

def printMenu():
    '''menu '''
    print("1.encode")
    print("2.decode")
    print("3. quit")
    x = input("Enter an option ")
    return x
print("caesar cipher")
option = 1; #vstup do while loop 

# globalni variables na urceni uzivatelskoho pozadavku 
encrypting = False
decrypting = False 



# hlavni script ktery skonci s option 
while (option!= 3):
    
    option = int(printMenu())
    key = int(input("enter key"))
    if (option == 1): # encode
        c = open("output_file.txt", "w")
        encrypting = True
        with open('input_file.txt','r') as f:
            message = f.readline()
        message = crypting(message) #premena textu 
        print( )
        print(message)
        encrypting = False #reset pro cistou loop 

    if (option == 2): # decode
        c = open("output_file.txt", "w")
        decrypting = True
        with open('input_file.txt','r') as f:
            message = f.readline()
        message = crypting(message)
        print( )
        print(message)
        decrypting = False
    # Write the final message to 'output_file.txt' and append a newline.
    c.write(message + "\n")
    c.close()

