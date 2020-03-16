#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" processingcoretest.py
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
import time

# Downloaded Libraries #


# Local Libraries #
import processingcore.processingcore as processingcore
from utilities.loggers.eventlogger import SubjectEventLogger


# Definitions #
# Classes #
class ProduceTask(processingcore.ProcessTask):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.number = 0

    def create_io(self):
        super().create_io()
        self.outputs.create_queue("RawQueueOut")

    def setup(self):
        print("Produce Setup in Process")

    def task(self, name=None):
        print("Producing an item...")
        item = self.number
        self.outputs.send_item("RawQueueOut", item)
        print("Item Sent")
        self.number += 1
        time.sleep(2)


class ProduceUnit(processingcore.ProcessingUnit):
    def construct(self, name=None, **kwargs):
        super().construct(name=name, **kwargs)
        self.set_task(ProduceTask(name=name))

    def setup(self):
        print("Produce Setup before Process")


# Main #
if __name__ == "__main__":
    take_one = ProduceUnit(name="GO", separate_process=True)
    take_one.start()
    time.sleep(10)
    take_one.stop()
    print("finish")
