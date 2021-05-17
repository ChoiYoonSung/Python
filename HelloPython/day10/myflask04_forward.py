from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')

def home():
    title = 'List'
    mylist = ['a', 'b', 'c', 'd']
    objList = {}
    objList.append({'e_id' : '1', 'e_name' : '이름1', 'e_birth' : '1996'})
    objList.append({'e_id' : '2', 'e_name' : '이름2', 'e_birth' : '1997'})
    
    return render_template('index.html', mylist = mylist, title=title, objList = objList)

if __name__ == '__main__':
    app.run(debug=True)