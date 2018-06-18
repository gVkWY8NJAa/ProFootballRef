import pytest
from profootballref.LinkBuilder import GetPositionLinks


@pytest.fixture(scope="class")
def receiving():
    return GetPositionLinks.Position('receiving').player_links('2017')


@pytest.fixture(scope="class")
def rushing():
    return GetPositionLinks.Position('rushing').player_links('2017')


@pytest.fixture(scope="class")
def passing():
    return GetPositionLinks.Position('passing').player_links('2017')


@pytest.fixture(scope="class")
def defense():
    return GetPositionLinks.Position('defense').player_links('2017')


@pytest.fixture(scope="class")
def kicking():
    return GetPositionLinks.Position('kicking').player_links('2017')


class TestReceiving:
    def test_receiving_type(self, receiving):
        assert type(receiving) == list

    def test_receiving_length(self, receiving):
        assert len(receiving) > 10

    def test_receiving_value(self, receiving):
        assert 'https://www.pro-football-reference.com/players/C/CookBr00.htm' in receiving

    def test_range(self):
        assert len(GetPositionLinks.Position('receiving').player_links(2016, 2017)) == 596


class TestRushing:
    def test_rushing_type(self, rushing):
        assert type(rushing) == list

    def test_rushing_length(self, rushing):
        assert len(rushing) > 10

    def test_rushing_value(self, rushing):
        assert 'https://www.pro-football-reference.com/players/K/KamaAl00.htm' in rushing

    def test_range(self):
        assert len(GetPositionLinks.Position('rushing').player_links(2016, 2017)) == 440


class TestPassing:
    def test_passing_type(self, passing):
        assert type(passing) == list

    def test_passing_len(self, passing):
        assert len(passing) > 10

    def test_passing_value(self, passing):
        assert 'https://www.pro-football-reference.com/players/N/NewtCa00.htm' in passing

    def test_range(self):
        assert len(GetPositionLinks.Position('passing').player_links(2016, 2017)) == 130

class TestDefense:
    def test_defense_type(self, defense):
        assert type(defense) == list

    def test_defense_len(self, defense):
        assert len(defense) > 10

    def test_defense_value(self, defense):
        assert 'https://www.pro-football-reference.com/players/O/OnwuPa00.htm' in defense

    def test_range(self):
        assert len(GetPositionLinks.Position('defense').player_links(2016, 2017)) == 1477

class TestKicking:
    def test_kicking_type(self, kicking):
        assert type(kicking) == list

    def test_kicking_len(self, kicking):
        assert len(kicking) > 10

    def test_kicking_value(self, kicking):
        assert 'https://www.pro-football-reference.com/players/Z/ZuerGr00.htm' in kicking

    def test_range(self):
        assert len(GetPositionLinks.Position('kicking').player_links(2016, 2017)) == 87
