""" EEA Faceted Vocabularies Installer
"""
import os
from setuptools import setup, find_packages

NAME = 'eea.faceted.vocabularies'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

tests_require = [
    'zope.component',
    ]

setup(name=NAME,
      version=VERSION,
      description="EEA Faceted Vocabularies",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zope3 vocabularies faceted eea plone zope python',
      author='European Environment Agency',
      author_email="webadmin@eea.europa.eu",
      url="http://svn.eionet.europa.eu/projects/",
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea', 'eea.faceted'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-

      ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
