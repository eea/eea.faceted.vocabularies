""" Utils
"""
from Products.CMFPlone.utils import safe_unicode
from zope.schema import interfaces
IVocabularyFactory = interfaces.IVocabularyFactory

#
# Util for sort method
#
def lowercase_text(values):
    return safe_unicode(values[1]).lower()
