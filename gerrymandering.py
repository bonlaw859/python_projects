# Building Python Programs
# Programming Project Chapter 6 Gerrymandering

# This program prompts the user for a state name and then outputs a chart 
# displaying the population of democrats and republicans in each district in 
# the state and whether or not that district is gerrymandered. If the user
# types in a state name that doesn't exist the program outputs a not found 
# message.

from turtle import *
from Lab5_functions import *

WIDTH = 500
HEIGHT = 500

def main():

    setworldcoordinates(0, HEIGHT, WIDTH, 0)
    clear()
    shape('turtle')
    pencolor('olive drab')
    fillcolor('sienna')
    bgcolor('grey')

    print_intro_message()
    state_name = input("Which state do you want to look up? ")
    details = get_state_details('districts.txt', state_name)
#   if the state name is not in districts.txt, end the program. 
    if details == None:
        return
    dem_votes, rep_votes, dem_list, rep_list = process_state_details(details)
    dem_waste, rep_waste = calculate_wastage(dem_list, rep_list)
    is_gerrymandered(dem_waste, rep_waste)
    eligible_voters = find_eligible_voters(state_name, 'eligible_voters.txt')
    draw_intro_graphics(state_name, eligible_voters)
    draw_district_graphics(dem_list, rep_list, WIDTH)
    
    
# function to output the introduction message to console.
def print_intro_message():
    print("This program allows you to search through")
    print("data about congressional voting districts")
    print("and determine whether a particular state is")
    print("gerrymandered.")
    print()


# function to check whether state exists or not
# if exits, returns the state details line
def get_state_details(file_name, state_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            data=line.split(",")
            if data[0].lower()== state_name.lower():
                return data
            
    print(f"\"{state_name}\" not found.")
    return None


# function to process the state details in the format:
# <state>,<district1>,<dem votes>,<gop votes>,<district2>,<dem votes>,<gop votes>,...
# calculate and return total dem and gop votes
# also prints the district graphics to the panel        
def process_state_details(details):
    data = details[1:]
    x = 1
    dem_votes = 0
    rep_votes = 0
    dem_list = []
    rep_list = []
    for item in data:
        if x == 2:
            item = int(item)
            dem_votes = dem_votes + item
            dem_list.append(item)
        if x == 3:
            item = int(item)
            rep_votes = rep_votes + item
            rep_list.append(item)
        x = x+1
        if x ==4:
            x = 1
    return dem_votes, rep_votes, dem_list, rep_list

# takes the total number of dem votes and total number of gop
# votes as parameters and calculates and returns the
# total wasted dem votes and total wasted gop votes
def calculate_wastage(dem_list, rep_list):
    from math import floor

    dem_waste = 0
    rep_waste = 0
    
    for district in range(len(dem_list)):
        half = floor((dem_list[district] + rep_list[district]) / 2)
        if dem_list[district] <= half:
            dem_waste += dem_list[district]
        if dem_list[district] > half:
            dem_waste += dem_list[district] - (half + 1)

    for district in range(len(rep_list)):
        half = floor((dem_list[district] + rep_list[district]) / 2)
        if rep_list[district] <= half:
            rep_waste += rep_list[district]
        if rep_list[district] > half:
            rep_waste += rep_list[district] - (half + 1)

    print(f"Total Wasted Democratic votes: {dem_waste}")
    print(f"Total Wasted Republican votes: {rep_waste}")

    return dem_waste, rep_waste
            

# function to check whether the votes are gerrymandered or not
# and prints out a message if the state is gerrymandered.
# If it is, prints out who has gerrymandered it
def is_gerrymandered(dem_waste, rep_waste):
    dif = abs(dem_waste - rep_waste)
    total = dem_waste + rep_waste
    if total * .07 <= dif:
        if dem_waste < rep_waste:
            print("Gerrymandered benefiting the Democrats")
        else:
            print("Gerrymandered benefiting the Republicans")


#function that finds the number of eligible voters in a state given
#state name and file name, returns and prints that number.
def find_eligible_voters(state_name, file_name):
    with open(file_name) as file:
        lines = file.readlines()
        eligible_voters = 0
        for line in lines:
            data=line.split(",")
            if data[0].lower()== state_name.lower():
                eligible_voters = int(data[1])
    print(f"{eligible_voters} eligible voters")
    return eligible_voters


# function to print state name, eligible voters and 
# horizontal and vertical lines to panel    
def draw_intro_graphics(state_name, eligible_voters):
    bgcolor('white')
    draw_line(WIDTH/2,0, WIDTH/2, HEIGHT, 'black')
    draw_line(0,20, WIDTH, 20, 'black')
    
    state = state_name.lower()
    state = state.capitalize()
    up()
    goto(0,10)
    color('black')
    write(state)
    
    up()
    goto(WIDTH-120,10)
    write(f"{eligible_voters} eligible voters")
 

# function which caluculate the width of dem_votes and gop_votes
# and print the rectangles to the panel using the y_index as starting point
def draw_district_graphics(dem_list, rep_list, WIDTH):
    for district in range(len(dem_list)):
        dem_rect = dem_list[district]/(dem_list[district] + rep_list[district]) * WIDTH
        draw_rect(0, (district+1)*25, dem_rect, 20, 'blue')

        rep_rect = rep_list[district]/(rep_list[district] + dem_list[district]) * WIDTH
        draw_rect(WIDTH - rep_rect, (district+1)*25, rep_rect, 20, 'red')

    hideturtle()

    ##########################################
       
main()
