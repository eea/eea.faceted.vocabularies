from zope.app.schema.vocabulary import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

class WidgetPositions(object):
    """ Widget position in page
    """
    implements(IVocabularyFactory)

    def __call__(self, context=None):

        positions = (
            SimpleTerm('top', 'top', 'Top'),
            SimpleTerm('left', 'left', 'Left'),
            SimpleTerm('center', 'center', 'Center top'),
            SimpleTerm('right', 'right', 'Right'),
            SimpleTerm('bottomcenter', 'bottomcenter', 'Center bottom'),
            SimpleTerm('bottom', 'bottom', 'Bottom'),
        )
        return SimpleVocabulary(positions)

VocabularyFactory = WidgetPositions()
