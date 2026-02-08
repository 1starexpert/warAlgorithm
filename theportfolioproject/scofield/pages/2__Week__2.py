import streamlit as st

st.header("Week 2: ")

st.write("""

I have found a way to host my project online without the use of a virtual machine.
I found an online proxy that will give me a fixed ip so that I can circumvent
Supercell's IP lock on their API.

This will me to access my project from anywhere without creating a new api key
each time as well as allow others to access my project should I decide to share it.

Thanks to this, my project has now gotten a much cleaner user interface as well.

We have gone from this:

[insert picture here]

""")
st.image("scofield/Images/UI_one.png")
st.write("To this:")

st.write("[insert picture here]")

st.image("scofield/Images/UI_second.png")
st.write("""

Of course, everything is still a bit bare bones at this stage, but it is all a
work in progree. Aside from that, I am learning first hand the many basic ideas
of software engineering. Creating front ends, back ends. git repositories, working
API's, etc. It is all a bit overwhelming if I am being honest.

Aside from figuring out code logic, figuring out file structures for code and how
it interacts with other code files can get out of hand quickly.
""")
