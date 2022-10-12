# 5*. Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
#
# Входные и выходные данные хранятся в отдельных текстовых файлах.


file_task_05 = open('new_file_task_05', 'w', encoding='utf-8')
file_task_05.write('15234617')
file_task_05.close()

new_file_task = open('new_file_task_05', 'r', encoding='utf-8')
list_file_task = list(new_file_task.read())
new_file_task.close()


for i in range(len(list_file_task)):
    list_file_task[i] = int(list_file_task[i])


def list_ask_seq(list_):
    list_ask = []
    for i in range(len(list_)):
        if list_[i] == max(list_[:i+1:]) and list_[i] not in list_ask:
            list_ask.append(list_[i])
    return list_ask

def liat_delit(list_):
    for i in range(1, len(list_)):
        val_ = max(list_[:i + 1:])
        while val_ in list_:
            list_.remove(val_)
            return list_


file_task_05_result = open('new_file_task_05_result', 'w', encoding='utf-8')
file_task_05_result.write(f'{list_file_task} \n')
file_task_05_result.close()

file_task_05_result = open('new_file_task_05_result', 'a', encoding='utf-8')
list_result = list_ask_seq(list_file_task)
file_task_05_result.write(f'{list_result} \n')
liat_delit(list_file_task)
list_result = list_ask_seq(list_file_task)
file_task_05_result.write(f'{list_result} \n')
liat_delit(list_file_task)
list_result = list_ask_seq(list_file_task)
file_task_05_result.write(f'{list_result} \n')
liat_delit(list_file_task)
list_result = list_ask_seq(list_file_task)
file_task_05_result.write(f'{list_result} \n')
liat_delit(list_file_task)
list_result = list_ask_seq(list_file_task)
file_task_05_result.write(f'{list_result} \n')
liat_delit(list_file_task)
list_result = list_ask_seq(list_file_task)
file_task_05_result.write(f'{list_result} \n')
file_task_05_result.close()




