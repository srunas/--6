import hashlib

name = str(input("Введите имя файла: "))


def hash_file(filename):
    h = hashlib.sha1()

    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()


message = hash_file(name)
file = open("database.txt")
database = file.read()
file.close()


if name in database:
    if message in database:
        print("Хэш файл есть в базе данных")
    else:
        print("Файл был изменён")
else:
    print("Хэша файла нет в базе данных")
    file = open("database.txt", "a")
    file.write(name + ' ' + message + '\n')
    file.close()
    print("Хэш добавлен в базу данных")
print(message)
