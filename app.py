from flask import Flask, render_template
from api import API

app = Flask(__name__)


@app.route("/")
def home():
    api = API()

    date = api.get_date()
    deaths = api.get_deaths()
    cases = api.get_cases()

    return render_template("home.html", date=date, deaths=deaths, cases=cases)


if __name__ == "__main__":
    app.run()
