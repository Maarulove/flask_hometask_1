from flask import Flask, url_for, render_template   

app = Flask(__name__)

"""
Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню, подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров. 
Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.
"""

@app.route("/")
def main_page():
    return render_template("main.html" )

@app.route("/Coats/")
def coats_():
    return render_template("coats.html")

@app.route("/shoes")
def shoes_():
    return render_template("shoes.html")



@app.route("/clothes")
def clothes_():
    return render_template("clothes.html")




