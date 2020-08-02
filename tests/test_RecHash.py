import pytest
import pandas as pd
from profootballref.Tools import Rechash

# The purpose of this test class is to ensure that each hash has the correct columns appended if they're not
# included from the corresponding season game log.
@pytest.fixture(scope="class")
def finalcols():
    return Rechash.RecHash().base[1:] + Rechash.RecHash().receiving + Rechash.RecHash().rushing + \
           Rechash.RecHash().kick_rt + Rechash.RecHash().punt_rt + Rechash.RecHash().scoring2p + \
           Rechash.RecHash().scoring


class TestRechash:
    def test_md5b3c4237d9a10de8cfaad61852cb552c4(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 32)])
        assert all(x in list(Rechash.RecHash().md5b3c4237d9a10de8cfaad61852cb552c4(empty)) for x in finalcols)

    def test_md5bcb96297b50fb2120f475e8e05fbabcd(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 41)])
        assert all(x in list(Rechash.RecHash().md5bcb96297b50fb2120f475e8e05fbabcd(empty)) for x in finalcols)

    def test_md54560c290b45e942c16cc6d7811345fce(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 37)])
        assert all(x in list(Rechash.RecHash().md54560c290b45e942c16cc6d7811345fce(empty)) for x in finalcols)

    def test_md54c82a489ec5b2c943e78c9018dcbbca1(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 36)])
        assert all(x in list(Rechash.RecHash().md54c82a489ec5b2c943e78c9018dcbbca1(empty)) for x in finalcols)

    def test_md5e8ffc7202223bb253e92da83b76e9944(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 39)])
        assert all(x in list(Rechash.RecHash().md5e8ffc7202223bb253e92da83b76e9944(empty)) for x in finalcols)

    def test_md550fcceaa170b1a1e501e3f40548e403d(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 29)])
        assert all(x in list(Rechash.RecHash().md550fcceaa170b1a1e501e3f40548e403d(empty)) for x in finalcols)

    def test_md5e160e714b29305ecfecf513cbf84b80f(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 25)])
        assert all(x in list(Rechash.RecHash().md5e160e714b29305ecfecf513cbf84b80f(empty)) for x in finalcols)

    def test_md5111e8480632f73642d7e20acbdbe6b16(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 25)])
        assert all(x in list(Rechash.RecHash().md5111e8480632f73642d7e20acbdbe6b16(empty)) for x in finalcols)

    def test_md5adc05c5af0f88775d3605d02c831c0ed(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 20)])
        assert all(x in list(Rechash.RecHash().md5adc05c5af0f88775d3605d02c831c0ed(empty)) for x in finalcols)

    def test_md5bfbf86ae0485a0a70692ae04124449b9(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 18)])
        assert all(x in list(Rechash.RecHash().md5bfbf86ae0485a0a70692ae04124449b9(empty)) for x in finalcols)

    def test_md56b4698269dd34a823cf6b233c6165614(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 17)])
        assert all(x in list(Rechash.RecHash().md56b4698269dd34a823cf6b233c6165614(empty)) for x in finalcols)

    def test_md57f97f3885d50fcf9b92797810856a89f(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 21)])
        assert all(x in list(Rechash.RecHash().md57f97f3885d50fcf9b92797810856a89f(empty)) for x in finalcols)

    def test_md5aa321161d6f3f5230259dbc4ae67299a(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 24)])
        assert all(x in list(Rechash.RecHash().md5aa321161d6f3f5230259dbc4ae67299a(empty)) for x in finalcols)

    def test_md51193d47266d4acdcf1b6fca165121100(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 43)])
        assert all(x in list(Rechash.RecHash().md51193d47266d4acdcf1b6fca165121100(empty)) for x in finalcols)

    def test_md552589e869a13d76c6d0dbf066cab536f(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 18)])
        assert all(x in list(Rechash.RecHash().md552589e869a13d76c6d0dbf066cab536f(empty)) for x in finalcols)