try:
    f = open("t\\c.txt", "r", encoding="utf-8")
    content = f.read()
    split = content.split()
    count = len(split)
    print(content)
    print("Words: "+ str(count))
except:
    print("File unable to be opened.")

