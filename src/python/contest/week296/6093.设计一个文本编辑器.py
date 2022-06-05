#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   6093.设计一个文本编辑器.py
@Time    :   2022/06/05 11:01:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   Copyright © 2020, wylu-CHINA-SHENZHEN. All rights reserved.
@Desc    :
"""


class Node:

    def __init__(self, val='#', prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class TextEditor:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cursor = self.head
        self.indice = 0
        self.total = 0

    def addText(self, text: str) -> None:
        tmp = self.cursor.next
        for ch in text:
            self.cursor.next = Node(ch, prev=self.cursor)
            self.cursor = self.cursor.next
        self.cursor.next = tmp
        tmp.prev = self.cursor
        self.indice += len(text)
        self.total += len(text)

    def deleteText(self, k: int) -> int:
        k = min(k, self.indice)
        self.indice -= k
        self.total -= k

        tmp = self.cursor.next
        for _ in range(k):
            self.cursor = self.cursor.prev
        self.cursor.next = tmp
        tmp.prev = self.cursor
        return k

    def cursorLeft(self, k: int) -> str:
        k = min(k, self.indice)
        self.indice -= k
        for _ in range(k):
            self.cursor = self.cursor.prev

        res = []
        cur = self.cursor
        for _ in range(min(self.indice, 10)):
            res.append(cur.val)
            cur = cur.prev
        res.reverse()
        return ''.join(res)

    def cursorRight(self, k: int) -> str:
        k = min(k, self.total - self.indice)
        self.indice += k
        for _ in range(k):
            self.cursor = self.cursor.next

        res = []
        cur = self.cursor
        for _ in range(min(self.indice, 10)):
            res.append(cur.val)
            cur = cur.prev
        res.reverse()
        return ''.join(res)

    def __str__(self) -> str:
        res = []
        cur = self.head.next
        while cur != self.tail:
            res.append(cur.val)
            cur = cur.next
        return ''.join(res)


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)

if __name__ == '__main__':
    obj = TextEditor()
    # ["TextEditor","addText","deleteText","addText","cursorLeft","addText","deleteText","addText","cursorLeft","deleteText"]
    # [[],["arnvmumatgmyw"],[5],["zrlufuifuy"],[2],["unh"],[20],["kwwp"],[6],[9]]
    obj.addText('arnvmumatgmyw')
    print(obj)
    print("==================================")

    print(obj.deleteText(5))
    print(obj)
    print("==================================")

    obj.addText('zrlufuifuy')
    print(obj)
    print("==================================")

    print(obj.cursorLeft(2))
    print(obj)
    print("==================================")

    # ==============================================================
    # ["TextEditor","addText","cursorLeft","deleteText","cursorLeft","addText","cursorRight"]
    # [[],["bxyackuncqzcqo"],[12],[3],[5],["osdhyvqxf"],[10]]
    # obj.addText('bxyackuncqzcqo')
    # print(obj)
    # print("==================================")

    # print(obj.cursorLeft(12))
    # print(obj)
    # print("==================================")

    # print(obj.deleteText(3))
    # print(obj)
    # print("==================================")

    # print(obj.cursorLeft(5))
    # print(obj)
    # print("==================================")

    # obj.addText('osdhyvqxf')
    # print(obj)
    # print("==================================")

    # print(obj.cursorRight(10))
    # print(obj)
    # print("==================================")

    # ==============================================================
    # obj.addText('leetcode')
    # print(obj)

    # print(obj.deleteText(4))
    # print(obj)

    # obj.addText('practice')
    # print(obj)

    # print(obj.cursorRight(3))
    # print(obj)

    # print(obj.cursorLeft(8))
    # print(obj)

    # print(obj.deleteText(10))
    # print(obj)

    # print(obj.cursorLeft(2))
    # print(obj)

    # print(obj.cursorRight(6))
    # print(obj)
