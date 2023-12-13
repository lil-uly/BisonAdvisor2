# Assuming your test file is named test_app.py

# Import necessary libraries for testing
import pytest
from app import app

# PyTest fixture to create a test client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test case for index route
def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Index Page' in response.data  # Adjust based on your index page content

# Test case for login route
def test_login_route(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login Page' in response.data  # Adjust based on your login page content

# Test case for profile route and functionality
def test_profile_route(client):
    response = client.get('/profile')
    assert response.status_code == 200
    # Add assertions to check profile rendering, content, and functionalit
def test_profile_template_rendering(client):
    # Simulate a GET request to the profile route/template
    response = client.get('/profile')  # Replace with your route URL

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that specific content is present in the response data
    assert b'<title>Profile</title>' in response.data
    assert b'<h2 class="mb-4">Profile</h2>' in response.data
    assert b'Full Name' in response.data
    assert b'Email' in response.data
    assert b'Major' in response.data
    assert b'Classification' in response.data
    assert b'Academic History' in response.data
    assert b'Update Profile' in response.data



def test_admin_route(client):
    # Simulate a GET request to the admin route
    response = client.get('/admin')  # Replace with your admin route URL

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that specific content is present in the response data
    assert b'<title>Admin Page</title>' in response.data  # Adjust based on your admin page content
    assert b'Welcome to Admin Page' in response.data 

def test_registration_route(client):
    # Simulate a GET request to the registration route
    response = client.get('/registration')  # Replace with your registration route URL

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that specific content is present in the response data
    assert b'<title>Registration Page</title>' in response.data  # Adjust based on your registration page content
    assert b'Welcome to Registration Page' in response.data 

def test_resource_library_route(client):
    # Simulate a GET request to the resource_library route
    response = client.get('/resource_library')  # Replace with your resource_library route URL

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that specific content is present in the response data
    assert b'<title>Resource Library</title>' in response.data  # Adjust based on your resource_library page content
    assert b'Welcome to Resource Library' in response.data  # Adjust based on your resource_library page content

    # Simulate a GET request to the advising_recommendation route
    response = client.get('/advising_recommendation')  # Replace with your advising_recommendation route URL

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that specific content is present in the response data
    assert b'<title>Advising Recommendation</title>' in response.data  # Adjust based on your advising_recommendation page content
    assert b'Welcome to Advising Recommendation' in response.data

def test_advising_recommendation_route(client):
    # Simulate a GET request to the advising_recommendation route
    response = client.get('/advising_recommendation')  # Replace with your advising_recommendation route URL

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that specific content is present in the response data
    assert b'<title>Academic Advising Recommendation</title>' in response.data  # Check page title
    assert b'Course Recommendations' in response.data  # Check for course recommendations section
    assert b'Major/Minor Suggestions' in response.data  # Check for major/minor suggestions section
    assert b'Academic Plan' in response.data

def test_appt_confirmation_route(client):
    # Simulate a GET request to the appt_confirmation route
    response = client.get('/appt_confirmation')  # Replace with your appt_confirmation route URL

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that specific content is present in the response data
    assert b'<title>Appointment Confirmation</title>' in response.data  # Check page title
    assert b'Appointment Confirmed!' in response.data  # Check for confirmation message
    assert b'Date: October 15, 2023' in response.data  # Check for appointment date
    assert b'Time: 10:00 AM' in response.data  # Check for appointment time
    assert b'Advisor: John Doe' in response.data  # Check for advisor name
    assert b'Location: Building A, Room 101' in response.data

def test_appt_scheduling_route(client):
    # Simulate a GET request to the appt_scheduling route
    response = client.get('/appt_scheduling')  # Replace with your appt_scheduling route URL

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that specific content is present in the response data
    assert b'<title>Appointment Scheduling</title>' in response.data  # Check page title
    assert b'Schedule an Appointment' in response.data  # Check for scheduling heading
    assert b'Available Dates' in response.data  # Check for available dates section
    assert b'Selected Appointment' in response.data 

def test_course_register_route(client):
    # Simulate a POST request to the course_register route with course code as input data
    response = client.post('/course/register/CS101', follow_redirects=True)  # Replace with your course_register route URL and course code

    # Assert the response status code is 200 (OK) or the expected redirection status code
    assert response.status_code == 200 or response.status_code == 302