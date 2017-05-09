""" Tests
"""
import doctest
import unittest

import zope.component
import zope.browserresource
import eea.faceted.vocabularies

from zope.component.testing import setUp, tearDown
from zope.configuration.xmlconfig import XMLConfig


def configurationSetUp(self):
    """ Setup
    """
    setUp()
    XMLConfig('meta.zcml', zope.component)()
    XMLConfig('meta.zcml', zope.browserresource)()
    XMLConfig('configure.zcml', eea.faceted.vocabularies)()


def test_suite():
    """ Suite
    """
    flags = (doctest.ELLIPSIS |
             doctest.NORMALIZE_WHITESPACE |
             doctest.REPORT_ONLY_FIRST_FAILURE)

    return unittest.TestSuite((
        doctest.DocFileSuite('README.txt',
                     package='eea.faceted.vocabularies',
                     setUp=configurationSetUp,
                     tearDown=tearDown,
                     optionflags=flags),
        ))
