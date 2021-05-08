"""
    Reddit Scapping
    ---------------
    This scrappes the reddit top forum and get
    the most upvoted post of the day and sends
    a message to a specific user about.

    By: (Kelvin) Chun Kit Cho
    May 8, 2021
"""

# Imports
from bs4 import BeautifulSoup
import requests, lxml
from pprint import pprint
from messenger import Messenger

# Get request for reddit server
response = requests.get("https://www.reddit.com/top/")
# Check the return status of the response
response.raise_for_status()

reddit_page = response.text
# Give soup the reddit web page
soup = BeautifulSoup(reddit_page, "lxml")

# posts = soup.find_all("div",  class_="_1oQyIsiPHYt6nx7VOmd1sz")
# post_titles = posts.find_all("h3",  class_="_eYtD2XCVieq6emjKBH3m")

# Find all the fields that is stated
post = soup.find("div",  class_="_1oQyIsiPHYt6nx7VOmd1sz")
# print(post.prettify())
post_title = post.find("h3",  class_="_eYtD2XCVieq6emjKBH3m")
post_upvote = post.find("div", class_="_25IkBM0rRUqWX5ZojEMAFQ")
post_url = post.find("a", class_="_3jOxDPIQ0KaOWpzvSQo-1s")
post_url = (post_url.get("href"))


MoTD = ("\nTitle: {}\nUpvotes: {}\nLink: {}".format(post_title.text, post_upvote.text, post_url))
# Create a Messenger object
messager = Messenger()
# Send a text message using the messenger 
messager.message(message=MoTD, number="your number")