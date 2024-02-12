

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Route for serving static files (CSS, JS, images, etc.)
app.route('/static/css/main.css')
def serve_static():
    return send_from_directory('static/css', 'main.css')

# Define the home route
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)




