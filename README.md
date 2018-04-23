Flask注册路由的两种方法:
1.
@app.route('/hello')
def hello():
    return 'Hello word'

2.
def hello():
    return 'Hello word'
app.add_url_rule('/hello', view_func=hello)