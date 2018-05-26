import pytest
from ProFootballRef.Parsers import TeamStats

@pytest.fixture(scope="class")
def offense():
    return TeamStats.TeamStats().offense(2017)

@pytest.fixture(scope="class")
def defense():
    return TeamStats.TeamStats().defense(2017)

class TestOffense:
    def test_bearsOff(self, offense):
        bears = offense[offense['Tm'] == 'Chicago Bears']
        assert bears['Yds'].values == 4599

    def test_intOffense(self, offense):
        assert offense.sum()['Int'] == 430

    def test_pfOffense(self, offense):
        assert offense.sum()['PF'] == 11120

class TestDefense:
    def test_bearsDef(self, defense):
        bears = defense[defense['Tm'] == 'Chicago Bears']
        assert bears['Yds'].values == 5106

    def test_intDefense(self, defense):
        assert defense.sum()['Int'] == 430

    def test_pfDefense(self, defense):
        assert defense.sum()['PF'] == 11120