import pytest
from ProFootballRef.Parsers import PlayerParser


@pytest.fixture(scope="class")
def pass_html():
    passurl = 'https://www.pro-football-reference.com/players/B/BradTo00.htm'
    return PlayerParser.PlayerParser().load_page(passurl)

@pytest.fixture(scope="class")
def rec_html():
    recurl = 'https://www.pro-football-reference.com/players/H/HopkDe00.htm'
    return PlayerParser.PlayerParser().load_page(recurl)

@pytest.fixture(scope="class")
def rush_html():
    rushurl = 'https://www.pro-football-reference.com/players/G/GurlTo01.htm'
    return PlayerParser.PlayerParser().load_page(rushurl)

@pytest.fixture(scope="class")
def kick_html():
    kickurl = 'https://www.pro-football-reference.com/players/Z/ZuerGr00.htm'
    return PlayerParser.PlayerParser().load_page(kickurl)

@pytest.fixture(scope="class")
def defense_html():
    defenseurl = 'https://www.pro-football-reference.com/players/M/MartBl01.htm'
    return PlayerParser.PlayerParser().load_page(defenseurl)

class TestPassing:
    def test_pass_html(self, pass_html):
        gen_info = PlayerParser.PlayerParser().parse_general_info(pass_html)
        assert ('Michigan','Tom Brady', 225) == (gen_info['college'], gen_info['name'], gen_info['weight'])

class TestReceiving:
    def test_rec_html(self, rec_html):
        gen_info = PlayerParser.PlayerParser().parse_general_info(rec_html)
        assert ('Clemson', 'DeAndre Hopkins', 214) == (gen_info['college'], gen_info['name'], gen_info['weight'])

class TestRushing:
    def test_rush_html(self, rush_html):
        gen_info = PlayerParser.PlayerParser().parse_general_info(rush_html)
        assert ('Georgia', 'Todd Gurley', 226) == (gen_info['college'], gen_info['name'], gen_info['weight'])

class TestKicking:
    def test_kick_html(self, kick_html):
        gen_info = PlayerParser.PlayerParser().parse_general_info(kick_html)
        assert ('Missouri Western St.', 'Greg Zuerlein', 187) == (gen_info['college'], gen_info['name'],
                                                               gen_info['weight'])

class TestDefense:
    def test_defense_html(self, defense_html):
        gen_info = PlayerParser.PlayerParser().parse_general_info(defense_html)
        assert ('Stanford', 'Blake Martinez', 239) == (gen_info['college'], gen_info['name'], gen_info['weight'])
