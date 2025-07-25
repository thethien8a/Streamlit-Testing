import datetime
from PIL import Image
from requests import codes
import streamlit as st
import pandas as pd
import numpy as np
# Lesson 2: make friends with dataframes, tables, and metrics
# table = ({
#     "Column 1": [1, 2, 3],
#     "Column 2": [4, 5, 6],
# })
# st.table(table)
# st.metric(label="Some Metric", value="42",
#           delta='5.7')
# st.markdown("That it's funny :joy: ")


# Lesson 3: Make friends with audio, video, and images
# st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png",
#          caption="Streamlit Logo")
# st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
#          start_time=20) #start time in seconds
# st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")


# Lesson 4: Make friends with widgets
# car = st.text_input("Type an car")
# car_type = ["Sedan", "SUV", "Truck", "Coupe", "Convertible"]
# def check_availability():
#     if st.session_state.my_car in car_type:
#         st.success(f"{st.session_state.my_car} is available!")
#     else:
#         st.error(f"Sorry, {st.session_state.my_car} is not available.")
# st.text_input("Type a car type", key="my_car")
# if st.button("Check"):
#     check_availability()


# Lesson 5: Make friends with turtle
# image_list = ["https://raw.githubusercontent.com/streamlit/demo-turtle/master/turtle.png",
#               "https://raw.githubusercontent.com/streamlit/demo-turtle/master/turtle2.png",
#               "https://raw.githubusercontent.com/streamlit/demo-turtle/master/turtle3.png"]
# caption_list = ["Turtle 1", "Turtle 2", "Turtle 3"]
# st.title('Turtle code')
# st.header('Turtle code')
# st.image(image=image_list, caption=caption_list, width=100)


#Lesson 6:
# image_list = [
#     "https://raw.githubusercontent.com/streamlit/demo-turtle/master/turtle.png",
#     "https://raw.githubusercontent.com/streamlit/demo-turtle/master/turtle2.png"
#     ]
# caption_list = ["Turtle 1", "Turtle 2"]
# st.header("Welcome to Turtle Code")
# checks = st.columns(2)
# with checks[0]:
#     images = st.checkbox("Do you want to see the images?")
# with checks[1]:
#     codes = st.checkbox("Do you want to see the code?")

# if codes:
#     st.code("print('Hello, Turtle!')")
# if images:
#     st.image(image=image_list, caption=caption_list, width=100)


# Lesson 7:
# st.header("Welcome to Turtle Code")
# toggle_video = st.toggle("Enable Video")
# if toggle_video:
#     st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")


# Lesson 8:
# st.header("Choose your Course")
# radio_button = st.radio("Choose a course", 
#                         ["Python", "Java", "JavaScript"],
#                         index=None)

# if radio_button == "Python":
#     st.write("You chose Python!")
# elif radio_button == "Java":
#     st.write("You chose Java!")
# elif radio_button == "JavaScript":
#     st.write("You chose JavaScript!")
# else:
#     st.write("Please choose a course from the list.")


# Lesson 9:
# st.header("Choose your Car")
# option = st.selectbox("Choose a car",
#                         ["Sedan", "SUV", "Truck", "Coupe", "Convertible"],
#                         index=None)
# st.write(option)


# Lesson 10:
# st.header("Choose 
# st.multiselect("Choose your favorite fruits",
#                 ["Apple", "Banana", "Cherry", "Date", "Elderberry"],


# Lesson 11:
# size = st.slider("Set image size",
#                  min_value=100,
#                  max_value=500
#                  )
# st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png",
#          caption="Streamlit Logo",
#          width=size)


# Lesson 12:
# st.header("Consumer Loan Calculator")
# loan_amount = st.select_slider(
#     "Amount",
#     options=[0,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
# )
# loan_maturity = st.select_slider(
#     "Month",
#     options=[6,12,18,24,30,36,42,48,54,60]
# )
# st.subheader("Interest Rate")
# st.text("%1")
# calculation = (())


# Lesson 13:
# name = st.text_input("What is your name ?")
# surname = st.text_input("What is your surname ?")
# if st.button("Submit"):
#     if name and surname:
#         st.success(f"Hello {name} {surname}!")
#     else:
#         st.error("Please enter both your name and surname.")


# Lesson 14:
# first_number = st.number_input("Enter the first number", value=0)
# second_number = st.number_input("Enter the second number", value=0)

# buttons = st.columns(4)
# with buttons[0]:
#     buttons_addition = st.button("Addition")
# with buttons[1]:
#     buttons_subtraction = st.button("Subtraction")
# with buttons[2]:
#     buttons_multiplication = st.button("Multiplication")
# with buttons[3]:
#     buttons_division = st.button("Division")

# if buttons_addition:
#     st.write(f"Result: {first_number + second_number}")
# elif buttons_subtraction:
#     st.write(f"Result: {first_number - second_number}")
# elif buttons_multiplication:
#     st.write(f"Result: {first_number * second_number}")
# elif buttons_division:
#     if second_number != 0:
#         st.write(f"Result: {first_number / second_number}")
#     else:
#         st.error("Cannot divide by zero.")
        

# Lesson 15:
# txt = st.text_area(
#     "Text to analyze",
#     placeholder="Type your text here",
# )
# analyze_button = st.button("Analyze") 


# Lesson 16:
# name = st.text_input("Name")
# company = st.text_input("Company")
# start_date = st.date_input("Starting Date",datetime.date(2023, 1, 1))
# end_date = st.date_input("Ending Date", datetime.date(2023, 12, 31))


# Lesson 17:
# uploaded_images = st.file_uploader("Choose an Image",
#                                    accept_multiple_files=True)
# for uploaded_image in uploaded_images:
#     if uploaded_image is not None:
#         image = Image.open(uploaded_image)
#         st.image(image, caption=uploaded_image.name)
#         st.write("Image Name:", uploaded_image.name)
#         st.write("Image Size:", uploaded_image.size, "bytes")
#         st.write("Image Type:", uploaded_image.type)


# Lesson 18:
# with st.form("my_form"):
#     name = st.text_input("Name")
#     surname = st.text_input("Surname")
#     age = st.slider("Age", 0, 100)
#     start_day = st.date_input("Starting Date")
    
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.write(f"Name: {name}")
#         st.write(f"Surname: {surname}")
#         st.write(f"Age: {age}")
#         st.write(f"Starting Date: {start_day}")
#     else:
#         st.write("Please fill out the form and submit.")
# st.write("Ouside of form")


# Lession 19:
# st.header("**Welcome to Streamlit**")
# st.video("https://youtu.be/rMLwiVrK3Fw")

# with st.sidebar:
#     add_selectbox = st.selectbox(
#         "How would you like to be contacted?",
#         ("Email", "Phone", "Social Media")
#     )
#     add_input = st.text_input("Enter your contact information")
    
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard", "Express", "Overnight")
#     )
    
#     send_button = st.button("Send")

# if send_button:
#    st.sidebar.success(f"Your contact information has been sent via {add_selectbox} to {add_input}.")


