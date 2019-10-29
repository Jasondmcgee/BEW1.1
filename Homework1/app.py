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

#this is how post requests work
@app.route('/posttest')
def posting():
    user = request.args.get('username')
    password = request.args.get('password')
    return 'username:' + str(user) + 'password:' + str(password)

@app.route('/firstpart', methods=['POST'])
def usernameandpassword():
    return """
    <form method=['POST'] action='/posttest'>
        whats your name? <input type='text' name='username'>
        whats your password<input type='text' name='password'>
        <input type="submit" value="Submit" >
    </form>
    """

if __name__ == '__main__':
    app.run(debug=True)