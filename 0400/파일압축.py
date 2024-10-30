import zipfile

def compress_file(file_path):
    with zipfile.ZipFile(file_path + '.zip', 'w') as zip_file:
        zip_file.write(file_path)

if __name__ == '__main__':
    compress_file('0314')