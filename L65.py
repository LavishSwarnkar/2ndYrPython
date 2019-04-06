f = open("files\\in.txt", mode="wb")
text = input("Enter text to be written:")
f.write(bytes(text.encode("utf-8")))
f.close()
print("File in.txt written successfully!")

