# https://docs.python.org/3/library/zipfile.html - nie zadziała. bo:
# "It supports decryption of encrypted files in ZIP archives,
# but it currently cannot create an encrypted file"

# lepiej: https://pypi.org/project/pyminizip/
# pyminizip.compress("/srcfile/path.txt", "file_path_prefix", "/distfile/path.zip", "password", int(compress_level))

# uwaga! ten kod wygenerował ChatGPT
import zipfile
# import pyminizip

filename = 'archive.zip'
password = b'haselko'

with zipfile.ZipFile(filename, mode='w', compression=zipfile.ZIP_DEFLATED) as archive:
    archive.setpassword(password) # docstring: """Set default password for encrypted files."""
    archive.write('file1.txt')
    archive.write('file2.txt')
    archive.write('file3.txt')

print(f'Archive file "{filename}" has been created with password "{password}".')

# lub :
"""
Sure, here's an example Python script for creating an encrypted archive zip file using the zipfile module:

python
Copy code
import zipfile

# Define the name of the archive file
archive_name = 'encrypted_archive.zip'

# Define the name of the file to be included in the archive
file_name = 'example.txt'

# Define the password for encrypting the archive
password = 'mysecretpassword'

# Create a new zip file and encrypt it with the given password
with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    zip_file.setpassword(password)

    # Add the file to the zip file
    zip_file.write(file_name)

print(f'Archive "{archive_name}" has been created and encrypted with the password "{password}".')
"""