# --- Define your functions below! ---
def hello():
    answer = input("Hi, I am Chatbot! What is your name?")
    say_hello(answer)
        #if answer == "hi":
            #print("hello")
        #else:
            #print("That's cool!")
def say_hello(name):
    print("Hi", name, "I know a lot about Seattle")

def food(blank):
    user_input = input("Would you like to learn about some good food here?(yes or no)")
    if user_input == "yes":
        print("You should try", blank)
        yes()
    if user_input == "no":
        activities()


def activities():
    user_input = input("What about activities? (yes or no)")
    if user_input == "yes":
        print("You should try the Space Needle")
        yes()
    if user_input == "no":
        yes()
def morefood():
    user_input= input("Do you like 'breakfast','lunch', or 'dinner'? (pick one)")
    if user_input == "breakfast":
        print("Try Portage Bay Cafe")
    if user_input == "lunch":
        print("Try the pizza place, Serious Pie")
    if user_input == "dinner":
        print("Try Din Tai Fung")
def morecolleges():
    user_input= input("Do you like 'smaller' or 'larger' schools? (pick one)")
    if user_input == "smaller":
        print("Take a look at Seattle University")
    if user_input == "larger":
        print("Take a look at UW")

#def validinput(user_input):
    #return True
#while not validinput(user_input):
    #morecolleges()

def yes():
    user_input = input("Pick a catergory: 'food' or 'activity' or 'colleges'")
    if user_input == "food":
        morefood()
    if user_input == "activity":
        print("Try the Ferris Wheel or Pike Place Market")
    if user_input == "colleges":
        morecolleges()
#def process_input():
# --- Put your main program below! ---
def main():
    answer=""
    user= "Pike Place Chowder"
    food(user)

    #while True:
    print("Thanks for talking to Chatbot!")

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  hello()
#  process_input()
  main()
