"""
Created by Allen on '2018/4/20 17:33'
"""
__author__ = 'Allen'

from celery import Celery

app = Celery(__name__, broker='amqp://guest:guest@localhost:5672//')

@app.task

def add(x, y):   

        return x + y

作者：小怪聊职场
链接：https://www.jianshu.com/p/42b98f5eacb3
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。