import pytest
from ProFootballRef.LinkBuilder import GetPositionLinks


@pytest.fixture(scope="class")
def receiving():
    return GetPositionLinks.GetPositionLinks('receiving').player_links('2017')


@pytest.fixture(scope="class")
def rushing():
    return GetPositionLinks.GetPositionLinks('rushing').player_links('2017')


@pytest.fixture(scope="class")
def passing():
    return GetPositionLinks.GetPositionLinks('passing').player_links('2017')


@pytest.fixture(scope="class")
def defense():
    return GetPositionLinks.GetPositionLinks('defense').player_links('2017')


@pytest.fixture(scope="class")
def kicking():
    return GetPositionLinks.GetPositionLinks('kicking').player_links('2017')


class TestReceiving:
    def test_receiving_type(self, receiving):
        assert type(receiving) == list

    def test_receiving_length(self, receiving):
        assert len(receiving) > 10

    def test_receiving_value(self, receiving):
        assert 'https://www.pro-football-reference.com/players/C/CookBr00.htm' in receiving


class TestRushing:
    def test_rushing_type(self, rushing):
        assert type(rushing) == list

    def test_rushing_length(self, rushing):
        assert len(rushing) > 10

    def test_rushing_value(self, rushing):
        assert 'https://www.pro-football-reference.com/players/K/KamaAl00.htm' in rushing


class TestPassing:
    def test_passing_type(self, passing):
        assert type(passing) == list

    def test_passing_len(self, passing):
        assert len(passing) > 10

    def test_passing_value(self, passing):
        assert 'https://www.pro-football-reference.com/players/N/NewtCa00.htm' in passing


class TestDefense:
    def test_defense_type(self, defense):
        assert type(defense) == list

    def test_defense_len(self, defense):
        assert len(defense) > 10

    def test_defense_value(self, defense):
        assert 'https://www.pro-football-reference.com/players/O/OnwuPa00.htm' in defense


class TestKicking:
    def test_kicking_type(self, kicking):
        assert type(kicking) == list

    def test_kicking_len(self, kicking):
        assert len(kicking) > 10

    def test_kicking_value(self, kicking):
        assert 'https://www.pro-football-reference.com/players/Z/ZuerGr00.htm' in kicking
