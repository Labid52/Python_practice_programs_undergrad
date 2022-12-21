file_obj = open('square.txt', 'w')
for n in range(13):
    square = n * n
    file_obj.write(str(square))
    file_obj.write('\n')
file_obj.close()

file_obj_1 = open('square.txt', 'r')
content = file_obj_1.read()
print(content)
file_obj_1.close()