# Assuming your test file is named test_nav_bar.py

# Import necessary libraries for testing
import pytest
from bs4 import BeautifulSoup

# Test case for the navigation bar
def test_nav_bar():
    # Load the HTML content of the template
    with open('your_template_path/nav_bar_template.html', 'r') as file:  # Replace 'your_template_path' with the path to your HTML template
        html_content = file.read()

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the navigation bar elements
    navbar_brand = soup.find('a', class_='navbar-brand')
    nav_links = soup.find_all('a', class_='nav-link')

    # Assertions to test the existence of navbar elements and links
    assert navbar_brand is not None
    assert len(nav_links) == 6  # Update this number based on the number of links in your navigation bar

    # Test specific links within the navigation bar
    assert navbar_brand['href'] == '/'
    assert nav_links[0]['href'] == '#'
    assert nav_links[1]['href'] == '/appt_scheduling'
    assert nav_links[2]['href'] == '/course/search'
    assert nav_links[3]['href'] == '/resource_library'
    assert nav_links[4]['href'] == 'https://bisonadvisor-mggczambhmgavuwfatao4a.streamlit.app/'
    assert nav_links[5]['href'] == '/profile'
