import base64

def load_files():
    file_logins = open("logins", "r")
    file_passwds = open("passwords", "r")
    logins, passwds = [],[]
    for login in file_logins:
        logins.append(login.strip())

    for passwd in file_passwds:
        passwds.append(passwd.strip())
    return logins, passwds

def make_dict(logins, passwds):
    return dict(zip(logins,passwds))

def encrypt_b64(login_passwd):
    for login, passwd in login_passwd.items():
        login_passwd[login] = base64.b64encode(passwd.encode('ascii'))
    return login_passwd

def decrypt_b64(login_cryptopass):
    for login, passwd in login_cryptopass.items():
        login_cryptopass[login] = base64.b64decode(passwd).decode("utf-8", "ignore")
    return login_cryptopass

print("Loading files 'logins' and 'passwords'...")
logins, passwds = load_files()
login_passwd = make_dict(logins,passwds)
print("Dictionary of login:password...")
print(login_passwd)
print("Encrypted login:passwd...")
login_crypted = encrypt_b64(login_passwd)
print(login_crypted)
print("Decrypted login:passwd...")
login_decrypted = decrypt_b64(login_crypted)
print(login_decrypted)
