# part 1 - If pattern
word = "glow" # str
continuous_tense = True # bool

# part 2
age = 5 # int
is_member = True # bool

# part 3

color_code = "R" # str: valid values are R-red, G-green and B-blue

time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

# <eoi>

# part 1 - basic if

new_word = word  #do not remove this line

    
# remove the "ing" suffix from `new_word` if it is there
if new_word.endswith("ing"):
    new_word=new_word[:-3]

# add the suffix "ing" to `new_word` if `continuous_tense` is True
if continuous_tense:
    new_word=new_word+"ing"
# write the whole if else block here
else: pass
# part 2 - If else pattern

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if age>=18:
    age_group="Adult"
else:
    age_group="Child"

# applicant_type:str should be age group with the member status like "Adult Member" or "Child Non-member"
# write the whole if else block
if is_member:
    applicant_type=age_group+" Member"
else:
    applicant_type=age_group+" Non-member"
# part 3 if ... elif .. else

# based on the value of `color_code` assign the `color` value in lower case and "black" if `color_code` is none of R, B and G

if color_code == "R":
    color = "red"
elif color_code == "G":
    color = "green"
elif color_code == "B":
    color = "blue"
else:
    color = "black"

is_time_valid = ... # bool: True if time is valid (should be ranging from 1 - 12 both including) else False 

# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
time_in_hrs = ...

# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range

# write your code here

h_str = time[:2]
period = time[3:]
h_int=int(h_str)
if period=="AM":
    if h_int==12:
        time_in_hrs=0
    else:
        time_in_hrs=h_int
else:
    time_in_hrs=h_int

# h_int= int(time[:2])
# period=time[3:]
# is_time_valid = (1 =< h_int =< 12)
# time_in_hrs= (h_int % 12) + (12 if period == "PM" else 0)