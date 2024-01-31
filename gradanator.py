# Building Python Programs.
# Programming Assignment Chapter 4 Gradanator Template.
#
# Calculates a student's course grade based on exam and homework scores.

ATTENDANCE_PTS = 3 # Points earned per section.
SECTION_MAX = 34 # Maximum possible section points.

# Define main.
def main():

    # List functions in order from exams, homework, quizzes, daily homework, and reported grade.
    print_intro()
    midterm_score = get_exam_score("Midterm 1")
    midterm_score2 = get_exam_score("Midterm 2")
    final_score = get_exam_score("Final")
    hw_score = get_homework_score()
    quizzes = get_weight_score("Quizzes")
    daily_hw = get_weight_score("Daily homework")
    report_grade(midterm_score + midterm_score2 + final_score +
                 hw_score + quizzes + daily_hw)


# Prints information about the program's behavior.
def print_intro():

    # Print introduction statement.
    print("This program reads exam/homework scores")
    print("and reports your overall course grade.")
    print()

# Prompts for exam score and shift.  Returns a weighted
# score.
def get_exam_score(exam):
    
    # Print exam name.
    print(exam + ":")
    
    # Input weight from 0 to 100.   
    weight=int(input("Weight (0-100)? "))

    # Input score.         
    score=float(input("Score earned? "))

    # Input shift choices.
    shift=int(input("Were scores shifted (1=yes, 2=no)? "))

    # Integrate shift amount into score, if selected "1".
    if shift==1:
        shift_amt=int(input("Shift amount? "))
        
    if shift==1:
        score=int(shift_amt+score)

    # If score is above 100, set the score to 100.    
    if score>100:
        score=int(100)
        
    # Print total points out of 100.        
    print("Total points = " + str(int(score)) + " / 100")

    # Set weighted score formula.
    weighted_score=round2(score*(weight/100),1)
    
    # Print weighted score out of weight.    
    print("Weighted score = " + str(weighted_score) + " / " + str(weight))

    # Print blank line.    
    print()

    # Return weighted score to determine grade
    return get_weighted_score(score, 100, weight)

# Prompts for homework scores and section attendance. Calculates and returns
# weighted homework score.
def get_homework_score():

    # Print homework name.
    print("Homework:")

    # Input weight from 0 -100.
    weight=int(input("Weight (0-100)? "))

    # Input homework count.
    hw_count=int(input("Number of assignments? "))

    #Create lists for homework earned and total points.
    hw_earned=[]
    hw_total=[]

    # Create for loop that ranges from the homework count given.
    for hw in range(1,hw_count+1):

        # Input score.
        score=int(input("Assignment " + str(hw) + " score? "))

        # Input max score.
        max_score=int(input("Assignment " + str(hw) + " max? "))

        # Integrate the score and max score into the lists.
        hw_earned.append(score)
        hw_total.append(max_score)

    # Add all the numbers within the list.
    hw_earned=int(sum(hw_earned))
    hw_total=int(sum(hw_total))

    # Input sections attended.
    sections=int(input("How many sections did you attend? "))

    # Set section points formula.
    section_points=sections*ATTENDANCE_PTS

    # If sections points is greater than section max, then set it equal to section max.
    if section_points>SECTION_MAX:
        section_points=SECTION_MAX

    # Set max and total points.
    max_points=hw_total+SECTION_MAX
    total_points=hw_earned+section_points

    # If total points is greater than the max points, then set it equal to max points.
    if total_points>max_points:
        total_points=max_points

    # Print section points out of section max.
    print("Section points = " + str(int(section_points)) + " / 34")

    # Print total points out of the max points.
    print("Total points = " + str(int(total_points)) + " / " + str(int(max_points)))

    # Set weighted score formula.
    weighted_score=round2((total_points)*(weight/(max_points)),1)

    # Print weighted score out of weight.
    print("Weighted score = " + str(weighted_score) + " / " + str(weight))
    
    # Print blank line.
    print()

    # Return weighted score to determine grade.

    return get_weighted_score(total_points, max_points, weight)

# Calculates, prints and returns the weighted score for a category.
def get_weighted_score(earned, total, weight):

    # Create weight score list to help determine grade.
    weight_score=[]

    #Set weighted to determine weighted score from all functions.
    weighted=round2(earned*(weight/total),1)

    # Add weighted into weight score list.
    weight_score.append(weighted)

    # Return list to help determine grade.
    return weight_score


# Reports a minimum guaranteed GPA and a message about the total score earned.
def report_grade(weight_score):

    # Add all values inside weight score to find grade.
    overall_grade=round2(sum(weight_score),1)

    #Print overall grade percentage.
    print("Overall percentage = " , overall_grade)

    # Create if statements to determine letter grade from percentage.
    if overall_grade>=90:
        grade="A"
    elif overall_grade>=80:
        grade="B"
    elif overall_grade>=70:
        grade="C"
    elif overall_grade>=60:
        grade="D"
    else:
        grade="F"

    # Print text of the person's grade.
    print("Your grade will be at least: " + grade)

    # Create if statements to get messages determined by letter grade.
    if grade=="A":
        print("GG EZ grade do so good")
    elif grade=="B":
        print("Good job! You did ok!")
    elif grade=="C":
        print("Just to get the credit right?")
    elif grade=="D":
        print("Dang, almost made it.")
    else:
        print("You should maybe change majors....")

# Rounds a value to a given number of digits.
def round2(value, digits):
    return round(value * pow(10, digits)) / pow(10, digits);

# Calculates, prints and returns the weighted score for a category.
def get_weight_score(item):

    # Print item name.
    print(item + ":")

    # Input weight from 0 - 100.
    weight=int(input("Weight (0-100)? "))

    # Input points.
    points=int(input("Total points earned? "))
    
    # Input possible points.
    points_possible=int(input("Total points possible? "))

    # If points is greater than possible points, then set it equal to possible points.
    if points>points_possible:
        points=points_possible

    # Print total points out of possible points.
    print("Total points = " + str(points)+ " / " + str(points_possible))

    # Set weight score to help determine grade.
    weight_score=round2(points*(weight/points_possible),1)
    
    # Print weighted score out of weight.
    print("Weighted score = " + str(weight_score) + "/" + str(weight))
    
    # Print blank line.
    print()

    # Return weighted score to determine grade

    return get_weighted_score(min(points, points_possible), points_possible, weight)

# Call main function to run.
main()
