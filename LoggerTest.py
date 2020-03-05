#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" test.py
Description:
"""
__author__ = "Anthony Fong"
__copyright__ = "Copyright 2020, Anthony Fong"
__credits__ = ["Anthony Fong"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Anthony Fong"
__email__ = ""
__status__ = "Prototype"

# Default Libraries #
import pathlib
import datetime


# Downloaded Libraries #


# Local Libraries #
from utilities.loggers.eventlogger import SubjectEventLogger


# Definitions #
# Classes #


# Main #
if __name__ == "__main__":
    path = pathlib.Path.cwd().joinpath("ECwork_B0w0_2020-01-16_11~58~09.h5")
    '''
    meth = SubjectEventLogger(test_path)
    with meth:
        meth.file_attrs
        print(meth.Subject)

    '''
    debug = SubjectEventLogger(path, subject="ECtest")
    with debug:
        debug.set_time()
        debug.append(**{"type_": "ThisChild", "1stField": 0})
        debug.resume_time(index=0)
        debug.append(**{"type_": "ThisChild", "1stField": 1})
        debug.get_event_type("ThisChild")
        debug.find_event(1579041281.5, type_="ThisChild")
        i, f = debug.find_event_range(1579041281.5, datetime.datetime.now(), "ThisChild")
        print(debug[0])

    reload = SubjectEventLogger(path)
    with reload:
        print(reload.event_types)
        child = reload.get_event_type("ThisChild")
        parent = reload.get_event_type("Events")
        print("done")
