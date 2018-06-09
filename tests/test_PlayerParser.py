import pytest
from profootballref.Parsers import PlayerParser

def general_parser(html):
    return PlayerParser.PlayerParser().parse_general_info(html)


# test requests response
class TestLoadPage:

    # check to see if the page even loaded
    def test_response_code(self, passing_req):
        assert passing_req.status_code == 200

    # see if we even have the right html coming back
    def test_response_type(self, passing_req):
        assert 'Tom Brady' in passing_req.content.decode()


class TestGeneralParsing:

    def test_general_info_college(self, passing_req):
        html = passing_req.content.decode()
        gen = general_parser(html)
        assert gen['college'] == 'Michigan'

    def test_general_info_weight(self, passing_req):
        html = passing_req.content.decode()
        gen = general_parser(html)
        assert gen['weight'] == 225

    def test_general_info_position(self, passing_req):
        html = passing_req.content.decode()
        gen = general_parser(html)
        assert gen['position'] == 'QB'


class TestPassing:

    # test to see if the dataframe is coming back correctly
    def test_df_name(self, passing_req):
        html = passing_req.content.decode()
        df = PlayerParser.PlayerParser().passing(html=html)
        assert df.iloc[0]['Name'] == 'Tom Brady'

    def test_df_pos(self, passing_req):
        html = passing_req.content.decode()
        df = PlayerParser.PlayerParser().passing(html=html)
        assert df.iloc[0]['Pos'] == 'QB'

class TestReceiving:

    # test to see if the dataframe is coming back correctly
    def test_df_name(self, receiving_req):
        html = receiving_req.content.decode()
        df = PlayerParser.PlayerParser().receiving(html=html)
        assert df.iloc[0]['Name'] == 'Antonio Brown'

    def test_df_pos(self, receiving_req):
        html = receiving_req.content.decode()
        df = PlayerParser.PlayerParser().receiving(html=html)
        assert df.iloc[0]['Pos'] == 'WR'


class TestRushing:

    # test to see if the dataframe is coming back correctly
    def test_df_name(self, rushing_req):
        html = rushing_req.content.decode()
        df = PlayerParser.PlayerParser().rushing(html=html)
        assert df.iloc[0]['Name'] == "Le'Veon Bell"


class TestKicking:

    # test to see if the dataframe is coming back correctly
    def test_df_name(self, kicking_req):
        html = kicking_req.content.decode()
        df = PlayerParser.PlayerParser().kicking(html=html)
        assert df.iloc[0]['Name'] == 'Greg Zuerlein'


class TestDefense:

    # test to see if the dataframe is coming back correctly
    def test_df_name(self, defense_req):
        html = defense_req.content.decode()
        df = PlayerParser.PlayerParser().defense(html=html)
        assert df.iloc[0]['Name'] == 'Demario Davis'
