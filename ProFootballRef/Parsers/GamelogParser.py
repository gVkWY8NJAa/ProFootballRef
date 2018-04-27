import calendar
import pandas as pd
import hashlib
import json
from ProFootballRef.Parsers import PlayerParser
from ProFootballRef.Tools import Loader
from ProFootballRef.Tools import Passhash

pd.set_option('display.max_columns', None)


class GameLog:
    def __init__(self):
        # Combinations of header labels
        self.base = ['Rk', 'Date', 'G#', 'Age', 'Tm', 'Home', 'Opp', 'Result', 'GS']
        self.passing = ['pass_cmp', 'pass_att', 'Cmp%', 'pass_yds', 'pass_td', 'Int', 'Rate', 'Sk', 'Sk-Yds',
                        'pass_Y/A', 'AY/A']
        self.rushing = ['rush_att', 'rush_yds', 'rush_Y/A', 'rush_TD']
        self.rush_sk = ['rush_sk', 'tkl', 'Ast']
        self.receiving = ['Rec_Tgt', 'Rec_Rec', 'Rec_Yds', 'Rec_Y/R', 'Rec_TD', 'Rec_Ctch%', 'Rec_Y/Tgt']
        self.scoring2p = ['2pm']
        self.scoring = ['Any_TD', 'Any_Pts']
        self.punting = ['Pnt', 'Pnt_Yds', 'Y/P', 'Blck']

    def common(self, dframe, year):
        # Drop rk col
        dframe.drop(['Rk'], axis=1, inplace=True)

        # drop summary line
        dframe = dframe.loc[pd.notnull(dframe.loc[:, 'G#'])]

        # clean home/away
        dframe.loc[:, 'Home'].fillna('H', inplace=True)
        homemap = {'H': True, '@': False}
        dframe.loc[:, 'Home'] = dframe.loc[:, 'Home'].map(homemap)

        # map home game started
        dframe.loc[:, 'GS'] = dframe.loc[:, 'GS'].fillna('False')
        gsmap = {'*': True, 'False': False}
        dframe.loc[:, 'GS'] = dframe.loc[:, 'GS'].map(gsmap)

        # Recalculate age. profootball ref gives Age in year and days so we'll turn that into a float
        if calendar.isleap(year):
            days = 366
        else:
            days = 365

        Age = dframe.loc[:, 'Age'].str.split('-', expand=True)
        Age[0] = pd.to_numeric(Age[0])
        Age[1] = pd.to_numeric(Age[1])

        dframe.loc[:, 'Age'] = Age[1] / days + Age[0]

        # Split wins and loses w/ points for (PF) and points againat (PA)
        rec = dframe.loc[:, 'Result'].str.split(' ', expand=True)
        dframe.loc[:, 'Result'] = rec[0]
        dframe.loc[:, 'PF'] = pd.to_numeric(rec[1].str.split('-', expand=True)[0])
        dframe.loc[:, 'PA'] = pd.to_numeric(rec[1].str.split('-', expand=True)[1])

        return dframe

    def gamelog_passing(self, player_link, year, **kwargs):
        # Set up the gamelog suffix
        gamelog_suffix = '/gamelog/%s/' % year

        # Modify the player url to point to the gamelog
        log_url = player_link[:-4] + gamelog_suffix

        # Get html
        html = Loader.Loader().load_page(log_url).content.decode()

        # gent general stats
        gen = PlayerParser.PlayerParser().parse_general_info(html)

        # parse tables w pandas
        df = pd.read_html(html)[0]

        which_cols = hashlib.md5(json.dumps(list(df.columns.levels[0])).encode()).hexdigest()

        if which_cols == "64b4c5df667e588d59b856ae9d724c7d":
            df = Passhash.PassHash().md564b4c5df667e588d59b856ae9d724c7d(df)

        elif which_cols == "b06cd4dff23f7376af6a879f99cc5a1c":
            df = Passhash.PassHash().md5b06cd4dff23f7376af6a879f99cc5a1c(df)

        elif which_cols == "677c3564a754183605775bac5aba623d":
            df = Passhash.PassHash().md5677c3564a754183605775bac5aba623d(df)

        elif which_cols == "1609c51a70ab5e3d763c0d698e00eb16":
            df = Passhash.PassHash().md51609c51a70ab5e3d763c0d698e00eb16(df)

        elif which_cols == "9d7339709d13dc7484e7090522596eda":
            df = Passhash.PassHash().md59d7339709d13dc7484e7090522596eda(df)

        elif which_cols == "47963026aa9103eea8203b6717da2caf":
            df = Passhash.PassHash().md547963026aa9103eea8203b6717da2caf(df)

        elif which_cols == "0feae896081ca775b997f372f93d1977":
            df = Passhash.PassHash().md50feae896081ca775b997f372f93d1977(df)

        elif which_cols == "366e35869d52cf189f6575ef82c562e1":
            df = Passhash.PassHash().md5366e35869d52cf189f6575ef82c562e1(df)

        elif which_cols == "c34721f06f1a5aad95fab7fc16577538":
            df = Passhash.PassHash().md5c34721f06f1a5aad95fab7fc16577538(df)

        elif which_cols == "afa7cf6859400c6023d114abc175c24d":
            df = Passhash.PassHash().md5afa7cf6859400c6023d114abc175c24d(df)

        elif which_cols == "2451894bb088c27b0a02ad350e35b9ad":
            df = Passhash.PassHash().md52451894bb088c27b0a02ad350e35b9ad(df)

        elif which_cols == "e22db471405382c6d4e868c4d29d9cb5":
            df = Passhash.PassHash().md5e22db471405382c6d4e868c4d29d9cb5(df)

        # send df to the common parser
        df = self.common(df, year)

        # Ensure any commonly missing values are set
        df.loc[:, 'Name'] = gen['name']
        df.loc[:, 'Pos'] = gen['position']

        # add additional player info
        df['Throws'] = gen['throws']
        df['Height'] = gen['height']
        df['Weight'] = gen['weight']
        df['DOB_mo'] = gen['bday_mo']
        df['DOB_day'] = gen['bday_day']
        df['DOB_yr'] = gen['bday_yr']
        df['College'] = gen['college']

        df = df[['Name','Pos', 'Height', 'Weight', 'DOB_mo', 'DOB_day', 'DOB_yr', 'College'] + self.base[1:] +
                ['PF', 'PA'] + self.passing + self.rushing + self.receiving + self.rush_sk + self.scoring2p +
                self.scoring + self.punting]

        return df