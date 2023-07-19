import pebl

with pebl.open("/foo.txt", "w") as f:
    f.write(b"hello world!")


with pebl.open("/foo.txt", "r") as f:
    print(f.read(20).decode())
