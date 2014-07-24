""" Types vocabularies
"""
import operator
from eea.faceted.vocabularies.utils import compare
from eea.faceted.vocabularies.utils import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from Products.CMFCore.utils import getToolByName

class PortalTypesVocabulary(object):
    """Vocabulary factory for portal types.
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        context = getattr(context, 'context', context)
        ttool = getToolByName(context, 'portal_types', None)
        if ttool is None:
            return None
        items = [ (ttool[t].Title(), t)
                  for t in ttool.listContentTypes() ]
        items.sort(key=operator.itemgetter(0), cmp=compare)
        items = [SimpleTerm(i[1], i[1], i[0]) for i in items]
        return SimpleVocabulary(items)
