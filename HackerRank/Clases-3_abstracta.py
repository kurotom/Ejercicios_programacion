# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self): pass

# Write MyBook class
class MyBook:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author

        Book.__init__(self, title, author)

        self.price = price

    def display(self):
        print("Title: {}".format(title))
        print("Author: {}".format(author))
        print("Price: {}".format(price))


"""
The Alchemist
Paulo Coelho
248
"""

title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
