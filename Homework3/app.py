from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/weather')
def index():
    return render_template('weather.html')

@app.route('/weather_results', methods=['POST'])
def results():
    city_name = str(request.form.get('city'))
    city = city_name.strip(" ")
    city = city.replace(" ", "+")
    api_key = "APPID=2608f679d4594364525f6c6cc2246c79"
    url = "http://api.openweathermap.org/"
    data = requests.get(url + "data/2.5/weather?q="+city+"&" + api_key)
    data = data.json()
    K = data['main']['temp']
    F_temp = (K - 273.15) * 9/5 + 32
    return render_template('results.html', F_temp=F_temp, city_name=city_name)


if __name__ == '__main__':
    app.run(debug=True)