#!/usr/bin/env python
# coding: utf-8

# In[1]:


# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 
         'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 
         'Edith','Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 
         'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']


# In[2]:


# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 
          'September', 'September', 'September', 'September', 'October', 'September', 'August', 
          'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October',
          'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September',
          'October', 'September', 'September', 'October']


# In[3]:


# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 
         1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 
         2016, 2017, 2017, 2018]


# In[4]:


# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175,
                       175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180,
                       175, 160]


# In[5]:


# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'], 
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], 
                  ['Jamaica', 'Yucatn Peninsula'], 
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], 
                  ['Lesser Antilles', 'Central America'], 
                  ['Texas', 'Louisiana', 'Midwestern United States'], 
                  ['Central America'], 
                  ['The Caribbean', 'Mexico', 'Texas'], 
                  ['Cuba', 'United States Gulf Coast'], 
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], 
                  ['Mexico'], 
                  ['The Caribbean', 'United States East coast'], 
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 
                  ['The Caribbean', 'United States East Coast'], 
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'], 
                  ['Central America', 'Yucatn Peninsula', 'South Florida'], 
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], 
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], 
                  ['Bahamas', 'United States Gulf Coast'], 
                  ['Cuba', 'United States Gulf Coast'], 
                  ['Greater Antilles', 'Central America', 'Florida'], 
                  ['The Caribbean', 'Central America'], 
                  ['Nicaragua', 'Honduras'], 
                ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'] 
                  ,['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]


# In[6]:


# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 
           'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B',
           '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']


# In[7]:


# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,
          124,17,1836,125,87,45,133,603,138,3057,74]


# In[8]:


# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


# In[ ]:





# In[193]:


#1
# write your update damages function here:
new_damages = []

def convert_to_float():
    #print(damages[0:-1])
    for number in damages:
        if number[-1] == "M":
            million = number.replace('M', '')
            new_million = float(million) * 1000000
            new_million = "{:.0f}".format(new_million)
            #print(new_million)
            new_damages.append(new_million)
        elif number[-1] == "B":
            billion = number.replace('B', '')
            new_billion = float(billion) * 1000000000
            new_billion = "{:.0f}".format(new_billion)
            #print(new_billion)
            new_damages.append(new_billion)
        else:
            new_damages.append(number)
    print(new_damages)
    #return new_damages


convert_to_float()        


# In[46]:


#2
# Create a Table

hurricane_names = [] #hurricane_names = names (didn't actually need a new list)
hurricane_data = []

def multiple_dictionaries():
    
    for index in range(0, len(names)):
        hurricane_names.append(names[index])
    #print(hurricane_names)  
    #print("")
    
    for number in range(0, len(new_damages)):
        hurricane_dictionary = {}
        hurricane_dictionary.update({
            "Name": names[number], 
            "Month": months[number],
            "Year": years[number], 
            "Max Sustained Wind": max_sustained_winds[number],
            "Areas Affected": areas_affected[number], 
            "Damage": new_damages[number],
            "Deaths": deaths[number]})
        #print(hurricane_data)
        #print("")
        
        hurricane_data.append(hurricane_dictionary.copy())
    #print(hurricane_data)
        
    new_hurricane_data = dict(zip(hurricane_names, hurricane_data))
    #print(new_hurricane_data)
    
    for key, value in new_hurricane_data.items():
        print(key + ": " + str(value))
        print("")

multiple_dictionaries()


# In[11]:


# 3
# Organizing by Year

def organize_by_year():
    #print(hurricane_data)
    
    hurricane_data_list = []
    
    for index in hurricane_data:
        #print(index)
        hurricane_data_list = list(zip(years, hurricane_data))
    #print(hurricane_data_list)

    for key, value in hurricane_data_list:
        print(str(key) + ": " + str(value))
        print("")

organize_by_year()  


# In[12]:


#4
#Counting Damaged Areas

from collections import defaultdict


def atlantic_areas_affected():
    #print(areas_affected)
    
    d = defaultdict(int)
    for group in areas_affected:
        #print(group)
        for name in group:
            #print(name)
            d[name] += 1
            #if I do "if" statement, it will break and not work properly
    
    #print(list(d.items()))
    for key, value in d.items():
        print(str(key) + ": " + str(value))
            
atlantic_areas_affected()    


# In[111]:


#5
#Calculating Maximum Hurricane Count


def maximum_hurricanes():
    #print(areas_affected)
    
    d = defaultdict(int)
    for group in areas_affected:
        #print(group)
        for name in group:
            #print(name)
            d[name] += 1
            
    sorted_list = sorted(d.items(), key=lambda item: item[1], reverse=True)
    #print(sorted_list)
    pair_iterator = iter(sorted_list)
    first_pair = next(pair_iterator)
    #print(list(first_pair))
    #print("")
        
    print(str(first_pair[0]) + ": " + str(first_pair[1]) + " total hurricanes")
    
maximum_hurricanes()   


# In[109]:


#6
#Calculating the Deadliest Hurricane

def maximum_deaths():
    #print(deaths)
    
    death_list = []
    for index in hurricane_data:
        death_list = list(zip(names, deaths))
    #print(death_list)    
    
    new_end_value = sorted(death_list, key = lambda x: x[1], reverse=True)
    #print(new_end_value)
    pair_iter = iter(new_end_value)
    new_deaths = next(pair_iter)
    #print(list(new_deaths))
    
    print("Hurricane " + str(new_deaths[0]) + ": " + str(new_deaths[1]) + " deaths")
    
maximum_deaths()    


# In[118]:


#7
#Rating Hurricanes by Mortality

def hurricanes_by_mortality():
    
    morality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    one_morality = {}
    two_morality = {}
    three_morality = {}
    four_morality = {}
    five_morality = {} #greater than 10000
    
    one_death_list = []
    two_death_list = []
    three_death_list = []
    four_death_list = []
    five_death_list = []
    
    deaths_and_hurricanes = []
    for index in hurricane_data:
        deaths_and_hurricanes = list(zip(names, deaths))
    #print(deaths_and_hurricanes)
    
    sorted_death_list = sorted(deaths_and_hurricanes, key = lambda x: x[1])
    #print(sorted_death_list)
    
    for number in range(0, len(sorted_death_list)):
        #print(number)
        #print(sorted_death_list[number][1])
        if sorted_death_list[number][1] <= 100:
            #print(sorted_death_list[number])
            one_death_list.append(sorted_death_list[number])
    #print(one_death_list)
        elif sorted_death_list[number][1] > 100 and sorted_death_list[number][1] <= 500:
            #print(sorted_death_list[number])
            two_death_list.append(sorted_death_list[number])
    #print(two_death_list)
        elif sorted_death_list[number][1] > 500 and sorted_death_list[number][1] <= 1000:
            #print(sorted_death_list[number])
            three_death_list.append(sorted_death_list[number])
    #print(three_death_list)
        elif sorted_death_list[number][1] > 1000 and sorted_death_list[number][1] <= 10000:
            #print(sorted_death_list[number])
            four_death_list.append(sorted_death_list[number])
    #print(four_death_list)
        elif sorted_death_list[number][1] > 10000:
            #print(sorted_death_list[number])
            five_death_list.append(sorted_death_list[number])
    #print(five_death_list)
    
    one_morality.update({1: one_death_list})
    #print(one_morality)
    for key, value in one_morality.items():
        print(str(key) + ": " + str(value))
        print("")
    
    two_morality.update({2: two_death_list})
    #print(two_morality)
    for key, value in two_morality.items():
        print(str(key) + ": " + str(value))
        print("")
    
    three_morality.update({3: three_death_list})
    #print(three_morality)
    for key, value in three_morality.items():
        print(str(key) + ": " + str(value))
        print("")
        
    four_morality.update({4: four_death_list})
    #print(four_morality)
    for key, value in four_morality.items():
        print(str(key) + ": " + str(value))
        print("")
        
    five_morality.update({5: five_death_list})
    #print(five_morality)
    for key, value in five_morality.items():
        print(str(key) + ": " + str(value))
            
    
hurricanes_by_mortality()    


# In[188]:


#8
#Calculating Hurricane Maximum Damage

def maximum_damage():
    
    #print(new_damages)
    hurricanes_damages = list(zip(names, new_damages))
    #print(hurricanes_damages)
    
    hurricanes_damages.remove(('Cuba I', 'Damages not recorded'))
    hurricanes_damages.remove(('Bahamas', 'Damages not recorded'))
    hurricanes_damages.remove(('Labor Day', 'Damages not recorded'))
    hurricanes_damages.remove(('Anita', 'Damages not recorded'))
    
    end_value = sorted(hurricanes_damages, key = lambda x: int(x[1]), reverse=True)
    #print(end_value)
    iter_pair = iter(end_value)
    new_hurricanes_damages = next(iter_pair)
    #print(list(new_hurricanes_damages))
    
    print("Hurricane " + new_hurricanes_damages[0] + ": " + "$" + str(new_hurricanes_damages[1]) + " in damages")


maximum_damage()


# In[190]:


#9
#Rating Hurricanes by Damage

def hurricanes_by_damage():
    
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    
    one_scale = {}
    two_scale = {}
    three_scale = {}
    four_scale = {}
    five_scale = {} #greater than 50000000000
    
    one_damage_list = []
    two_damage_list = []
    three_damage_list = []
    four_damage_list = []
    five_damage_list = []
    
    hurricane_damages = list(zip(names, new_damages))
    #print(hurricanes_damages)
    end_value = sorted(hurricane_damages, key = lambda x: x[1], reverse=True)
    #print(end_value)
    
    end_value.remove(('Cuba I', 'Damages not recorded'))
    end_value.remove(('Bahamas', 'Damages not recorded'))
    end_value.remove(('Labor Day', 'Damages not recorded'))
    end_value.remove(('Anita', 'Damages not recorded'))
    #print(end_value)
    
    for value in range(0, len(end_value)):
        if int(end_value[value][1]) <= 100000000:
            #print(end_value[value])
            one_damage_list.append(end_value[value])
    #print(one_damage_list)
        elif int(end_value[value][1]) > 100000000 and int(end_value[value][1]) <= 1000000000:
            #print(end_value[value])
            two_damage_list.append(end_value[value])
    #print(two_damage_list)
        elif int(end_value[value][1]) > 1000000000 and int(end_value[value][1]) <= 10000000000:
            #print(end_value[value])
            three_damage_list.append(end_value[value])
    #print(three_damage_list)
        elif int(end_value[value][1]) > 10000000000 and int(end_value[value][1]) <= 50000000000:
            #print(end_value[value])
            four_damage_list.append(end_value[value])
    #print(four_damage_list)     
        elif int(end_value[value][1]) > 50000000000:
            #print(end_value[value])
            five_damage_list.append(end_value[value])
    #print(five_damage_list)
    
    one_scale.update({1: one_damage_list})
    #print(one_scale)
    for key, value in one_scale.items():
        print(str(key) + ": " + str(value))
        print("")
    
    two_scale.update({2: two_damage_list})
    #print(two_scale)
    for key, value in two_scale.items():
        print(str(key) + ": " + str(value))
        print("")
    
    three_scale.update({3: three_damage_list})
    #print(three_scale)
    for key, value in three_scale.items():
        print(str(key) + ": " + str(value))
        print("")
    
    four_scale.update({4: four_damage_list})
    #print(four_scale)
    for key, value in four_scale.items():
        print(str(key) + ": " + str(value))
        print("")
    
    five_scale.update({5: five_damage_list})
    #print(five_scale)
    for key, value in five_scale.items():
        print(str(key) + ": " + str(value))
    
    

hurricanes_by_damage()





