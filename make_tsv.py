import os
import glob
import hashlib
import base64

PREFIX = "https://raw.githubusercontent.com/cd-public/books/main/"

BK_DIR = "./books/"

OUT = "books.tsv"

def make_tsv():
    book_data = []
    file_paths = os.listdir(BK_DIR)
    files = [f for f in file_paths if f.endswith(".txt")]

    for file in files:
        size = os.path.getsize(os.path.join(BK_DIR, file))
        with open(os.path.join(BK_DIR, file), "rb") as f: # have to encode in binary first!
            data = f.read()
            md5 = hashlib.md5(data).digest()
            md5_64 = base64.b64encode(md5).decode("utf-8")
        url = PREFIX + file
        book_data.append((url, str(size), md5_64))
    return book_data

def write_tsv(output, input):
    with open(output, "w") as f:
        f.write("TsvHttpData-1.0\n")
        for item in input:
            f.write("\t".join(item) + "\n")

if __name__ == "__main__":
    data = make_tsv()
    write_tsv(OUT, data)