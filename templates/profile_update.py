"""""
###code to be added to app.py to update profile in database
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

# Assume you have a Profile model defined
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    # Add other profile fields as needed

@app.route('/update_profile', methods=['POST'])
def update_profile():
    if request.method == 'POST':
        profile_id = 1  # Assuming profile_id for the logged-in user
        profile = Profile.query.get(profile_id)
        if profile:
            profile.name = request.form['name']
            profile.email = request.form['email']
            # Update other profile fields as needed

            db.session.commit()
            return 'Profile updated successfully'

    return 'Failed to update profile'

@app.route('/profile')
def show_profile():
    profile_id = 1  # Assuming profile_id for the logged-in user
    profile = Profile.query.get(profile_id)
    return render_template('profile.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
"""