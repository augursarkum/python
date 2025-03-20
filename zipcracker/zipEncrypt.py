import pyzipper

# Files to add to zip
files_to_zip = input("Enter the file name to secure compress: ")
zip_filename = 'protected_archive.zip'
password = b'strong_password123'  # Password must be in bytes

with pyzipper.AESZipFile(zip_filename,
                         'w',
                         compression=pyzipper.ZIP_LZMA,
                         encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(password)
    zf.write(files_to_zip)
    print(f"Added {files_to_zip} to archive.")

print(f"Created password-protected ZIP: {zip_filename}")
