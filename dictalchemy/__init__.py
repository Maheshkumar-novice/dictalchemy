# vim: set fileencoding=utf-8 :
"""

~~~~~~~~~~~
Dictalchemy
~~~~~~~~~~~

"""


from dictalchemy.classes import DictableModel
from dictalchemy.utils import make_class_dictable, asdict
from dictalchemy.errors import (DictalchemyError, UnsupportedRelationError,
                                MissingRelationError)

__all__ = ['DictableModel',
           'make_class_dictable',
           'asdict',
           'DictalchemyError',
           'UnsupportedRelationError',
           'MissingRelationError']
