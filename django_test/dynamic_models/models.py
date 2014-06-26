
import yaml

from django.db import models

from .utils import get_model_fields
from .config import DYNAMIC_MODELS


def create_dynamic_models(config):
    dynamic_models = yaml.load(open(config))
    for model, settings in dynamic_models.iteritems():
        attrs = dict(
            Meta=type('Meta',
                (),
                {
                    'ordering': ('-id',),
                    'verbose_name': u'%s' % settings['title'],
                    'verbose_name_plural': u'%s' % settings['title'],
                }
            ),
            __module__=__name__,
            objects=models.Manager()
        )
        attrs.update(
            get_model_fields(settings['fields'])
        )
        yield model, type(
                model,
                (models.Model, ),
                attrs
        )

dynamic_models = dict(create_dynamic_models(DYNAMIC_MODELS))
