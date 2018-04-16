import pytest
from ProFootballRef.Parsers import PlayerParser

class TestParsers:
    def __init__(self):

        #Pre define urls to test
        self.passurl = 'https://www.pro-football-reference.com/players/B/BradTo00.htm'
        self.recurl = 'https://www.pro-football-reference.com/players/H/HopkDe00.htm'
        self.rushurl = 'https://www.pro-football-reference.com/players/G/GurlTo01.htm'
        self.kickurl = 'https://www.pro-football-reference.com/players/Z/ZuerGr00.htm'
        self.defenseurl = 'https://www.pro-football-reference.com/players/M/MartBl01.htm'

    def gethtml(self):
        # load each url and return the corresponding string of html
        pass_html = PlayerParser.PlayerParser().load_page(self.passurl)
        rec_html = PlayerParser.PlayerParser().load_page(self.recurl)
        rush_html = PlayerParser.PlayerParser().load_page(self.rushurl)
        kick_html = PlayerParser.PlayerParser().load_page(self.kickurl)
        defense_html = PlayerParser.PlayerParser().load_page(self.defenseurl)

        return pass_html, rec_html, rush_html, kick_html, defense_html

# load position pages for later testing
pass_html, rec_html, rush_html, kick_html, defense_html = TestParsers().gethtml()

def test_pass_html():
    gen_info = PlayerParser.PlayerParser().parse_general_info(pass_html)
    assert ('Michigan','Tom Brady', 225) == (gen_info['college'], gen_info['name'], gen_info['weight'])


def test_rec_html():
    gen_info = PlayerParser.PlayerParser().parse_general_info(rec_html)
    assert ('Clemson', 'DeAndre Hopkins', 214) == (gen_info['college'], gen_info['name'], gen_info['weight'])


def test_rush_html():
    gen_info = PlayerParser.PlayerParser().parse_general_info(rush_html)
    assert ('Georgia', 'Todd Gurley', 226) == (gen_info['college'], gen_info['name'], gen_info['weight'])


def test_kick_html():
    gen_info = PlayerParser.PlayerParser().parse_general_info(kick_html)
    assert ('Missouri Western St.', 'Greg Zuerlein', 187) == (gen_info['college'], gen_info['name'],
                                                               gen_info['weight'])


def test_defense_html():
    gen_info = PlayerParser.PlayerParser().parse_general_info(defense_html)
    assert ('Stanford', 'Blake Martinez', 239) == (gen_info['college'], gen_info['name'],
                                                               gen_info['weight'])






