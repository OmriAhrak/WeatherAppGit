
import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    try:
        return render_template('template.html')
    except:
        return render_template("errors.html")


@app.route('/', methods=["POST", "GET"])
def parse():
    try:
        city = request.form.get("city")
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/next7days?unitGroup=metric&key=FEHEJ9RBDEYRXEYYRB3WUHE7C&contentType=json"
        data = requests.get(url).json()
    except:
        return render_template('errors.html')
    days = []
    nights = []
    humidity = []
    location = data["resolvedAddress"]
    currenthum = data["days"][0]["humidity"]
    temperature = data["days"][0]["temp"]
    description = data["description"]

    for i in range(7):
        days.append(data['days'][i]['hours'][11]['temp'])
        nights.append(data['days'][i]['hours'][23]['temp'])
        humidity.append(data['days'][i]['humidity'])

    weather = {"location": location, "days": days, "nights": nights, "humidity": humidity}
    return render_template("form.html", weather=weather, temperature=temperature, currenthum=currenthum,\
                           description=description, location=location)


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0')
