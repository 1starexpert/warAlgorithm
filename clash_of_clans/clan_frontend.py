import streamlit as st
import os
print("WORKING DIR:", os.getcwd())

import clan_backend
print("Backend imported successfully!")

import requests


import clan_backend

st.sidebar.title("US Leaderboards")
#clan_backend.displayClanLeaders()

st.title("⚔️Clash of Clans: Clan War Simulator⚔️ ")

# Get the user input
clan_tag = st.text_input("Enter a clan tag: (ex: #QYQUVRLV)")
clan_tag2 = st.text_input("Enter a second clan tag: (ex: #2VP2UG2R)")

# Only call backend if the user entered something
if clan_tag:
    try:
        clan_info = clan_backend.displayClanInformation(clan_tag)
        st.image(clan_info[1])
        #for line in clan_info[0]:
            #st.write(line)
        st.write(clan_info[0][:10])
    except:
        st.write("Tag error. Check clan tag and try again or try again with a different tag.")
if clan_tag2:
    try:
        clan_info2 = clan_backend.displayClanInformation(clan_tag2)
        st.image(clan_info2[1])
        #for line in clan_info2[0]:
            #st.write(line)
        st.write(clan_info2[0][:10])
    except:
        st.write("Tag error. Check clan tag and try again or try again with a different tag.")
#war win algorithm here: 
def warAlgorithm():
    
    if clan_tag and clan_tag2:
        clan1 = int(clan_info[0][10])
        clan2 = int(clan_info2[0][10])

        if (clan1 > 10) and (clan2 > 10):
            st.title("Winner: Tie. Both clans are very strong. A tie is the most likely outcome.")
            return
        if (clan1 == clan2):
            st.title("Winner: Tie. It is pretty close. Both clans are around the same level.")
            return
        if (clan1 - clan2) >= 10: 
            st.title("Winner: " + clan_info[0][0])
            st.write(clan_info[0][0] + " is heavily expected to win because they have a winstreak that is MUCH higher.")
            st.image(clan_info[1])
            return
        if (clan2 - clan1) >= 10: 
            st.title("Winner: " + clan_info2[0][0])
            st.write(clan_info2[0][0] + " is heavily expected to win because they have a winstreak that is MUCH higher.")
            st.image(clan_info2[1])
            return
        if clan1 < clan2:
            st.title("Winner: " + clan_info2[0][0]); st.image(clan_info2[1])
            st.write(clan_info2[0][0] + " is marginally expected to win because they have a higher war win streak. ")
            return
        if clan1 > clan2:
            st.title("Winner: " + clan_info[0][0]); st.image(clan_info[1])
            st.write(clan_info[0][0] + " is marginally expected to win because they have a higher war win streak. ")
            return
warAlgorithm()




