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
        return render_template('spicyfuture.html', a=a, c=c)
    if (spicevalue <= 3 and c == '2'):
        return render_template('nospiceonlycream.html', a=a, c=c)
    if (spicevalue <=3 and c == '1'):
        return render_template('notsospice.html')
    else:
        return "you broke our quiz please retake for better results"


#class challenge routes
@app.route('/square/<int:number>')
def square(number):
    numbersquare = number * number
    request.args 
    return str(numbersquare)

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

if __name__ == '__main__':
    app.run(debug=True)