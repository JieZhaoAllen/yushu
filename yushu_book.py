"""
Created by Allen on '2018/5/26 11:46'
"""
__author__ = 'Allen'
from httper import HTTP


class YuShuBook:
    isbn_url = "http://t.yushu.im/v2/book/isbn/{0}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={0}&count={1}&start={2}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.isbn_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result