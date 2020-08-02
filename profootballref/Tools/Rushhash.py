import pandas as pd


class RushHash:
    def __init__(self):
        # Combinations of header labels
        # Combinations of header labels
        self.base = ['Rk', 'Date', 'G#', 'Age', 'Tm', 'Home', 'Opp', 'Result', 'GS']
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

    def md5c3695be2dd2fa9307301dccf047b4e86(self, df):
        # Rename columns
        df.columns = self.base + self.rushing + self.receiving + self.kick_rt + self.scoring2p + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.punt_rt)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.punt_rt] = 0

        return df

    def md57f97f3885d50fcf9b92797810856a89f(self, df):
        # Rename columns
        df.columns = self.base + self.rushing + self.receiving + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt + self.punt_rt + self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt + self.punt_rt + self.scoring2p] = 0

        return df

    def md5aa321161d6f3f5230259dbc4ae67299a(self,df):
        # Rename columns
        df.columns = self.base + self.rushing + self.receiving + self.scoring + self.rush_sk

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt + self.punt_rt + self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt + self.punt_rt + self.scoring2p] = 0

        return df

    def md59c11c15180efbf7aec4300fc190cd3a5(self, df):
        # Rename columns
        df.columns = self.base + self.rushing + self.receiving + self.passing + self.scoring2p + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt + self.punt_rt)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt + self.punt_rt] = 0

        return df

    def md5ad9a12e06546e3019128fec57cdc9d0e(self,df):
        # Rename columns
        df.columns = self.base + self.rushing + self.receiving + self.scoring2p + self.scoring + self.rush_sk

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt + self.punt_rt)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt + self.punt_rt] = 0

        return df

    def md500f83a7c4b3e891e3c448db700cc9ada(self,df):
        # Rename columns
        df.columns = self.base + self.rushing + self.receiving + self.scoring2p + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt + self.punt_rt)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt + self.punt_rt] = 0

        return df

    def md55980508dab2f61013bd07809c5ca0e41(self,df):
        # Rename columns
        df.columns = self.base + self.rushing + self.receiving

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.scoring2p + self.scoring + self.kick_rt + self.punt_rt)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.scoring2p + self.scoring + self.kick_rt + self.punt_rt] = 0

        return df

    def md5c35b37a5f0f696bfd1576753faffe81c(self,df):
        # Rename columns
        df.columns = self.base + self.rushing + self.receiving + self.passing + self.scoring + self.rush_sk

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.scoring2p + self.kick_rt + self.punt_rt)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.scoring2p + self.kick_rt + self.punt_rt] = 0

        return df

    def md5aed81e3e77b9842532b5efa73458a259(self,df):
        # Rename columns
        df.columns = self.base + self.rushing + self.receiving + self.kick_rt + self.scoring + self.rush_sk

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.scoring2p + self.punt_rt)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.scoring2p + self.punt_rt] = 0

        return df

    def md57d21a9a4ab9adde626d633fbd62db5c0(self,df):
        # Rename columns
        df.columns = self.base + self.rushing + self.receiving + self.passing + self.scoring2p + self.scoring + self.rush_sk

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.punt_rt + self.kick_rt)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.punt_rt + self.kick_rt] = 0

        return df

    def md591138c3c08c339b71b8323e2bac3aac7(self,df):
        # Rename columns
        df.columns = self.base + self.rushing + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.punt_rt + self.receiving + self.kick_rt + self.scoring2p)],
                       axis=1)

        # set all the new columns to zero
        df.loc[:, self.punt_rt + self.kick_rt + self.receiving + self.scoring2p] = 0

        return df

    def md5ddcb0610869ff21799f008209ac6d229(self, df):
        # Rename columns
        df.columns = self.base + self.rushing + self.receiving + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.punt_rt + self.kick_rt + self.scoring2p)],
                       axis=1)

        # set all the new columns to zero
        df.loc[:, self.punt_rt + self.kick_rt + self.scoring2p] = 0

        return df
