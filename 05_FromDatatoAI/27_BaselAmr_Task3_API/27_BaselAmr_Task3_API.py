"""
Author: Basel Amr Barakat
Email: baselamr52@gmail.com
Date: 2025-01-07
Task Name : Simple Calculator Task
Task Number : 27
Part : Create the API & Configure Apache to Serve the API
Module : From Data to AI
Submit_Number : 1

Description:
In this task, you will create a simple REST API using Python's Flask (or a basic script) to manage data with GET and POST methods. The API will return JSON responses and 
handle errors with try-except blocks. Additionally, you will configure Apache on Windows to serve this API by setting up Virtual Hosts to host multiple domain names on a single server and configure URL routing.

Requirement 1:
Title: Create the API
Description: Use Python's Flask (or a basic Python script) to create a simple REST API.

Requirement 2:
Title: Configure Apache to Serve the API
"""

import os
import sqlite3
from flask import Flask, request, jsonify, render_template
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_marshmallow import Marshmallow
from flask_restx import Api, Resource, fields
import re  # Regular expression library for name validation

# Initialize Flask app, Marshmallow for serialization, and SQLite
app = Flask(__name__)
#   app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Set JWT secret key

#   jwt = JWTManager(app)
#   ma = Marshmallow(app)

# Create or connect to SQLite database and insert initial data
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        age INTEGER NOT NULL)''')
    
    # Insert initial data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        # Initial data to be inserted
        initial_data = [
            (1, "Basel Amr Barakat", "baselamr52@gmail.com", 26),
            (2, "Aya Amr Barakat", "ayaamr@gmail.com", 26),
            (3, "Mostafa Amr Barakat", "mostafa@gmail.com", 28)
        ]
        cursor.executemany("INSERT INTO users (id, name, email, age) VALUES (?, ?, ?, ?)", initial_data)
    
    conn.commit()
    conn.close()

# Call init_db to create the database and table if it doesn't exist
init_db()

# ---------------------- API Routes ----------------------

# Home Page
@app.route('/')
def home():
    """
    Home Page Route
    Description: Displays a welcome message with an image.
    Returns:
        HTML: Welcome page with an image.
    """
    return render_template('index.html')

# API Documentation Page - /docs
@app.route('/docs')
def docs():
    return render_template('docs.html')

# Handle invalid routes (404 error)
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors for undefined routes.
    Provides a custom error message and lists valid routes.

    Args:
        e: The exception object for the 404 error.

    Returns:
        JSON: List of valid routes.
    """
    valid_routes = [
        {"method": "GET", "route": "/"},
        {"method": "GET", "route": "/users"},
        {"method": "POST", "route": "/users"},
        {"method": "DELETE", "route": "/users/<id>"},
        {"method": "GET", "route": "/search"}
    ]
    return jsonify({
        "error": "Page not found",
        "message": "The route you entered does not exist.",
        "valid_routes": valid_routes
    }), 404

# GET Route: Retrieve all users
@app.route('/users', methods=['GET'])
def get_all_users():
    """
    Users Page Route
    Description: Displays all users in an HTML page or returns JSON data based on the request.
    Query Parameters:
        format (str): 'json' to return JSON response, otherwise returns HTML.
    Returns:
        HTML: User list rendered in a template.
        JSON: User list in JSON format.
    """
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()

        # Convert users list to a dictionary format
        user_list = [{"id": user[0], "name": user[1], "email": user[2], "age": user[3]} for user in users]

        # Check if 'format=json' is in the query string
        if request.args.get('format') == 'json':
            return jsonify(user_list), 200
        else:
            return render_template('users.html', users=users)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST Route: Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    """
    Add a new user to the SQLite database.
    Args:
        JSON: A JSON payload containing "id", "name", and "email".
    Description:
        - Validates required fields.
        - Checks for unique 'id' and 'email'.
        - Validates 'name' contains only alphabetic characters.
        - Validates 'email' format.
    Returns:
        JSON: A JSON response containing the status of the operation.
    """
    try:
        new_user = request.json  # Get JSON data from the POST request
        
        # Validate required fields
        if not new_user.get('id') or not new_user.get('name') or not new_user.get('email') or not new_user.get('age'):
            missing_fields = [field for field in ['id', 'name', 'email', 'age'] if field not in new_user]
            return jsonify({"error": f"Missing required field(s): {', '.join(missing_fields)}"}), 400  # 400: Bad Request
        
        # Validate name format (only letters and spaces)
        if not re.match("^[A-Za-z ]+$", new_user['name']):
            return jsonify({"error": "The 'name' field must only contain alphabetic characters and spaces."}), 400
        
        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", new_user['email']):
            return jsonify({"error": "Invalid email format."}), 400
        
        # Check if ID is unique
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE id=?", (new_user['id'],))
        if cursor.fetchone():
            conn.close()
            return jsonify({"error": "A user with this 'id' already exists."}), 400
        
        # Check if email is unique
        cursor.execute("SELECT email FROM users WHERE email=?", (new_user['email'],))
        if cursor.fetchone():
            conn.close()
            return jsonify({"error": "A user with this 'email' already exists."}), 400

        # Add the new user to the database
        cursor.execute("INSERT INTO users (id, name, email, age) VALUES (?, ?, ?, ?)", 
                       (new_user['id'], new_user['name'], new_user['email'], new_user['age']))
        conn.commit()
        conn.close()

        return jsonify({"message": "User added successfully"}), 201  # 201: Created
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 500: Internal Server Error

# DELETE Route: Delete a user by ID
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    Delete a user by ID.
    Args:
        id (int): The ID of the user to delete.
    Description:
        This endpoint deletes a user with the specified ID from the database.
    Returns:
        JSON: A JSON response with a success or error message.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Check if the user exists
        cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        user = cursor.fetchone()
        if not user:
            conn.close()
            return jsonify({"error": f"User with ID {id} not found."}), 404  # 404: Not Found

        # Delete the user
        cursor.execute("DELETE FROM users WHERE id=?", (id,))
        conn.commit()
        conn.close()

        return jsonify({"message": f"User with ID {id} deleted successfully."}), 200  # 200: OK
    
    except sqlite3.Error as db_error:
        return jsonify({"error": f"Database error: {str(db_error)}"}), 500  # 500: Internal Server Error
    
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500  # 500: Internal Server Error


# Search Route: Search for users by name or email
@app.route('/search', methods=['GET'])
def search_users():
    """
    Search for users by name or email.
    Args:
        query (str): The search query parameter.
    Description:
        This endpoint searches for users by name or email using a case-insensitive search.
    Returns:
        JSON: A list of matching users.
    """
    try:
        search_query = request.args.get('query')
        if not search_query:
            return jsonify({"error": "Query parameter is required"}), 400  # 400: Bad Request

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name LIKE ? OR email LIKE ?", 
                       ('%' + search_query + '%', '%' + search_query + '%'))
        users = cursor.fetchall()
        conn.close()

        if not users:
            return jsonify({"error": "No users found matching the search criteria"}), 404  # 404: Not Found

        # Convert users list to a dictionary format
        user_list = [{"id": user[0], "name": user[1], "email": user[2], "age": user[3]} for user in users]
        return jsonify(user_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 500: Internal Server Error
    
# Custom 404 Page
@app.errorhandler(404)
def page_not_found(e):
    """
    404 Error Page Route
    Description: Custom page for 404 errors.
    Returns:
        HTML: 404 error page content.
    """
    return render_template('404.html'), 404

# Users Page
@app.route('/users')
def list_users():
    """
    Users Page Route
    Description: Displays all users in a table format.
    Returns:
        HTML: List of users.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template('users.html', users=users)

# Contact Page
@app.route('/contact')
def contact():
    """
    Contact Page Route
    Description: Displays contact information or form.
    Returns:
        HTML: Contact page content.
    """
    return render_template('contact.html')

# About Page
@app.route('/about')
def about():
    """
    About Page Route
    Description: Provides information about the application.
    Returns:
        HTML: About page content.
    """
    return render_template('about.html')

# Settings Page
@app.route('/settings')
def settings():
    """
    Settings Page Route
    Description: Allows users to adjust application preferences.
    Returns:
        HTML: Settings page.
    """
    return render_template('settings.html')


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False)
