import pytest
from profootballref.Parsers import GamelogParser

urls = {'passing': 'https://www.pro-football-reference.com/players/B/BradTo00.htm',
        'receiving': 'https://www.pro-football-reference.com/players/B/BrowAn04.htm',
        'rushing': 'https://www.pro-football-reference.com/players/B/BellLe00.htm',
        'kicking': 'https://www.pro-football-reference.com/players/Z/ZuerGr00.htm',
        'defense': 'https://www.pro-football-reference.com/players/W/WillTr99.htm',
        }


class TestGamelogPassing:

    def test_brady_2001(self):
        df = GamelogParser.GameLog().passing(urls['passing'], 2001)
        assert df['pass_yds'].sum() == 2843


class TestGamelogReceiving:

    def test_brown_2013(self):
        df = GamelogParser.GameLog().receiving(urls['receiving'], 2013)
        assert df['Rec_TD'].sum() == 8


class TestGameLogRushing:

    def test_bell_2015(self):
        df = GamelogParser.GameLog().rushing(urls['rushing'], 2015)
        assert df['rush_yds'].sum() == 556


class TestGameLogKicking:

    def test_zuerlein_2017(self):
        df = GamelogParser.GameLog().kicking(urls['kicking'], 2017)
        assert df['XPM'].sum() == 44

class TestGameLogDefense:

    def test_williams_2009(self):
        df = GamelogParser.GameLog().defense(urls['defense'], 2009)
        assert df['tkl'].sum() == 39