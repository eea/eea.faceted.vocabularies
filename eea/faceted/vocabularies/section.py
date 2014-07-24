""" Widget Sections Vocabularies
"""
from eea.faceted.vocabularies.utils import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

from eea.faceted.vocabularies import EEAMessageFactory as _

class WidgetSections(object):
    """ Widget position in page
    """
    implements(IVocabularyFactory)

    def __call__(self, context=None):

        items = (
            SimpleTerm('default', 'default', _('Basic search')),
            SimpleTerm('advanced', 'advanced', _('Extended search')),
        )
        return SimpleVocabulary(items)

__all__ = [
   IVocabularyFactory.__name__,
]
