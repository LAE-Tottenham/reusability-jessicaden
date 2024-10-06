import requests
from pyfiglet import Figlet
import os, time

# Help! I'm trying to make this cool bot but my code is too messy :( Please help me organise it into reusable components.

# Define your reusable functions here:
# Make sure each function only does ONE thing!!!!!!!!!!!
f = Figlet(font="slant")
print(f.renderText("HEY!"))
print("Welcome to the weird weather bot :)")
print("-----------------------------------\n")

def guess_gender(name):
    gender_resp = requests.get(f"https://api.genderize.io/?name={name}").json()
    gender = gender_resp["gender"]
    prob_percent = gender_resp["probability"] * 100
    return [gender, prob_percent]

def weird_weather_bot(postcode):
    postcode_resp = requests.get(f"https://api.postcodes.io/postcodes/{postcode}").json()

    area = postcode_resp['result']['admin_ward']
    longitude = postcode_resp['result']['longitude']
    latitude = postcode_resp['result']['latitude']
    return [area, longitude, latitude]

def catfactbot():
    joke_resp = requests.get("https://catfact.ninja/fact").json()
    joke = joke_resp['fact']
    return joke

def weather_results():
    weather_resp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=4d30afa58f6f935d861edecad3639cda").json()
    weather_kelvin = weather_resp["main"]["temp"]
    weather_degrees = int(weather_kelvin - 273.15)
    main_weather_desc = weather_resp["weather"][0]["main"]
    second_weather_desc = weather_resp["weather"][0]["description"]
    return [weather_degrees,main_weather_desc,second_weather_desc]

name = input("May I take your first name please? ")
gender_result = guess_gender(name)
gender = gender_result[0]
prob_percent = gender_result[1]
print(f"\nHmmm, I'm {prob_percent}% sure you are a {gender}.")

gender_correct = input("Am I right? :) (Y/n)")
if gender_correct.lower() in ["", "yes", "y", "ye"]:
    print("Wooooooh! Computer 1, Human 0.")
else:
    print("Ahhhh, sorry! :(")
###########################################
postcode=input("\nSo, what's your postcode? ")
post=weird_weather_bot(postcode)
area=post[0]
latitude=post[1]
longitude=post[2]
print(f"Nice! so you live in",area+".\n")

print("Let me just check the weather there today...\n")
    
for i in range(3):
    time.sleep(1)
    print("...")
###########################################
input("\nWould you like a cat fact while you wait? ")
print("Doesn't matter what you think, I'm going to give you one anyway :)")
time.sleep(3)
print("\n###########################")
print("CAT FACT:")
jokeres=catfactbot()
print("\n"+jokeres,"\n")
print("So interesting isn't it!")
print("###########################")

print("\nWaiting 5 seconds for you to read the fact...")
time.sleep(5)
print("\nNow, back to getting the weather...")

for i in range(3):
    time.sleep(1)
    print("...")


res=weather_results()
degs=res[0]
main=res[1]
second=res[2]
print(f"\nThe weather in",area,":\n")
print(str(degs) + "℃")
print(f"{main} - {second}")
print("\nThank you! Bye.")

# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break?
# - the name has to only be letters, degrees have to be an integer, postcode input has to be an actual postcode
# 2. Validate the user's input based on your preconditions.
# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
# - to make the code cleaner and easier to understand for which part of the code is being ran for each function, such as the first function being for gender guessing

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. Make sure all of your functions (except the main one) only do ONE thing or process.
# 3. Add your own twist to the code.

# Extension:
# Add the following apis as reusable components and use them in your code:
# https://www.exchangerate-api.com/docs/overview
