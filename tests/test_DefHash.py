import pytest
import pandas as pd
from profootballref.Tools import Defhash

# The purpose of this test class is to ensure that each hash has the correct columns appended if they're not
# included from the corresponding season game log.
@pytest.fixture(scope="class")
def finalcols():
    return Defhash.DefHash().base[1:] + Defhash.DefHash().punt_rt + Defhash.DefHash().kick_rt + \
                Defhash.DefHash().scoring + Defhash.DefHash().rush_sk + Defhash.DefHash().def_int


class TestDefhash:

    def test_md50c329a15f241e5c132d0d5c7612032c0(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 18)])
        assert all(x in list(Defhash.DefHash().md50c329a15f241e5c132d0d5c7612032c0(empty)) for x in finalcols)

    def test_md558ffdd172c2358c5e5ab2e0a1994252a(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 21)])
        assert all(x in list(Defhash.DefHash().md558ffdd172c2358c5e5ab2e0a1994252a(empty)) for x in finalcols)

    def test_md5141f3f6945aa9495c6580650649f4b8f(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 14)])
        assert all(x in list(Defhash.DefHash().md5141f3f6945aa9495c6580650649f4b8f(empty)) for x in finalcols)

    def test_md5109394668745222b0ccbd92bfd0ac4c1(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 22)])
        assert all(x in list(Defhash.DefHash().md5109394668745222b0ccbd92bfd0ac4c1(empty)) for x in finalcols)

    def test_md560dfaf4e946c4ae3d47c6d8b430c92a4(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 16)])
        assert all(x in list(Defhash.DefHash().md560dfaf4e946c4ae3d47c6d8b430c92a4(empty)) for x in finalcols)
