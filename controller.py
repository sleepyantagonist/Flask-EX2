from model import guitar_shop_DAL as db

from flask import Flask, render_template

app = Flask(__name__, template_folder='view/templates', static_folder='view/static')


@app.route('/')
def index():
    category_list = db.get_all_categories()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
