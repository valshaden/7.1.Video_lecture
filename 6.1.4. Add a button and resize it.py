# 6.1.1. API сайтов
# 6.1.2. Создаем проект и репозиторий
# 6.1.3. Создаем функцию для загрузки изображений
# 6.1.4. Добавляем кнопку и изменяем размер

# Добавляем кнопку для повторной загрузки

from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image(url):
    try:
        # Отправляем GET-запрос с использованием requests.get()
        response = requests.get(url)
        # Проверяем успешность запроса (код ответа 200)
        response.raise_for_status()
        # Читаем байты из ответа в объект BytesIO
        image_data = BytesIO(response.content)
        # Открываем изображение с помощью PIL
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None

def set_image():
    # Вызываем функцию для загрузки изображения
    img = load_image(url)

    if img:
        # Устанавливаем изображение в метку
        label.config(image=img)
        label.image = img 

window = Tk()
window.title("Cats!")
window.geometry("600x520")

# Создаем метку без изображения
label = Label()
label.pack()

# Добавляем кнопку для обновления изображения
update_button = Button(text="Обновить", command=set_image)
update_button.pack()

url = 'https://cataas.com/cat'

# Вызываем функцию для установки изображения в метку
set_image()

window.mainloop()
