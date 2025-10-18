from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/goodbye')
def goodbye():
    return "<p>Goodbye, World!</p>"
@app.route('/greet/<name>')
def greet(name):
    return f"<p>Hello, {name}!</p>"
@app.route('/showimage')
def show_image():
    return '''
    <html>
        <body>
            <h1>Here is an image:</h1>
            <img src="A online" alt="A online">
        </body>
    </html>
    ''' 
