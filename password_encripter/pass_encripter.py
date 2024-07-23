from cryptography.fernet import Fernet

def generation__key():
    key = Fernet.generate_key()         # Generate the encrypt key
    with open('pass.key', 'wb') as f1:
        f1.write(key)                   # Save the encrypt key

def load_key():
    return open('pass.key', 'rb').read()

generation__key()

key=load_key()

password= b'26_75+ABcd0600'             # INSERT THE PASSWORD

f2 = open('pass.enc', 'wb')

clave = Fernet(key)                     # Instantiation of Fernet type object
pass_enc = clave.encrypt(password)
f2.write(pass_enc)                      # Save the encoded password
f2.close()
