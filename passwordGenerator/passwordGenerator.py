import random
import string


want_Number=False
want_specialCharacter=False
print("A safe password must be of length more than 8")
length=int(input("Enter the length of Password you want:"))

while length<8:
    print("Length of Password must be more than or equal to 8")
    length=int(input("Enter the length of Password you want:"))


needNumber=input("Do you want any number in your password (yes/no):")
if (needNumber.lower()=="yes"):
    want_Number=True
else:
    want_Number=False
    

needSpecialCharacter=input("Do you want any special character in your password (yes/no):")
if (needSpecialCharacter.lower()=="yes"):
    want_specialCharacter=True
else:
    want_specialCharacter=False


def password_generator(length,Numbers=True,specialCharacter=True):
    alpha=string.ascii_letters
    numb=string.digits
    specialChar=string.punctuation
    
    characters=alpha

    if Numbers:
        characters+=numb
    if specialCharacter:
        characters+=specialChar
    
    pwd=""
    meet_criteria=False
    has_number=False
    has_specChar=False

    while not meet_criteria or len(pwd)<length:
        new_char=random.choice(characters)
        pwd+=new_char
        
        if new_char in numb:
            has_number=True
        elif new_char in specialChar:
            has_specChar=True
        
        meet_criteria=True
        if Numbers:
            meet_criteria=has_number
        if specialCharacter:
            meet_critera=meet_criteria and has_specChar
        
    return pwd
            
        

print(password_generator(length,want_Number,want_specialCharacter ))