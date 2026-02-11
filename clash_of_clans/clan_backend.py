##This file contains basic information about clans
##backend

import requests

from pprint import pprint
import streamlit as st

#API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjI3ODI2ZGM5LWM3M2EtNGZmOS04NzEzLTQ0Nzc0M2ZhZjBmMyIsImlhdCI6MTc2NDYwNTAwNSwic3ViIjoiZGV2ZWxvcGVyLzViMjBmYzM1LTEwOGEtNDM1YS0yNmMwLTQ4Njk2OTA4MDQyOCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE0OS4xMDIuMjQyLjkxIl0sInR5cGUiOiJjbGllbnQifV19.OcbKnvwVw7lbPmkPMsl0kHS1Z88_mN3rstpAfm0LURK8DU38AihsPXjkhpsZLoxAN7VkhHaD_rKlvSpNnfIeGw"
#API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjdkYzEwOTliLTIwN2EtNDNkOC05OTMzLWQzMmJiYzllYWFiMiIsImlhdCI6MTc2NDYxNzcxOSwic3ViIjoiZGV2ZWxvcGVyLzViMjBmYzM1LTEwOGEtNDM1YS0yNmMwLTQ4Njk2OTA4MDQyOCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE0OS4xMDIuMjQyLjkwIl0sInR5cGUiOiJjbGllbnQifV19.LG-PxSC9JYBUMNK1NGNaHHd2Re9N_862sWSF_cB4Q8jZzpyD9cp2WLtJJrhPNOt9tgcRveysAUC-qYJm_i0KMA"
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjliYjE0MDVjLTMxY2MtNGY2MC1hOWY5LWViY2E3ODk2NzBhMyIsImlhdCI6MTc2NDYxODI3OSwic3ViIjoiZGV2ZWxvcGVyLzViMjBmYzM1LTEwOGEtNDM1YS0yNmMwLTQ4Njk2OTA4MDQyOCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjQ1Ljc5LjIxOC43OSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.C6EoL9aIDnsZ4ZYrPKKJvhoRkzrKan8HB6W7KMkFxyJHnjp1Ryj2Evo3J3DdfKb8hLiZWoaHILErNg-w1jg1tQ"

def displayClanLeaders():
    url = f"https://cocproxy.royaleapi.dev/v1/locations/32000009/rankings/clans?limit=10"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    clan_dict = response.json()
    #pprint(clan_dict["items"][0])
    cd = clan_dict["items"]

    for i in range(10):
        lb = []
        name = cd[i]["name"]
        tag = cd[i]["tag"]
        st.image(cd[i]["badgeURLs"]["small"])
        st.write("Clan Name: " + name + " Clan Tag: " + tag)
    #name = cd[0]["name"]
    #tag = cd[0]["tag"]

    #print(name)
    #print(tag)
def displayClanInformation(tag):

    CLAN_TAG = tag.replace("#", "%23")  # URL encode the hashtag
    url = f"https://cocproxy.royaleapi.dev/v1/clans/{CLAN_TAG}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    clan_dict = response.json()

    ################################################
    
    clan_level = str(clan_dict["clanLevel"])
    num_members = str(clan_dict["members"])
    clan_points = str(clan_dict["clanPoints"])
    chat_language = str(clan_dict["chatLanguage"]["name"])
    clan_capital_points = str(clan_dict["clanCapitalPoints"])
    clan_location = clan_dict["location"]["name"]
    clan_name = clan_dict["name"]
    required_townhall = clan_dict["requiredTownhallLevel"]
    clan_war_league = clan_dict["warLeague"]["name"]
    join_type = clan_dict["type"]
    required_trophies = clan_dict["requiredTrophies"]
    badge = clan_dict["badgeUrls"]["medium"]
    description = clan_dict["description"]
    winStreak = str(clan_dict["warWinStreak"])
    
    #print("Basic Clan Information:")

    clan_list = [
    
    ["Clan Name: " + clan_name,
    "Clan Description: " + description,
    "Clan Level: " + clan_level,
    "Number of Members in Clan: " + num_members,
    "Clan War League: " + clan_war_league,
    "Clan Points: " + clan_points,
    "Clan Capital Points: " + clan_capital_points,
    "Clan Chat Language: " + chat_language,
    "Clan Location: " + clan_location,
    "War Win Streak: " + winStreak,
    winStreak],
    badge
          
    ]
    
    return clan_list






"""

url2 =f"https://api.clashofclans.com/v1/clans/%232VP2UG2R/warlog?limit=10"
headers2 = {
    "Authorization": f"Bearer {API_TOKEN}"
    }

response2 = requests.get(url2, headers=headers2)

#pprint(response.json())

##################################################


war_log = response2.json()

#war:

war_wins = clan_dict["warWins"]
war_losses = clan_dict["warLosses"]
war_ties = clan_dict["warTies"]
war_frequency = clan_dict["warFrequency"]



#required league:
#required builderbase league

#clan tag
#clan descrption

#Start of code here



def displayWarLog():

    print("Basic Information About Clan War Log:")

    
    return

"""       










