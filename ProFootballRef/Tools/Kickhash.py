import pandas as pd


class KickHash:
    def __init__(self):
        # Combinations of header labels
        self.base = ['Rk', 'Date', 'G#', 'Age', 'Tm', 'Home', 'Opp', 'Result']
        self.rush_sk = ['rush_sk', 'tkl', 'Ast']
        self.scoring = ['XPM', 'XPA', 'XP%', 'FGM', 'FGA', 'FG%', 'TD', 'Pts']

    def md5080683052961d92b5efd07588e614700(self, df):
        # Rename columns
        df.columns = self.base + self.scoring + self.rush_sk

        return df

    def md5c0fe30e42184e7a59c00c04dc917bb87(self, df):
        # Rename columns
        df.columns = self.base + self.scoring

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.rush_sk)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.rush_sk] = 0

        return df
