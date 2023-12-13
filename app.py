"""
1.python -m venv myenv
2. source myenv/bin/activate
3.$ pip install -r requirements.txt
4.$ python3 app.py - runs web server
http://127.0.0.1:5000/ to view changes locally
"""



from flask import Flask, render_template, redirect, url_for, session, request
# from werkzeug.urls import url_encode
# from flask_oauthlib.client import OAuth
from flask_sqlalchemy import SQLAlchemy
from model import db, User
import streamlit as st
import requests
import atexit
import streamlit as st


app = Flask(__name__)
app.secret_key = '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'  # Change this to your own secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database file
db.init_app(app)

# Replace these with your actual credentials
GOOGLE_CLIENT_ID = '976199159022-h9rdvh12gh6hiql3kvq7okjo4kepvp5r.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_REDIRECT_URI = 'http://127.0.0.1:5000/student'

app.config['GOOGLE_CLIENT_ID'] = GOOGLE_CLIENT_ID
app.config['GOOGLE_CLIENT_SECRET'] = GOOGLE_CLIENT_SECRET

# oauth = OAuth(app)
# google = oauth.remote_app(
#     'google',
#     consumer_key=app.config.get('GOOGLE_CLIENT_ID'),
#     consumer_secret=app.config.get('GOOGLE_CLIENT_SECRET'),
#     request_token_params={
#         'scope': 'email'
#     },
#     base_url='https://www.googleapis.com/oauth2/v1/',
#     request_token_url=None,
#     access_token_method='POST',
#     access_token_url='https://accounts.google.com/o/oauth2/token',
#     authorize_url='https://accounts.google.com/o/oauth2/auth'
# )

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/login')
# def login():
#     return google.authorize(callback=url_for('authorized', _external=True))


# @app.route('/logout')
# def logout():
#     session.pop('google_token', None)
#     return redirect(url_for('index'))


# @app.route('/login/authorized')
# def authorized():
#     resp = google.authorized_response()
#     if resp is None or resp.get('access_token') is None:
#         return 'Access denied: reason={}, error={}'.format(
#             request.args['error_reason'],
#             request.args['error_description']
#         )
    
#     session['google_token'] = (resp['access_token'], '')
#     user_info = google.get('userinfo')
#     # Here you can access user_info.data to get user details
#     return 'Logged in as: {}'.format(user_info.data['email'])


# @google.tokengetter
# def get_google_oauth_token():
#     return session.get('google_token')


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/sign_up')
def register():
    if request.method == 'POST':
        return redirect(url_for('profile'))
    return render_template('sign_up.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile(user_id):
    if request.method == 'POST':
        # Update student profile data here
        # Save updated details to database
        user = User.query.get_or_404(user_id)
        
        # Redirect to profile page after update
        return redirect(url_for('profile'))
    # Fetch student data from database and render profile template
    # student_data = {'name': 'John Doe', 'email': 'john@example.com', 'major': 'Computer Science'}
    return render_template('profile.html', user=user)

@app.route('/course/search', methods=['GET'])
def course_search():
    # Logic to fetch available courses from database
    courses = [{'code': 'CS101', 'name': 'Introduction to Computer Science', 'schedule': 'MWF 10:00AM'}]
    return render_template('course_search.html', courses=courses)

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/resource_library')
def resource_library():
    return render_template('resource_library.html')

@app.route('/advising_recommendation')
def advising_recommendation():
    return render_template('advising_recommendation.html')

@app.route('/appt_confirmation')
def appt_confirmation():
    return render_template('appt_confirmation.html')

@app.route('/appt_scheduling')
def appt_scheduling():
    return render_template('appt_scheduling.html')

@app.route('/advisor_dashboard')
def advisor_dashboard():
    return render_template('advisor_dashboard.html')

@app.route('/course/register/<course_code>', methods=['POST'])
def course_register(course_code):
    # Logic to register student for a course (check prerequisites, save to database)
    # Redirect to course search or confirmation page after registration
    return redirect(url_for('course_search'))




if __name__ == '__main__':
    app.run(debug=True)