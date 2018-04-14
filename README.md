
# ProFootballRef

This is a python module that lets you scrape player stats from profootballreference.com.
### Installation
```python
git clone git@github.com:gVkWY8NJAa/ProFootballRef.git
cd ProFootballRef
pip install -r requirements.txt
```
### Testing
```python
cd <path/to/ProFootballRef>
python3.6 -m pytest tests/
```
### Overview of usage

1. Generate links to scrape.
2. Request and return html for each link.
3. Parse general info such as height and weight from the returned html.
4. Parse performance metrics specific to the position.
5. Combine the general heigh/weight with the performance metrics.

## Specific Usage


```python
from ProFootballRef import GetPositionLinks
from ProFootballRef import PlayerParser
```

First we need to generate pages to scrape based on position. This is a two step process.
1. Pass a position to the **GetPositionLinks()** class: passing, receiving, rushing, kicking, or defense.
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




```python
df.columns
```




    Index(['Name', 'Year', 'Age', 'Throws', 'Height', 'Weight', 'DOB_mo',
           'DOB_day', 'DOB_yr', 'College', 'Tm', 'Pos', 'No.', 'G', 'GS', 'QBrec',
           'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'TD%', 'Int', 'Int%', 'Lng',
           'Pass_Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'QBR', 'Sk', 'Sk_Yds', 'NY/A',
           'ANY/A', 'Sk%', '4QC', 'GWD', 'AV', 'Rush', 'Rush_Yds', 'Rush_TD',
           'Rush_Lng', 'Rush_Y/A', 'Rush_Y/G', 'A/G', 'Tgt', 'Rec', 'Rec_Yds',
           'Y/R', 'Rec_TD', 'Rec_Lng', 'R/G', 'Rec_Y/G', 'Ctch%', 'YScm', 'RRTD',
           'Fmb'],
          dtype='object')


