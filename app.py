from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/86383fc2-054b-493d-9e44-4b43250ab63d/np1Ryx6RcQ.json")
img_py = Image.open("images/thumbnail.png")
img_i = Image.open("images/thumbnail2.png")
img_ca = Image.open("images/thumbnail3.png")


# Header
st.subheader("Welcome to my webpage")
st.title("I use python, javascript and typescript!")
st.write("Wanna try python? Visit https://python.org")
st.markdown("[Visit My Github >](https://github.com/Prompt-bit)")

# Plans List
st.write("---")
left_column, right_column = st.columns(2)

with left_column:
    st.header("What do I do")
    st.subheader("What do I actually code?")
    st.write("- I code typescript stuff")
    st.write("- I use Python and VBScript")
    st.write("- I sometimes try C++")
    st.write("- I also sometimes try C and C#")
    st.write("Try it yourself!")


with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

# Projects

with st.container():
    st.write("---")
    st.header("My Videos")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_py)
    with text_column:
        st.title("Learn Python")
        st.write(
        """
        Learn how to code in python!
        Learn how to prompt the user!
        Even Learn how to print out something in the console!
        """
        )
        st.markdown("[Watch It >](https://www.youtube.com/watch?v=AywAs5krJAo&t=22s)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_i)
    with text_column:
        st.title("Learn how to install a IDE")
        st.write(
        """
        Learn how to install a IDE!
        Know what is python!
        Even Learn what python can do!
        """
        )
        st.markdown("[Watch It >](https://www.youtube.com/watch?v=d8RHdtKgoRU)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_ca)
    with text_column:
        st.title("Learn Canva")
        st.write(
        """
        Learn how to designa bookmark!
        Know what is canva!
        Even Learn how to add multiple pages to your design!
        """
        )
        st.markdown("[Watch It >](https://www.youtube.com/watch?v=AEOX3Q5wByI)")


# Contact

with st.container():
    st.write("---")
    st.header("Get In Touch with Me!")
    st.write("##")

contact_form = """
<form action="https://formsubmit.co/phawach4prompt@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Name" required>
     <input type="email" name="email" placeholder="Email" required>
     <textarea name="message" placeholder="Message" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
