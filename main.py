import qrcode
import date
import os
# пример данных можно отредактировать в date.py
data = date.site
# имя конечного файла
filename = date.name
# создаем директорию для сохранения
os.chdir('qrcodes')
# генерируем qr-код
img = qrcode.make(data)
# сохраняем img в файл
img.save(filename)