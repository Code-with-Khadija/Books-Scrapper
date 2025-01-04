### README: Book Scrapper Project

## Overview

The **Book Scrapper Project** is a web scraping and frontend integration application designed to scrape book data from the "Books to Scrape" website. The project provides a simple and user-friendly interface through a Flask-based web frontend to specify the number of pages to scrape and display progress in real time. The backend uses Selenium to scrape book details, such as titles, prices, ratings, availability, and image URLs, saving the data in a structured CSV format.

## Features

1. **Web Scraping**:
   - Extracts book details, including:
     - **Title**
     - **Price**
     - **Rating**
     - **Availability**
     - **Image URL**
   - Supports scraping across multiple pages.

2. **Frontend Interface**:
   - Interactive web interface to enter the number of pages to scrape.
   - Real-time progress feedback during scraping.
   - Modern and intuitive design with responsive behavior.

3. **CSV Export**:
   - Saves the scraped data into a CSV file for further analysis.

## Tech Stack

- **Backend**:
  - Python
  - Selenium (for web scraping)
- **Frontend**:
  - Flask (HTML rendering)
  - Vanilla CSS and JavaScript (for styling and interactivity)
- **Data Export**:
  - CSV module in Python

## File Descriptions

1. **`book_scrapping.py`**:
   - Contains the main logic for scraping the "Books to Scrape" website.
   - Key functionalities:
     - Initializes Selenium WebDriver for Chrome.
     - Scrapes book data for multiple pages.
     - Saves results to a CSV file.

2. **`Books_scrapper_frontend.py`**:
   - Implements the Flask web application for the project.
   - Provides an HTML form to input the number of pages.
   - Displays progress updates and feedback during scraping

## Requirements

### Python Libraries

- `selenium`
- `flask`

### Other Requirements

- **ChromeDriver**: Ensure that the appropriate version of ChromeDriver is installed and accessible.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repository/book-scrapper.git
   cd book-scrapper
   ```

2. **Install Dependencies**:
   ```bash
   pip install selenium flask
   ```

3. **Download ChromeDriver**:
   - Download the version matching your Chrome browser from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).

4. **Run the Backend Scraper**:
   ```bash
   python book_scrapping.py
   ```

5. **Run the Frontend Application**:
   ```bash
   python Books_scrapper_frontend.py
   ```

6. **Access the Web Application**:
   - Open your browser and go to `http://127.0.0.1:5000`.

---

## Usage

1. Launch the web application.
2. Enter the number of pages to scrape.
3. Click **Scrape** to initiate the process.
4. Monitor progress on the web interface.
5. Check the generated `books.csv` file for the scraped results.

## Notes

- Ensure a stable internet connection while scraping to avoid timeout errors.
- Always use the application responsibly and avoid overloading the target website.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
