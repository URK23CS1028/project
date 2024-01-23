#encryption of a password 
from random import randint
import pickle
x=input("Enter your password:")
l2=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789#@$%^&*()!")
l=len(x)
encryption=[]
for i in range(l):
    x3=randint(0,l)
    encryption.append(l2[x3])
f=open("Encryption.txt",'w')
f.writelines(encryption)
f.close()
f2=open("bianr.bin",'wb')
pickle.dump(x,f2)
f2.close()
f2=open("bianr.bin",'rb')
decryption=pickle.load(f2)
print(decryption)
f2.close()