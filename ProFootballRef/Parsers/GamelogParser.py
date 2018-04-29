import calendar
import pandas as pd
import hashlib
import json
from ProFootballRef.Parsers import PlayerParser
from ProFootballRef.Tools import Loader
from ProFootballRef.Tools import Passhash
from ProFootballRef.Tools import Rechash

pd.set_option('display.max_columns', None)


class GameLog:
    def __init__(self):
        pass

    def common(self, dframe, year):

        # Drop rk col
        dframe.drop(['Rk'], axis=1, inplace=True)

        # drop summary line
        dframe = dframe.loc[pd.notnull(dframe.loc[:, 'G#'])]

        # clean home/away
        dframe.loc[:, 'Home'].fillna('H', inplace=True)
        homemap = {'H': True, '@': False}
        dframe.loc[:, 'Home'] = dframe.loc[:, 'Home'].map(homemap)

        # map if the player was listed as a starter, this is only used for QBs
        if 'GS' in dframe.columns:
            dframe.loc[:, 'GS'] = dframe.loc[:, 'GS'].fillna('False')
            gsmap = {'*': True, 'False': False}
            dframe.loc[:, 'GS'] = dframe.loc[:, 'GS'].map(gsmap)

        # Recalculate age. profootball ref gives Age in year and days so we'll turn that into a float
        if calendar.isleap(year):
            days = 366
        else:
            days = 365

        age = dframe.loc[:, 'Age'].str.split('-', expand=True)
        age[0] = pd.to_numeric(age[0])
        age[1] = pd.to_numeric(age[1])

        dframe.loc[:, 'Age'] = age[1] / days + age[0]

        # Split wins and loses w/ points for (PF) and points againat (PA)
        rec = dframe.loc[:, 'Result'].str.split(' ', expand=True)
        dframe.loc[:, 'Result'] = rec[0]
        dframe.loc[:, 'PF'] = pd.to_numeric(rec[1].str.split('-', expand=True)[0])
        dframe.loc[:, 'PA'] = pd.to_numeric(rec[1].str.split('-', expand=True)[1])

        return dframe

    def passing(self, player_link, year, **kwargs):
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

        # make a hash of the column names to tell which values exist
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

        df = df[['Name', 'Pos', 'Height', 'Weight', 'DOB_mo', 'DOB_day', 'DOB_yr', 'College'] +
                Passhash.PassHash().base[1:] + ['GS'] + ['PF', 'PA'] + Passhash.PassHash().passing +
                Passhash.PassHash().rushing + Passhash.PassHash().receiving + Passhash.PassHash().rush_sk +
                Passhash.PassHash().scoring2p + Passhash.PassHash().scoring + Passhash.PassHash().punting]

        return df

    def receiving(self, player_link, year, **kwargs):
        # Set up the gamelog suffix
        gamelog_suffix = '/gamelog/%s/' % year

        # Modify the player url to point to the gamelog
        log_url = player_link[:-4] + gamelog_suffix

        # Get html
        html = Loader.Loader().load_page(log_url).content.decode()

        # ************** generate general stats, these need to be combined later ******************
        gen = PlayerParser.PlayerParser().parse_general_info(html)

        # parse tables w pandas
        df = pd.read_html(html)[0]

        # hash the columns to determine which fields are being used
        which_cols = hashlib.md5(json.dumps(list(df.columns.levels[0])).encode()).hexdigest()

        if which_cols == "b3c4237d9a10de8cfaad61852cb552c4":
            df = Rechash.RecHash().md5b3c4237d9a10de8cfaad61852cb552c4(df)

        elif which_cols == "bcb96297b50fb2120f475e8e05fbabcd":
            df = Rechash.RecHash().md5bcb96297b50fb2120f475e8e05fbabcd(df)

        elif which_cols == "4560c290b45e942c16cc6d7811345fce":
            df = Rechash.RecHash().md54560c290b45e942c16cc6d7811345fce(df)

        elif which_cols == "4c82a489ec5b2c943e78c9018dcbbca1":
            df = Rechash.RecHash().md54c82a489ec5b2c943e78c9018dcbbca1(df)

        elif which_cols == "e8ffc7202223bb253e92da83b76e9944":
            df = Rechash.RecHash().md5e8ffc7202223bb253e92da83b76e9944(df)

        elif which_cols == "50fcceaa170b1a1e501e3f40548e403d":
            df = Rechash.RecHash().md550fcceaa170b1a1e501e3f40548e403d(df)

        elif which_cols == "e160e714b29305ecfecf513cbf84b80f":
            df = Rechash.RecHash().md5e160e714b29305ecfecf513cbf84b80f(df)

        elif which_cols == "111e8480632f73642d7e20acbdbe6b16":
            df = Rechash.RecHash().md5111e8480632f73642d7e20acbdbe6b16(df)

        elif which_cols == "adc05c5af0f88775d3605d02c831c0ed":
            df = Rechash.RecHash().md5adc05c5af0f88775d3605d02c831c0ed(df)

        elif which_cols == "bfbf86ae0485a0a70692ae04124449b9":
            df = Rechash.RecHash().md5bfbf86ae0485a0a70692ae04124449b9(df)

        elif which_cols == "6b4698269dd34a823cf6b233c6165614":
            df = Rechash.RecHash().md56b4698269dd34a823cf6b233c6165614(df)

        elif which_cols == "7f97f3885d50fcf9b92797810856a89f":
            df = Rechash.RecHash().md57f97f3885d50fcf9b92797810856a89f(df)

        elif which_cols == "aa321161d6f3f5230259dbc4ae67299a":
            df = Rechash.RecHash().md5aa321161d6f3f5230259dbc4ae67299a(df)

        elif which_cols == "1193d47266d4acdcf1b6fca165121100":
            df = Rechash.RecHash().md51193d47266d4acdcf1b6fca165121100(df)

        # send df to the common parser
        df = self.common(df, year)

        # Add the name
        df.loc[:, 'Name'] = gen['name']

        # Add the players position
        df.loc[:, 'Pos'] = gen['position']

        df['Throws'] = gen['throws']
        df['Height'] = gen['height']
        df['Weight'] = gen['weight']
        df['DOB_mo'] = gen['bday_mo']
        df['DOB_day'] = gen['bday_day']
        df['DOB_yr'] = gen['bday_yr']
        df['College'] = gen['college']

        df = df[['Name', 'Pos', 'Height', 'Weight', 'DOB_mo', 'DOB_day', 'DOB_yr', 'College'] +
                Rechash.RecHash().base[1:] + ['PF', 'PA'] + Rechash.RecHash().receiving + Rechash.RecHash().rushing +
                Rechash.RecHash().kick_rt + Rechash.RecHash().punt_rt + Rechash.RecHash().scoring2p +
                Rechash.RecHash().scoring]

        return df