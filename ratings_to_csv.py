# -*- coding: utf-8 -*-
"""
imdb ratings.list parser
@author: aknorre
"""

import re
import csv

data_file="./ratings.txt"
output_file="./parsed_ratings.csv"
data=[]
votes=[]
ranks=[]
descs=[]

titles=[]
years=[]
are_series=[]
episode_titles=[]
seasons=[]
episodes=[]
episodeless=False
with open(data_file,'r') as r:
    data = r.readlines()

#Parsing columns
    
for i in data:
    line=i[16:]

    vote=int(re.findall("\d+\s{2}", line)[0])
    votes.append(vote)
    
    rank=float(re.findall("\s\d+\.\d\s", line)[0])
    ranks.append(rank)
    
    desc=str(re.findall("\d\.\d\s\s.*", line)[0])[5:]
    descs.append(desc)

print "Done initial reading. Processing regex..."    
for i in descs:    
    print "RAW     "+ i
    
    title=str(re.findall(".*\(\d{4}|.*\(\?\?\?\?", i)[0])[:-6]  
    
    
    year=str(re.findall("\(\d{4}|\(\?\?\?\?", i)[0][1:])
    
    
    episode_title=re.findall("\{.*\(\#", i)
    if episode_title==[]:
        is_series=False
        episode_title=""
        season=""
        episode=""
        
        
    else:
        is_series=True
        episode_title=episode_title[0][1:-2]
        
        try:
            season=int(re.findall("\(\#\d{1,2}\.", i)[0][2:-1])  
        except:
            season=int(re.findall("\(\#\d{1,2}\)", i)[0][2:-1])
            episodeless=True
        if episodeless==False:
            episode=int(re.findall("\d\.\d{1,6}\)", i)[0][2:-1])            
        else:
            episode=""
        episodeless=False    
    

    
    titles.append(title)
    years.append(year)
    episode_titles.append(episode_title)
    episodes.append(episode)
    seasons.append(season)
    are_series.append(is_series)

print "Done parsing. Writing to file..."
   
a=[1,2,3]   
b=["q","w","e"]  
with open(output_file, 'w') as csvfile:
    w=csv.writer(csvfile, delimiter=';')
    w.writerow(["Numba 1","Numba 2","Numba 3"])
    for i in range(1,len(data)):
        w.writerow([i,votes[i],ranks[i],titles[i]])
    
    #for i,j in zip(a,b):
    #    w.writerow(i)

   
#   print "STRUCT  "+ title, year, episode_title[3:-4], season, episode
