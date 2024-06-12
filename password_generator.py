import random
x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
y = int(input("¿Cual es la longitud de la contraseña?: "))
password = ""
for i in range(y):
    z = random.choice(x)
    password += z    
print("La contraseña generada fue: ",password)
