import pandas as pd


class DefHash:
    def __init__(self):
        # Combinations of header labels
        self.base = ['Rk', 'Date', 'G#', 'Age', 'Tm', 'Home', 'Opp', 'Result']

        self.rush_sk = ['rush_sk', 'tkl', 'Ast']

        self.def_int = ['Int', 'Yds', 'TD']

        self.scoring = ['Any_TD', 'Any_Pts']

        self.punt_rt = ['Pnt_rt', 'Pnt_Yds', 'Y/Pnt', 'Pnt_TD']

        self.kick_rt = ['Kick_Rt', 'Kick_RtYds', 'Y/Rt', 'Kick_TD']

    def md50c329a15f241e5c132d0d5c7612032c0(self, df):
        # Rename columns
        df.columns = self.base + self.punt_rt + self.rush_sk + self.def_int

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt + self.scoring)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt + self.scoring] = 0

        return df

    def md558ffdd172c2358c5e5ab2e0a1994252a(self, df):
        # Rename columns
        df.columns = self.base + self.kick_rt + self.punt_rt + self.scoring + self.def_int

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.rush_sk)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.rush_sk] = 0

        return df

    def md5141f3f6945aa9495c6580650649f4b8f(self, df):
        # Rename columns
        df.columns = self.base + self.rush_sk + self.def_int

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt + self.punt_rt + self.scoring)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt + self.punt_rt + self.scoring] = 0

        return df

    def md5109394668745222b0ccbd92bfd0ac4c1(self, df):
        # Rename columns
        df.columns = self.base + self.kick_rt + self.punt_rt + self.rush_sk + self.def_int

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.scoring)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.scoring] = 0

        return df

    def md560dfaf4e946c4ae3d47c6d8b430c92a4(self, df):
        # Rename columns
        df.columns = self.base + self.scoring + self.rush_sk + self.def_int

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.kick_rt + self.punt_rt)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.kick_rt + self.punt_rt] = 0

        return df