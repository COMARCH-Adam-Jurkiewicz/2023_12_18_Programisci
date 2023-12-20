# https://docs.python.org/3/library/zipfile.html - nie zadziała. bo:
# "It supports decryption of encrypted files in ZIP archives,
# but it currently cannot create an encrypted file"

# lepiej: https://pypi.org/project/pyminizip/
# pyminizip.compress("/srcfile/path.txt", "file_path_prefix", "/distfile/path.zip", "password", int(compress_level))

import pyminizip

filename = 'mini_archive.zip'
password = 'hasełko'
compress_level = 4
lista_plikow = ["file1.txt", "file2.txt", "file3.txt"]

pyminizip.compress_multiple(lista_plikow,
                   [],
                   filename,
                   password,
                   int(compress_level))

print(f'Archive file "{filename}" has been created with password "{password}".')

