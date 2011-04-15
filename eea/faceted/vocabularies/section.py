""" Widget Sections Vocabularies
"""
from eea.faceted.vocabularies.utils import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

class WidgetSections(object):
    """ Widget position in page
    """
    implements(IVocabularyFactory)

    def __call__(self, context=None):

        items = (
            SimpleTerm('default', 'default', 'Basic search'),
            SimpleTerm('advanced', 'advanced', 'Extended search'),
        )
        return SimpleVocabulary(items)

VocabularyFactory = WidgetSections()

__all__ = [
   IVocabularyFactory.__name__,
]
