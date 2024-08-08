
file_path = r"C:\Users\Julia\Desktop\Юля\pass.txt"

menu = int(input("1 - зашифровать\n2 - расшифровать\nВыберите цифру и нажмите Enter: "))

if menu == 1:
    with open(file_path, "rb") as file:  # rb - бинарный режим
        txt = file.read()
    txt = txt.decode('cp1251')  # переводим значение byte
    bytes = txt.encode('cp1251')
    decode = int.from_bytes(bytes, byteorder='big')
    num = input("Введите любое число: ")  # вводим число, с помощью которого будем проводить шифрование
    output = int(decode) + int(num)  # складываем полученный массив байтов и число
    with open(file_path, "w") as file:  # записываем зашифрованный файл
        file.write(str(output))
    print("Зашифрованный файл записан")

elif menu == 2:
    with open(file_path, "rb") as file:  # читаем файл и извлекаем число из него
        txt = file.read()
    txt = txt.decode('cp1251')
    num = input("Введите число для расшифровки: ")  # вводим число, с помощью которого было зашифровано сообщение
    txt = int(txt) - int(num)  # находим исходный массив данных
    byte_str = int(txt).to_bytes((int(txt).bit_length() + 7) // 8, byteorder="big")  # переводим массив обратно в текст
    b = byte_str.decode('cp1251')  # byte переводим в str
    with open(file_path, "w") as file:  # записываем расшифрованный файл
        file.write(str(b))
    print("Расшифрованный файл записан")
