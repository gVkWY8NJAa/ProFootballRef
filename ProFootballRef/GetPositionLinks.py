import requests
import re


class GetPositionLinks:
    def __init__(self, *args):
        # setup urls based on position passed into the class
        if args[0] == 'receiving':
            self.url = 'https://www.pro-football-reference.com/years/%s/receiving.htm'
        elif args[0] == 'rushing':
            self.url = 'https://www.pro-football-reference.com/years/%s/rushing.htm'
        elif args[0] == 'passing':
            self.url = 'https://www.pro-football-reference.com/years/%s/passing.htm'
        elif args[0] == 'defense':
            self.url = 'https://www.pro-football-reference.com/years/%s/defense.htm'
        elif args[0] == 'kicking':
            self.url = 'https://www.pro-football-reference.com/years/%s/kicking.htm'
        else:
            print('Must pass either receiving, rushing, passing, defense, or kicking')
            return 0

    def parse_links(self, year):
        # load the positions page
        url = self.url % year
        page = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/51.0.2704.103 Safari/537.36'})
        content = page.content.decode()

        # Parse urls from the position page that point to the players page
        players = re.compile(
            'data-append-csv=".*?" data-stat="player" csk=".*?" ><a href="(\/players\/[a-zA-Z]\/.*?.htm)"').findall(
            content)

        # Since they're relative links, attach the base url and append to a list to be returned
        links = []
        for x in players:
            links.append('https://www.pro-football-reference.com' + x)

        return links