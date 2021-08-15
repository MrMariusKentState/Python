
from flask import Flask, render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')
def template():
    return render_template("index.html")

@app.route('/play/<int:num>')          # The "@" decorator associates this route with the function immediately following
def template2(num):
    return render_template("index.html", num = num)

@app.route('/play/<int:num>/<string:color>')
def template3(num, color):
    return render_template("index.html", num = num, color = color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.