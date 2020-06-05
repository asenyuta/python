# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке

file = open("Task-2.txt", "r")
lines = 0
for line in file:
    lines = lines + 1
    letters = len(line)
    in_word = False
    word_count = 0
    for letter in line:
        if letter != ' ' and in_word == False:
            word_count += 1
            in_word=True
        elif letter == ' ':
            in_word = False
    print(f"В строке {lines} - {word_count} слов")

print("Всего строк - ", lines)

file.close()
