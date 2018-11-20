l = []
while True:
    word = input('Введите слово: ')
    if word == '':
        break
    else:
        l.append(word)
with open (r"new 1.txt", "a", encoding="utf-8") as f:
    for i in range(len(l)):
        if len(l[i]) > 5:
            f.write(l[i])
            f.write('\n')
