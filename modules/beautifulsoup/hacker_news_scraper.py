import requests
from bs4 import BeautifulSoup
import pprint
import time

BASE_URL = 'https://news.ycombinator.com'
# response = requests.get(BASE_URL)

def get_lists_and_points(soup):
    # extract all the links using the class selector
    links_list = soup.select('.storylink')

    # extract all the points using the class selector
    points_list = soup.select('.score')

    return (links_list, points_list)

def parse_response(response):
    # extract the text content of the web page
    response_text = response.text
    # parse HTML
    soup = BeautifulSoup(response_text, 'html.parser')
    return soup

def get_paginated_data(pages):
    total_links_list = []
    total_points_list = []
    for page in range(pages):
        URL = BASE_URL + f'?p={page+1}'
        response = requests.get(URL)
        soup = parse_response(response)
        links_list, points_list = get_lists_and_points(soup)
        for link in links_list:
            total_links_list.append(link)
        for point in points_list:
            total_points_list.append(point)
        # add 30 seconds delay as per hacker news robots.txt rules
        time.sleep(30)
    return (total_links_list, total_points_list)

def generate_popular_posts(links_list, points_list):
    # create an empty popular posts list
    popular_posts = []

    # loop though all links
    for idx, link in enumerate(links_list):
        # fetch the title of the post
        post_title = link.get_text()
        # fetch the link of the post
        post_href = link.get('href')
        # fetch the point text using the index of the link
        # convert the point to integer
        # if points data is not available, assign it a default of 0
        try:
            post_points = int(
                points_list[idx].get_text().replace(' points', ''))
        except:
            points_list = 0
        # append to popular posts as a dictionary object if points is atleast 100
        if post_points >= 100:
            popular_posts.append(
                {'title': post_title, 'link': post_href, 'points': post_points})
    return popular_posts

def sort_posts_by_points(posts):
    return sorted(posts, key=lambda x: x['points'], reverse=True)

def main():
    total_links_list, total_points_list = get_paginated_data(5)
    popular_posts = generate_popular_posts(total_links_list, total_points_list)
    sorted_posts = sort_posts_by_points(popular_posts)
    # print posts sorted by highest to lowest
    pprint.pprint(sorted_posts)

if(__name__ == '__main__'):
    main()