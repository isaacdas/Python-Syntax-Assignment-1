# Task 1

weather = "sunny"
if weather == "sunny":
    print("Wear Sunglasses") #wrong indentation
else:
    print("Take an umbrella") #wrong indentation


#Task 2

user_feel = "Are you feeling happy or sad"
print(user_feel)
user_input = input()
if "app" in user_input: #allows for capital
    print("That's great to hear!")
elif "ad" in user_input: #(sad, mad, bad)
    print("I hope your day gets better")
else:
    print("Please narrow it down to either 'happy' or 'sad' please") #reasks user if foreign input
    user_input = input() 
    if "app" in user_input:
        print("That's great to hear!")
    elif "ad" in user_input:
        print("I hope your day gets better")
    else:
        print("hmm, I don't seem to understand. end of program") #termination message
