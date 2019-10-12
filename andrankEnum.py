#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
import os

try:
    from requests_futures.sessions import FuturesSession
    from concurrent.futures import ThreadPoolExecutor,wait, as_completed
except ImportError:
    print("[!] You'll need to pip install requests-futures for this tool.")
    sys.exit()


BANNER = '''
=========================
    Android Rank scrapper
=========================
'''

def get_package(max_apk=500,price="free",threads=25):
    """
    Scrap 'https://https://www.androidrank.org/app/ranking/all?start=<pages>&price=<price>' to find
    individual APK pages
        -pages = number of pages to iterate
        -price = free(default) or paid
    """
    
    session = FuturesSession(executor=ThreadPoolExecutor(max_workers=threads))
    queue = []

    for page in range(1,max_apk,20): # page starts from 1 not 0 
        # Just dump all async request into the "queue" dict
        queue.append(session.get('https://www.androidrank.org/app/ranking/all?start={}&price={}'.format(page,price)))
       
    # Then, grab all the response from the queue
    for page in range(len(queue)):
        response = queue[page].result()
        soup = BeautifulSoup(response.content, 'html.parser')
        #results = soup.find_all('td', attrs={'style':'text-align:left;'})
        b = soup.find_all('tr', attrs={'class':['odd','even']})
        for result in b:
            app = result.find('a').text
            downloads = result('td')[4].string
            package = result.find('a')['href'].split("/")[3]
            print("{},{},{}".format(app,package,downloads))


def main():
    """
    Main program function
    """
    #args = parse_arguments()

    # check if keyword module is requested
    #if args.keyword:
    #    keyword_search.execute(args.mutations, args.keyword, args.threads)
    print(BANNER)

    print("[+] Fetching Playstore apps with at least 100M downloads...")
    get_package()

    print("[+] All done")

if __name__== '__main__':
    main()

