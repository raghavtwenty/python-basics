a = open("notes.txt", "w")
a.write("hi hello")
a.close()

b = open("notes.txt", "r")
w = b.read()
words = w.split()
print("no of words:", len(words))
