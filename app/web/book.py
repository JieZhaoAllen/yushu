"""
Created by Allen on '2018/5/26 13:32'
"""
from flask import jsonify

from fisher.helper import is_isbn_or_key
from fisher.yushu_book import YuShuBook
from fisher import app

__author__ = 'Allen'



@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if is_isbn_or_key == "isbn":
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)