from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def home():
    if request.method =='GET': 
        a = request.args.get("a","World!")
    else:
        a = request.form.get("a","World!")
    return 'Hello, {}'.format(a)

if __name__ == '__main__':
    app.run(debug=True)