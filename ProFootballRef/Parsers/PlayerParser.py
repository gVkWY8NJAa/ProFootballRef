import re
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup, Comment
from ProFootballRef.Tools import Loader

class PlayerParser:
    def __init__(self):
        pass

    def parse_general_info(self, html):

        # initialize a dict to hold stats/metrics not contained in tabular form
        general_stats = {}

        # scrape data off the players page not contained in the stats table
        general_stats['name'] = re.compile('<h1 itemprop="name">(.*?)\s*<\/h1>').findall(html)[0]

        general_stats['position'] = re.compile('<strong>Position<\/strong>:\W([a-zA-Z]{1,})').findall(html)[0]

        try:
            general_stats['throws'] = re.compile('<strong>Throws:<\/strong>\\n\\t\\t(.*?)\\n\\t\\n<\/p>').findall(html)[0]
        except:
            general_stats['throws'] = np.nan

        # convert height to inches
        height = re.compile('<span itemprop="height">(.*?)<\/span>').findall(html)[0]
        general_stats['height'] = int(height.split('-')[0]) * 12 + int(height.split('-')[1])

        general_stats['weight'] = int(re.compile('<span itemprop="weight">([0-9]{1,3})lb<\/span>').findall(html)[0])

        # break up DOB into seperate cols for m/d/y
        bday = re.compile('<span itemprop="birthDate" id="necro-birth" data-birth="(.*?)">').findall(html)[0]
        general_stats['bday_mo'] = int(bday.split('-')[1])
        general_stats['bday_day'] = int(bday.split('-')[2])
        general_stats['bday_yr'] = int(bday.split('-')[0])

        try:
            general_stats['college'] = re.compile('<a href="\/schools\/\w+.*?\/">(.*?)<\/a>').findall(html)[0]
        except:
            general_stats['college'] = np.nan

        return general_stats

    def parse_receiver_stats(self, url=None, **kwargs):
        # We generally pass in a url and then load the page, for testing the function allow html to be passed in
        if url:
            response = Loader.Loader().load_page(url)
            html = response.content.decode()
        else:
            for k, v in kwargs.items():
                if k == 'html':
                    html = v

        #Scrape general stats
        general_stats = self.parse_general_info(html)

        # load the stats table into pandas dataframe. Using 'df' as the variable name to signify it's a pd.DataFrame.
        df = pd.read_html(html)[0]

        # rename columns from origional multirow colums
        cols = ['Year', 'Age', 'Tm', 'Pos', 'No', 'G', 'GS', 'Tgt', 'Rec', 'Rec_Yds', 'Y/R', 'Rec_TD', 'Rec_Lng', 'R/G',
                'Rec_Y/G', 'Ctch%', 'Rush', 'Rush_Yds', 'Rush_TD', 'Rush_Lng', 'Y/A', 'Rush_Y/G', 'A/G', 'YScm', 'RRTD',
                'Fmb', 'AV']
        df.columns = cols

        # remove the career totals row
        df = df[df.Year != 'Career']

        # remove spec characters that are sometimes added to the year to indicate probowl, all pro etc
        df['Year'] = df['Year'].str.replace('+', '')
        df['Year'] = df['Year'].str.replace('*', '')

        # some players have multiple rows w.o a year if they played on more than 1 team in that year
        df['Year'] = df['Year'].astype(str)
        df = df[df.Year != 'nan']
        df['Year'] = pd.to_numeric(df['Year'])

        # remove % sign on ctch% and convert to float
        df['Ctch%'] = df['Ctch%'].str.replace('%', '')
        df['Ctch%'] = pd.to_numeric(df['Ctch%'])

        # uppercase some qualitatives
        df['Pos'] = df['Pos'].str.upper()
        df['Tm'] = df['Tm'].str.upper()

        # Insert general scraped info from player page
        df['Name'] = general_stats['name']

        df['Throws'] = general_stats['throws']
        df['Height'] = general_stats['height']
        df['Weight'] = general_stats['weight']
        df['DOB_mo'] = general_stats['bday_mo']
        df['DOB_day'] = general_stats['bday_day']
        df['DOB_yr'] = general_stats['bday_yr']
        df['College'] = general_stats['college']

        # This is hacky but position info isn't always contained in every row
        if df['Pos'].isnull().values.any():
            df['Pos'] = general_stats['position']

        # rearange the dataframe columns, this is personal preference
        df = df[['Name', 'Year', 'Age', 'Throws', 'Height', 'Weight', 'DOB_mo', 'DOB_day', 'DOB_yr', 'College',
                 'Tm', 'Pos', 'No', 'G', 'GS', 'Tgt', 'Rec', 'Rec_Yds', 'Y/R', 'Rec_TD', 'Rec_Lng', 'R/G', 'Rec_Y/G', 'Ctch%', 'Rush',
             'Rush_Yds', 'Rush_TD', 'Rush_Lng', 'Y/A', 'Rush_Y/G', 'A/G', 'YScm', 'RRTD', 'Fmb', 'AV']]

        return df

    def parse_rushing_stats(self, url=None, **kwargs):
        # We generally pass in a url and then load the page, for testing the function allow html to be passed in
        if url:
            response = Loader.Loader().load_page(url)
            html = response.content.decode()
        else:
            for k, v in kwargs.items():
                if k == 'html':
                    html = v

        # Scrape general stats
        general_stats = self.parse_general_info(html)

        # load the stats table into pandas dataframe. Using 'df' as the variable name to signify it's a pd.DataFrame.
        df = pd.read_html(html)[0]

        # drop a nunch of unused columns
        df = df.iloc[:, 0:27]

        # rename columns from origional multirow colums
        cols = ['Year', 'Age', 'Tm', 'Pos', 'No', 'G', 'GS', 'Rush', 'Rush_Yds', 'Rush_TD', 'Rush_Lng', 'Y/A',
                'Rush_Y/G', 'A/G', 'Tgt', 'Rec', 'Rec_Yds', 'Y/R', 'Rec_TD', 'Rec_Lng', 'R/G', 'Rec_Y/G', 'Ctch%',
                'YScm', 'RRTD', 'Fmb', 'AV']
        df.columns = cols

        # remove the career totals row
        df = df[df.Year != 'Career']

        # remove spec characters that are sometimes added to the year to indicate probowl, all pro etc
        df['Year'] = df['Year'].str.replace('+', '')
        df['Year'] = df['Year'].str.replace('*', '')

        # some players have multiple rows w.o a year if they played on more than 1 team in that year
        df['Year'] = df['Year'].astype(str)
        df = df[df.Year != 'nan']
        df['Year'] = pd.to_numeric(df['Year'])

        # remove % sign on ctch% and convert to float
        df['Ctch%'] = df['Ctch%'].str.replace('%', '')
        df['Ctch%'] = pd.to_numeric(df['Ctch%'])

        # uppercase some qualitatives
        df['Pos'] = df['Pos'].str.upper()
        df['Tm'] = df['Tm'].str.upper()

        # Insert general scraped info from player page
        df['Name'] = general_stats['name']

        df['Throws'] = general_stats['throws']
        df['Height'] = general_stats['height']
        df['Weight'] = general_stats['weight']
        df['DOB_mo'] = general_stats['bday_mo']
        df['DOB_day'] = general_stats['bday_day']
        df['DOB_yr'] = general_stats['bday_yr']
        df['College'] = general_stats['college']

        # This is hacky but position info isn't always contained in every row
        if df['Pos'].isnull().values.any():
            df['Pos'] = general_stats['position']

        # rearange the dataframe columns, this is personal preference
        df = df[
            ['Name', 'Year', 'Age', 'Throws', 'Height', 'Weight', 'DOB_mo', 'DOB_day', 'DOB_yr', 'College', 'Tm', 'Pos',
             'No', 'G', 'GS', 'Tgt', 'Rec', 'Rec_Yds', 'Y/R', 'Rec_TD', 'Rec_Lng', 'R/G', 'Rec_Y/G', 'Ctch%', 'Rush',
             'Rush_Yds', 'Rush_TD', 'Rush_Lng', 'Y/A', 'Rush_Y/G', 'A/G', 'YScm', 'RRTD', 'Fmb', 'AV']]

        return df

    def parse_passing_stats(self, url=None, **kwargs):
        # We generally pass in a url and then load the page, for testing the function allow html to be passed in
        if url:
            response = Loader.Loader().load_page(url)
            html = response.content.decode()
        else:
            for k,v in kwargs.items():
                if k == 'html':
                    html = v

        # Scrape general stats
        general_stats = self.parse_general_info(html)

        # load the stats table into pandas dataframe. Using 'df' as the variable name to signify it's a pd.DataFrame.
        df = pd.read_html(html)[0]

        cols = ['Year', 'Age', 'Tm', 'Pos', 'No.', 'G', 'GS', 'QBrec', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int',
                'Int%', 'Lng', 'Pass_Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'QBR', 'Sk', 'Sk_Yds', 'NY/A', 'ANY/A', 'Sk%',
                '4QC', 'GWD', 'AV']
        df.columns = cols

        # remove the career totals row
        df = df[df.Year != 'Career']

        # remove spec characters that are sometimes added to the year to indicate probowl, all pro etc
        df['Year'] = df['Year'].str.replace('+', '')
        df['Year'] = df['Year'].str.replace('*', '')

        # some players have multiple rows w.o a year if they played on more than 1 team in that year
        df['Year'] = df['Year'].astype(str)
        df = df[df.Year != 'nan']
        df['Year'] = pd.to_numeric(df['Year'])

        # uppercase some qualitatives
        df['Pos'] = df['Pos'].str.upper()
        df['Tm'] = df['Tm'].str.upper()

        # Insert general scraped info from player page
        df['Name'] = general_stats['name']

        df['Throws'] = general_stats['throws']
        df['Height'] = general_stats['height']
        df['Weight'] = general_stats['weight']
        df['DOB_mo'] = general_stats['bday_mo']
        df['DOB_day'] = general_stats['bday_day']
        df['DOB_yr'] = general_stats['bday_yr']
        df['College'] = general_stats['college']

        # This is hacky but position info isn't always contained in every row
        if df['Pos'].isnull().values.any():
            df['Pos'] = general_stats['position']


        # rearange the dataframe columns, this is personal preference
        df = df[['Name', 'Year', 'Age', 'Throws', 'Height', 'Weight', 'DOB_mo', 'DOB_day', 'DOB_yr', 'College',
                 'Tm', 'Pos', 'No.', 'G', 'GS', 'QBrec', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%',
                 'Lng', 'Pass_Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'QBR', 'Sk', 'Sk_Yds', 'NY/A', 'ANY/A', 'Sk%', '4QC',
                 'GWD', 'AV']]

        # Parse out rushing and receiving information and append to the pssing info
        soup = BeautifulSoup(html, 'lxml')

        # parse out the chunk of rushing and receiving info from the html comments
        for comment in soup.findAll(text=lambda text: isinstance(text, Comment)):
            if 'id="div_rushing_and_receiving">' in comment:
                new_html = comment

        rush_df = pd.read_html(new_html)[0]

        # rename columns
        new_cols = ['Year', 'Age', 'Tm', 'Pos', 'No.', 'G', 'GS', 'Rush', 'Rush_Yds', 'Rush_TD', 'Rush_Lng', 'Rush_Y/A',
                    'Rush_Y/G', 'A/G', 'Tgt', 'Rec', 'Rec_Yds', 'Y/R', 'Rec_TD', 'Rec_Lng', 'R/G', 'Rec_Y/G', 'Ctch%',
                    'YScm', 'RRTD', 'Fmb']

        rush_df.columns = new_cols

        # munge the columns similar to above
        # remove the career totals row
        rush_df = rush_df[rush_df.Year != 'Career']

        # remove spec characters that are sometimes added to the year to indicate probowl, all pro etc
        rush_df['Year'] = rush_df['Year'].str.replace('+', '')
        rush_df['Year'] = rush_df['Year'].str.replace('*', '')

        # some players have multiple rows w.o a year if they played on more than 1 team in that year
        rush_df['Year'] = rush_df['Year'].astype(str)
        rush_df = rush_df[rush_df.Year != 'nan']
        rush_df['Year'] = pd.to_numeric(rush_df['Year'])

        # uppercase some qualitatives
        rush_df['Pos'] = rush_df['Pos'].str.upper()
        rush_df['Tm'] = rush_df['Tm'].str.upper()

        # merging on GS breaks for some reason so drop the col
        rush_df = rush_df.drop(['GS'], axis=1)

        # merge the two DataFrames on overlaping columns and return
        combined_df = pd.merge(df, rush_df, on=['Year', 'Age', 'No.', 'G', 'Pos', 'Tm'])

        return combined_df

    def parse_defense_stats(self, url=None, **kwargs):
        # We generally pass in a url and then load the page, for testing the function allow html to be passed in
        if url:
            response = Loader.Loader().load_page(url)
            html = response.content.decode()
        else:
            for k, v in kwargs.items():
                if k == 'html':
                    html = v

        # Scrape general stats
        general_stats = self.parse_general_info(html)

        # load the stats table into pandas dataframe. Using 'df' as the variable name to signify it's a pd.DataFrame.
        df = pd.read_html(html)[0]

        df = df.iloc[:, :22]

        cols = ['Year', 'Age', 'Tm', 'Pos', 'No.', 'G', 'GS', 'Int', 'Yds', 'TD', 'Lng', 'PD', 'FF', 'Fmb', 'FR',
                'Fmb_Yds','Fmb_TD', 'Sk', 'Tkl', 'Ast', 'Sfty', 'AV']

        df.columns = cols

        # remove the career totals row
        df = df[df.Year != 'Career']

        # remove spec characters that are sometimes added to the year to indicate probowl, all pro etc
        df['Year'] = df['Year'].str.replace('+', '')
        df['Year'] = df['Year'].str.replace('*', '')

        # some players have multiple rows w.o a year if they played on more than 1 team in that year
        df['Year'] = df['Year'].astype(str)
        df = df[df.Year != 'nan']
        df['Year'] = pd.to_numeric(df['Year'])

        # uppercase some qualitatives
        df['Pos'] = df['Pos'].str.upper()
        df['Tm'] = df['Tm'].str.upper()

        # Insert general scraped info from player page
        df['Name'] = general_stats['name']

        df['Throws'] = general_stats['throws']
        df['Height'] = general_stats['height']
        df['Weight'] = general_stats['weight']
        df['DOB_mo'] = general_stats['bday_mo']
        df['DOB_day'] = general_stats['bday_day']
        df['DOB_yr'] = general_stats['bday_yr']
        df['College'] = general_stats['college']

        # This is hacky but position info isn't always contained in every row
        if df['Pos'].isnull().values.any():
            df['Pos'] = general_stats['position']

        df = df[['Name', 'Year', 'Age', 'Throws', 'Height', 'Weight', 'DOB_mo', 'DOB_day', 'DOB_yr', 'College', 'Tm',
                 'Pos', 'No.', 'G', 'GS', 'Int', 'Yds', 'TD', 'Lng', 'PD', 'FF', 'Fmb', 'FR', 'Fmb_Yds', 'Fmb_TD',
                 'Sk', 'Tkl', 'Ast', 'Sfty', 'AV']]

        return df

    def parse_kicking_stats(self, url=None, **kwargs):
        # We generally pass in a url and then load the page, for testing the function allow html to be passed in
        if url:
            response = Loader.Loader().load_page(url)
            html = response.content.decode()
        else:
            for k, v in kwargs.items():
                if k == 'html':
                    html = v

        # Scrape general stats
        general_stats = self.parse_general_info(html)

        # load the stats table into pandas dataframe. Using 'df' as the variable name to signify it's a pd.DataFrame.
        df = pd.read_html(html)[0]

        # sometimes there's unneeded cols
        df = df.iloc[:, :30]

        # rename columns from origional multirow colums
        cols = ['Year', 'Age', 'Tm', 'Pos', 'No.', 'G', 'GS', '0-19FGA', '0-19FGM', '20-29FGA', '20-29FGM', '30-39FGA',
                '30-39FGM', '40-49FGA', '40-49FGM', '50+FGA', '50+FGM', 'scr_FGA', 'scr_FGM', 'Lng', 'scr_FG%',
                'scr_XPA', 'scr_XPM', 'scr_XP%', 'Pnt', 'Yds', 'Lng', 'Blck', 'Y/P', 'AV']

        df.columns = cols

        # remove the career totals row
        df = df[df.Year != 'Career']

        # remove spec characters that are sometimes added to the year to indicate probowl, all pro etc
        df['Year'] = df['Year'].str.replace('+', '')
        df['Year'] = df['Year'].str.replace('*', '')

        # some players have multiple rows w.o a year if they played on more than 1 team in that year
        df['Year'] = df['Year'].astype(str)
        df = df[df.Year != 'nan']
        df['Year'] = pd.to_numeric(df['Year'])

        # uppercase some qualitatives
        df['Pos'] = df['Pos'].str.upper()
        df['Tm'] = df['Tm'].str.upper()

        # Insert general scraped info from player page
        df['Name'] = general_stats['name']

        df['Throws'] = general_stats['throws']
        df['Height'] = general_stats['height']
        df['Weight'] = general_stats['weight']
        df['DOB_mo'] = general_stats['bday_mo']
        df['DOB_day'] = general_stats['bday_day']
        df['DOB_yr'] = general_stats['bday_yr']
        df['College'] = general_stats['college']

        # This is hacky but position info isn't always contained in every row
        if df['Pos'].isnull().values.any():
            df['Pos'] = general_stats['position']

        df = df[['Name', 'Year', 'Age', 'Throws', 'Height', 'Weight', 'DOB_mo', 'DOB_day', 'DOB_yr', 'College', 'Tm',
                 'Pos', 'No.', 'G', 'GS', '0-19FGA', '0-19FGM', '20-29FGA', '20-29FGM', '30-39FGA', '30-39FGM',
                 '40-49FGA', '40-49FGM', '50+FGA', '50+FGM', 'scr_FGA', 'scr_FGM', 'Lng', 'scr_FG%', 'scr_XPA',
                 'scr_XPM', 'scr_XP%', 'Pnt', 'Yds', 'Lng', 'Blck', 'Y/P', 'AV']]

        return df
