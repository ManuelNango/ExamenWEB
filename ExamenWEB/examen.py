from flask import Flask, render_template

app = Flask(__name__)
    
@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

if __name__ == '__main__':
	app. run(port=4000, host="0.0.0.0")