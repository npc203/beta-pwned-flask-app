from flask import Flask,request,render_template
import re
app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def index():
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    email=request.form['email']
    if re.search(regex,email):
        data=pwned(email)
    else:
        data = "Please enter valid email!"
    return render_template('index.html',data=data)

def pwned(email):
    return 'Not pwned'

if __name__=='__main__':
    app.run()
