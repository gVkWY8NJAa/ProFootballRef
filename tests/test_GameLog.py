import pytest
from ProFootballRef.Parsers import GamelogParser

urls = {'passing' : 'https://www.pro-football-reference.com/players/B/BradTo00.htm',
        'receiving' : 'https://www.pro-football-reference.com/players/B/BrowAn04.htm',
        'rushing' : 'https://www.pro-football-reference.com/players/B/BellLe00.htm',
        'kicking' : 'https://www.pro-football-reference.com/players/Z/ZuerGr00.htm',
        'defense': 'https://www.pro-football-reference.com/players/D/DaviDe00.htm',
        }


class TestGamelogPassing:

    def test_brady_2001(self):
        df = GamelogParser.GameLog().gamelog_passing(urls['passing'], 2001)
        assert df['pass_yds'].sum() == 2843

    