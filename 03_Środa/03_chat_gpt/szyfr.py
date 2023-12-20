import zipfile

# Define the name of the archive file
zip_file_name = "encrypted_archive.zip"

# Define the password for the archive
password = "Haselko"

# Create a ZipFile object with the name of the archive file
zip_file = zipfile.ZipFile(zip_file_name, mode="w")

# Add files to the archive
zip_file.write("file1.txt")
zip_file.write("file2.txt")

# Set the password for the archive
zip_file.setpassword(password.encode())

# Close the archive
zip_file.close()