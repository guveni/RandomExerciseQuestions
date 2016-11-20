# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    
"""
__author__ = 'guven'


class StackQueue(object):

    def __init__(self):
        self.stack_enq = []
        self.stack_deq = []

    @staticmethod
    def _transfer(list_1, list_2):
        for item in list_1:
            list_2.append(item)

    def enqueue(self, new_obj):
        if not new_obj:
            return
        if len(self.stack_deq) > 0:
            self._transfer(self.stack_deq, self.stack_enq)
        self.stack_enq.append(new_obj)

    def dequeue(self):
        if len(self.stack_deq)  + len(self.stack_enq) == 0:
            raise ValueError('Empty Queue!!!')
        if len(self.stack_enq) > 0:
            self._transfer(self.stack_enq, self.stack_deq)
        return self.stack_deq.pop()

if __name__ == "__main__":
    queue = StackQueue()
    queue.enqueue(1)
    print queue.dequeue()