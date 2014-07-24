""" Faceted vocabularies
"""
import operator
from eea.faceted.vocabularies.utils import compare
from eea.faceted.vocabularies.utils import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from Products.CMFCore.utils import getToolByName
#
# Intersect portal_types with portal_faceted types
#
class FacetedPortalTypesVocabulary(object):
    """Vocabulary factory for faceted portal types.
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        context = getattr(context, 'context', context)
        ptool = getToolByName(context, 'plone_utils', None)
        ttool = getToolByName(context, 'portal_types', None)
        ftool = getToolByName(context, 'portal_faceted', None)

        if ptool is None or ttool is None:
            return SimpleVocabulary([])

        items = dict((t, ttool[t].Title())
                     for t in ptool.getUserFriendlyTypes())

        if ftool is not None:
            faceted_items = dict((t.getId(), t.title_or_id())
                                 for t in ftool.objectValues())
            items.update(faceted_items)

        items = items.items()
        items.sort(key=operator.itemgetter(1), cmp=compare)

        items = [SimpleTerm(i[0], i[0], i[1]) for i in items]
        return SimpleVocabulary(items)

#
# Get only portal_faceted types
#
class FacetedOnlyPortalTypesVocabulary(object):
    """Vocabulary factory only for faceted portal types.
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        context = getattr(context, 'context', context)
        ftool = getToolByName(context, 'portal_faceted', None)

        if ftool is None:
            return SimpleVocabulary([])

        items = dict((t.getId(), t.title_or_id())
                     for t in ftool.objectValues())

        items = items.items()
        items.sort(key=operator.itemgetter(1), cmp=compare)

        items = [SimpleTerm(i[0], i[0], i[1]) for i in items]
        return SimpleVocabulary(items)
