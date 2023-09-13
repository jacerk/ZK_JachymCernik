

import random




# Lists se znaky 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
symbols = ['@', '#', '$', '%', '^', '&', '*', '_', '+', '/', '-', '.', ',', '<', '>', '?', '!', '+']

#password is an empty list in which items from lists above are randomly appended to before the list is made into string
password = []
#definován počítač pro ustanovení délky uživatelem 
counter = 0

#########################################


def pickLetter():
    """Funkce na vybrání písmen"""
    letterPicker = random.randint(0, len(alphabet) - 1)
    password.append(alphabet[letterPicker])


def pickCapital():
    """Funkce na vybrání velkých písmen """
    capitalPicker = random.randint(0, len(capital) - 1)
    password.append(capital[capitalPicker])


def pickSymbol():
    """funkce na vybrání symbolů"""
    symbolPicker = random.randint(0, len(symbols) - 1)
    password.append(symbols[symbolPicker])


def pickNumber():
    """funkce na vybrání číselm"""
    number = random.randint(0, 9)
    password.append(str(number))




# merge function which takes the genereted password list and makes into string
def mergeList(password): #receives password list 
    """funkce do které je poslaný list který je následně konvertován na string"""
    string = ""
    for i in password: 
        string += i #adds the items in the list together into string
        
    return string


#randomizes and generetes the passwords
def randomizer(pass_length):
    """funkce randomizer příjmá délku hesla, a zároveň ujišťuje že passsword bude vždy mít všechny 4 typy symbolů
     to je zaručeno Booleany který se mění v případě že v heslu se objeví symbol nebo ne, program tak pojede dokuď zde nebudou všchny """
    numberPresent = False
    capitalPresent = False
    letterPresent = False
    symbolPresent = False

    
    runAgain = True
    
    while runAgain == True:
        password.clear()
        for i in range(pass_length): #
            choice = random.randint(1, 4)
            if choice == 1:
                pickLetter()
                letterPresent = True 
            if choice == 2:
                pickCapital()
                capitalPresent = True 
            if choice == 3:
                pickNumber()
                numberPresent = True
            if choice == 4:
                pickSymbol()
                symbolPresent = True
            
        if numberPresent and capitalPresent and letterPresent and symbolPresent: 
            runAgain = False
        else: 
            numberPresent = False
            capitalPresent = False
            letterPresent = False
            symbolPresent = False            

          
    product = (mergeList(password))
    return product


##################################

#user input
#quantity je uživatelský údaj o tom, kolik hesel chce uživatel vygenerovat.
# length
print("Dobrý den, vítejte v generátoru hesel, zadejte požadovanou délku hesla, které má alespoň 8 znaků.")
length = int(input("zvolte délku: "))

while length < 4:
    print("heslo musí být alespoň 4 znaky dlouhé")
    length = int(input("zvolte délku: "))
else:
    print("vaše heslo bude mít {} znaků".format(length))
    quantity = int(input("Zadejte požadovaný počet hesel, ze kterých chcete heslo vybrat.: "))
    
###################################
    
# hlavní proces
#Loop který se odehrává dle quantity, funkce randomizer je zavolána a je do ní poslaná požadovaná délka 
f = open("passwords.txt", "w")
for x in range(quantity):
    
    newPassword = randomizer(length)#lenght passed into randomizer 
    counter = counter + 1 #numbers the passwords genereted
    print("Password number {}. is:  {} ".format(counter, newPassword))#
    f.write(newPassword + "\n")

