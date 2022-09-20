from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.html')


@page.route('/terms')
def terms():
    return render_template('page/terms.html')


@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')


@page.route('/FAQ')
def FAQ():
    return render_template('page/FAQ.html')


@page.route('/create')
def create():
    return render_template('page/create.html')


@page.route('/update')
def update():
    return render_template('page/update.html')


@page.route('/calc')
def calc():
    return render_template('page/calculator.html')


@page.route('/datalist')
def datalist():
    return render_template('page/datalist.html')


@page.route('/delete')
def delete():
    return render_template('page/delete.html')


@page.route('/data')
def data():
    return render_template('page/data.html')





