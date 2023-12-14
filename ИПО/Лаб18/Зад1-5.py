from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Загрузка изображения
img = Image.open("C:\GitHub\image.jpg")

# Сохранение изображения в другом формате
img.save('image1_25.png')

# Вывод характеристик изображения
print(f'Формат: {img.format}')
print(f'Размер: {img.size}')
print(f'Цветовой режим: {img.mode}')

# Поворот изображения
img_rotated = img.rotate(30)  # Измените угол на нужный вам
img_rotated.save('image2_25.png')

# Обрезка изображения
img_cropped = img.crop((0, 80, 600, 400))
img_cropped.save('image3_25.png')

# Применение фильтра к изображению
img_filtered = img_cropped.filter(ImageFilter.BLUR)  # Используйте любой фильтр, который вам нравится
img_filtered.save('image4_25.png')

# Применение нескольких фильтров к изображению
img_multi_filtered = img_cropped.filter(ImageFilter.BLUR).filter(ImageFilter.FIND_EDGES)
img_multi_filtered.save('image44_25.png')

# Создание объекта, позволяющего рисовать на изображении
draw = ImageDraw.Draw(img)
# Загрузка шрифта
font = ImageFont.truetype("arial", 16)
# Добавление текста в левом верхнем углу, заключенного в прямоугольник
text = "Сурвило"
text_color = "black"
background_color = "white"
text_position = (768, 387)
rectangle_size = draw.textbbox(text_position, text, font=font)
draw.rectangle(rectangle_size, fill=background_color)
draw.text(text_position, text, font=font, fill=text_color)
# Новое имя для сохранения подписанного изображения
new_name = 'image5_25.png'
# Сохранение изображения под новым именем
img.save("image5_25.png")

