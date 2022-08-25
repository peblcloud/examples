import pebl

if handle := pebl.syscall.spawn():
    print("hello with:", handle)
else:
    print("hello world!")
