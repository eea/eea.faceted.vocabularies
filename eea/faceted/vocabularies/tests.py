import unittest

import zope.app.component
import eea.faceted.vocabularies

from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig
from zope.testing import doctest
from zope.testing.doctestunit import DocFileSuite

def configurationSetUp(self):
    setUp()
    XMLConfig('meta.zcml', zope.app.component)()
    XMLConfig('configure.zcml', eea.faceted.vocabularies)()

def test_suite():
    flags = (doctest.ELLIPSIS |
             doctest.NORMALIZE_WHITESPACE |
             doctest.REPORT_ONLY_FIRST_FAILURE)

    return unittest.TestSuite((
        DocFileSuite('README.txt',
                     setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=flags),
        ))
