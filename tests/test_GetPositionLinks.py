from ProFootballRef.LinkBuilder.GetPositionLinks import GetPositionLinks

receiving = GetPositionLinks('receiving').parse_links('2017')
rushing = GetPositionLinks('rushing').parse_links('2017')
passing = GetPositionLinks('passing').parse_links('2017')
defense = GetPositionLinks('defense').parse_links('2017')
kicking = GetPositionLinks('kicking').parse_links('2017')

def test_receiving_type():
    assert type(receiving) == list

def test_receiving_length():
    assert len(receiving) > 10

def test_receiving_value():
    assert 'https://www.pro-football-reference.com/players/C/CookBr00.htm' in receiving

def test_rushing_type():
    assert type(rushing) == list

def test_rushing_length():
    assert len(rushing) > 10

def test_rushing_value():
    assert 'https://www.pro-football-reference.com/players/K/KamaAl00.htm' in rushing

def test_passing_type():
    assert type(passing) == list

def test_passing_len():
    assert len(passing) > 10

def test_passing_value():
    assert 'https://www.pro-football-reference.com/players/N/NewtCa00.htm' in passing

def test_defense_type():
    assert type(defense) == list

def test_defense_len():
    assert len(defense) > 10

def test_defense_value():
    assert 'https://www.pro-football-reference.com/players/O/OnwuPa00.htm' in defense

def test_kicking_type():
    assert type(kicking) == list

def test_kicking_len():
    assert len(kicking) > 10

def test_kicking_value():
    assert 'https://www.pro-football-reference.com/players/Z/ZuerGr00.htm' in kicking
