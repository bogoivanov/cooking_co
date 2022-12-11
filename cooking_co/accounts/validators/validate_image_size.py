from django.core.exceptions import ValidationError


def megabytes_to_bytes(mb):
    return mb * 1024 * 1024


def validate_file_less_than_5mb(file_object):
    filesize = file_object.file.size
    megabyte_limit = 5.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f'Max file size is {megabyte_limit}MB')

