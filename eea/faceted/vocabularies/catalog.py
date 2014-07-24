""" Catalog specific vocabularies
"""
import operator
from eea.faceted.vocabularies.utils import compare
from eea.faceted.vocabularies.utils import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from Products.CMFCore.utils import getToolByName
#
# Object provides
#
class ObjectProvidesVocabulary(object):
    """Vocabulary factory for object provides index.
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        """ See IVocabularyFactory interface
        """
        ctool = getToolByName(context, 'portal_catalog')
        if not ctool:
            return SimpleVocabulary([])

        provides = ctool.Indexes.get('object_provides', None)
        if not provides:
            return SimpleVocabulary([])

        items = list(provides.uniqueValues())
        items.sort(key=str.lower)
        items = [SimpleTerm(i, i, i) for i in items]
        return SimpleVocabulary(items)
#
# Catalog indexes
#
class CatalogIndexesVocabulary(object):
    """ Return catalog indexes as vocabulary
    """
    implements(IVocabularyFactory)

    def _labels(self, context):
        """ Get indexes labels from portal_atct settings
        """
        atool = getToolByName(context, 'portal_atct')
        indexes = atool.getIndexes()
        res = {}
        for index in indexes:
            ob = atool.getIndex(index)
            res[index] = ob.friendlyName

        return res

    def _create_vocabulary(self, context, indexes):
        """ Create voc
        """
        labels = self._labels(context)
        res = [(term, labels.get(term, '') or term) for term in indexes]
        res.sort(key=operator.itemgetter(1), cmp=compare)
        res.insert(0, ('', ''))
        items = [SimpleTerm(key, key, value) for key, value in res]
        return SimpleVocabulary(items)

    def __call__(self, context):
        """ See IVocabularyFactory interface
        """
        ctool = getToolByName(context, 'portal_catalog')
        indexes = ctool.Indexes.keys()
        return self._create_vocabulary(context, indexes)

#
# Rangeable catalog indexes
#
class RangeCatalogIndexesVocabulary(CatalogIndexesVocabulary):
    """ Filter catalog indexes for alphabetic widget
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        """ See IVocabularyFactory interface
        """
        ctool = getToolByName(context, 'portal_catalog')
        res = []
        for index in ctool.getIndexObjects():
            index_id = index.getId()
            if index.meta_type in ('FieldIndex',):
                res.append(index_id)

        return self._create_vocabulary(context, res)

#
# Alphabetic catalog indexes
#
class AlphabeticCatalogIndexesVocabulary(CatalogIndexesVocabulary):
    """ Filter catalog indexes for alphabetic widget
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        """ See IVocabularyFactory interface
        """
        ctool = getToolByName(context, 'portal_catalog')
        schema = ctool.schema()
        res = []
        for index in ctool.getIndexObjects():
            index_id = index.getId()
            if index_id not in schema:
                continue
            elif index.meta_type not in ('FieldIndex',
                                       'TextIndex', 'ZCTextIndex'):
                continue
            else:
                res.append(index_id)

        return self._create_vocabulary(context, res)

#
# Date range catalog indexes
#
class DateRangeCatalogIndexesVocabulary(CatalogIndexesVocabulary):
    """ Filter catalog indexes for daterange widget
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        """ See IVocabularyFactory interface
        """
        ctool = getToolByName(context, 'portal_catalog')
        res = []
        for index in ctool.getIndexObjects():
            index_id = index.getId()
            if index.meta_type in ('DateIndex', 'DateRecurringIndex'):
                res.append(index_id)

        return self._create_vocabulary(context, res)

#
# Text catalog indexes
#
class TextCatalogIndexesVocabulary(CatalogIndexesVocabulary):
    """ Filter catalog indexes for text widget
    """
    def __call__(self, context):
        """ See IVocabularyFactory interface
        """
        ctool = getToolByName(context, 'portal_catalog')
        res = []
        for index in ctool.getIndexObjects():
            index_id = index.getId()
            if index.meta_type not in ('DateIndex', 'DateRangeIndex'):
                res.append(index_id)

        return self._create_vocabulary(context, res)

#
# Path catalog indexes
#
class PathCatalogIndexesVocabulary(CatalogIndexesVocabulary):
    """ Filter catalog indexes for path widget
    """
    def __call__(self, context):
        """ See IVocabularyFactory interface
        """
        ctool = getToolByName(context, 'portal_catalog')
        res = []
        for index in ctool.getIndexObjects():
            index_id = index.getId()
            if index.meta_type in ('PathIndex', 'ExtendedPathIndex'):
                res.append(index_id)

        return self._create_vocabulary(context, res)

#
# Simple fields catalog indexes
# Monovalued indexes
#
class SimpleFieldCatalogIndexesVocabulary(CatalogIndexesVocabulary):
    """ Filter catalog indexes for simple fields
    """
    def __call__(self, context):
        """ See IVocabularyFactory interface
        """
        ctool = getToolByName(context, 'portal_catalog')
        res = []
        for index in ctool.getIndexObjects():
            index_id = index.getId()
            if index.meta_type in ('FieldIndex', 'BooleanIndex'):
                res.append(index_id)

        return self._create_vocabulary(context, res)
#
# Sorting catalog indexes
#
class SortingCatalogIndexesVocabulary(CatalogIndexesVocabulary):
    """ Also include sort_on and sort_order indexes
    """
    def __call__(self, context):
        voc = super(SortingCatalogIndexesVocabulary, self).__call__(context)
        terms = voc._terms
        terms.extend((
            SimpleTerm('sort_on', 'sort_on', 'Sort On'),
            SimpleTerm('sort_order', 'sort_order', 'Sort Order')
        ))
        return SimpleVocabulary(terms)
