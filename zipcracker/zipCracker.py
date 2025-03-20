import pyzipper

zip_filename = input("Enter the file name to crack: ")
wordlist_file = 'wordlist.txt'

with open(wordlist_file, 'r') as f:
    passwords = f.read().splitlines()

found = False
for pwd in passwords:
    try:
        with pyzipper.AESZipFile(zip_filename) as zf:
            zf.setpassword(pwd.encode('utf-8'))
            # Try to list files; if it works, password is correct
            zf.namelist()
            print(f"[✔] Password found: {pwd}")
            found = True
            break
    except:
        print(f"[-] Incorrect: {pwd}")

if not found:
    print("[✘] Password not found in wordlist.")
