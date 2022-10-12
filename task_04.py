# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

file_task_04 = open('new_file_task_04', 'w', encoding='utf-8')
file_task_04.write('aaaaaadddddbbbbcccffy')
file_task_04.close()

new_file_ = open('new_file_task_04', 'r', encoding='utf-8')
list_file_ = list(new_file_.read())
new_file_.close()
print(list_file_)

list_element = []
list_amout = []
index = len(list_file_)

for i in range(index):
    count = 0
    val_ = list_file_[i]
    for j in range(index):
        while val_ == list_file_[j]:
            if val_ == list_file_[i-1]:
                break
            elif val_ == list_file_[j]:
                count += 1
                break
    if count > 0:
        list_element.append(list_file_[i])
        list_amout.append(count)


list_file_compress = []
for k in range(len(list_element)):
    list_file_compress.append(list_element[k] + str(list_amout[k]))

print(list_file_compress)