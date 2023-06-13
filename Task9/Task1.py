# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
new_text = ''
with open('test_file/task1_data.txt', encoding='utf-8') as file:
    old_text = file.read()
    for char in old_text:
        if char.isdigit():
            continue
        new_text += char
with open('test_file/task1_answer.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(new_text)
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as new_text:
        answer = file1.readlines()
        ethalon = new_text.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')


