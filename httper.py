"""
Created by Allen on '2018/5/26 10:30'
"""
__author__ = 'Allen'
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        response = requests.get(url)
        if response.status_code != 200:
            return {} if return_json else ""
        return response.json() if return_json else response.text