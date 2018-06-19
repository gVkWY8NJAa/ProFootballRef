

[![Build Status](https://travis-ci.org/gVkWY8NJAa/ProFootballRef.svg?branch=master)](https://travis-ci.org/gVkWY8NJAa/ProFootballRef) [![Coverage Status](https://coveralls.io/repos/github/gVkWY8NJAa/ProFootballRef/badge.svg?branch=master)](https://coveralls.io/github/gVkWY8NJAa/ProFootballRef?branch=master)
# ProFootballRef </hr>

This is a python toolkit that lets you scrape statistics from https://www.pro-football-reference.com/, and return the resulting data as a Pandas DataFrame.

Please consider contributing the $20/yr to support the site, they do a great job: https://www.pro-football-reference.com/my/?do=ad_free_browsing

## Contents
* [Installation](#installation)
* [Testing](#testing)
* [Find players](#find_players)
* [Player stats](#player_stats)
    * [Individual player stats](#career_player_stats)
    * [Multiple player stats](#multi_player_stats)
    * [Gamelog](#gamelog)
* [Team stats](#team_stats)
    * [Team offense stats](#team_offense)
    * [Team defense stats](#team_defense)

## Key Features
* Aggregate player data for each season.
* Ability to combine qualitative (height/weight) with quantitative (TDs).
* Multi column headers have been simplified and closly match the canonical source.
* Scrape team stats for a given season.
* Player gamelog data available for a given season.
* Returned objects are Pandas DataFrames for ease of analysis.

<a id='installation'></a>
## Installation
```
git clone git@github.com:gVkWY8NJAa/ProFootballRef.git
cd ProFootballRef
pip install -r requirements.txt
```
<a id='testing'></a>
## Testing
```
cd <path/to/ProFootballRef>
python3.6 -m pytest tests/
```
<a id='find_players'></a>
## Find Players
---
Before we do anything, we need to gather a list of urls for various players to parse.

This is easily done by importing the **GetPositionLinks** module that resides in the 'LinkBuilder' directory:


```python
from profootballref.LinkBuilder import GetPositionLinks
```

The **GetPositionLinks** module contains a class called **Position**.

To generate urls to parse, we'll call the **player_links** method from the **Position** class, and save the output to a list.
The **Position** class takes one of five possible arguments:
* passing
* receiving
* rushing
* kicking
* defense

The **player_links** method takes either a season, or a range of seasons, as integers:


```python
urls = GetPositionLinks.Position('passing').player_links(2017)
```

or to grab all players from a range of seaons do:


```python
urls = GetPositionLinks.Position('passing').player_links(2015, 2017)
```

If a range of seasons is passed to **player_links**, any duplicate urls will be removed automatically.

We'll look at the first five urls in the list:


```python
print(urls[:5])
```

    ['https://www.pro-football-reference.com/players/R/RivePh00.htm', 'https://www.pro-football-reference.com/players/B/BreeDr00.htm', 'https://www.pro-football-reference.com/players/B/BradTo00.htm', 'https://www.pro-football-reference.com/players/M/MannEl00.htm', 'https://www.pro-football-reference.com/players/R/RyanMa00.htm']


<a id='player_stats'></a>
## Player stats
---
The following code demonstrates how to return career position statistics given a player. This is the data that would be found on the [players page](https://www.pro-football-reference.com/players/B/BradTo00.htm).
<a id='career_player_stats'></a>
### Individual player stats
In this example, we will [pass a url as a string for a given player](#find_players) that we created previously to return their career stats for their position. If you do not yet have a list of urls for a given position, see the above section [Find Players](#find_players).

This is easily done by importing the **PlayerParser** module that resides in the 'Parsers' directory:


```python
from profootballref.Parsers import PlayerParser
```

The **PlayerParser** module contains a class also called **PlayerParser**.

To scrape a player(s) career stats, we'll call one of five methods from the **PlayerParser** class, and save the output to a variable.

The available methods from the **PlayerParser** class are:
* passing
* receiving
* rushing
* kicking
* defense

Remember we're using the 'urls' data from what we did in the [Find Players](#find_players) section above.


```python
passing_df = PlayerParser.PlayerParser().passing(urls[:1][0])
```

    https://www.pro-football-reference.com/players/R/RivePh00.htm



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
      <td>Philip Rivers</td>
      <td>2004</td>
      <td>23.0</td>
      <td>Right</td>
      <td>77</td>
      <td>228</td>
      <td>12</td>
      <td>8</td>
      <td>1981</td>
      <td>North Carolina St.</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-5</td>
      <td>0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Philip Rivers</td>
      <td>2005</td>
      <td>24.0</td>
      <td>Right</td>
      <td>77</td>
      <td>228</td>
      <td>12</td>
      <td>8</td>
      <td>1981</td>
      <td>North Carolina St.</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>-1</td>
      <td>0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Philip Rivers</td>
      <td>2006</td>
      <td>25.0</td>
      <td>Right</td>
      <td>77</td>
      <td>228</td>
      <td>12</td>
      <td>8</td>
      <td>1981</td>
      <td>North Carolina St.</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>49</td>
      <td>0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Philip Rivers</td>
      <td>2007</td>
      <td>26.0</td>
      <td>Right</td>
      <td>77</td>
      <td>228</td>
      <td>12</td>
      <td>8</td>
      <td>1981</td>
      <td>North Carolina St.</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>33</td>
      <td>1</td>
      <td>11.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Philip Rivers</td>
      <td>2008</td>
      <td>27.0</td>
      <td>Right</td>
      <td>77</td>
      <td>228</td>
      <td>12</td>
      <td>8</td>
      <td>1981</td>
      <td>North Carolina St.</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>84</td>
      <td>0</td>
      <td>8.0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 58 columns</p>
</div>



<a id='multi_player_stats'></a>
### Multiple player stats
**This can generate a ton of traffic to the website so use caution with how many players you retrieve at one time.**


```python
import pandas as pd
from profootballref.LinkBuilder import GetPositionLinks
from profootballref.Parsers import PlayerParser
import random

# Initialize an empty DataFrame to store all the players
all_qb = pd.DataFrame()

# Specify which position and season we want
position = 'passing'

# In this example we'll generate a list of urls multiple seasons
links = GetPositionLinks.Position(position).player_links(2013,2015)

all_qb = pd.DataFrame()
# We will scrape the 10 players at random in the list of links
for player in random.sample(links, 10):
    # pass the url to the position parser
    stats = PlayerParser.PlayerParser().passing(player)

    # concat the results with our catch-all dataframe
    all_qb = pd.concat([all_qb, stats], axis=0)
```

    https://www.pro-football-reference.com/players/P/PondCh00.htm
    https://www.pro-football-reference.com/players/T/TannRy00.htm
    https://www.pro-football-reference.com/players/P/PetePa00.htm  is not a quarterback we can parse so we're skipping this player
    https://www.pro-football-reference.com/players/K/KeenCa00.htm
    https://www.pro-football-reference.com/players/L/LechSh20.htm  is not a quarterback we can parse so we're skipping this player
    https://www.pro-football-reference.com/players/G/GlenMi00.htm
    https://www.pro-football-reference.com/players/S/SandAc00.htm  is not a quarterback we can parse so we're skipping this player
    https://www.pro-football-reference.com/players/F/FlynMa00.htm
    https://www.pro-football-reference.com/players/F/FostAr00.htm  is not a quarterback we can parse so we're skipping this player
    https://www.pro-football-reference.com/players/A/AndeDe00.htm


Notice that in the above example, some links output "*url* is not a quarterback we can parse so we're skipping this player". This is due to players other than quarterbacks who have made passes, such as kickers, RBs etc. To avoid this, we ignore the player completely and do not try to parse the page as if it were a quarterback.

This is intended behavior of all position methods in the **PlayerParser** class.

In addition, RB's and WR's have the same net DataFrame structure. This means that if a WR url gets passed to the **rushing** method instead of **receiving**, the **rushing** method will call the correct position method for the player. This works for all WR, TE, FB, RB positions as they are interchangeable.  


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
      <th>Cmp</th>
      <th>Att</th>
      <th>...</th>
      <th>Tgt</th>
      <th>Rec</th>
      <th>Rec_Yds</th>
      <th>Y/R</th>
      <th>Rec_TD</th>
      <th>Rec_Lng</th>
      <th>R/G</th>
      <th>Rec_Y/G</th>
      <th>YScm</th>
      <th>RRTD</th>
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
      <th>Case Keenum</th>
      <td>10075</td>
      <td>135.0</td>
      <td>365</td>
      <td>1075</td>
      <td>10</td>
      <td>85</td>
      <td>9940</td>
      <td>48.0</td>
      <td>779</td>
      <td>1258.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>323</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Christian Ponder</th>
      <td>6036</td>
      <td>72.0</td>
      <td>222</td>
      <td>666</td>
      <td>6</td>
      <td>75</td>
      <td>5964</td>
      <td>21.0</td>
      <td>610</td>
      <td>1013.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>-15.0</td>
      <td>-15.0</td>
      <td>0.0</td>
      <td>-15.0</td>
      <td>0.1</td>
      <td>-0.9</td>
      <td>608</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Derek Anderson</th>
      <td>22126</td>
      <td>313.0</td>
      <td>858</td>
      <td>2519</td>
      <td>66</td>
      <td>165</td>
      <td>21813</td>
      <td>33.0</td>
      <td>863</td>
      <td>1600.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>227</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Matt Flynn</th>
      <td>14077</td>
      <td>182.0</td>
      <td>518</td>
      <td>1596</td>
      <td>42</td>
      <td>140</td>
      <td>13895</td>
      <td>65.0</td>
      <td>219</td>
      <td>357.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>69</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Mike Glennon</th>
      <td>2013</td>
      <td>24.0</td>
      <td>78</td>
      <td>229</td>
      <td>12</td>
      <td>12</td>
      <td>1989</td>
      <td>8.0</td>
      <td>247</td>
      <td>416.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>37</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Ryan Tannehill</th>
      <td>10070</td>
      <td>130.0</td>
      <td>380</td>
      <td>1080</td>
      <td>35</td>
      <td>135</td>
      <td>9940</td>
      <td>85.0</td>
      <td>1653</td>
      <td>2637.0</td>
      <td>...</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>0.2</td>
      <td>0.3</td>
      <td>1070</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
<p>6 rows × 47 columns</p>
</div>



<a id='gamelog'></a>
### Gamelog
Individual player gamelog stats can be obtained for a player(s) for a given season(s). Descriptive information about the player such as their alma mater, height, weight, etc is also attached to the results.


```python
from profootballref.LinkBuilder import GetPositionLinks
from profootballref.Parsers import GamelogParser

# gather player urls for a given season
position = 'passing'
season = 2017

urls = GetPositionLinks.Position(position).player_links(season)

# view the first url as a string
urls[:1][0]
```




    'https://www.pro-football-reference.com/players/B/BradTo00.htm'




```python
# pass the url and the season to the passing method in the GameLog class.
GamelogParser.GameLog().passing(urls[:1][0], season)
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Pos</th>
      <th>Height</th>
      <th>Weight</th>
      <th>DOB_mo</th>
      <th>DOB_day</th>
      <th>DOB_yr</th>
      <th>College</th>
      <th>Date</th>
      <th>G#</th>
      <th>Age</th>
      <th>Tm</th>
      <th>Home</th>
      <th>Opp</th>
      <th>Result</th>
      <th>GS</th>
      <th>GS</th>
      <th>PF</th>
      <th>PA</th>
      <th>pass_cmp</th>
      <th>pass_att</th>
      <th>Cmp%</th>
      <th>pass_yds</th>
      <th>pass_td</th>
      <th>Int</th>
      <th>Rate</th>
      <th>Sk</th>
      <th>Sk-Yds</th>
      <th>pass_Y/A</th>
      <th>AY/A</th>
      <th>rush_att</th>
      <th>rush_yds</th>
      <th>rush_Y/A</th>
      <th>rush_TD</th>
      <th>Rec_Tgt</th>
      <th>Rec_Rec</th>
      <th>Rec_Yds</th>
      <th>Rec_Y/R</th>
      <th>Rec_TD</th>
      <th>Rec_Ctch%</th>
      <th>Rec_Y/Tgt</th>
      <th>rush_sk</th>
      <th>tkl</th>
      <th>Ast</th>
      <th>2pt</th>
      <th>Any_TD</th>
      <th>Any_Pts</th>
      <th>Pnt</th>
      <th>Pnt_Yds</th>
      <th>Y/P</th>
      <th>Blck</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-09-07</td>
      <td>1.0</td>
      <td>40.095890</td>
      <td>NWE</td>
      <td>True</td>
      <td>KAN</td>
      <td>L</td>
      <td>True</td>
      <td>True</td>
      <td>27</td>
      <td>42</td>
      <td>16</td>
      <td>36</td>
      <td>44.44</td>
      <td>267</td>
      <td>0</td>
      <td>0</td>
      <td>70.0</td>
      <td>3</td>
      <td>20</td>
      <td>7.42</td>
      <td>7.42</td>
      <td>2</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-09-17</td>
      <td>2.0</td>
      <td>40.123288</td>
      <td>NWE</td>
      <td>False</td>
      <td>NOR</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>36</td>
      <td>20</td>
      <td>30</td>
      <td>39</td>
      <td>76.92</td>
      <td>447</td>
      <td>3</td>
      <td>0</td>
      <td>139.6</td>
      <td>2</td>
      <td>11</td>
      <td>11.46</td>
      <td>13.00</td>
      <td>2</td>
      <td>9</td>
      <td>4.5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-09-24</td>
      <td>3.0</td>
      <td>40.142466</td>
      <td>NWE</td>
      <td>True</td>
      <td>HOU</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>36</td>
      <td>33</td>
      <td>25</td>
      <td>35</td>
      <td>71.43</td>
      <td>378</td>
      <td>5</td>
      <td>0</td>
      <td>146.2</td>
      <td>5</td>
      <td>41</td>
      <td>10.80</td>
      <td>13.66</td>
      <td>1</td>
      <td>6</td>
      <td>6.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-10-01</td>
      <td>4.0</td>
      <td>40.161644</td>
      <td>NWE</td>
      <td>True</td>
      <td>CAR</td>
      <td>L</td>
      <td>True</td>
      <td>True</td>
      <td>30</td>
      <td>33</td>
      <td>32</td>
      <td>45</td>
      <td>71.11</td>
      <td>307</td>
      <td>2</td>
      <td>0</td>
      <td>104.6</td>
      <td>3</td>
      <td>14</td>
      <td>6.82</td>
      <td>7.71</td>
      <td>1</td>
      <td>2</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-10-05</td>
      <td>5.0</td>
      <td>40.172603</td>
      <td>NWE</td>
      <td>False</td>
      <td>TAM</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>19</td>
      <td>14</td>
      <td>30</td>
      <td>40</td>
      <td>75.00</td>
      <td>303</td>
      <td>1</td>
      <td>1</td>
      <td>94.1</td>
      <td>3</td>
      <td>14</td>
      <td>7.58</td>
      <td>6.95</td>
      <td>2</td>
      <td>5</td>
      <td>2.5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-10-15</td>
      <td>6.0</td>
      <td>40.200000</td>
      <td>NWE</td>
      <td>False</td>
      <td>NYJ</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>24</td>
      <td>17</td>
      <td>20</td>
      <td>38</td>
      <td>52.63</td>
      <td>257</td>
      <td>2</td>
      <td>1</td>
      <td>80.7</td>
      <td>0</td>
      <td>0</td>
      <td>6.76</td>
      <td>6.63</td>
      <td>1</td>
      <td>-1</td>
      <td>-1.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-10-22</td>
      <td>7.0</td>
      <td>40.021918</td>
      <td>NWE</td>
      <td>True</td>
      <td>ATL</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>23</td>
      <td>7</td>
      <td>21</td>
      <td>29</td>
      <td>72.41</td>
      <td>249</td>
      <td>2</td>
      <td>0</td>
      <td>121.2</td>
      <td>2</td>
      <td>8</td>
      <td>8.59</td>
      <td>9.97</td>
      <td>5</td>
      <td>5</td>
      <td>1.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-10-29</td>
      <td>8.0</td>
      <td>40.238356</td>
      <td>NWE</td>
      <td>True</td>
      <td>LAC</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>21</td>
      <td>13</td>
      <td>32</td>
      <td>47</td>
      <td>68.09</td>
      <td>333</td>
      <td>1</td>
      <td>0</td>
      <td>95.4</td>
      <td>3</td>
      <td>16</td>
      <td>7.09</td>
      <td>7.51</td>
      <td>1</td>
      <td>2</td>
      <td>2.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-11-12</td>
      <td>9.0</td>
      <td>40.276712</td>
      <td>NWE</td>
      <td>False</td>
      <td>DEN</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>41</td>
      <td>16</td>
      <td>25</td>
      <td>34</td>
      <td>73.53</td>
      <td>266</td>
      <td>3</td>
      <td>0</td>
      <td>125.4</td>
      <td>1</td>
      <td>6</td>
      <td>7.82</td>
      <td>9.59</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-11-19</td>
      <td>10.0</td>
      <td>40.295890</td>
      <td>NWE</td>
      <td>False</td>
      <td>OAK</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>33</td>
      <td>8</td>
      <td>30</td>
      <td>37</td>
      <td>81.08</td>
      <td>340</td>
      <td>3</td>
      <td>0</td>
      <td>132.0</td>
      <td>1</td>
      <td>8</td>
      <td>9.19</td>
      <td>10.81</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-11-26</td>
      <td>11.0</td>
      <td>40.315068</td>
      <td>NWE</td>
      <td>True</td>
      <td>MIA</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>35</td>
      <td>17</td>
      <td>18</td>
      <td>28</td>
      <td>64.29</td>
      <td>227</td>
      <td>4</td>
      <td>1</td>
      <td>114.1</td>
      <td>1</td>
      <td>6</td>
      <td>8.11</td>
      <td>9.36</td>
      <td>5</td>
      <td>-4</td>
      <td>-0.8</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-12-03</td>
      <td>12.0</td>
      <td>40.334247</td>
      <td>NWE</td>
      <td>False</td>
      <td>BUF</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>23</td>
      <td>3</td>
      <td>21</td>
      <td>30</td>
      <td>70.00</td>
      <td>258</td>
      <td>0</td>
      <td>1</td>
      <td>82.4</td>
      <td>3</td>
      <td>14</td>
      <td>8.60</td>
      <td>7.10</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-12-11</td>
      <td>13.0</td>
      <td>40.035616</td>
      <td>NWE</td>
      <td>False</td>
      <td>MIA</td>
      <td>L</td>
      <td>True</td>
      <td>True</td>
      <td>20</td>
      <td>27</td>
      <td>24</td>
      <td>43</td>
      <td>55.81</td>
      <td>233</td>
      <td>1</td>
      <td>2</td>
      <td>59.5</td>
      <td>2</td>
      <td>10</td>
      <td>5.42</td>
      <td>3.79</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-12-17</td>
      <td>14.0</td>
      <td>40.372603</td>
      <td>NWE</td>
      <td>False</td>
      <td>PIT</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>27</td>
      <td>24</td>
      <td>22</td>
      <td>35</td>
      <td>62.86</td>
      <td>298</td>
      <td>1</td>
      <td>1</td>
      <td>87.6</td>
      <td>2</td>
      <td>15</td>
      <td>8.51</td>
      <td>7.80</td>
      <td>2</td>
      <td>-2</td>
      <td>-1.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-12-24</td>
      <td>15.0</td>
      <td>40.391781</td>
      <td>NWE</td>
      <td>True</td>
      <td>BUF</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>37</td>
      <td>16</td>
      <td>21</td>
      <td>28</td>
      <td>75.00</td>
      <td>224</td>
      <td>2</td>
      <td>1</td>
      <td>106.8</td>
      <td>2</td>
      <td>6</td>
      <td>8.00</td>
      <td>7.82</td>
      <td>2</td>
      <td>6</td>
      <td>3.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Tom Brady</td>
      <td>QB</td>
      <td>76</td>
      <td>225</td>
      <td>8</td>
      <td>3</td>
      <td>1977</td>
      <td>Michigan</td>
      <td>2017-12-31</td>
      <td>16.0</td>
      <td>40.041096</td>
      <td>NWE</td>
      <td>True</td>
      <td>NYJ</td>
      <td>W</td>
      <td>True</td>
      <td>True</td>
      <td>26</td>
      <td>6</td>
      <td>18</td>
      <td>37</td>
      <td>48.65</td>
      <td>190</td>
      <td>2</td>
      <td>0</td>
      <td>82.0</td>
      <td>2</td>
      <td>12</td>
      <td>5.14</td>
      <td>6.22</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



The gamelog positions you can choose from are:

**passing()**

**receiving()**

**rushing()**

**defense()**

**kicking()**

Each of these parsers will return a Pandas DataFrame object.

<a id='team_stats'></a>
## Team stats
---
<a id='team_offense'></a>
### Team offense stats
Simply pass a season (year) to the **offense()** method in the **TeamStats()** class


```python
from profootballref.Parsers import TeamStats

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
      <th>Pass_Att</th>
      <th>Pass_Yds</th>
      <th>Pass_TD</th>
      <th>Int</th>
      <th>NY/A</th>
      <th>Pass_1stD</th>
      <th>Rush_Att</th>
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
      <td>501.0</td>
      <td>3589.0</td>
      <td>35.0</td>
      <td>10.0</td>
      <td>6.7</td>
      <td>197.0</td>
      <td>526.0</td>
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
      <td>562.0</td>
      <td>4616.0</td>
      <td>35.0</td>
      <td>13.0</td>
      <td>7.8</td>
      <td>237.0</td>
      <td>452.0</td>
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
      <td>629.0</td>
      <td>4587.0</td>
      <td>36.0</td>
      <td>7.0</td>
      <td>6.9</td>
      <td>230.0</td>
      <td>383.0</td>
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
      <td>590.0</td>
      <td>4603.0</td>
      <td>26.0</td>
      <td>21.0</td>
      <td>7.4</td>
      <td>207.0</td>
      <td>388.0</td>
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
      <td>489.0</td>
      <td>3790.0</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>7.1</td>
      <td>190.0</td>
      <td>500.0</td>
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
</div>



<a id='team_defense'></a>
### Team defense stats
Simply pass a season (year) to the **defense()** method in the **TeamStats()** class


```python
from profootballref.Parsers import TeamStats

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
      <th>Pass_Att</th>
      <th>Pass_Yds</th>
      <th>Pass_TD</th>
      <th>Int</th>
      <th>NY/A</th>
      <th>Pass_1stD</th>
      <th>Rush_Att</th>
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
      <td>548.0</td>
      <td>3364.0</td>
      <td>14.0</td>
      <td>14.0</td>
      <td>5.8</td>
      <td>175.0</td>
      <td>362.0</td>
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
      <td>646.0</td>
      <td>3976.0</td>
      <td>18.0</td>
      <td>21.0</td>
      <td>5.8</td>
      <td>202.0</td>
      <td>344.0</td>
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
      <td>607.0</td>
      <td>3698.0</td>
      <td>25.0</td>
      <td>22.0</td>
      <td>5.7</td>
      <td>193.0</td>
      <td>383.0</td>
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
      <td>573.0</td>
      <td>3193.0</td>
      <td>19.0</td>
      <td>14.0</td>
      <td>5.1</td>
      <td>162.0</td>
      <td>408.0</td>
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
      <td>561.0</td>
      <td>3762.0</td>
      <td>24.0</td>
      <td>13.0</td>
      <td>6.2</td>
      <td>189.0</td>
      <td>411.0</td>
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
</div>
