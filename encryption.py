import random

def create_gamma1(plaintext, key, start_value):
    gamma = ''
    random.seed(start_value)
    for _ in range(len(plaintext)):
        shift = ord(key)
        gamma += chr(shift)
    return gamma

def create_gamma2(plaintext, key, start_value):
    gamma = ''
    random.seed(start_value)
    for _ in range(len(plaintext)):
        xor = ord(key) ^ start_value
        gamma += chr(xor)
    return gamma


def encrypt(plaintext, gamma, language):
    cipher = ''
    if language == 1:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,!?;:() -–—"\n'
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,!?;:() -–—"\n'
    for i in range(len(plaintext)):
        if plaintext[i] in alphabet:
            idx = alphabet.index(plaintext[i])
            shift = ord(gamma[i])
            new_idx = (idx - shift) % len(alphabet)
            cipher += alphabet[new_idx]
    return cipher
0
def decrypt(cipher, gamma, language):
    decrypted_text = ''
    if language == 1:
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,!?;:() -–—"\n'
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,!?;:() -–—"\n'
    for i in range(len(cipher)):
        if cipher[i] in alphabet:
            idx = alphabet.index(cipher[i])
            shift = ord(gamma[i])
            new_idx = (idx + shift) % len(alphabet)
            decrypted_text += alphabet[new_idx]
    return decrypted_text

def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

choice = int(input("Выберите функцию создания гамма-шифра (1 - сдвиг, 2 - XOR): "))
language = int(input("Выберете язык (1 - русский, 2 - английский): "))
sets = int(input("Выберете режим (1 - шифрование, 2 - расшифровка): "))

if sets == 1:
    if choice == 1:
        key = input("Введите ключ для гаммирования (буква для сдвига или XOR): ")
        input_file = input("Файл для шифрования: ")
        output_file = input("Файл для сохранения зашифрованного текста: ")
        start_value = int(input("Введите стартовое значение: "))

        plaintext = read_from_file(input_file)
        gamma = create_gamma1(plaintext, key, start_value)

        cipher = encrypt(plaintext, gamma, language)
        # print("Зашифрованный текст:", cipher)

        write_to_file(output_file, cipher)

        print("Успешный успех!")
    elif choice == 2:
        key = input("Введите ключ для гаммирования (буква для сдвига или XOR): ")
        input_file = input("Файл для шифрования: ")
        output_file = input("Файл для сохранения зашифрованного текста: ")
        start_value = int(input("Введите стартовое значение: "))

        plaintext = read_from_file(input_file)
        gamma = create_gamma2(plaintext, key, start_value)

        cipher = encrypt(plaintext, gamma, language)
        # print("Зашифрованный текст:", cipher)

        write_to_file(output_file, cipher)

        print("Успешный успех!")
    else:
        print("Некорректный выбор")
else:
    if choice == 1:
        key = input("Введите ключ для гаммирования (буква для сдвига или XOR): ")
        input_file = input("Файл для шифрования: ")
        d_file = input("Файл для расшифровки: ")
        descrypt_file = input("Файл для сохранения расшифрованного текста: ")
        start_value = int(input("Введите стартовое значение: "))

        plaintext = read_from_file(input_file)
        gamma = create_gamma1(plaintext, key, start_value)

        cipher = read_from_file(d_file)
        # print("Зашифрованный текст:", cipher)

        decrypted_text = decrypt(cipher, gamma, language)
        # print("Расшифрованный текст:", decrypted_text)

        write_to_file(descrypt_file, decrypted_text)

        print("Успешный успех!")
    elif choice == 2:
        key = input("Введите ключ для гаммирования (буква для сдвига или XOR): ")
        input_file = input("Файл для шифрования: ")
        d_file = input("Файл для расшифровки: ")
        descrypt_file = input("Файл для сохранения расшифрованного текста: ")
        start_value = int(input("Введите стартовое значение: "))

        plaintext = read_from_file(input_file)
        gamma = create_gamma2(plaintext, key, start_value)

        cipher = read_from_file(d_file)
        # print("Зашифрованный текст:", cipher)

        decrypted_text = decrypt(cipher, gamma, language)
        # print("Расшифрованный текст:", decrypted_text)

        write_to_file(descrypt_file, decrypted_text)

        print("Успешный успех!")
    else:
        print("Некорректный выбор")

