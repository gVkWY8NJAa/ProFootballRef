import pandas as pd


class RecHash:
    def __init__(self):
        # Combinations of header labels
        self.base = ['Rk', 'Date', 'G#', 'Age', 'Tm', 'Home', 'Opp', 'Result']
        self.receiving = ['Rec_Tgt', 'Rec_Rec', 'Rec_Yds', 'Rec_Y/R', 'Rec_TD', 'Rec_Ctch%', 'Rec_Y/Tgt']
        self.rushing = ['rush_att', 'rush_yds', 'rush_Y/A', 'rush_TD']
        self.passing = ['pass_cmp', 'pass_att', 'Cmp%', 'pass_yds', 'pass_td', 'Int', 'Rate', 'Sk', 'Sk-Yds',
                        'pass_Y/A', 'AY/A']
        self.rush_sk = ['rush_sk', 'tkl', 'Ast']
        self.scoring2p = ['2pt']
        self.scoring = ['Any_TD', 'Any_Pts']
        self.punting = ['Pnt', 'Pnt_Yds', 'Y/P', 'Blck']
        self.kick_rt = ['Kick_Rt', 'Kick_RtYds', 'Y/Rt', 'Kick_TD']
        self.punt_rt = ['Pnt_rt', 'Pnt_Yds', 'Y/Pnt', 'Pnt_TD']

    def md5b3c4237d9a10de8cfaad61852cb552c4(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.rushing + self.kick_rt + self.punt_rt + self.scoring + self.rush_sk

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.scoring2p] = 0

        return df


    def md5bcb96297b50fb2120f475e8e05fbabcd(self,df):

        # Rename columns
        df.columns = self.base + self.receiving + self.rushing + self.passing + self.kick_rt + self.punt_rt + self.scoring2p + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.rush_sk)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.rush_sk] = 0

        return df

    def md54560c290b45e942c16cc6d7811345fce(self,df):

        # Rename columns
        df.columns = self.base + self.receiving + self.rushing + self.passing + self.punt_rt + self.scoring2p + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt] = 0

        return df

    def md54c82a489ec5b2c943e78c9018dcbbca1(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.rushing + self.passing + self.punt_rt + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt + self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt + self.scoring2p] = 0

        return df

    def md5e8ffc7202223bb253e92da83b76e9944(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.rushing + self.passing + self.punt_rt + self.scoring + self.rush_sk

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt + self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt + self.scoring2p] = 0

        return df

    def md550fcceaa170b1a1e501e3f40548e403d(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.rushing + self.kick_rt + self.punt_rt + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.scoring2p] = 0

        return df

    def md5e160e714b29305ecfecf513cbf84b80f(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.rushing + self.punt_rt + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt + self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt + self.scoring2p] = 0

        return df

    def md5111e8480632f73642d7e20acbdbe6b16(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.rushing + self.kick_rt + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.punt_rt + self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.punt_rt + self.scoring2p] = 0

        return df

    def md5adc05c5af0f88775d3605d02c831c0ed(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.scoring + self.rush_sk

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.punt_rt + self.scoring2p + self.rushing + self.kick_rt)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.punt_rt + self.scoring2p + self.rushing + self.kick_rt] = 0

        return df

    def md5bfbf86ae0485a0a70692ae04124449b9(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.scoring2p + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.punt_rt + self.rushing + self.kick_rt + self.rush_sk)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.punt_rt + self.rushing + self.kick_rt + self.rush_sk] = 0

        return df

    def md56b4698269dd34a823cf6b233c6165614(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.scoring

        # add missing cols
        df = pd.concat(
            [df, pd.DataFrame(columns=self.punt_rt + self.rushing + self.kick_rt + self.rush_sk + self.scoring2p)],
            axis=1)

        # set all the new columns to zero
        df.loc[:, self.punt_rt + self.rushing + self.kick_rt + self.rush_sk + self.scoring2p] = 0

        return df

    def md57f97f3885d50fcf9b92797810856a89f(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.rushing + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.punt_rt + self.kick_rt + self.rush_sk + self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.punt_rt + self.kick_rt + self.rush_sk + self.scoring2p] = 0

        return df

    def md5aa321161d6f3f5230259dbc4ae67299a(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.rushing + self.scoring + self.rush_sk

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.punt_rt + self.kick_rt + self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.punt_rt + self.kick_rt + self.scoring2p] = 0

        return df

    def md51193d47266d4acdcf1b6fca165121100(self, df):

        # Rename columns
        df.columns = self.base + self.receiving + self.rushing + self.passing + self.kick_rt + self.punt_rt + \
                     self.scoring + self.rush_sk

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.scoring2p] = 0

        return df

    def md552589e869a13d76c6d0dbf066cab536f(self, df):
        # Rename columns
        df.columns = self.base + self.receiving + self.rush_sk

        # add missing cols
        df = pd.concat(
            [df, pd.DataFrame(columns=self.punt_rt + self.rushing + self.kick_rt + self.scoring + self.scoring2p)],
            axis=1)

        # set all the new columns to zero
        df.loc[:, self.punt_rt + self.rushing + self.kick_rt + self.scoring + self.scoring2p] = 0

        return df

