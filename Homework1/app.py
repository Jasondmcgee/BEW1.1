from flask import Flask, render_template, request

app = Flask(__name__)


#get user from data base 
#username = ""

@app.route('/', methods=['GET'])
def index():
    b = request.args.get('favoritecream')
    return render_template('fortune_form.html', b=b)

@app.route('/nextquestion', methods=['GET'])
def nextquestion():
    a = request.args.get('name')
    c = request.args.get('icecream')
    namevalues = [
        request.args.get('baby'),
        request.args.get('scary'),
        request.args.get('sporty'),
        request.args.get('ginger'),
        request.args.get('posh')]

    spicevalue = 0

    for value in namevalues:
        if (value != None):
            spicevalue = spicevalue + int(value)
    
    if (spicevalue >= 3 and c == '2'):
        return render_template('spicyfuture.html', a=a, c=c, test='test.js')
    if (spicevalue <= 3 and c == '2'):
        return render_template('nospiceonlycream.html', a=a, c=c)
    if (spicevalue <=3 and c == '1'):
        return render_template('notsospice.html')
    else:
        return "you broke our quiz please retake for better results"


#class challenge routes
@app.route('/square')
def square():
    value = int(request.args.get('number'))
    return str(value * value)

@app.route('/namextimes/<int:x>/<name>')
def lotsofnames(x, name):
    output = ""
    for i in range(0,x): 
        output = output + " "  + name
    return(output)

@app.route('/backwordname/<name>')
def backwardname(name):
    name = name[::-1]
    return name

@app.route('/weather', methods=['GET','POST'])
def sunnyornot():
    return """
    <form method=["POST"] action="/weather_request">
        <select name="weather">
            <option value="sunny">Sunny</option>
            <option value="sad">not sunny</option>
        </select>
        <input type="submit" value="Submit" >
    </form>
    """
@app.route('/weather_request')
def weather_report():
    report = request.args.get('weather')
    return render_template('weather.html', report=report)

@app.route('/item_details')
def details():
    """
    takes the url of the item and creates a page with the details
    """

#this is how post requests work
@app.route('/posttest')
def posting():
    return """
    <form action='/login' method='POST'>
    Username: <input type='text' name='username'>
    <br>
    Password: <input type='password' name='password'>
    <br>
    <input type='submit'>
    </form> """

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    return username + password

#docstring practice
def sum_2_numbers(x, y):
    """
    this function adds to numbers together

    x (int): first operand
    y (int): second operand
    """
    return x + y

def sum_of_list(list):
    """
    takes a list and sums all the numbers

    list(list): only operand
    """
    return sum(list)


if __name__ == '__main__':
    app.run(debug=True)