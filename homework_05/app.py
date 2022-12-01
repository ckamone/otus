"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask
from flask import render_template, request

from views.products import products_app

app = Flask(__name__)
app.register_blueprint(products_app, url_prefix="/products")

@app.get("/")
def get_root():
    print(request.args)
    return render_template("index.html")

@app.route("/hello/")
def hello_world():
    return "<h1>Hello world!</h1>"


@app.route("/about/")
def about():
    return "<h1>text...</h1>"


if __name__ == "__main__":
    app.run(debug=True)
