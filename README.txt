========================
EEA Faceted Vocabularies
========================

Overview
========

Zope 3 vocabularies to be used within eea.facetednavigation


Contents
========

.. contents::

Installation
============

To get started you will simply need to add the package to your "eggs" and
"zcml" sections, run buildout and restart your Plone instance

  .. _`zc.buildout`: http://pypi.python.org/pypi/zc.buildout/

A sample buildout configuration file, i.e. ``buildout.cfg``, could look like
this::

  [buildout]
  parts = instance

  [instance]
  eggs =
      eea.faceted.vocabularies
  zcml =
    eea.faceted.vocabularies

Source code
===========

Latest source code in EEA svn:
   http://svn.eionet.europa.eu/repositories/Zope/trunk/eea.faceted.vocabularies


Copyright and license
=====================
The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The EEA Faceted Vocabularies (the Original Code) is free software;
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later
version.

Contributor(s):
 - Alin Voinea (Eau de Web),
 - Antonio De Marinis (European Environment Agency),
 - Alec Ghica (Eau de Web),
 - Sasha Vincic (Valentine Web Systems)
 - Thomas Desvenain (Ecreall, Lille, France)

More details under docs/License.txt

Funding
=======

  EEA_ - European Enviroment Agency (EU)

.. _EEA: http://www.eea.europa.eu/
