import pytest
from profootballref.Tools import Loader

urls = {'passing' : 'https://www.pro-football-reference.com/players/B/BradTo00.htm',
        'receiving' : 'https://www.pro-football-reference.com/players/B/BrowAn04.htm',
        'rushing' : 'https://www.pro-football-reference.com/players/B/BellLe00.htm',
        'kicking' : 'https://www.pro-football-reference.com/players/Z/ZuerGr00.htm',
        'defense': 'https://www.pro-football-reference.com/players/D/DaviDe00.htm',
        }


# setup response object
@pytest.fixture(scope="module" )
def passing_req():
    print('loaded passing html')
    return Loader.Loader().load_page(urls['passing'])

@pytest.fixture(scope="module" )
def receiving_req():
    print('loaded receiving html')
    return Loader.Loader().load_page(urls['receiving'])

@pytest.fixture(scope="module" )
def rushing_req():
    print('loaded rushing html')
    return Loader.Loader().load_page(urls['rushing'])

@pytest.fixture(scope="module" )
def kicking_req():
    print('loaded kicking html')
    return Loader.Loader().load_page(urls['kicking'])

@pytest.fixture(scope="module" )
def defense_req():
    print('loaded defense html')
    return Loader.Loader().load_page(urls['defense'])
