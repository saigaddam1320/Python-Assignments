# Open the file and read its contents
file = open("sample.txt", "r")   # Change 'sample.txt' to your file name
text = file.read()

# Split the text into words and count them
words = text.split()
print("Number of words:", len(words))

# Close the file
file.close()
