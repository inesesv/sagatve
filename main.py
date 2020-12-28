from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'sveika  hello hell'
@app.route('/json')
def hello_world1():
    f=open('dati.json','r',encoding='utf-8')
    return f.read()
if __name__ == '__main__':
    app.run(debug=True)
