from flask import Flask
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
from flask_apscheduler import APScheduler

# Function to scrape the webpage for product information
def scrape_webpage():
    url = 'https://www.nike.com/w/mens-shoes-nik1zy7ok'   # The URL of the webpage to scrape
    response = requests.get(url)  # Send a GET request to the webpage
    soup = BeautifulSoup(response.text, 'html5lib')   # Parse the HTML content using BeautifulSoup

     # Loop through all product cards on the page and extract the title and price
    for product in soup.find_all('div', class_='product-card__body'):
        title = product.find('div', class_='product-card__title').text   # Extract the product title
        price = product.find('div', class_='product-card__price').text   # Extract the product price
        print(title, price)    # Print the title and price to the console

# Initialize the Flask app
app = Flask(__name__)
scheduler = APScheduler()   # Initialize the APScheduler

# Function to test the scheduler
def scheduleTask():
    print("THis test runs every 3 seconds")
    

@app.route('/')
def home():
    # Define a route for the home page that returns a simple message
    return 'Web Scraper lab Running'

# Function to start the web scraper with the scheduler
def start_scraper():
    scheduler.add_job(id='Scheduled Task', func=scrape_webpage,trigger="interval",seconds=3)
    scheduler.start()   # Start the scheduler


if __name__ == '__main__':
    start_scraper()   # Start the scraper when the script runs
    app.run(host="0.0.0.0")  # Run the Flask app on all available IP addresses (0.0.0.0)

