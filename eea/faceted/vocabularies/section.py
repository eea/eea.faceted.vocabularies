""" Widget Sections Vocabularies
"""
from eea.faceted.vocabularies.utils import IVocabularyFactory
from eea.faceted.vocabularies import EEAMessageFactory as _
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm


class WidgetSections(object):
    """ Widget position in page
    """
    implements(IVocabularyFactory)

    def __call__(self, *args, **kwargs):

        items = (
            SimpleTerm('default', 'default', _('Basic search')),
            SimpleTerm('advanced', 'advanced', _('Extended search')),
        )
        return SimpleVocabulary(items)
