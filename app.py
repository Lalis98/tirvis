from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/aboutus')
def aboutus():
    return render_template('about.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/our-team')
def our_team():
    return render_template('our-team.html')


if __name__ == '__main__':
    app.run(debug=False)
