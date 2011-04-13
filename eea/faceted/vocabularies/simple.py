""" Simple static vocabularies
"""
from zope.app.schema.vocabulary import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

#
# Use catalog
#
class UseCatalogVocabulary(object):
    """ Use catalog vocabulary
    """
    implements(IVocabularyFactory)

    def __call__(self, context=None):
        """ See IVocabularyFactory interface
        """
        items = (
            SimpleTerm('', '', 'No'),
            SimpleTerm('portal_catalog', 'portal_catalog', 'Yes'),
        )
        return SimpleVocabulary(items)

UseCatalogVocabularyFactory = UseCatalogVocabulary()
#
# JsTree themes
#
class JsTreeThemes(object):
    """ Widget position in page
    """
    implements(IVocabularyFactory)

    def __call__(self, context=None):

        items = (
            SimpleTerm('default', 'default', 'Default'),
            SimpleTerm('classic', 'classic', 'Classic'),
            SimpleTerm('apple', 'apple', 'Apple'),
            SimpleTerm('green', 'green', 'Green'),
        )
        return SimpleVocabulary(items)

JsTreeThemesFactory = JsTreeThemes()
