# Создаем русский алфавит
rus_alphabet = 'абвгдеёжзийклмнопрстуфхцшщъыьэюяабвгдеёжзийклмнопрстуфхцшщъыьэюя'


#Предоставляем возможность выбрать расшифровку или зашифровку!
choise = input("Введите 'расшифровать' или 'зашифровать': ")
choise = choise.lower()

def shifr(choise):
    while True:
        #Проверяем, что написал пользователь
        if choise == 'зашифровать':

            # Просим пользвателя ввести текст для шифрования
            message = input('Введите ваш текст для шифрования: ')
            message = message.lower()

            # Просим пользователя ввести ключ шифрования
            key = int(input('Введите ключ шифрования: '))

            #Будет храниться зашифрованный текст
            shifr_text = ''

            # Перебирем все буквы, введенные пользователем
            for letter_message in message:
                if letter_message in rus_alphabet:
                    # Ищем букву в алфавите и сохраняем её индекс
                    position_in_alphabet = rus_alphabet.find(letter_message)

                    # Сохраняем индекс уже зашифрованной буквы
                    shifr_index = position_in_alphabet + key

                    # Сохраняем зашифрованную букву
                    shifr_letter = rus_alphabet[shifr_index]

                    # Сохраняем зашифрованный текст
                    shifr_text = shifr_text + shifr_letter
                else:
                    shifr_text = shifr_text + letter_message


            #Выводим текст на экран
            print(shifr_text)
            break


        elif choise == 'расшифровать':
            # Просим пользвателя ввести текст для расшифровки
            message = input('Введите ваш текст для расшифровки: ')
            message = message.lower()

            # Просим пользователя ввести ключ расшифровки
            key = int(input('Введите ключ расшифровки: '))

            # Будет храниться расшифрованный текст
            decipher_text = ''

            # Перебирем все буквы, введенные пользователем
            for letter_message in message:
                if letter_message in rus_alphabet:

                    # Ищем букву в алфавите и сохраняем её индекс
                    position_in_alphabet = rus_alphabet.find(letter_message)

                    # Сохраняем индекс уже расшифрованной буквы
                    shifr_index = position_in_alphabet - key

                    # Сохраняем расшифрованную букву
                    shifr_letter = rus_alphabet[shifr_index]

                    # Сохраняем расшифрованный текст
                    decipher_text = decipher_text + shifr_letter

                else:
                    decipher_text = decipher_text + letter_message

            # Выводим текст на экран
            print(decipher_text)
            break


        else:
            choise = input("Вы ввели неверно! "
                        "Введите 'расшифровать' или 'зашифровать': ")

shifr(choise)







