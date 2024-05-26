# ASCII Art Generator

## Project Overview

The ASCII Art Generator is a Flask web application that allows users to upload images and convert them into ASCII art. The application resizes the uploaded images, converts them to grayscale, and then generates ASCII art from the grayscale images.

## About the Developer

This project was developed by Mohammed Rinshad P.

## Setup Instructions

To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/ascii-art-generator.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd ascii-art-generator
    ```

3. **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install the required packages using pip:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Flask application:**

    ```bash
    python app.py
    ```

7. **Open your web browser and go to http://127.0.0.1:5000 to access the application.**

## How to Use

1. Upload an image using the provided form.
2. Click the "Upload" button.
3. Once the image is uploaded, the original image and its corresponding ASCII art will be displayed.
4. Optionally, you can copy the ASCII art by clicking the "Copy ASCII Art" button.

## Credits

- This project uses Flask, a micro web framework for Python.
- ASCII art generation is based on image processing techniques using the PIL library.
