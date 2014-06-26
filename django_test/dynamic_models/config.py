
import os

from django.conf import settings
from django.db.models import CharField, IntegerField, DateTimeField

from .utils import metadata_filter


# The dynamic models that comes from different configuration files (models.yaml, etc.)
# have metadata that help us to build specific fields of django models. For example, 'id'
# is intended to set the name of model attribute. See 'models.yaml' for details.
# Please update this list if you have any extra attributes.
FIELDS_METADATA = ['title', 'type', 'id']

# Mapping rules.
DYNAMIC_FIELDS = {
    'char': {
        'type': metadata_filter(CharField),
        'settings': {
            'max_length': getattr(settings, 'DYNAMIC_MAX_LENGHT_CHAR', 128)
        }
    },
    'int': {
        'type': metadata_filter(IntegerField),
    },
    'date':{
        'type': metadata_filter(DateTimeField),
    },
}

APP_PATH = os.path.abspath(os.path.dirname(__file__))
DYNAMIC_MODELS = getattr(settings, 'DYNAMIC_MODELS_FILE', os.path.join(APP_PATH, "models.yaml"))
