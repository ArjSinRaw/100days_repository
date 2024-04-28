# f = open('sample.txt', '')
f = open("sample.txt",'w') # by default it take read mode
meta = f.write("arjun")
try:
    print(meta)
    f.close()
except Exception as e:
    print("Some error occured", e)