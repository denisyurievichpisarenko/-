capitals = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У","Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ы", "Э", "Ю", "Я"]

def read_book(filename):
    f = open(filename, encoding = 'utf-8')
    text = f.read()
    f.close()
    return text


def listen_question():
    while True:
        question = input('Что жаждешь ты узнать, заплутавший? ')
        if question[-1] == '?':
            break
        else:
            print('Чёрная аура здешних мест и отсутствие вопросительной интонации в твоей речи смущают меня, о, странствующий!')
    return question


def answer(text, question):
    lines = text.splitlines()
    words_in_question = question.split()
    w = len(words_in_question)
    for word in lines[w: len(lines)]:
        if len(word) > 1 and len(words_in_question) <= len(lines) and word[0] in capitals:
            answer = word
            break
        elif len(words_in_question) >= len(lines):
            answer = 'начало'
            return answer


def print_answer(answer):
    print('Силы космоса транслировали мне ответ на твой вопрос: ', answer)


def main():
    magic_book = read_book(r'book.txt')
    vopros = listen_question()
    otvet = answer(magic_book, vopros)
    print_answer(otvet)


if __name__ == '__main__':
    main()

#Денис Писаренко, 2 вариант


