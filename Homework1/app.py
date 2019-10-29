from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    b = request.args.get('nextq')
    return render_template('fortune_form.html', b=b)

@app.route('/nextquestion', methods=['GET'])
def nextquestion():
    a = request.args.get('name')
    c = request.args.get('icecream')
    return render_template('nextquestion.html', a=a, c=c)
if __name__ == '__main__':
    app.run(debug=True)