from django.core.exceptions import ValidationError
from PIL import Image
import io
import PyPDF2
import os


def validate_file_size(value):
    max_file_size = 10485760  # 10MB
    if value.size > max_file_size:
        raise ValidationError(f"Файл слишком большой. Максимальный размер файла: {max_file_size // 1048576}MB.")


def validate_file_type(value):
    allowed_extensions = ['jpg', 'jpeg', 'png', 'pdf']
    ext = value.name.split('.')[-1]
    if ext.lower() not in allowed_extensions:
        raise ValidationError(
            f"Недопустимый тип файла. Разрешены следующие типы файлов: {', '.join(allowed_extensions)}")


def validate_file_content(value):
    file_extension = os.path.splitext(value.name)[1].lower()

    if file_extension in ['.jpg', '.jpeg', '.png']:
        try:
            # Загрузка изображения из файла с помощью Pillow
            image = Image.open(value)
            # Проверка, является ли файл действительным изображением
            image.verify()
            # Если проверка прошла успешно, закройте файл
            value.seek(0)
        except Exception as e:
            raise ValidationError(f"Ошибка при чтении файла изображения: {e}")
    elif file_extension == '.pdf':
        try:
            # Загрузка PDF-файла с помощью PyPDF2
            reader = PyPDF2.PdfFileReader(value)
            # Проверка, является ли файл действительным PDF-файлом
            if not reader.getIsEncrypted() and reader.getNumPages() > 0:
                value.seek(0)
            else:
                raise ValidationError("Файл PDF поврежден или зашифрован.")
        except Exception as e:
            raise ValidationError(f"Ошибка при чтении файла PDF: {e}")
    else:
        raise ValidationError("Файл не поддерживается. Разрешены только файлы 'jpg', 'jpeg', 'png' и 'pdf'.")