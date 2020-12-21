from flask import Flask, Response, render_template, request
import json
from wtforms import TextField, Form
import pandas as pd


app = Flask(__name__)


class SearchForm(Form):
    stock = TextField('Insert Stock', id='stock_autocomplete')
    country = TextField('Insert Country', id='stock_autocomplete')


@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    nasdaq = list(pd.read_csv('utils/nasdaq_list.csv').iloc[:, 0])

    print(nasdaq)
    return Response(json.dumps(nasdaq), mimetype='application/json')




@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template("search.html", form=form)



@app.route("/submit", methods=['POST'])
def getUserInput():

    form = SearchForm(request.form)
    # get the city value from the form
    city = form.stock.data
    print(city)
    return render_template("search.html", form=form)


@app.route("/submitcountry", methods=['POST'])
def getCountryInput():

    form = SearchForm(request.form)
    # get the city value from the form
    country = form.country.data
    print(country)
    return render_template("search.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)
