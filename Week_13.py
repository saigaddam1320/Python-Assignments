
file = open("sample.txt", "r")   
text = file.read()

words = text.split()
print("Number of words:", len(words))

file.close()
