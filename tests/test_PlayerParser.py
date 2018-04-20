import pytest
from ProFootballRef.Parsers import PlayerParser

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


class TestPassing:

    # test to see if the dataframe is coming back correctly
    def test_df_name(self, passing_req):
        html = passing_req.content.decode()
        df = PlayerParser.PlayerParser().parse_passing_stats(html=html)
        assert df.iloc[0]['Name'] == 'Tom Brady'


class TestReceiving:

    # test to see if the dataframe is coming back correctly
    def test_df_name(self, receiving_req):
        html = receiving_req.content.decode()
        df = PlayerParser.PlayerParser().parse_receiver_stats(html=html)
        assert df.iloc[0]['Name'] == 'Antonio Brown'


class TestRushing:

    # test to see if the dataframe is coming back correctly
    def test_df_name(self, rushing_req):
        html = rushing_req.content.decode()
        df = PlayerParser.PlayerParser().parse_rushing_stats(html=html)
        assert df.iloc[0]['Name'] == "Le'Veon Bell"


class TestKicking:

    # test to see if the dataframe is coming back correctly
    def test_df_name(self, kicking_req):
        html = kicking_req.content.decode()
        df = PlayerParser.PlayerParser().parse_kicking_stats(html=html)
        assert df.iloc[0]['Name'] == 'Greg Zuerlein'


class TestDefense:

    # test to see if the dataframe is coming back correctly
    def test_df_name(self, defense_req):
        html = defense_req.content.decode()
        df = PlayerParser.PlayerParser().parse_defense_stats(html=html)
        assert df.iloc[0]['Name'] == 'Demario Davis'