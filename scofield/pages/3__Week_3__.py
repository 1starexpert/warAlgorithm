import streamlit as st

st.header("Week 3:")

st.subheader("Images:")

st.write("""

This api is seriously advanced. I have discovered that it even includes images. These images are not viewable when running pure python code. However, because I have deployed the project online, these images can be displayed via Streamlit. 

The most interesting thing is that the images are not hard coded.

They are refreshed constantly in the api to match the most up to date in-game image. 

For example, in the image below, here is the current

clan banner of 652 alliance: 


""")

st.image("scofield/Images/clan_banner1.png")

st.write("""

However, if it gets changed in game, the api will update it

nearly instantaneously, so the image in my code updates to reflect. 
 

""")

st.image("scofield/Images/clan_banner2.png")

st.write("""

The Supercell API is seriously advanced.  
 
""")
