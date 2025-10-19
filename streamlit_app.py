import streamlit as st
from datetime import date
import json
import pandas as pd
import numpy as np
st.header("LockerRoom")
st.write("Welcome to the Beta/Testing Version of LockerRoom! More stuff is coming soon!")
st.write("How are you feeling today?")
mood = st.slider(" ", 0, 10)

if mood == 9:
    st.write("That's great!! Continue to crush the day!!")
if mood == 5:
    st.write("I'm sorry to hear that. Keep on pushing forward, tomorrow is a new day.")
if mood == 0 or mood < 5:
    st.write("I'm sorry to hear that. Keep on pushing forward, tomorrow is a new day.")
if mood < 9 and mood > 5:
 st.write("I'm glad to hear it! Continue on that pace!")
if mood == 10:
 st.write("That's great!! Continue to crush the day!!")

# Initialize session state for journal entries
if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = []

# Chat/journal input
user_input = st.text_area("Write your journal entry here:")

# Add entry button
if st.button("Add Entry"):
    if user_input.strip():  # Only add non-empty input
        st.session_state.journal_entries.append(user_input.strip())
        st.success("Entry added!")
    else:
        st.warning("Please type something before adding.")

# Show all entries
if st.session_state.journal_entries:
    st.subheader("Your Journal Entries:")
    for i, entry in enumerate(st.session_state.journal_entries, start=1):
        day_label = f"Day {i}"":"
        st.write(day_label, entry)

    # Download button
    st.download_button(
        label="Download All Entries",
        data=json.dumps(st.session_state.journal_entries, indent=2),
        file_name="my_journal.json",
        mime="application/json"
    )

def file_uploaded():
    uploaded_file = st.file_uploader("Choose a file")
st.file_uploader("Add some photos to your journal here...", type=None, accept_multiple_files=True, key=None,
help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")


page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://cdn.wallpapersafari.com/88/75/cLUQqJ.jpg");
  background-size: cover;
}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)


def get_daily_message():
    today = date.today()
    messages = {
        date(2025, 10, 18): "\"If you can dream it, you can do it.\" — Walt Disney",
        date(2025, 10, 19): "\"I am not a product of my circumstances. I am a product of my decisions.\" — Stephen R. Covey ",
        date(2025, 10, 20): "\"Stay afraid, but do it anyway. What's important is the action. You don't have to wait to be confident. Just do it and eventually the confidence will follow.\" — Carrie Fisher ",
        date(2025, 10, 21): "\"The elevator to success is out of order. You'll have to use the stairs, one step at a time.\" — Joe Girard",
        date(2025, 10, 22): "\"If you look at how long the Earth has been here, we're living in the blink of an eye. So, whatever it is you want to do, you go out and do it.\" - Jamie Foxx"
    }
    # Return the message for today, or a default message if not found
    return messages.get(today, "Welcome to your daily dose of inspiration!")

st.header("Daily Quote")
daily_text = get_daily_message()
st.write(daily_text)

