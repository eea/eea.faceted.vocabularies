""" Types vocabularies
"""
from eea.faceted.vocabularies.utils import lowercase_text
from eea.faceted.vocabularies.utils import IVocabularyFactory
from zope.interface import implementer
from zope.component.hooks import getSite
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from Products.CMFCore.utils import getToolByName


@implementer(IVocabularyFactory)
class PortalTypesVocabulary(object):
    """Vocabulary factory for portal types.
    """

    def __call__(self, *args, **kwargs):
        ttool = getToolByName(getSite(), 'portal_types', None)
        if ttool is None:
            return None
        items = [(ttool[t].Title(), t)
                 for t in ttool.listContentTypes()]
        items.sort(key=lowercase_text)
        items = [SimpleTerm(i[1], i[1], i[0]) for i in items]
        return SimpleVocabulary(items)
