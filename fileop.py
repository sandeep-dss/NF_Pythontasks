
file1 = open("sample.txt", "r")
read_content = file1.read()
print(read_content)
file1.close()

file2 = open("sample2.txt", "w")
file2.write("Write operation replaced")
print(file2)
file2.close()
