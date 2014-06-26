
from functools import wraps


def get_model_fields(fields):
    """ Create django fields based on DYNAMIC_FIELDS (see `config.py`) """
    def create(field):
        django_field = DYNAMIC_FIELDS[field['type']]
        settings = django_field.get('settings', {})
        settings.update(field)
        return django_field['type'](settings)
    return (
        (field['id'], create(field))
        for field in fields
    )


def metadata_filter(cls):
    """ Remove metadata before passing attributes into Field* constructor """
    @wraps(cls)
    def wrapper(settings):
        return cls(
            settings['title'],
            **{k: v for k, v in settings.iteritems() if k not in FIELDS_METADATA}
        )
    return wrapper
from .config import DYNAMIC_FIELDS, FIELDS_METADATA
