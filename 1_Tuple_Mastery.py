# Task 1

passengers = [('Alice', 'New York', 'London'), ("Bob", 'Tokyo', 'San Francisco'), ('Tim', 'Denver', 'Orlando')]
# passengers = ("Alice", "Denver", 'Tokyo')

#  Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should loop through the list of itineraries and print a formatted string for each.


def loop(passengers):    
        number = 1                                                                      #Needed to add the itinerary number
        for data in passengers:                                                         #for all tuples in the list 
            print(f'Itinerary {number}: ', data[0],'- From', data[1], 'to', data[2])     #call upon each tuple by index

            number += 1                                                                 # Adding an number to each statement after the next one

loop(passengers)


