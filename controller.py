from model import guitar_shop_DAL as db

from flask import Flask, render_template, request, url_for

app = Flask(__name__, template_folder='view/templates', static_folder='view/static')


@app.route('/', methods=['GET'])
def index():
    category_key = request.args.get('category_key')

    category_list = db.get_all_categories()

    if category_key is None or category_key not in category_list:
        category_key = category_list[1]
        return redirect(url_for('index', category_key=category_key)

    product_list = db.get_all_products_in_category(category_key)

    return render_template('index.html',
                           category_list=category_list,
                           product_list=product_list,
                           category_key=category_key)

@app.route('/delete_product', methods=['POST'])
def delete_product():
    product_code = request.form.get('product_code')
    db.delete_product(product_code)
    return redirect(url_for('index', category_key=category_key)

    if __name__ == '__main__':
    app.run()
