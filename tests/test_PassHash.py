import pytest
import pandas as pd
from ProFootballRef.Tools import Passhash

# The purpose of this test class is to ensure that each hash has the correct columns appended if they're not
# included from the corresponding season game log. 
@pytest.fixture(scope="class")
def finalcols():
    return Passhash.PassHash().base[1:] + Passhash.PassHash().passing + Passhash.PassHash().rushing + \
           Passhash.PassHash().receiving + Passhash.PassHash().rush_sk + Passhash.PassHash().scoring2p + \
           Passhash.PassHash().scoring + Passhash.PassHash().punting

class TestPasshash:

    def test_md564b4c5df667e588d59b856ae9d724c7d(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 20)])
        assert all(x in list(Passhash.PassHash().md564b4c5df667e588d59b856ae9d724c7d(empty)) for x in finalcols)

    def test_md5b06cd4dff23f7376af6a879f99cc5a1c(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 24)])
        assert all(x in list(Passhash.PassHash().md5b06cd4dff23f7376af6a879f99cc5a1c(empty)) for x in finalcols)

    def test_md5677c3564a754183605775bac5aba623d(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 26)])
        assert all(x in list(Passhash.PassHash().md5677c3564a754183605775bac5aba623d(empty)) for x in finalcols)

    def test_md51609c51a70ab5e3d763c0d698e00eb16(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 27)])
        all(x in list(Passhash.PassHash().md51609c51a70ab5e3d763c0d698e00eb16(empty)) for x in finalcols)

    def test_md59d7339709d13dc7484e7090522596eda(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 28)])
        all(x in list(Passhash.PassHash().md59d7339709d13dc7484e7090522596eda(empty)) for x in finalcols)

    def test_md547963026aa9103eea8203b6717da2caf(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 27)])
        all(x in list(Passhash.PassHash().md547963026aa9103eea8203b6717da2caf(empty)) for x in finalcols)

    def test_md50feae896081ca775b997f372f93d1977(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 30)])
        all(x in list(Passhash.PassHash().md50feae896081ca775b997f372f93d1977(empty)) for x in finalcols)

    def test_md5366e35869d52cf189f6575ef82c562e1(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 29)])
        all(x in list(Passhash.PassHash().md5366e35869d52cf189f6575ef82c562e1(empty)) for x in finalcols)

    def test_md5c34721f06f1a5aad95fab7fc16577538(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 29)])
        all(x in list(Passhash.PassHash().md5366e35869d52cf189f6575ef82c562e1(empty)) for x in finalcols)

    def test_md5afa7cf6859400c6023d114abc175c24d(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 31)])
        all(x in list(Passhash.PassHash().md5afa7cf6859400c6023d114abc175c24d(empty)) for x in finalcols)

    def test_md560befa83b7115d584e02dea9908a707d(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 31)])
        all(x in list(Passhash.PassHash().md560befa83b7115d584e02dea9908a707d(empty)) for x in finalcols)

    def test_md52451894bb088c27b0a02ad350e35b9ad(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 33)])
        all(x in list(Passhash.PassHash().md52451894bb088c27b0a02ad350e35b9ad(empty)) for x in finalcols)

    def test_md5e22db471405382c6d4e868c4d29d9cb5(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 36)])
        all(x in list(Passhash.PassHash().md5e22db471405382c6d4e868c4d29d9cb5(empty)) for x in finalcols)

