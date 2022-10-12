# 1. Напишите программу, удаляющую из текста все слова,
# содержащие ""абв"".

file_task_01 = open('new_file_task_01', 'w', encoding='utf-8')
file_task_01.write('абпабвторфабввбакиыфыабв')
file_task_01.close()

new_file_ = open('new_file_task_01', 'r', encoding='utf-8')
list_file_ = list(new_file_.read())
new_file_.close()

list_desired_object = ['а', 'б', 'в']
list_object_index = []
print('Исходный: ', *list_file_)
print('Искомые объекты: ', *list_desired_object)

for j in range(len(list_file_)-1):
    if (list_desired_object[0]==list_file_[j] and list_desired_object[1]==list_file_[j+1] \
            and list_desired_object[2]==list_file_[j+2]):
        list_object_index.append(j)
        list_object_index.append(j+1)
        list_object_index.append(j+2)

for i in range(len(list_object_index) - 1, -1, -1):
    index_ = list_object_index[i]
    if list_file_[index_] == list_desired_object[2] or list_file_[index_] == list_desired_object[1]\
            or list_file_[index_] == list_desired_object[0]:
        list_file_.pop(index_)

print('С удаленными элиментами: ', *list_file_)


