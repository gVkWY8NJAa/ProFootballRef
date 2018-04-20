import calendar
import pandas as pd
from ProFootballRef.Tools import Loader

class GameLog:
    def __init__(self):
        pass

    def common(self, df, year):
        # Drop rk col
        df.drop(['Rk'], axis=1, inplace=True)

        # drop summary line
        df = df.loc[pd.notnull(df['G#'])]

        # clean home/away
        df['Home'] = df['Home'].fillna('H')
        homemap = {'H': True, '@': False}
        df['Home'] = df['Home'].map(homemap)

        # map home game started
        df['GS'] = df['GS'].fillna('False')
        gsmap = {'*': True, 'False': False}
        df['GS'] = df['GS'].map(gsmap)

        # Recalculate age. profootball ref gives Age in year and days so we'll turn that into a float
        if calendar.isleap(year):
            days = 366
        else:
            days = 365

        Age = df['Age'].str.split('-', expand=True)
        Age[0] = pd.to_numeric(Age[0])
        Age[1] = pd.to_numeric(Age[1])

        df['Age'] = Age[1] / days + Age[0]

        # Split wins and loses w/ points for (PF) and points againat (PA)
        rec = df['Result'].str.split(' ', expand=True)
        df['Result'] = rec[0]
        df['PF'] = pd.to_numeric(rec[1].str.split('-', expand=True)[0])
        df['PA'] = pd.to_numeric(rec[1].str.split('-', expand=True)[1])

        return df

    def gamelog_passing(self, player_link, year, **kwargs):
        # Set up the gamelog suffix
        gamelog_suffix = '/gamelog/%s/' % year

        # Modify the player url to point to the gamelog
        log_url = player_link[:-4] + gamelog_suffix

        # Get html
        html = Loader.Loader().load_page(log_url).content.decode()

        df = pd.read_html(html)[0]

        # Rename columns
        cols = ['Rk', 'Date', 'G#', 'Age', 'Tm', 'Home', 'Opp', 'Result', 'GS',
                'pass_cmp', 'pass_att', 'Cmp%', 'pass_yds', 'pass_td', 'Int', 'Rate',
                'Sk', 'Sk-Yds', 'pass_Y/A', 'AY/A', 'rush_att', 'rush_yds', 'rush_Y/A',
                'rush_TD']

        df.columns = cols

        # send df to the common parser
        df = self.common(df, year)

        df = df[['Date', 'G#', 'Age', 'Tm', 'Home', 'Opp', 'Result', 'PF', 'PA', 'GS', 'pass_cmp', 'pass_att', 'Cmp%',
                 'pass_yds', 'pass_td', 'Int', 'Rate', 'Sk', 'Sk-Yds', 'pass_Y/A', 'AY/A', 'rush_att', 'rush_yds',
                 'rush_Y/A', 'rush_TD']]

        return df