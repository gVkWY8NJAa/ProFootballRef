import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString


class TeamStats:
    def __init__(self):
        pass

    def offense(self, year):
        # Get offense
        url = 'https://www.pro-football-reference.com/years/%s/#team_stats' % year
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
        soup = BeautifulSoup(page.content, "html5lib")
        comment = soup.find(text=lambda x: isinstance(x, NavigableString) and "team_stats" in x)

        df = pd.read_html(comment)[0]

        # drop a nunch of unused columns
        df = df.iloc[:, 1:28]

        # Rename columns
        cols = ['Tm', 'G', 'PF', 'Yds', 'Ply', 'Y/P', 'TO', 'FL', '1stD', 'Pass_Cmp', 'Pass_Att', 'Pass_Yds', 'Pass_TD',
                'Int', 'NY/A', 'Pass_1stD', 'Rush_Att', 'Rush_Yds', 'Rush_TD', 'Y/A', 'Rush_1stD', 'Pen', 'Pen_Yds',
                '1stPy', 'Sc%', 'TO%', 'EXP']

        df.columns = cols

        # Remove last row
        df = df[df.Tm != 'Avg Team']

        # Ensure values are numeric
        df[cols] = df[cols].apply(pd.to_numeric, errors='ignore')

        return df

    def defense(self, year):
        defense = pd.read_html('https://www.pro-football-reference.com/years/%s/opp.htm' % (year))[0]

        # drop rk and multiple unuse cols
        defense = defense.iloc[:, 1:28]

        # rename cols
        cols = ['Tm', 'G', 'PF', 'Yds', 'Ply', 'Y/P', 'TO', 'FL', '1stD', 'Pass_Cmp', 'Pass_Att', 'Pass_Yds', 'Pass_TD',
                'Int', 'NY/A', 'Pass_1stD', 'Rush_Att', 'Rush_Yds', 'Rush_TD', 'Y/A', 'Rush_1stD', 'Pen', 'Pen_Yds',
                '1stPy', 'Sc%', 'TO%', 'EXP']
        defense.columns = cols

        # drop avg row
        defense = defense[defense.Tm != 'Avg Team']

        # Ensure values are numeric
        defense[cols] = defense[cols].apply(pd.to_numeric, errors='ignore')

        return defense