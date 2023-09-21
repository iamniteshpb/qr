import streamlit as st
import random
import datetime
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

st.title("ID CARD Generator with QR Code")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("%d-%m-%Y  ID CARD Generator  %I:%M:%S %p")

st.write(reg_format_date)

company = st.text_input('Enter Your Company Name:')
name = st.text_input('Enter Your Full Name:')
gender = st.text_input('Enter Your Gender:')
age = st.number_input('Enter Your Age:', min_value=0, value=0)
dob = st.date_input('Enter Your Date Of Birth:')
blood_group = st.text_input('Enter Your Blood Group:')
No = st.text_input('Enter Your Mobile Number:')
address = st.text_input('Enter Your Address:')

if st.button('Generate ID Card'):
    image = Image.new('RGB', (1000, 900), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('arial.ttf', size=45)

    os.system("Title: ID CARD Generator with QR Code by Rohan Kasabe")

    (x, y) = (50, 50)
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=80)
    draw.text((x, y), company, fill=color, font=font)

    (x, y) = (600, 75)
    idno = random.randint(10000000, 90000000)
    message = str('ID: ' + str(idno))
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=60)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (50, 250)
    fname = str('Name: ' + str(name))
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), fname, fill=color, font=font)

    (x, y) = (50, 350)
    fgender = str('Gender: ' + str(gender))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), fgender, fill=color, font=font)

    (x, y) = (400, 350)
    fage = str('Age: ' + str(age))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), fage, fill=color, font=font)

    (x, y) = (50, 450)
    fdob = str('Date of Birth: ' + str(dob))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), fdob, fill=color, font=font)

    (x, y) = (50, 550)
    flood_group = str('Blood Group: ' + str(blood_group))
    color = 'rgb(255, 0, 0)'  # black color
    draw.text((x, y), flood_group, fill=color, font=font)

    (x, y) = (50, 650)
    fNo = str('Mobile Number: ' + str(No))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), fNo, fill=color, font=font)

    (x, y) = (50, 750)
    faddress = str('Address: ' + str(address))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), faddress, fill=color, font=font)

    image.save(f'{name}.png')

    QR = qrcode.make(f'{company}\n{name}\n{idno}')
    QR.save(f'{idno}.bmp')

    ID = Image.open(f'{name}.png')
    QR = Image.open(f'{idno}.bmp')
    ID.paste(QR, (650, 350))

    ID.save(f'{name}.png')

    st.image(f'{name}.png')
