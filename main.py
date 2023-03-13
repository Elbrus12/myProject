import os

def makeQR():
    site = input('Введите точный URL-адрес или нужную вам вещь: ')  # Пишем сайт или различные вещи для QR
    name = str(input('Как хотите назвать изображение: ')) + ".png"  # Генерация имени для изображения
    # создаем директорию для сохранения
    dir_name = 'qrcodes'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    # пример данных можно отредактировать в date.py
    data = site
    # имя конечного файла
    filename = name
    # генерируем qr-код
    img = qrcode.make(data)
    # переходим в данную директорию
    fullpath = os.path.join(dir_name, filename)
    #сохраняем файл
    img.save(fullpath)

makeQR()