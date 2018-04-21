import calendar
import pandas as pd
from ProFootballRef.Parsers import PlayerParser
from ProFootballRef.Tools import Loader

pd.set_option('display.max_columns', None)


class GameLog:
    def __init__(self):
        pass

    def common(self, df, year):
        # Drop rk col
        df.drop(['Rk'], axis=1, inplace=True)

        # drop summary line
        df = df.loc[pd.notnull(df.loc[:, 'G#'])]

        # clean home/away
        df.loc[:, 'Home'] = df.loc[:, 'Home'].fillna('H')
        homemap = {'H': True, '@': False}
        df.loc[:, 'Home'] = df.loc[:, 'Home'].map(homemap)

        # map home game started
        df.loc[:, 'GS'] = df.loc[:, 'GS'].fillna('False')
        gsmap = {'*': True, 'False': False}
        df.loc[:, 'GS'] = df.loc[:, 'GS'].map(gsmap)

        # Recalculate age. profootball ref gives Age in year and days so we'll turn that into a float
        if calendar.isleap(year):
            days = 366
        else:
            days = 365

        Age = df.loc[:, 'Age'].str.split('-', expand=True)
        Age[0] = pd.to_numeric(Age[0])
        Age[1] = pd.to_numeric(Age[1])

        df.loc[:, 'Age'] = Age[1] / days + Age[0]

        # Split wins and loses w/ points for (PF) and points againat (PA)
        rec = df.loc[:, 'Result'].str.split(' ', expand=True)
        df.loc[:, 'Result'] = rec[0]
        df.loc[:, 'PF'] = pd.to_numeric(rec[1].str.split('-', expand=True)[0])
        df.loc[:, 'PA'] = pd.to_numeric(rec[1].str.split('-', expand=True)[1])

        return df

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

        # Combinations of header labels
        base = ['Rk', 'Date', 'G#', 'Age', 'Tm', 'Home', 'Opp', 'Result', 'GS']
        passing = ['pass_cmp', 'pass_att', 'Cmp%', 'pass_yds', 'pass_td', 'Int', 'Rate', 'Sk', 'Sk-Yds', 'pass_Y/A',
                   'AY/A']
        rushing = ['rush_att', 'rush_yds', 'rush_Y/A', 'rush_TD']
        rush_sk = ['rush_sk', 'tkl', 'Ast']
        receiving = ['Rec_Tgt', 'Rec_Rec', 'Rec_Yds', 'Rec_Y/R', 'Rec_TD', 'Rec_Ctch%', 'Rec_Y/Tgt']
        scoring = ['Any_TD', 'Any_Pts']
        punting = ['Pnt', 'Pnt_Yds', 'Y/P', 'Blck']

        if len(df.columns) == 20:
            cols = base + passing

            # Rename columns
            df.columns = cols

            # add missing cols
            df = pd.concat([df, pd.DataFrame(columns=rushing + receiving + rush_sk + scoring + punting)], axis=1)

            # set all the new columns to zero
            df.loc[:, rushing + receiving + rush_sk + scoring + punting] = 0

        elif len(df.columns) == 24:

            # Rename columns
            df.columns = base + passing + rushing

            # add missing cols
            df = pd.concat([df, pd.DataFrame(columns=receiving + rush_sk + scoring + punting)], axis=1)

            # set all the new columns to zero
            df.loc[:, receiving + rush_sk + scoring + punting] = 0


        elif len(df.columns) == 26:

            # rename colsums
            cols = base + passing + rushing + scoring
            df.columns = cols

            # add missing cols
            df = pd.concat([df, pd.DataFrame(columns=receiving + rush_sk + punting)], axis=1)

            # set all the new columns to zero
            df.loc[:, receiving + rush_sk + scoring + punting] = 0


        elif len(df.columns) == 27:
            # Rename columns
            cols = base + passing + rushing + rush_sk
            df.columns = cols

            # add missing cols
            df = pd.concat([df, pd.DataFrame(columns=receiving + scoring + punting)], axis=1)

            # set all the new columns to zero
            df.loc[:, receiving + scoring + punting] = 0


        elif len(df.columns) == 28:
            # Rename columns
            cols = base + passing + rushing + punting
            df.columns = cols

            # add missing cols
            df = pd.concat([df, pd.DataFrame(columns=receiving + rush_sk + scoring)], axis=1)

            # set all the new columns to zero
            df.loc[:, receiving + rush_sk + scoring] = 0


        elif len(df.columns) == 29:
            # Rename columns
            cols = base + passing + rushing + scoring + rush_sk
            df.columns = cols

            # add missing cols
            df = pd.concat([df, pd.DataFrame(columns=receiving + punting)], axis=1)

            # set all the new columns to zero
            df.loc[:, receiving + punting] = 0


        elif len(df.columns) == 30:
            # Rename columns
            cols = base + passing + rushing + scoring + punting
            df.columns = cols

            # add missing cols
            df = pd.concat([df, pd.DataFrame(columns=receiving + rush_sk)], axis=1)

            # set all the new columns to zero
            df.loc[:, receiving + rush_sk] = 0


        elif len(df.columns) == 31:

            # rename cols
            cols = base + passing + rushing + receiving
            df.columns = cols

            # add missing cols
            df = pd.concat([df, pd.DataFrame(columns=rush_sk + scoring + punting)], axis=1)

            # set all the new columns to zero
            df.loc[:, rush_sk + scoring + punting] = 0


        elif len(df.columns) == 33:

            # rename cols
            cols = base + passing + rushing + receiving + scoring
            df.columns = cols

            # add missing cols
            df = pd.concat([df, pd.DataFrame(columns=rush_sk + punting)], axis=1)

            # set all the new columns to zero
            df.loc[:, rush_sk + punting] = 0


        elif len(df.columns) == 36:

            # rename cols
            cols = base + passing + rushing + receiving + scoring + rush_sk
            df.columns = cols

            # add missing cols
            df = pd.concat([df, pd.DataFrame(columns=punting)], axis=1)

            # set all the new columns to zero
            df.loc[:, punting] = 0

        # send df to the common parser
        df = self.common(df, year)

        # Add the name
        df.loc[:, 'Name'] = gen['name']

        # Add the players position
        df.loc[:, 'Pos'] = gen['position']

        df = df[['Name', 'Pos', 'Date'] + base[1:] + passing + rushing + receiving + rush_sk + scoring + punting]

        return df