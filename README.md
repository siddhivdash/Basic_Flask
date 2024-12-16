# Flask Application - Basic Guide

This README provides an overview of how to set up a basic Flask application, navigate between tabs (routes), and deploy the app locally.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.7 or above
- pip (Python package manager)

## Getting Started

### Step 1: Install Flask

Run the following command to install Flask:

```bash
pip install flask
```

### Step 2: Create a Basic Flask App

Below is the code for a basic Flask application:

```python
from flask import Flask, render_template

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return "Welcome to the Flask App! Navigate to /about or /contact for other tabs."

# About Route
@app.route('/about')
def about():
    return "This is the About Page."

# Contact Route
@app.route('/contact')
def contact():
    return "This is the Contact Page."

if __name__ == '__main__':
    app.run(debug=True)
```

### Step 3: Run the Application

1. Save the above code in a file named `app.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory containing `app.py`.
4. Run the following command:

```bash
python app.py
```

### Step 4: Access the Application

After running the application, you will see output similar to this:

```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
```

Open your browser and visit the following URLs:

- `http://127.0.0.1:5000/` - Home Page
- `http://127.0.0.1:5000/about` - About Page
- `http://127.0.0.1:5000/contact` - Contact Page

### Step 5: Add Templates for Navigation (Optional)

If you want to use HTML templates for better navigation, create a `templates` folder in the same directory as `app.py`