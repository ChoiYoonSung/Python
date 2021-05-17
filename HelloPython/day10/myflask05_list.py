from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')

def home():
    title = 'List'
    mylist = ['a', 'b', 'c', 'd']
    return render_template('index.html', mylist = mylist, title=title)

if __name__ == '__main__':
    app.run(debug=True)