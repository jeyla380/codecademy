#!/usr/bin/env python
# coding: utf-8

# ![](https://cdn2.steamgriddb.com/file/sgdb-cdn/grid/53078424bffd4f61f37db5fc749e1afd.png)

# # Binding of Isaac: Rebirth Project
# 
# <b>About this dataset: </b>[The Binding of Isaac: Rebirth](https://en.wikipedia.org/wiki/The_Binding_of_Isaac:_Rebirth) is an indie roguelike video game designed by Edmund McMillen and developed and published by Nicalis.
# <br>
# 
# Similar to the original Binding of Isaac, the plot is based on the biblical story of the same name and was inspired by McMillen's religious upbringing. The player controls the eponymous Isaac, a young boy whose mother, convinced that she is doing God's work, strips him of everything and locks him in his room. When Isaac's mother is about to sacrifice him, he escapes to the basement and fights through random, roguelike dungeons. The player defeats monsters, using Isaac's tears as projectiles, and collects items which modify his appearance, attributes, and abilities, potentially creating powerful combinations.
# <br>
# 
# Three expansions have been released. Afterbirth and Afterbirth+, in October 2015 and January 2017, respectively, with more game content and gameplay modes; Afterbirth+ also added support for user-created content. The third and final expansion, Repentance, was released in March 2021.
# 
# <hr>
# 
# ## Tasks:
# 
# The purpose of this project is to focus on gathering the data through websites and cleaning up the data before analyzing it.
# 
# 1. Use [this website](https://platinumgod.co.uk/all-items) and scrape the information to get data about all the items used in Binding of Isaac: Rebirth, Afterbirth, Afterbirth+, and the Repentance expansion packs.
# 2. Create a `.csv` file using the scraped data.
# 3. Tidy the Dataframe to easier to read and break down the Dataframe if sections need to be extracted.
# 4. Analyze all the data gathered and make possible predictions.
# 
# <hr>

# ### BeautifulSoup Web Scraping:
# 
# Because there isn't any datasets for Binding of Isaac, I had to use BeautifulSoup to Web Scrape data and create my own `.csv` file.[<sup id="fn1-back">1</sup>](#fn1)

# In[184]:


import requests
from bs4 import BeautifulSoup

webpage_response = requests.get('https://platinumgod.co.uk/all-items')
webpage = webpage_response.content
soup = BeautifulSoup(webpage, 'html.parser')

print(soup)


# In[185]:


textbox = soup.find_all('li', class_ = 'textbox')
print(textbox)


# In[186]:


get_rid = soup.find("strong", class_ = 'pri')
get_rid.decompose()

#print(get_rid)


# In[187]:


title = []
ID = []
pickup = []
quality = []
description = []


#the elements will automatically be put into lists when appended to list
for element in textbox:
    item_title = element.find("p", class_ = 'item-title')
    item_id = element.find("p", class_ = 'r-itemid')
    item_pickup = element.find("p", class_ = 'pickup')
    item_quality = element.find("p", class_ = 'quality')
    #item_description = element.find("p", class_ = None)
    
    
    #print(item_description)

    for x in item_title:
        #print(x)
        title.append(x)

    if item_id != None:
        for x in item_id:
            #print(x)
            ID.append(x)
    
    if item_pickup != None:
        for x in item_pickup:
            #print(x)
            pickup.append(x)
    
    if item_quality != None:
        for x in item_quality:
            #print(x)
            quality.append(x)
    
    for x in element.find('p', class_ = None):
        for strong in element.findAll('strong', class_ = 'pri'):
            #print(strong)
            strong.decompose()
        #print(x)
        description.append(x)
        
pickup.insert(960, '"D6 + D20"') #The Dice Shard's Pickup was not included in the website
title[199] = 'Humbling Bundle'
title[543] = 'Broken Shovel (Top)'
title[544] = 'Broken Shovel (Bottom)'
title[545] = "Mom's Shovel (Top + Bottom Broken Shovel)"
description[233] = "Increases your chances to find an Angel Room instead of a Devil Room."
description[234] = "Increases your chances to find an Angel Room instead of a Devil Room."

        
#print(title)
#print(ID)
#print(pickup)
#print(quality)
#print(description)


# In[188]:


paragraph = []
item_types = []
item_pool = []

for p in soup.select("ul > p"):
    #print(p.text)
    paragraph.append(p.text)
#print(paragraph)

for p in paragraph:
    if 'Type' in p:
        #print(p)
        item_types.append(p)
    if 'Item Pool' in p:
        #print(p)
        item_pool.append(p)

item_types[645] = 'Type: Active, Familiar'        

item_pool[8] = 'Item Pool: Arcade Shell Game'
item_pool[17] = 'Item Pool: Arcade Machine'
item_pool[69] = 'Item Pool: One of the Horsemen Bosses (Famine, Pestilence, War, Death)'
item_pool[86] = 'Item Pool: Tinted Rock'
item_pool[88] = "Item Pool: Item Room, Boss Room"
item_pool[115] = 'Item Pool: Blood Donation Machine'
item_pool[116] = 'Item Pool: Item Room, Secret Room'
item_pool[126] = 'Item Pool: Headless Horseman Boss'
item_pool[128] = 'Item Pool: Krampus Boss'
item_pool[131] = 'Item Pool: Blood Donation Machine'
item_pool[233] = 'Item Pool: Angel Statue in Angel Room'
item_pool[234] = 'Item Pool: Angel Statue in Angel Room'
item_pool[547] = 'Item Pool: Item Room'
item_pool[615] = 'Item Pool: Shop'
item_pool[616] = 'Item Pool: Boss Room, Crane Game, Shop'
item_pool[621] = 'Item Pool: Crane Game, Key Beggar, Item Room'
item_pool[652] = 'Item Pool: Secret Room'
item_pool[657] = 'Item Pool: Shop'
item_pool[698] = 'Item Pool: Curse Room, Secret Room, Super Secret Room'
item_pool[699] = 'Item Pool: Library, Devil Room'

item_pool.insert(543, " ")
item_pool.insert(544, " ")
item_pool.insert(545, " ")
#print(item_pool)


# ### Create the CSV File:
# 
# Here the `.csv` is created under the name `items.csv`.

# In[189]:


import csv
from itertools import zip_longest

data = [ID, title, pickup, quality, description, item_types, item_pool]
export_data = zip_longest(*data, fillvalue = '')

with open('items.csv', 'w', encoding = 'UTF-8', newline = '') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(("ID", "Name of Item", "Pickup", "Quality", "Description", "Type", "Item Pool"))
    wr.writerows(export_data)
myfile.close()


# In[190]:


import pandas as pd

items = pd.read_csv('items.csv')
items.head()


# ### Tidy and Wrangle Data:

# In[191]:


#items.tail(8)
items = items[:-8]
items.tail(10)


# #### Miscellaneous Stuff

# In[192]:


misc = items.iloc[1004:]
misc = misc.loc[:, ('Name of Item', 'Description')]
misc = misc.reset_index(drop = True)

misc.head(10)


# #### Cards & Other Useable Items

# In[193]:


cards = items.iloc[907:1004]
cards = cards.loc[:, ('Name of Item', 'Pickup', 'Description')]
cards = cards.reset_index(drop = True)

cards.tail()


# #### Trinkets

# In[194]:


trinkets = items.iloc[719:907]
trinkets = trinkets.loc[:, ('Name of Item', 'Pickup', 'Description')]
trinkets = trinkets.reset_index(drop = True)

trinkets.head()


# #### Useable Items

# In[195]:


useable_items = items.iloc[:719]
useable_items = useable_items.loc[:, ('Name of Item', 'Pickup', 'Quality', 'Description', 'Type', 'Item Pool')]
useable_items = useable_items.reset_index(drop = True)

#useable_items.head()


# In[196]:


useable_items['Quality'] = useable_items['Quality'].str.split(':')
useable_items['Quality'] = useable_items['Quality'].str.get(1)
useable_items['Quality'] = pd.to_numeric(useable_items['Quality'])

#useable_items.head()


# In[197]:


useable_items['Type'] = useable_items['Type'].str.split(':')
useable_items['Type'] = useable_items['Type'].str.get(1)

useable_items['Secondary Type'] = useable_items['Type'].str[9:]
useable_items['Type'] = useable_items['Type'].str.split(', ')
useable_items['Type'] = useable_items['Type'].str.get(0)

useable_items = useable_items[['Name of Item', 'Pickup', 'Quality', 'Description', 'Type', 'Secondary Type', 'Item Pool']]

#useable_items.head()


# In[198]:


useable_items['Item Pool'] = useable_items['Item Pool'].str.split(':')
useable_items['Item Pool'] = useable_items['Item Pool'].str.get(1)

useable_items = useable_items.fillna(" ")

#useable_items.head()


# In[199]:


pd.set_option('display.max_rows', None, 'display.max_columns', None)
pd.set_option('display.width', 5000)
useable_items.to_html('useable_items_dataframe.html')


# #### Pills

# In[200]:


#scrape the info for pills and turn that into a dataframe
extra = []
pills = []

rebirth_one = soup.find_all('li', {'data-sid': '1000'})
#print(rebirth_one)
for pill in rebirth_one:
    #print(pill)
    rebirth_pill_one = pill.find_all('p', class_ = None)
    #print(rebirth_pill_one)
    
for pill in rebirth_pill_one:
    for x in pill:
        #print(x)
        pills.append(x)
        

rebirth_two = soup.find_all('li', {'data-sid': '1001'}) 
#print(rebirth_two)
for pill in rebirth_two:
    rebirth_pill_two = pill.find_all('p', class_ = None)
    #print(rebirth_pill_two)

for pill in rebirth_pill_two:
    for x in pill:
        #print(x)
        pills.append(x)

        
afterbirth = soup.find_all('li', {'data-sid': '1002'}) 
for pill in afterbirth:
    afterbirth_pill = pill.find_all('p', class_ = None)
    #print(afterbirth_pill)

for pill in afterbirth_pill:
    for x in pill:
        #print(x)
        pills.append(x)

        
             
afterbirth_plus = soup.find_all('li', {'data-sid': '1003'})
for pill in afterbirth_plus:
    afterbirth_plus_pill = pill.find_all('p', class_ = None)
    #print(afterbirth_plus_pill)

for pill in afterbirth_plus_pill:
    for x in pill:
        #print(x)
        pills.append(x)
        
        
    
repentance = soup.find_all('li', {'data-sid': '1004'})
for pill in repentance:
    repentance_pill = pill.find_all('p', class_ = None)
    #print(repentance_pill)

for pill in repentance_pill:
    for x in pill:
        #print(x)
        pills.append(x)

        
#print(pills)


# In[201]:


data = [pills]
export_data = zip_longest(*data, fillvalue = '')

with open('pills.csv', 'w', encoding = 'UTF-8', newline = '') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(("P"))
    wr.writerows(export_data)
myfile.close()


# In[202]:


pills = pd.read_csv('pills.csv')
#pills.head()


# In[203]:


pills['str_split'] = pills['P'].str.split(' - ')
pills['Pill Name'] = pills['str_split'].str.get(0)
pills['Description'] = pills['str_split'].str.get(1)


# In[204]:


del pills['str_split']
del pills['P']

pills.head()


# #### Characters

# *These following characters were removed from the `.csv`:
# - Eden: Heart containers, damage, tears, shot speed, range, speed, luck, starting pickups are all randomized each round.
# - The Forgotton + The Soul: This is a 2-in-1 character, each with different heart containers, damage, etc. If one dies, then both die.
# - Jacob + Esau: These 2 characters are played together, but each has different statistics. If one character dies, then both die.
# - Dark Judas: Didn't want to include Dark Judas as I didn't want Judas to be confused with Dark Judas.
# - The Keeper: The Keeper has special heart containers made of coins that can be refilled with picking up coins.
# 

# In[224]:


import numpy as np


characters = pd.read_csv('binding_of_isaac_characters.csv')

characters['Health in Red Hearts'] = pd.to_numeric(characters['Health in Red Hearts'])

characters.head(13)


# ### Analyze Data:

# #### 1. Use a Bar Graph to Look at Each Character's Health Stats

# In[232]:


import matplotlib.pyplot as plt

#Bar 1
n = 1
t = 3
d = 13
w = 0.3
x_values1 = [t * element + w * n for element in range(d)]

#Bar 2
n = 2
x_values2 = [t * element + w * n for element in range(d)]

#Bar 3
n = 3
x_values3 = [t * element + w * n for element in range(d)]


plt.figure(figsize = (10, 8))
ax = plt.subplot()
plt.bar(x_values1, characters['Health in Red Hearts'], label = 'Red Heart', color = 'crimson')
plt.bar(x_values2, characters['Health in Soul Heart'], label = 'Soul Heart', color = 'powderblue')
plt.bar(x_values3, characters['Health in Black Heart'], label = 'Black Heart', color = 'dimgray')

ax.set_xticks(x_values2)
ax.set_xticklabels(characters['Character'], rotation = 90)
ax.set_yticks(range(5))

plt.legend()

plt.show()


# There are a majority of characters that start out with red hearts with the exception of ??? (Blue Baby), Azazel, and Lilith. ??? (Blue Baby) starts with 3 soul hearts, Azazel starts with 3 black hearts, and Lilith starts with 1 red heart, and 2 black hearts.

# #### 2. Use Bar Graphs to Look at Each Character's Damage, Shot Speed, etc. and Compare Them

# In[209]:


#Bar 1
n = 1
t = 6
d = 13
w = 0.7
x_values1 = [t * element + w * n for element in range(d)]

#Bar 2
n = 2
x_values2 = [t * element + w * n for element in range(d)]

#Bar 3
n = 3
x_values3 = [t * element + w * n for element in range(d)]

#Bar 4
n = 4
x_values4 = [t * element + w * n for element in range(d)]

#Bar 5
n = 5
x_values5 = [t * element + w * n for element in range(d)]

#Bar 6
n = 6
x_values6 = [t * element + w * n for element in range(d)]


plt.figure(figsize = (15, 8))
ax = plt.subplot()
plt.bar(x_values1, characters['Damage'], label = 'Damage', color = 'firebrick')
plt.bar(x_values2, characters['Tears'], label = 'Tears', color = 'lightskyblue')
plt.bar(x_values3, characters['Shot Speed'], label = 'Shot Speed', color = 'sandybrown')
plt.bar(x_values4, characters['Range'], label = 'Range', color = 'gold')
plt.bar(x_values5, characters['Speed'], label = 'Speed', color = 'mediumpurple')
plt.bar(x_values6, characters['Luck'], label = 'Luck', color = 'forestgreen')

ax.set_xticks(x_values3)
ax.set_xticklabels(characters['Character'], rotation = 90)
plt.axhline(y=0, color='black')
plt.legend()

plt.show()


# This just shows the starting statistics (outside of health) for each character. Most of the characters tend to have the same starting statistics, but a couple have a higher/lower tear rate or luck than the rest.

# #### 3. How Many Items are Active and How Many are Passive?

# In[181]:


#separate the active and passive items

useable_items['Type'] = useable_items['Type'].astype('string') #need to change 'Type' to string type instead of object type
useable_items['Type'] = useable_items['Type'].str.strip()

active_items = useable_items[useable_items['Type'] == 'Active']
active_items.head()


# In[182]:


passive_items = useable_items[useable_items['Type'] == 'Passive']
passive_items.head()


# In[217]:


item_graph = []
item_graph.append(len(active_items['Type']))
item_graph.append(len(passive_items['Type']))
#print(item_graph)

labels = ['Active Items', 'Passive Items']

plt.figure(figsize = (10, 8))
plt.pie(item_graph, labels = labels, colors = ['gold', 'cornflowerblue'], autopct = '%0.1f%%')

plt.title("Active or Passive?")
plt.show()


# A majority of items in the game are passive (usually adds to character's statistics), while less than a quarter are active items.

# #### 4. What is the Percent of Cards, Trinkets, etc. to Items?

# In[230]:


#use a pie chart to find the proportion of cards, trinkets, misc, and items

all_items_graph = []
all_items_graph.append(len(misc))
all_items_graph.append(len(cards))
all_items_graph.append(len(pills))
all_items_graph.append(len(trinkets))
all_items_graph.append(len(useable_items))

labels = ['Miscellaneous', 'Cards', 'Pills', 'Trinkets', 'Items']


plt.figure(figsize = (10, 8))

plt.pie(all_items_graph, labels = labels, colors = ['skyblue', 'sandybrown', 'forestgreen', 'firebrick', 'slateblue'], autopct = '%0.1f%%')
plt.show()


# When looking at the total things within the game, a majority are items (both passive and aggressive), with a smaller percentage in trinkets, cards, pills, and miscellaneous (in that order from largest to smallest).

# #### 5. When Dropping an Item, What is it Likely to Be: A Card, or Trinket?

# First we need to find the sample size needed using the Baseline Conversion Rate, Minimum Detectable Effect, and the Significance Threshold for trinkets.

# In[236]:


amount_trinkets = len(trinkets)
amount_total = len(items)

baseline = (amount_trinkets / amount_total) * 100
print("Baseline: " + str(round(baseline, 2)) + "%")


# Suppose that 18.56% of trinkets will be dropped over a card. We're thinking about adding a new trinket, but it would be more worth it if the trinket was dropped 23% instead.

# In[239]:


new_baseline = 23 #23%

mde = ((new_baseline - baseline) / baseline) * 100
print("Minimum Detectable Effect: " + str(round(mde, 2)) + "%")


# The most common Significance Threshold is 95%, so we will stick with using that too.
# 
# <br>
# 
# Using a [sample size calculator](https://www.optimizely.com/sample-size-calculator/?conversion=18.56&effect=23.93&significance=95), we get the sample size of <b>830</b>. Now we will use that number to create a simulation to determine if a card or trinket would be more likely to be dropped.

# In[242]:


card_percent = (len(cards) / amount_total) * 100
print(str(round(card_percent, 2)) + "%")


# In[246]:


sample_trinket = np.random.choice(['yes', 'no'], size = 415, p = [0.1856, 0.8144])
sample_card = np.random.choice(['yes', 'no'], size = 415, p = [0.0958, 0.9042])


# In[248]:


group = ['trinket'] * 415 + ['card'] * 415
outcome = list(sample_trinket) + list(sample_card)

sim_data = {'Trinket or Card?': group, "Dropped?": outcome}
sim_data = pd.DataFrame(sim_data)
sim_data.head()


# In[251]:


sim_data_trinket = sim_data[sim_data['Trinket or Card?'] == 'trinket']
sim_data_trinket_dropped = sim_data_trinket[sim_data_trinket['Dropped?'] == 'yes']
#print(len(sim_data_trinket_dropped))
sim_data_trinket_not_dropped = sim_data_trinket[sim_data_trinket['Dropped?'] == 'no']

sim_data_card = sim_data[sim_data['Trinket or Card?'] == 'card']
sim_data_card_dropped = sim_data_card[sim_data_card['Dropped?'] == 'yes']
#print(len(sim_data_card_dropped))
sim_data_card_not_dropped = sim_data_card[sim_data_card['Dropped?'] == 'no']


plt.figure(figsize = (15, 8))
ax1 = plt.subplot(1, 2, 1)
plt.pie([len(sim_data_trinket_dropped), len(sim_data_trinket_not_dropped)], labels = ['Yes', 'No'], autopct = '%0.1f%%', 
        colors = ['lightcoral', 'lightsalmon'])
plt.title("Trinket Dropped?")

ax2 = plt.subplot(1, 2, 2)
plt.pie([len(sim_data_card_dropped), len(sim_data_card_not_dropped)], labels = ['Yes', 'No'], autopct = '%0.1f%%', 
        colors = ['peru', 'tan'])
plt.title("Card Dropped?")


plt.show()


# In[253]:


import seaborn as sns

plt.figure(figsize = (10, 8))
sns.histplot(data = sim_data, x = 'Trinket or Card?', hue = 'Dropped?', multiple = 'dodge', shrink = 0.8, palette = ['#BC8F8F', '#B0C4DE'])

plt.show()


# Looking at these 2 graphs, it is most likely that neither a card or trinket will drop; at a 21.9% a trinket will drop, and a card will drop at even less at 10.8%. It's likely that another item may drop, or nothing at all.

# <hr>
# 
# [<sup id="fn1">1</sup>](#fn1-back) [Descriptions for Items in Binding of Isaac](https://platinumgod.co.uk/all-items).

# In[ ]:




