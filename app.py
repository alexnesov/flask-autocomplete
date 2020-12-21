from flask import Flask, Response, render_template, request
import json
from wtforms import TextField, Form

app = Flask(__name__)


class SearchForm(Form):
    autocomp = TextField('Insert City', id='city_autocomplete')
    country = TextField('Insert Country', id='city_autocomplete')


@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
    cities = ["Olongapo City",
              "Angeles City",
              "Manila",
              "Makati",
              "Pasig",
              "Davao",
              "Cebu",
              "Quezon City",
              "Taguig"]
    print(cities)
    return Response(json.dumps(cities), mimetype='application/json')


@app.route("/submit", methods=['POST'])
def getUserInput():

    form = SearchForm(request.form)
    # get the city value from the form
    city = form.autocomp.data
    print(city)
    return render_template("search.html", form=form)


@app.route("/submitcountry", methods=['POST'])
def getCountryInput():

    form = SearchForm(request.form)
    # get the city value from the form
    country = form.country.data
    print(country)
    return render_template("search.html", form=form)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template("search.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
