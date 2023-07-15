
def populationInTheWorld():
    x = 1.4       # population of China in billions
    y = 1.3       # population of India in billions
    z = 0.33      # population of America in billions
    q = 0.27      # population of Indonesia in billions
    g = 0.22      # population of Pakistan in billions
    w = 4.38      # population of other countries in billions
    print(x + y + z + q + g + w, 'billions')

populationInTheWorld() 




def DFBMP():           # Distribution of the World's five billionaires' money to the world's population
    q = 237700000000   # Bernard Arnault & family total money in billions $
    x = 172100000000   # Elon Musk's total money in billions $
    y = 127100000000   #Jeff Bezos's total money in billions $
    z = 118400000000   #Larry Ellison's total money in billions $
    f = 113100000000   # Bill Gates's total money in billions $
    P = 7900000000     # population in the worlds in billions $
    print((q + x + y + z + f )/P, "dollar per person in the world")
DFBMP()




def daysOfTheYear():
    x = 30        # Days of a month
    y = 12        # Months of a year
    z = 5         # Remaining days of 31-day months
    print(x * y + z, "Days per year")

daysOfTheYear()




def number_of_hours_in_a_year():
    x = 24      # numbers of housrs per full day
    y = 365     # Days of a year
    print(x * y," hours per year")

number_of_hours_in_a_year()



def workingdays(): # numbers of working days in 2023 in Tajikistan  
    x = 52         # Sundays
    y = 12         # holidays
    z = 6          # Eid days
    g = 365        # Days of a year
    print(g - (x + y + z), "days per year" )

workingdays()