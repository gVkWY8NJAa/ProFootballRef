import pytest
import pandas as pd
from ProFootballRef.Tools import Rushhash

# The purpose of this test class is to ensure that each hash has the correct columns appended if they're not
# included from the corresponding season game log.
@pytest.fixture(scope="class")
def finalcols():
    return Rushhash.RushHash().base[1:] + Rushhash.RushHash().receiving + Rushhash.RushHash().rushing + \
           Rushhash.RushHash().kick_rt + Rushhash.RushHash().punt_rt + Rushhash.RushHash().scoring2p + \
           Rushhash.RushHash().scoring


class TestRushhash:
    def test_md5c3695be2dd2fa9307301dccf047b4e86(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 26)])
        assert all(x in list(Rushhash.RushHash().md5c3695be2dd2fa9307301dccf047b4e86(empty)) for x in finalcols)

    def test_md57f97f3885d50fcf9b92797810856a89f(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 21)])
        assert all(x in list(Rushhash.RushHash().md57f97f3885d50fcf9b92797810856a89f(empty)) for x in finalcols)

    def test_md5aa321161d6f3f5230259dbc4ae67299a(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 24)])
        assert all(x in list(Rushhash.RushHash().md5aa321161d6f3f5230259dbc4ae67299a(empty)) for x in finalcols)

    def test_md59c11c15180efbf7aec4300fc190cd3a5(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 33)])
        assert all(x in list(Rushhash.RushHash().md59c11c15180efbf7aec4300fc190cd3a5(empty)) for x in finalcols)

    def test_md5ad9a12e06546e3019128fec57cdc9d0e(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 25)])
        assert all(x in list(Rushhash.RushHash().md5ad9a12e06546e3019128fec57cdc9d0e(empty)) for x in finalcols)

    def test_md500f83a7c4b3e891e3c448db700cc9ada(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 22)])
        assert all(x in list(Rushhash.RushHash().md500f83a7c4b3e891e3c448db700cc9ada(empty)) for x in finalcols)

    def test_md55980508dab2f61013bd07809c5ca0e41(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 19)])
        assert all(x in list(Rushhash.RushHash().md55980508dab2f61013bd07809c5ca0e41(empty)) for x in finalcols)

    def test_md5c35b37a5f0f696bfd1576753faffe81c(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 35)])
        assert all(x in list(Rushhash.RushHash().md5c35b37a5f0f696bfd1576753faffe81c(empty)) for x in finalcols)

    def test_md5aed81e3e77b9842532b5efa73458a259(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 28)])
        assert all(x in list(Rushhash.RushHash().md5aed81e3e77b9842532b5efa73458a259(empty)) for x in finalcols)

    def test_md57d21a9a4ab9adde626d633fbd62db5c0(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 36)])
        assert all(x in list(Rushhash.RushHash().md57d21a9a4ab9adde626d633fbd62db5c0(empty)) for x in finalcols)

    def test_md591138c3c08c339b71b8323e2bac3aac7(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 14)])
        assert all(x in list(Rushhash.RushHash().md591138c3c08c339b71b8323e2bac3aac7(empty)) for x in finalcols)


