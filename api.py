import requests
from datetime import datetime


def beautify_number(number):
    return "{:,}".format(number)


class API:

    def __init__(self):
        self.data = requests.get("https://disease.sh/v3/covid-19/all").json()

    def get_date(self):
        if self.data is None:
            raise Exception("unable to get data from the server")

        date = int(self.data['updated']) / 1000
        fixed_date = datetime.utcfromtimestamp(date).strftime('%B %mst %Y, %-I:%M:%S %p')
        return {'date': fixed_date}

    def get_deaths(self):
        if self.data is None:
            raise Exception("unable to get data from the server")

        return {"totalDeaths": beautify_number(self.data['deaths']), "todayDeaths": beautify_number(self.data['todayDeaths'])}

    def get_cases(self):
        if self.data is None:
            raise Exception("unable to get data from the server")

        return {"totalCases": beautify_number(self.data['cases']), "todayCases": beautify_number(self.data['todayCases'])}
