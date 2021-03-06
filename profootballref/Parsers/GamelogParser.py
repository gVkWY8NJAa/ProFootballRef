import calendar
import pandas as pd
import hashlib
import json
from profootballref.Parsers import PlayerParser
from profootballref.Tools import Loader
from profootballref.Tools import Passhash
from profootballref.Tools import Rechash
from profootballref.Tools import Rushhash
from profootballref.Tools import Kickhash
from profootballref.Tools import Defhash

pd.set_option('display.max_columns', None)


class GameLog:
    def __init__(self):
        pass

    def common(self, dframe, year):

        # Drop rk col
        dframe = dframe.drop(['Rk'], axis=1)

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

        dframe.loc[:, 'Age'] = dframe.loc[:, 'Age'].astype(str)
        age = dframe.loc[:, 'Age'].str.split('.', expand=True)
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

        # drop first level of cols
        df.columns = df.columns.droplevel()

        # rename the home column
        df = df.rename(columns={df.columns[5]: "Home"})

        # There may be many extra blank cols, delet them

        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # send df to the common parser
        df = self.common(df, year)

        # Add the name
        df.loc[:, 'Name'] = gen['name']

        # Add the players position
        df.loc[:, 'Pos'] = gen['position']

        # add additional player info
        df['Throws'] = gen['throws']
        df['Height'] = gen['height']
        df['Weight'] = gen['weight']
        df['DOB_mo'] = gen['bday_mo']
        df['DOB_day'] = gen['bday_day']
        df['DOB_yr'] = gen['bday_yr']
        df['College'] = gen['college']

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

        # Here we make a dict of hashes and their corresponding column parser, this is faster than if/else
        options = { "b3c4237d9a10de8cfaad61852cb552c4": Rechash.RecHash().md5b3c4237d9a10de8cfaad61852cb552c4,
                    "bcb96297b50fb2120f475e8e05fbabcd": Rechash.RecHash().md5bcb96297b50fb2120f475e8e05fbabcd,
                    "4560c290b45e942c16cc6d7811345fce": Rechash.RecHash().md54560c290b45e942c16cc6d7811345fce,
                    "4c82a489ec5b2c943e78c9018dcbbca1": Rechash.RecHash().md54c82a489ec5b2c943e78c9018dcbbca1,
                    "e8ffc7202223bb253e92da83b76e9944": Rechash.RecHash().md5e8ffc7202223bb253e92da83b76e9944,
                    "50fcceaa170b1a1e501e3f40548e403d": Rechash.RecHash().md550fcceaa170b1a1e501e3f40548e403d,
                    "e160e714b29305ecfecf513cbf84b80f": Rechash.RecHash().md5e160e714b29305ecfecf513cbf84b80f,
                    "111e8480632f73642d7e20acbdbe6b16": Rechash.RecHash().md5111e8480632f73642d7e20acbdbe6b16,
                    "adc05c5af0f88775d3605d02c831c0ed": Rechash.RecHash().md5adc05c5af0f88775d3605d02c831c0ed,
                    "bfbf86ae0485a0a70692ae04124449b9": Rechash.RecHash().md5bfbf86ae0485a0a70692ae04124449b9,
                    "6b4698269dd34a823cf6b233c6165614": Rechash.RecHash().md56b4698269dd34a823cf6b233c6165614,
                    "7f97f3885d50fcf9b92797810856a89f": Rechash.RecHash().md57f97f3885d50fcf9b92797810856a89f,
                    "aa321161d6f3f5230259dbc4ae67299a": Rechash.RecHash().md5aa321161d6f3f5230259dbc4ae67299a,
                    "1193d47266d4acdcf1b6fca165121100": Rechash.RecHash().md51193d47266d4acdcf1b6fca165121100,
                    "52589e869a13d76c6d0dbf066cab536f": Rechash.RecHash().md552589e869a13d76c6d0dbf066cab536f,
                    "d522b9357244c20714a3b21f8f404918": Rechash.RecHash().md5d522b9357244c20714a3b21f8f404918}

        df = options[which_cols](df)

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

    def rushing(self, player_link, year, **kwargs):

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

        # Here we make a dict of hashes and their corresponding column parser, this is faster than if/else
        options = {'c3695be2dd2fa9307301dccf047b4e86': Rushhash.RushHash().md5c3695be2dd2fa9307301dccf047b4e86,
                   '7f97f3885d50fcf9b92797810856a89f': Rushhash.RushHash().md57f97f3885d50fcf9b92797810856a89f,
                   'aa321161d6f3f5230259dbc4ae67299a': Rushhash.RushHash().md5aa321161d6f3f5230259dbc4ae67299a,
                   '9c11c15180efbf7aec4300fc190cd3a5': Rushhash.RushHash().md59c11c15180efbf7aec4300fc190cd3a5,
                   'ad9a12e06546e3019128fec57cdc9d0e': Rushhash.RushHash().md5ad9a12e06546e3019128fec57cdc9d0e,
                   '00f83a7c4b3e891e3c448db700cc9ada': Rushhash.RushHash().md500f83a7c4b3e891e3c448db700cc9ada,
                   '5980508dab2f61013bd07809c5ca0e41': Rushhash.RushHash().md55980508dab2f61013bd07809c5ca0e41,
                   'c35b37a5f0f696bfd1576753faffe81c': Rushhash.RushHash().md5c35b37a5f0f696bfd1576753faffe81c,
                   'aed81e3e77b9842532b5efa73458a259': Rushhash.RushHash().md5aed81e3e77b9842532b5efa73458a259,
                   '7d21a9a4ab9adde626d633fbd62db5c0': Rushhash.RushHash().md57d21a9a4ab9adde626d633fbd62db5c0,
                   '91138c3c08c339b71b8323e2bac3aac7': Rushhash.RushHash().md591138c3c08c339b71b8323e2bac3aac7,
                   'ddcb0610869ff21799f008209ac6d229': Rushhash.RushHash().md5ddcb0610869ff21799f008209ac6d229}

        df = options[which_cols](df)

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
                Rushhash.RushHash().base[1:] + ['PF', 'PA'] + Rushhash.RushHash().receiving + Rushhash.RushHash().rushing +
                Rushhash.RushHash().kick_rt + Rushhash.RushHash().punt_rt + Rushhash.RushHash().scoring2p +
                Rushhash.RushHash().scoring]

        return df

    def kicking(self, player_link, year, **kwargs):
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

        # Here we make a dict of hashes and their corresponding column parser, this is faster than if/else
        options = {'080683052961d92b5efd07588e614700': Kickhash.KickHash().md5080683052961d92b5efd07588e614700,
                   'c0fe30e42184e7a59c00c04dc917bb87': Kickhash.KickHash().md5c0fe30e42184e7a59c00c04dc917bb87,
                   '7ad30bf95e287937864b02dca25801bf': Kickhash.KickHash().md57ad30bf95e287937864b02dca25801bf}

        df = options[which_cols](df)

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
                Kickhash.KickHash().base[1:] + ['PF', 'PA'] + Kickhash.KickHash().scoring]

        return df

    def defense(self, player_link, year, **kwargs):
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

        # Here we make a dict of hashes and their corresponding column parser, this is faster than if/else
        options = {'0c329a15f241e5c132d0d5c7612032c0': Defhash.DefHash().md50c329a15f241e5c132d0d5c7612032c0,
                   '58ffdd172c2358c5e5ab2e0a1994252a': Defhash.DefHash().md558ffdd172c2358c5e5ab2e0a1994252a,
                   '141f3f6945aa9495c6580650649f4b8f': Defhash.DefHash().md5141f3f6945aa9495c6580650649f4b8f,
                   '109394668745222b0ccbd92bfd0ac4c1': Defhash.DefHash().md5109394668745222b0ccbd92bfd0ac4c1,
                   '60dfaf4e946c4ae3d47c6d8b430c92a4': Defhash.DefHash().md560dfaf4e946c4ae3d47c6d8b430c92a4,
                   'fa476dd5c907f86452c016e54b3fe0f8': Defhash.DefHash().md5fa476dd5c907f86452c016e54b3fe0f8}

        df = options[which_cols](df)

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
                Defhash.DefHash().base[1:] + ['PF', 'PA'] +  Defhash.DefHash().punt_rt + Defhash.DefHash().kick_rt +
                Defhash.DefHash().scoring + Defhash.DefHash().rush_sk + Defhash.DefHash().def_int]

        return df
