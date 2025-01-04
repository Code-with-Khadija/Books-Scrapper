from flask import Flask, request, render_template_string
import time
app = Flask(__name__)
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Scrapper</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #FDF6E3;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: #FFFFFF;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 400px;
        }
        h1 {
            color: #2E86DE;
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        form {
            margin-top: 15px;
        }
        label {
            font-weight: bold;
        }
        input[type="number"] {
            width: 80%;
            padding: 10px;
            margin-top: 8px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 1em;
        }
        button {
            background-color: #2E86DE;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1em;
        }
        button:hover {
            background-color: #1B4F72;
        }
        .error {
            color: red;
            font-weight: bold;
            margin-top: 10px;
        }
        #progress {
            margin-top: 15px;
            font-size: 1.1em;
            color: #2E86DE;
        }
        #loading {
            display: none;
            margin-top: 20px;
        }
        #loading img {
            width: 50px;
            height: 50px;
        }
    </style>
    <script>
        function showLoading() {
            document.getElementById('loading').style.display = 'block';
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>:Book Scrapper</h1>
        <p>Enter the number of pages to scrape and let the magic happen!</p>
        <form method="POST" action="/scrape" onsubmit="showLoading()">
            <label for="pages">Number of Pages:</label><br>
            <input type="number" id="pages" name="pages" min="1" required><br>
            <button type="submit">Scrape</button>
        </form>
        {% if error %}
        <p class="error">{{ error }}</p>
        {% endif %}
        <div id="progress">{{ progress }}</div>
        <div id="loading">
            <img src="https://i.gifer.com/ZZ5H.gif" alt="Loading...">
            <p>Loading, please wait...</p>
        </div>
    </div>
</body>
</html>
"""
@app.route('/')
def index():
    return render_template_string(HTML_PAGE)
@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        pages = int(request.form['pages'])
        progress = ""
        for page in range(1, pages + 1):
            time.sleep(1)
            progress += f"Scraping page {page}..."
        return render_template_string(HTML_PAGE, progress=progress)
    except ValueError:
        return render_template_string(HTML_PAGE, error="Please enter a valid number of pages.")
if __name__ == '__main__':
    app.run(debug=True)

