from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/aboutus.html')  # Add .html extension
def aboutus():
    return render_template('about.html')


@app.route('/services.html')  # Add .html extension
def services():
    return render_template('services.html')


@app.route('/our-team.html')  # Add .html extension
def our_team():
    return render_template('our-team.html')


if __name__ == '__main__':
    app.run(debug=False)
