import streamlit as st
import requests

# Function to fetch a random quote from the API


def get_quote():
    url = "http://api.forismatic.com/api/1.0/"
    params = {
        "method": "getQuote",
        "format": "json",
        "lang": "en"
    }
    response = requests.post(url, data=params)  # Use POST instead of GET
    data = response.json()
    return data["quoteText"], data.get("quoteAuthor", "Unknown")

# App layout
st.title("Quote of the Day")

try:
    # Fetch a random quote
    quote, author = get_quote()

    # Display the quote
    st.success(f"\"{quote}\"")
    st.write(f"- {author}")

except Exception as e:
    st.error("No quotes today. Please try again later.")

# Display app version
st.write("App version: v0.1")