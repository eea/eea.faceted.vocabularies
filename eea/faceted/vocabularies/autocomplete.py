""" Autocomplete widget specific vocabulary
"""
from eea.faceted.vocabularies.utils import IVocabularyFactory

from zope.component import getAdapters

from zope.interface import Attribute
from zope.interface import Interface
from zope.interface import implements

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class AutocompleteVocabulary(object):
    """
    Vocabulary factory listing autocomplete suggestions views
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        """
        See IVocabularyFactory interface
        """
        factories = getAdapters(
            (context, context.REQUEST),
            IAutocompleteSuggest
        )
        terms = [SimpleTerm(f[0], f[0], getattr(f[1], 'label', f[0]))
                 for f in factories]
        return SimpleVocabulary(terms)


class IAutocompleteSuggest(Interface):
    """
    Interface for views generating autocomplete suggestions vocabulary.
    """

    label = Attribute("Suggestions name")

    def __call__(self):
        """
        Should return a json array of value/label objects.
        eg: [{'value':'42', 'label:'Answer to some question..'}, ...]
        """
