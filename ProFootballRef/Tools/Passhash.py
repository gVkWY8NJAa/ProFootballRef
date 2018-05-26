import pandas as pd


class PassHash:
    def __init__(self):
        # Combinations of header labels
        self.base = ['Rk', 'Date', 'G#', 'Age', 'Tm', 'Home', 'Opp', 'Result', 'GS']
        self.passing = ['pass_cmp', 'pass_att', 'Cmp%', 'pass_yds', 'pass_td', 'Int', 'Rate', 'Sk', 'Sk-Yds', 
                        'pass_Y/A', 'AY/A']
        self.rushing = ['rush_att', 'rush_yds', 'rush_Y/A', 'rush_TD']
        self.rush_sk = ['rush_sk', 'tkl', 'Ast']
        self.receiving = ['Rec_Tgt', 'Rec_Rec', 'Rec_Yds', 'Rec_Y/R', 'Rec_TD', 'Rec_Ctch%', 'Rec_Y/Tgt']
        self.scoring2p = ['2pt']
        self.scoring = ['Any_TD', 'Any_Pts']
        self.punting = ['Pnt', 'Pnt_Yds', 'Y/P', 'Blck']

    def md564b4c5df667e588d59b856ae9d724c7d(self, df):
        cols = self.base + self.passing

        # Rename columns
        df.columns = cols

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.rushing + self.receiving + self.rush_sk + self.scoring2p +
                                                 self.scoring + self.punting)],axis=1)
        
        # set all the new columns to zero
        df.loc[:, self.rushing + self.receiving + self.rush_sk + self.scoring2p + self.scoring + self.punting] = 0

        return df
    
    def md5b06cd4dff23f7376af6a879f99cc5a1c(self, df):

        # Rename columns
        df.columns = self.base + self.passing + self.rushing   
        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.receiving + self.rush_sk + self.scoring2p + self.scoring + self.punting)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.receiving + self.rush_sk + self.scoring2p + self.scoring + self.punting] = 0
        
        return df
    
    def md5677c3564a754183605775bac5aba623d(self, df):

        # rename colsums
        cols = self.base + self.passing + self.rushing + self.scoring
        df.columns = cols

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.receiving + self.rush_sk + self.scoring2p + self.punting)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.receiving + self.rush_sk + self.scoring2p + self.punting] = 0
        
        return df
    
    def md51609c51a70ab5e3d763c0d698e00eb16(self, df):
        # Rename columns
        cols = self.base + self.passing + self.rushing + self.rush_sk
        df.columns = cols

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.receiving + self.scoring2p + self.scoring + self.punting)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.receiving + self.scoring2p + self.scoring + self.punting] = 0
        
        return df
    
    def md59d7339709d13dc7484e7090522596eda(self, df):
        # Rename columns
        cols = self.base + self.passing + self.rushing + self.punting
        df.columns = cols

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.receiving + self.rush_sk + self.scoring2p + self.scoring)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.receiving + self.rush_sk + self.scoring2p + self.scoring] = 0
        
        return df
    
    def md547963026aa9103eea8203b6717da2caf(self, df):
        cols = self.base + self.passing + self.rushing + self.scoring2p + self.scoring

        df.columns = cols
        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.receiving + self.rush_sk + self.punting)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.receiving + self.rush_sk + self.punting] = 0
        
        return df
    
    def md50feae896081ca775b997f372f93d1977(self, df):
        cols = self.base + self.passing + self.rushing + self.rush_sk + self.scoring2p + self.scoring

        df.columns = cols

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.receiving + self.punting)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.receiving + self.punting] = 0
        
        return df
    
    def md5366e35869d52cf189f6575ef82c562e1(self, df):
        # Rename columns
        cols = self.base + self.passing + self.rushing + self.scoring + self.rush_sk
        df.columns = cols

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.receiving + self.scoring2p + self.punting)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.receiving + self.scoring2p + self.punting] = 0
        
        return df

    def md5c34721f06f1a5aad95fab7fc16577538(self, df):
        # Rename columns
        cols = self.base + self.passing + self.rushing + self.scoring + self.punting
        df.columns = cols

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.receiving + self.scoring2p + self.rush_sk)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.receiving + self.scoring2p + self.rush_sk] = 0
        
        return df

    def md5afa7cf6859400c6023d114abc175c24d(self, df):
        # rename cols
        cols = self.base + self.passing + self.rushing + self.receiving
        df.columns = cols

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.rush_sk + self.scoring2p + self.scoring + self.punting)],
                       axis=1)

        # set all the new columns to zero
        df.loc[:, self.rush_sk + self.scoring2p + self.scoring + self.punting] = 0
        
        return df

    def md560befa83b7115d584e02dea9908a707d(self, df):

        #slice df
        df = df.iloc[:, :31]
        # rename cols
        cols = self.base + self.passing + self.rushing + self.receiving
        df.columns = cols

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.rush_sk + self.scoring2p + self.scoring + self.punting)],
                       axis=1)

        # set all the new columns to zero
        df.loc[:, self.rush_sk + self.scoring2p + self.scoring + self.punting] = 0

        return df

    def md52451894bb088c27b0a02ad350e35b9ad(self, df):
        # rename cols
        cols = self.base + self.passing + self.rushing + self.receiving + self.scoring
        df.columns = cols

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.rush_sk + self.scoring2p + self.punting)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.rush_sk + self.scoring2p + self.punting] = 0
        
        return df

    def md5e22db471405382c6d4e868c4d29d9cb5(self, df):
        # rename cols
        cols = self.base + self.passing + self.rushing + self.receiving + self.scoring + self.rush_sk
        df.columns = cols

        # add missing cols
        df = pd.concat([df, pd.DataFrame(columns=self.punting + self.scoring2p)], axis=1)

        # set all the new columns to zero
        df.loc[:, self.punting + self.scoring2p] = 0
        
        return df
