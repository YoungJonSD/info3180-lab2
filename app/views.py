from app import app
from flask import render_template
import datetime


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html', name="Mary Jane")


def format_date_joined(date_joined):
    return date_joined.strftime("%B, %Y")


@app.route('/profile')
def profile():
    date_joined = datetime.date(2026, 2, 7)

    user = {
        "full_name": "Stephen-Jon Dixon",
        "username": "stephen",
        "location": "Kingston, Jamaica",
        "date_joined": format_date_joined(date_joined),
        "bio": "I am a web development student (again) who wants to start doing better in life with myself and taking things more seriously.",
        "posts": 7,
        "following": 100,
        "followers": 250
    }

    return render_template('profile.html', user=user)


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404