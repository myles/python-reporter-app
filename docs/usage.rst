=====
Usage
=====

To use Python Reporter App in a project::

    from reporterapp import ReporterApp
    r = ReporterApp()

Get a list of questions::

    for q in r.questions:
        q.prompt

Get a list of snapshots::

    for s in r.snapshots:
        s.uniqueIdentifer
