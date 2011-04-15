""" Utils
"""
try:
    # Don't blame me, blame #pyflakes
    from zope.schema import interfaces
    IVocabularyFactory = interfaces.IVocabularyFactory
except ImportError:
    # < Zope 2.10
    from zope.app.schema import vocabulary
    IVocabularyFactory = vocabulary.IVocabularyFactory
#
# Util sort method
#
def compare(a, b):
    """ Compare lower values """
    if not isinstance(a, unicode):
        a = a.decode('utf-8')
    if not isinstance(b, unicode):
        b = b.decode('utf-8')
    return cmp(a.lower(), b.lower())
