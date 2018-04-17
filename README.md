[![Build Status](https://travis-ci.org/gVkWY8NJAa/ProFootballRef.svg?branch=master)](https://travis-ci.org/gVkWY8NJAa/ProFootballRef)
# ProFootballRef

This is a python toolkit that lets you scrape statistics from https://www.pro-football-reference.com/, and return the resulting data as a Pandas DataFrame. The toolkit is highly modular such that you are free to use various components as you see fit.

Please consider contributing the $20/yr to support the site, they do a great job: https://www.pro-football-reference.com/my/?do=ad_free_browsing

## Key Features
* Aggregate player data for each season.
* Ability to combine qualitative (height/weight) with quantitative (TDs).
* Multi column headers have been simplified and closely match the canonical source.
* Scrape team stats for a given season.
* Returned objects are Pandas DataFrames for ease of analysis.

## Installation
```
git clone git@github.com:gVkWY8NJAa/ProFootballRef.git
cd ProFootballRef
pip install -r requirements.txt
```
## Testing
```
cd <path/to/ProFootballRef>
python3.6 -m pytest tests/
```
## Usage

### Quick Example


```python
# Individual player statistics for passing
from ProFootballRef.LinkBuilder import GetPositionLinks 
from ProFootballRef.Parsers import PlayerParser

links = GetPositionLinks.GetPositionLinks('passing').parse_links(2017)
html = PlayerParser.PlayerParser().load_page(links[:1][0])
general_stats = PlayerParser.PlayerParser().parse_general_info(html)

passing_df = PlayerParser.PlayerParser().parse_passing_stats(general_stats, html)
```


```python
passing_df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Year</th>
      <th>Age</th>
      <th>Throws</th>
      <th>Height</th>
      <th>Weight</th>
      <th>DOB_mo</th>
      <th>DOB_day</th>
      <th>DOB_yr</th>
      <th>College</th>
      <th>...</th>
      <th>Rec_Yds</th>
      <th>Y/R</th>
      <th>Rec_TD</th>
      <th>Rec_Lng</th>
      <th>R/G</th>
      <th>Rec_Y/G</th>
      <th>Ctch%</th>
      <th>YScm</th>
      <th>RRTD</th>
      <th>Fmb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom Brady</td>
      <td>2001</td>
      <td>24.0</td>
      <td>Right</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>...</td>
      <td>23.0</td>
      <td>23.0</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>0.1</td>
      <td>1.5</td>
      <td>100.0%</td>
      <td>66</td>
      <td>0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tom Brady</td>
      <td>2002</td>
      <td>25.0</td>
      <td>Right</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>110</td>
      <td>1</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tom Brady</td>
      <td>2003</td>
      <td>26.0</td>
      <td>Right</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>63</td>
      <td>1</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tom Brady</td>
      <td>2004</td>
      <td>27.0</td>
      <td>Right</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28</td>
      <td>0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tom Brady</td>
      <td>2005</td>
      <td>28.0</td>
      <td>Right</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>89</td>
      <td>1</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 58 columns</p>
</div>



### Detailed Usage

Individual player metrics are gathered using a five step process to allow you granular control as to how much data you want to obtain. The modularity also aids in refactoring if/when the website code is ever updated:
1. Generate links to scrape.
2. Request, and return, html for each link.
3. Parse general info such as height and weight from the returned html.
4. Parse performance metrics specific to the position.
5. Combine the general heigh/weight with the performance metrics.


```python
from ProFootballRef.LinkBuilder import GetPositionLinks 
from ProFootballRef.Parsers import PlayerParser
```

First we need to generate pages to scrape based on position. This is a two step process.
1. Pass a position to the **GetPositionLinks()** class: passing, receiving, rushing, kicking, or defense. This tells the class which url it needs to request.
2. Pass a season (year) to the **parse_links()** function to get the players of the corresponding position who played during the season.


```python
position = 'passing'
season = 2017
links = GetPositionLinks.GetPositionLinks(position).parse_links(season)
```

As you can see below, a list of urls is returned for each player of the position, and season, that was requested.


```python
links[:5]
```




    ['https://www.pro-football-reference.com/players/B/BradTo00.htm',
     'https://www.pro-football-reference.com/players/R/RivePh00.htm',
     'https://www.pro-football-reference.com/players/M/MannEl00.htm',
     'https://www.pro-football-reference.com/players/S/StafMa00.htm',
     'https://www.pro-football-reference.com/players/R/RoetBe00.htm']



Next, We call the **PlayerParser** class method, **load_page()**, to return an html object for parsing. For this example we will only parse one link from the list above.


```python
links[:1][0]
```




    'https://www.pro-football-reference.com/players/B/BradTo00.htm'




```python
html = PlayerParser.PlayerParser().load_page(links[:1][0])
```

Each player has qualitative information such as height, weight, date of birth etc. so we will grab that by passing our html object to the **parse_general_info()** method which will return a dict of the info:


```python
general_stats = PlayerParser.PlayerParser().parse_general_info(html)
```


```python
general_stats
```




    {'bday_day': 3,
     'bday_mo': 8,
     'bday_yr': 1977,
     'college': 'Michigan',
     'height': 76,
     'name': 'Tom Brady',
     'throws': 'Right',
     'weight': 225}



Then, we will call the parser specific to the position, and pass to it the general_stats dict in the last step, as well as our html object from before. 

You can choose from:

**parse_receiver_stats()**

**parse_rushing_stats()**

**parse_passisng_stats()**

**parse_defense_stats()**

**parse_kicking_stats()**

Each of these parsers will return a Pandas DataFrame object.


```python
df = PlayerParser.PlayerParser().parse_passing_stats(general_stats, html)
```


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Year</th>
      <th>Age</th>
      <th>Throws</th>
      <th>Height</th>
      <th>Weight</th>
      <th>DOB_mo</th>
      <th>DOB_day</th>
      <th>DOB_yr</th>
      <th>College</th>
      <th>...</th>
      <th>Rec_Yds</th>
      <th>Y/R</th>
      <th>Rec_TD</th>
      <th>Rec_Lng</th>
      <th>R/G</th>
      <th>Rec_Y/G</th>
      <th>Ctch%</th>
      <th>YScm</th>
      <th>RRTD</th>
      <th>Fmb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom Brady</td>
      <td>2001</td>
      <td>24.0</td>
      <td>Right</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>...</td>
      <td>23.0</td>
      <td>23.0</td>
      <td>0.0</td>
      <td>23.0</td>
      <td>0.1</td>
      <td>1.5</td>
      <td>100.0%</td>
      <td>66</td>
      <td>0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tom Brady</td>
      <td>2002</td>
      <td>25.0</td>
      <td>Right</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>110</td>
      <td>1</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tom Brady</td>
      <td>2003</td>
      <td>26.0</td>
      <td>Right</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>63</td>
      <td>1</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tom Brady</td>
      <td>2004</td>
      <td>27.0</td>
      <td>Right</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28</td>
      <td>0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tom Brady</td>
      <td>2005</td>
      <td>28.0</td>
      <td>Right</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>89</td>
      <td>1</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 58 columns</p>
</div>



### Scrape multiple players pages for a given season
**This will generate a ton of traffic to the website so use caution.**


```python
import pandas as pd
from ProFootballRef.LinkBuilder import GetPositionLinks 
from ProFootballRef.Parsers import PlayerParser

# Initialize an empty DataFrame to store all the players
all_qb = pd.DataFrame()

# Specify which position and season we want
position = 'passing'
season = 2017

# Generate a list of urls for the players in that season
links = GetPositionLinks.GetPositionLinks(position).parse_links(season)

# We will scrape the first 5 players in the list of links
for player in links[:5]:
    
    # load the page and return the html
    html = PlayerParser.PlayerParser().load_page(player)
    
    # scrape height and weight info
    general_stats = PlayerParser.PlayerParser().parse_general_info(html)
    
    # pass that to the position parser
    stats = PlayerParser.PlayerParser().parse_passing_stats(general_stats, html)
    
    # concat the results with our catch all dataframe
    all_qb = pd.concat([all_qb, stats], axis=0)   
```


```python
all_qb.groupby(['Name']).sum()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Age</th>
      <th>Height</th>
      <th>Weight</th>
      <th>DOB_mo</th>
      <th>DOB_day</th>
      <th>DOB_yr</th>
      <th>No.</th>
      <th>G</th>
      <th>Cmp</th>
      <th>...</th>
      <th>Rec</th>
      <th>Rec_Yds</th>
      <th>Y/R</th>
      <th>Rec_TD</th>
      <th>Rec_Lng</th>
      <th>R/G</th>
      <th>Rec_Y/G</th>
      <th>YScm</th>
      <th>RRTD</th>
      <th>Fmb</th>
    </tr>
    <tr>
      <th>Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Ben Roethlisberger</th>
      <td>28147</td>
      <td>399.0</td>
      <td>1078</td>
      <td>3360</td>
      <td>42</td>
      <td>28</td>
      <td>27748</td>
      <td>98</td>
      <td>200</td>
      <td>4164</td>
      <td>...</td>
      <td>1.0</td>
      <td>-11.0</td>
      <td>-7.0</td>
      <td>0.0</td>
      <td>-8.0</td>
      <td>0.1</td>
      <td>-0.8</td>
      <td>1241</td>
      <td>16</td>
      <td>91.0</td>
    </tr>
    <tr>
      <th>Eli Manning</th>
      <td>28147</td>
      <td>413.0</td>
      <td>1064</td>
      <td>3052</td>
      <td>14</td>
      <td>42</td>
      <td>27734</td>
      <td>140</td>
      <td>216</td>
      <td>4424</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>540</td>
      <td>6</td>
      <td>115.0</td>
    </tr>
    <tr>
      <th>Matthew Stafford</th>
      <td>18117</td>
      <td>225.0</td>
      <td>666</td>
      <td>2070</td>
      <td>18</td>
      <td>63</td>
      <td>17892</td>
      <td>81</td>
      <td>125</td>
      <td>3005</td>
      <td>...</td>
      <td>2.0</td>
      <td>-3.0</td>
      <td>-3.0</td>
      <td>0.0</td>
      <td>-3.0</td>
      <td>0.2</td>
      <td>-0.2</td>
      <td>946</td>
      <td>14</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>Philip Rivers</th>
      <td>28147</td>
      <td>413.0</td>
      <td>1078</td>
      <td>3192</td>
      <td>168</td>
      <td>112</td>
      <td>27734</td>
      <td>238</td>
      <td>196</td>
      <td>4171</td>
      <td>...</td>
      <td>0.0</td>
      <td>-9.0</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>-9.0</td>
      <td>0.0</td>
      <td>-0.6</td>
      <td>564</td>
      <td>3</td>
      <td>99.0</td>
    </tr>
    <tr>
      <th>Tom Brady</th>
      <td>32145</td>
      <td>513.0</td>
      <td>1216</td>
      <td>3600</td>
      <td>128</td>
      <td>48</td>
      <td>31632</td>
      <td>192</td>
      <td>251</td>
      <td>5621</td>
      <td>...</td>
      <td>2.0</td>
      <td>59.0</td>
      <td>59.0</td>
      <td>0.0</td>
      <td>59.0</td>
      <td>0.2</td>
      <td>3.8</td>
      <td>1027</td>
      <td>17</td>
      <td>114.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 50 columns</p>
</div>



### Scrape multiple players pages from multiple seasons
If you need to get players from multiple seasons, it is easiest to make a pruned list of players to avoid overlap. Then just literate through the list like above.


```python
big_list = []
for year in range(2015,2017):
    big_list = big_list + GetPositionLinks.GetPositionLinks('passing').parse_links(year)
```


```python
# this will contain duplicate urls
len(big_list)
```




    182




```python
# remove the duplicate urls
pruned_list = list(dict.fromkeys(big_list))
```


```python
len(pruned_list)
```




    129



You would then simply iterate through this list and call:
```python
load_page(url)
parse_general_info(html)
parse_passing_stats(general_stats, html)
``` 
The result would be a DataFrame of 129 different passing players. 

**Again, this will generate a ton of traffic to the website so use caution.**

## Team metrics

### Team offense stats
Simply pass a season (year) to the **offense()** method in the **TeamStats()** class


```python
from ProFootballRef.Parsers import TeamStats

year = 2015
df = TeamStats.TeamStats().offense(year)
```


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Tm</th>
      <th>G</th>
      <th>PF</th>
      <th>Yds</th>
      <th>Ply</th>
      <th>Y/P</th>
      <th>TO</th>
      <th>FL</th>
      <th>1stD</th>
      <th>Pass_Cmp</th>
      <th>...</th>
      <th>Rush_Yds</th>
      <th>Rush_TD</th>
      <th>Y/A</th>
      <th>Rush_1stD</th>
      <th>Pen</th>
      <th>Pen_Yds</th>
      <th>1stPy</th>
      <th>Sc%</th>
      <th>TO%</th>
      <th>EXP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Carolina Panthers</td>
      <td>16.0</td>
      <td>500.0</td>
      <td>5871.0</td>
      <td>1060.0</td>
      <td>5.5</td>
      <td>19.0</td>
      <td>9.0</td>
      <td>357.0</td>
      <td>300.0</td>
      <td>...</td>
      <td>2282.0</td>
      <td>19.0</td>
      <td>4.3</td>
      <td>136.0</td>
      <td>103.0</td>
      <td>887.0</td>
      <td>24.0</td>
      <td>42.9</td>
      <td>9.6</td>
      <td>125.65</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Arizona Cardinals</td>
      <td>16.0</td>
      <td>489.0</td>
      <td>6533.0</td>
      <td>1041.0</td>
      <td>6.3</td>
      <td>24.0</td>
      <td>11.0</td>
      <td>373.0</td>
      <td>353.0</td>
      <td>...</td>
      <td>1917.0</td>
      <td>16.0</td>
      <td>4.2</td>
      <td>92.0</td>
      <td>94.0</td>
      <td>758.0</td>
      <td>44.0</td>
      <td>42.5</td>
      <td>11.8</td>
      <td>161.96</td>
    </tr>
    <tr>
      <th>2</th>
      <td>New England Patriots</td>
      <td>16.0</td>
      <td>465.0</td>
      <td>5991.0</td>
      <td>1050.0</td>
      <td>5.7</td>
      <td>14.0</td>
      <td>7.0</td>
      <td>348.0</td>
      <td>404.0</td>
      <td>...</td>
      <td>1404.0</td>
      <td>14.0</td>
      <td>3.7</td>
      <td>87.0</td>
      <td>96.0</td>
      <td>860.0</td>
      <td>31.0</td>
      <td>43.2</td>
      <td>5.7</td>
      <td>127.68</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pittsburgh Steelers</td>
      <td>16.0</td>
      <td>423.0</td>
      <td>6327.0</td>
      <td>1011.0</td>
      <td>6.3</td>
      <td>28.0</td>
      <td>7.0</td>
      <td>331.0</td>
      <td>391.0</td>
      <td>...</td>
      <td>1724.0</td>
      <td>16.0</td>
      <td>4.4</td>
      <td>91.0</td>
      <td>94.0</td>
      <td>868.0</td>
      <td>33.0</td>
      <td>40.5</td>
      <td>13.7</td>
      <td>116.15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Seattle Seahawks</td>
      <td>16.0</td>
      <td>423.0</td>
      <td>6058.0</td>
      <td>1035.0</td>
      <td>5.9</td>
      <td>16.0</td>
      <td>8.0</td>
      <td>335.0</td>
      <td>333.0</td>
      <td>...</td>
      <td>2268.0</td>
      <td>10.0</td>
      <td>4.5</td>
      <td>128.0</td>
      <td>117.0</td>
      <td>1007.0</td>
      <td>17.0</td>
      <td>42.0</td>
      <td>8.6</td>
      <td>132.31</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 27 columns</p>
</div>



### Team defense stats
Simply pass a season (year) to the **defense()** method in the **TeamStats()** class


```python
from ProFootballRef.Parsers import TeamStats

year = 2015
df = TeamStats.TeamStats().defense(year)
```


```python
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Tm</th>
      <th>G</th>
      <th>PF</th>
      <th>Yds</th>
      <th>Ply</th>
      <th>Y/P</th>
      <th>TO</th>
      <th>FL</th>
      <th>1stD</th>
      <th>Pass_Cmp</th>
      <th>...</th>
      <th>Rush_Yds</th>
      <th>Rush_TD</th>
      <th>Y/A</th>
      <th>Rush_1stD</th>
      <th>Pen</th>
      <th>Pen_Yds</th>
      <th>1stPy</th>
      <th>Sc%</th>
      <th>TO%</th>
      <th>EXP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Seattle Seahawks</td>
      <td>16.0</td>
      <td>277.0</td>
      <td>4668.0</td>
      <td>947.0</td>
      <td>4.9</td>
      <td>23.0</td>
      <td>9.0</td>
      <td>273.0</td>
      <td>333.0</td>
      <td>...</td>
      <td>1304.0</td>
      <td>10.0</td>
      <td>3.6</td>
      <td>71.0</td>
      <td>94.0</td>
      <td>795.0</td>
      <td>27.0</td>
      <td>29.3</td>
      <td>13.2</td>
      <td>50.54</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cincinnati Bengals</td>
      <td>16.0</td>
      <td>279.0</td>
      <td>5453.0</td>
      <td>1032.0</td>
      <td>5.3</td>
      <td>28.0</td>
      <td>7.0</td>
      <td>307.0</td>
      <td>415.0</td>
      <td>...</td>
      <td>1477.0</td>
      <td>8.0</td>
      <td>4.3</td>
      <td>74.0</td>
      <td>116.0</td>
      <td>1063.0</td>
      <td>31.0</td>
      <td>28.9</td>
      <td>15.0</td>
      <td>24.23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kansas City Chiefs</td>
      <td>16.0</td>
      <td>287.0</td>
      <td>5269.0</td>
      <td>1037.0</td>
      <td>5.1</td>
      <td>29.0</td>
      <td>7.0</td>
      <td>313.0</td>
      <td>349.0</td>
      <td>...</td>
      <td>1571.0</td>
      <td>7.0</td>
      <td>4.1</td>
      <td>86.0</td>
      <td>110.0</td>
      <td>941.0</td>
      <td>34.0</td>
      <td>27.3</td>
      <td>15.3</td>
      <td>69.97</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Denver Broncos</td>
      <td>16.0</td>
      <td>296.0</td>
      <td>4530.0</td>
      <td>1033.0</td>
      <td>4.4</td>
      <td>27.0</td>
      <td>13.0</td>
      <td>289.0</td>
      <td>344.0</td>
      <td>...</td>
      <td>1337.0</td>
      <td>10.0</td>
      <td>3.3</td>
      <td>81.0</td>
      <td>104.0</td>
      <td>773.0</td>
      <td>46.0</td>
      <td>26.9</td>
      <td>11.9</td>
      <td>146.71</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Minnesota Vikings</td>
      <td>16.0</td>
      <td>302.0</td>
      <td>5510.0</td>
      <td>1015.0</td>
      <td>5.4</td>
      <td>22.0</td>
      <td>9.0</td>
      <td>318.0</td>
      <td>359.0</td>
      <td>...</td>
      <td>1748.0</td>
      <td>7.0</td>
      <td>4.3</td>
      <td>94.0</td>
      <td>109.0</td>
      <td>875.0</td>
      <td>35.0</td>
      <td>33.3</td>
      <td>11.9</td>
      <td>3.87</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 27 columns</p>
</div>


