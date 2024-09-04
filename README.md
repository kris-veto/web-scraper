# web-scraper
A Python project that scrapes product titles and prices from a webpage at regular intervals using Flask and APScheduler.

Installation

Clone the repository:
git clone https://github.com/yourusername/web-scraper-flask.git
cd web-scraper-flask

Create a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt

Run the app:
python app.py

Usage
The app scrapes data every 3 seconds from a specified URL and prints it to the console.
Visit http://localhost:5000/ to confirm the app is running.

Features
Automated Web Scraping: Scrapes data at regular intervals.
Flask Server: Manages scheduling and serves a simple web page.
Scheduler: Uses APScheduler to automate the scraping task.

Contributing
Feel free to submit issues or pull requests.

License
Licensed under the MIT License.

