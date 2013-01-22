# -*- coding: utf-8 -*-

""" django-popo -- Plain Old Python Object for Django """

__author__ = 'Grok <Grokzen@gmail.com>'
__version_info__ = (0, 1, 0)
__version__ = '.'.join(map(str, __version_info__))

# python std import
import inspect
from functools import wraps, WRAPPER_ASSIGNMENTS

# python std logging
import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

def __available_attrs(fn):
    """
    Copied from django.

    Return the list of functools-wrappable attributes on a callable.
    This is required as a workaround for http://bugs.python.org/issue3445.
    """
    return tuple(a for a in WRAPPER_ASSIGNMENTS if hasattr(fn, a))

def popo(**targets):
    """
    Main decorator. See README.md for usage examples.
    """
    def decorator(func):
        @wraps(func, assigned=__available_attrs(func) )
        def inner(request, *args, **kwargs):
            objs = {}

            for key, Class in targets.items():
                if not inspect.isclass(Class):
                    log.error("POPO: object is not class : %s" % Class)
                    continue

                instance = Class()

                for k, v in request.POST.items():
                    split = k.split(".")
                    if len(split) != 2:
                        continue
                    if key != split[0]:
                        continue
                    if not hasattr(instance, split[1]):
                        log.error("POPO: instance obj has not attr: %s" % split[1])
                        continue

                    setattr(instance, split[1], v)

                objs[key] = instance

            # Reinserts all parsed objects into the output to be passed down to the calling function
            kwargs.update(objs)

            return func(request, *args, **kwargs)
        return inner
    return decorator
