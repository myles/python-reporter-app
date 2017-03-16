===================
Python Reporter App
===================

.. image:: https://img.shields.io/travis/myles/python-reporter-app.svg
        :target: https://travis-ci.org/myles/python-reporter-app
        :alt: CI Status

.. image:: https://pyup.io/repos/github/myles/python-reporter-app/shield.svg
        :target: https://pyup.io/repos/github/myles/python-reporter-app/
        :alt: Dependencies Status

A Python library for interacting with Reporter App exports.

* Free software: MIT License

Features
--------

* TODO

Quick Start
-----------

    >>> from reporterapp import ReporterApp
    >>> r = ReporterApp()
    >>> for s in r.snapshots:
    ...     print(s.batteryDisplay)
    ...
    ...
    60%
    56%
    39%
    100%
