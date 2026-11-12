#ATM pin verification- provide a valid pin, get a pin from user and check the validity
pin=12345
atmpin=""
while atmpin!=pin:
    atmpin= int(input("Enter the pin: "))
    if atmpin!=pin:
        print("Invalid pin. 2 attempts left")
print("ATM pin verified successfully")