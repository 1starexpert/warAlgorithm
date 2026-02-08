import streamlit as st

st.header("Week 1:")

st.subheader("Miracle??!")

st.write("""

I didn’t forget about this project after Day 1 like I did with myLeetCode account.

Honestly, that alone feels like progress.

""")

st.subheader("Lessons Learned")

st.write("""

This week I learned a lot about the Clash of Clans API. It’s surprisingly professional-grade, and the sheer amount of data available is
overwhelming at first. Because of that, I decided to start small by building a simple clan lookup tool to help me understand how the API is structured.
I also ran into my first real deployment problem. The API requires you to whitelist specific IP addresses that are allowed to call the API. Unfortunately,
Streamlit deployments use dynamic IPs, which means the app will crash as soon as the IP changes. This is something they definitely never mentioned in Intro to
Python at Georgia Tech.
After doing some research, the only real workaround I found involves running the app on a virtual machine with a static IP—something like Fly.io or Oracle Cloud. The problem is that these solutions aren’t free, and I’m trying to keep this project cost-free.
So for now, it looks like I won’t be able to deploy this project publicly. 😭
The best I can do is upload the source code and let people download and run it locally.
Until next time,
—JT
""")

st.image("scofield/Images/secondPicture.jpg", width = 200)

