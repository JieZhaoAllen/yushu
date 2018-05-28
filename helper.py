"""
Created by Allen on '2018/5/25 18:53'
"""
__author__ = 'Allen'


def is_isbn_or_key(word):
    """
    判断请求类型(isbn还是key)
    :param word:
    :return:
    """
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "isbn"
    short_word = word.replace("-", "")
    if "-" in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = "isbn"
    return isbn_or_key


def dd():
    pass