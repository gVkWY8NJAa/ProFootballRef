from ProFootballRef.LinkBuilder.GetPositionLinks import GetPositionLinks

receiving = GetPositionLinks('receiving').parse_links('2017')
rushing = GetPositionLinks('rushing').parse_links('2017')
passing = GetPositionLinks('passing').parse_links('2017')
defense = GetPositionLinks('defense').parse_links('2017')
kicking = GetPositionLinks('kicking').parse_links('2017')

def test_receiving():
    assert type(receiving) == list

def test_rushing():
    assert type(rushing) == list

def test_passing():
    assert type(passing) == list

def test_defense():
    assert type(defense) == list

def test_kicking():
    assert type(kicking) == list
