from flask import Flask,jsonify, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/work')
def how_it_works():
    return render_template('work.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        file = request.files['image']
        # Process the image file here
        # image = process_image(file)  # Function to convert image to model input format
        # result = your_ai_function(image)  # Call your AI model function
        result = {"message": "Image uploaded successfully"}  # Placeholder result
        return jsonify(result)
    return render_template('upload.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Save or send the data as needed
        return jsonify({"message": "Contact form submitted successfully"})
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
