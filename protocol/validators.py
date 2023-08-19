from django.core.exceptions import ValidationError
from PIL import Image
import os


def validate_file_size(value):
    max_file_size = 1073741824  # 1000MB
    if value.size > max_file_size:
        raise ValidationError(f"The file is too large. Maximum file size: {max_file_size // 1073741824}MB.")


def validate_file_type(value):
    allowed_extensions = ['jpg', 'jpeg', 'png', 'pdf']
    ext = value.name.split('.')[-1]
    if ext.lower() not in allowed_extensions:
        raise ValidationError(
            f"The file is not supported. Only files allowed: {', '.join(allowed_extensions)}")


def validate_file_content(value):
    file_extension = os.path.splitext(value.name)[1].lower()

    if file_extension in ['.jpg', '.jpeg', '.png']:
        try:
            image = Image.open(value)
            image.verify()
            value.seek(0)
        except Exception as e:
            raise ValidationError(f"Error while reading image file: {e}")
    elif file_extension == '.pdf':
        if not value.read(4) == b"%PDF":
            raise ValidationError("The file is not a valid PDF.")
        value.seek(0)
    else:
        raise ValidationError("The file is not supported. Only files allowed 'jpg', 'jpeg', 'png' и 'pdf'.")
