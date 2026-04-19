# Write + Read + Append

# Write
f = open("sample.txt", "w")
f.write("Hello\n")
f.close()

# Append
f = open("sample.txt", "a")
f.write("Welcome\n")
f.close()

# Read
f = open("sample.txt", "r")
print(f.read())
f.close()
