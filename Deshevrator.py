import random
import string

# Определяем набор символов для кириллических букв
RUSSIAN_UPPER = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
RUSSIAN_LOWER = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ALL_RUSSIAN = RUSSIAN_UPPER + RUSSIAN_LOWER
ALL_CHARACTERS = string.ascii_letters + string.digits + ALL_RUSSIAN

def generate_key(length):
    """Генерирует случайный ключ длиной length из латинских букв, кириллических букв и цифр."""
    return ''.join(random.choice(ALL_CHARACTERS) for _ in range(length))

def vigenere_cipher_encrypt(text, key):
    """Шифрует текст с использованием шифра Виженера."""
    encrypted_text = ''
    key_length = len(key)
    key_index = 0
    
    for char in text:
        if char in string.ascii_letters:
            key_char = key[key_index]
            key_index = (key_index + 1) % key_length
            
            if char.isupper():
                start = ord('A')
                key_shift = ord(key_char.upper()) - ord('A')
            else:
                start = ord('a')
                key_shift = ord(key_char.lower()) - ord('a')
                
            encrypted_text += chr((ord(char) - start + key_shift) % 26 + start)
        elif char in RUSSIAN_UPPER:
            key_char = key[key_index]
            key_index = (key_index + 1) % key_length
            
            if key_char.isupper():
                start = ord('А')
                key_shift = ord(key_char.upper()) - ord('А')
            else:
                start = ord('а')
                key_shift = ord(key_char.lower()) - ord('а')
                
            encrypted_text += chr((ord(char) - start + key_shift) % 33 + start)
        elif char in RUSSIAN_LOWER:
            key_char = key[key_index]
            key_index = (key_index + 1) % key_length
            
            if key_char.isupper():
                start = ord('А')
                key_shift = ord(key_char.upper()) - ord('А')
            else:
                start = ord('а')
                key_shift = ord(key_char.lower()) - ord('а')
                
            encrypted_text += chr((ord(char) - start + key_shift) % 33 + start)
        elif char.isdigit():
            key_char = key[key_index]
            key_index = (key_index + 1) % key_length
            
            start = ord('0')
            key_shift = ord(key_char) - ord('0')
            encrypted_text += chr((ord(char) - start + key_shift) % 10 + start)
        else:
            encrypted_text += char  # Не изменяемые символы (например, пробелы и знаки препинания)
    
    return encrypted_text

def vigenere_cipher_decrypt(text, key):
    """Расшифровывает текст с использованием шифра Виженера."""
    decrypted_text = ''
    key_length = len(key)
    key_index = 0
    
    for char in text:
        if char in string.ascii_letters:
            key_char = key[key_index]
            key_index = (key_index + 1) % key_length
            
            if char.isupper():
                start = ord('A')
                key_shift = ord(key_char.upper()) - ord('A')
            else:
                start = ord('a')
                key_shift = ord(key_char.lower()) - ord('a')
                
            decrypted_text += chr((ord(char) - start - key_shift) % 26 + start)
        elif char in RUSSIAN_UPPER:
            key_char = key[key_index]
            key_index = (key_index + 1) % key_length
            
            if key_char.isupper():
                start = ord('А')
                key_shift = ord(key_char.upper()) - ord('А')
            else:
                start = ord('а')
                key_shift = ord(key_char.lower()) - ord('а')
                
            decrypted_text += chr((ord(char) - start - key_shift) % 33 + start)
        elif char in RUSSIAN_LOWER:
            key_char = key[key_index]
            key_index = (key_index + 1) % key_length
            
            if key_char.isupper():
                start = ord('А')
                key_shift = ord(key_char.upper()) - ord('А')
            else:
                start = ord('а')
                key_shift = ord(key_char.lower()) - ord('а')
                
            decrypted_text += chr((ord(char) - start - key_shift) % 33 + start)
        elif char.isdigit():
            key_char = key[key_index]
            key_index = (key_index + 1) % key_length
            
            start = ord('0')
            key_shift = ord(key_char) - ord('0')
            decrypted_text += chr((ord(char) - start - key_shift) % 10 + start)
        else:
            decrypted_text += char  # Не изменяемые символы
    
    return decrypted_text

def main():
    print("Выберите опцию:")
    print("1 - Шифрование")
    print("2 - Расшифрование")
    choice = input("Введите номер опции (1 или 2): ")

    if choice == '1':
        text = input("Введите текст для шифрования (можно использовать латинские, кириллические буквы и цифры): ")
        key_length = len(text)
        key = generate_key(key_length)
        print(f"Случайный ключ: {key}")

        encrypted_text = vigenere_cipher_encrypt(text, key)
        print(f"Зашифрованный текст: {encrypted_text}")

    elif choice == '2':
        text = input("Введите зашифрованный текст (можно использовать латинские, кириллические буквы и цифры): ")
        key = input("Введите ключ для расшифрования: ")
        
        if len(key) < len(text):
            print("Ошибка: ключ короче текста.")
            return
        
        decrypted_text = vigenere_cipher_decrypt(text, key)
        print(f"Расшифрованный текст: {decrypted_text}")

    else:
        print("Неверный выбор. Пожалуйста, введите 1 или 2.")

if __name__ == "__main__":
    main()