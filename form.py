import streamlit as st
import csv
import os
import pandas as pd

st.title("Contact Info Collector")

# form
with st.form(key="my_form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    fav_number = st.number_input("Favourite Number", step=1, value=0)
    submitted = st.form_submit_button("Register")

# submit form
if submitted:
    if first_name and last_name: # check if they are not empty
        # to ensure there is title
        if not os.path.exists("contacts.csv"): # check if this file is established already
            # only if there isnt this file will has the below executed
            with open("contacts.csv", mode="w", newline="", encoding="utf-8") as file: # if not, then need to have title
                # "utf-8" supports all languages and emojis because perhaps users input chinese, etc
                writer = csv.writer(file) # store the crv.writer tool which specify for this file only
                writer.writerow(["First Name", "Last Name", "Favorite Number"]) # to write the headrow

        # if there is the file already, then the new user info will be appended to the file
        with open("contacts.csv", mode="a", newline="", encoding="utf-8") as file: # mode "a" = append
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, fav_number]) # to save the user input data
        
        st.success("Contact saved successfully!")
    else:
        st.error("First Name and Last Name cannot be empty")

# 顯示 CSV 內容
st.subheader("Saved Contacts") # show a small title
if os.path.exists("contacts.csv"): # to check if the file really exists
    df = pd.read_csv("contacts.csv") # use pandas to read the csv file
    st.dataframe(df) # then to show the form in the app
else:
    st.write("No contacts yet.")
