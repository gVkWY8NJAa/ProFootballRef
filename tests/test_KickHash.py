import pytest
import pandas as pd
from profootballref.Tools import Kickhash

# The purpose of this test class is to ensure that each hash has the correct columns appended if they're not
# included from the corresponding season game log.
@pytest.fixture(scope="class")
def finalcols():
    return Kickhash.KickHash().base[1:] + Kickhash.KickHash().scoring


class TestKickhash:

    def test_md5080683052961d92b5efd07588e614700(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 19)])
        assert all(x in list(Kickhash.KickHash().md5080683052961d92b5efd07588e614700(empty)) for x in finalcols)

    def test_md5c0fe30e42184e7a59c00c04dc917bb87(self, finalcols):
        # generate empty df with cols of length that the site would return in this instance
        empty = pd.DataFrame(columns=[x for x in range(0, 16)])
        assert all(x in list(Kickhash.KickHash().md5c0fe30e42184e7a59c00c04dc917bb87(empty)) for x in finalcols)

