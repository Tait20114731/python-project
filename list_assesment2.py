# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:34:20 2024

@author: Tatenda Marimo 20114731
@description:The code allows users to create, add, delete, sort, and search 
within lists categorized as Actors, Movies, or Games.
@version: 1.0
"""

# Establishing lists for each category.
Actors = []
Movies = []
Games = []

# Function to add a value to a list.
def add_value(list_type, value):
    list_type.append(value)
    return list_type

# Function to delete a value from a list.
def delete_value(list_type, value):
    if value in list_type:
        list_type.remove(value)
    else:
        print("Value does not exist")
    return list_type

# Function to sort a list in ascending and descending order.
def sort_value(list_type, sort_order='ascending'):
    if sort_order == 'ascending':
        list_type.sort()
    elif sort_order == 'descending':
        list_type.sort(reverse=True)
    else:
        raise ValueError("Order must be either 'ascending' or 'descending'")
    return list_type

# Function to list values
def list_values():
    values = []
    for i in range(12):
        value = input("Please enter value " + str(i+1) + ": ")
        values.append(value)
    return values

# Function to perform binary search
def binary_search(sequence, item):
    sequence.sort()  # Ensure the list is sorted
    begin_index = 0
    end_index = len(sequence) - 1
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

# Main program loop, prompts users to choose a category of choice and edit the list.
def main():
    while True:
        # Ask the user to select a category
        category_type = input("Please select the category of your choice (Actors, Movies, or Games) or type 'End' to stop program: ").strip().lower()
    
        # End the program if the user types 'end'
        if category_type == 'end':
            print("Program has ended")
            break
        elif category_type == 'actors':
            actors_list = list_values()
            print("Actors list:", actors_list)
            selected_list = actors_list
        elif category_type == 'movies':
                movies_list = list_values()
                print("Movies list:", movies_list)
                selected_list = movies_list
        elif category_type == 'games':
            games_list = list_values()
            print("Games list:", games_list)
            selected_list = games_list
        else:
            print("Invalid input. Please choose from Actors, Movies, or Games.")
            continue

        # Inner loop for modifying the selected list
        while True:
            # Ask the user to select a function type to edit the list
            instruction_type = input("Please select function type to edit the list (Add, Delete, Search, or Sort). Type 'END' to stop: ").strip().lower()
        
            # End the program if the user types 'end'
            if instruction_type == 'end':
                print("Program has ended")
                break
            elif instruction_type == 'add':
                value = input("Please Enter Value: ")
                selected_list = add_value(selected_list, value)
                print("Updated list:", selected_list)
            elif instruction_type == 'delete':
                value = input("Please Enter Value: ")
                selected_list = delete_value(selected_list, value)
                print("Updated list:", selected_list)
            elif instruction_type == 'search':
                value = input("Please enter Search value: ")
                result = binary_search(selected_list, value)
                if result is not None:
                  print("Your search item is at index:", result)
                else:
                  print("Item not found")
            elif instruction_type == 'sort':
                sort_order = input("Please enter sorting order ('Ascending' or 'Descending'): ").strip().lower()
                if sort_order == 'ascending' or sort_order == 'descending':
                    selected_list = sort_value(selected_list, sort_order)
                    print("Sorted list:", selected_list)
                else:
                    print("Invalid sorting order. Please enter 'Ascending' or 'Descending'.")
            else:
                print("Invalid function type. Please choose from Add, Delete, Search, or Sort.")
            
#for unit testing       
if __name__ == '__main__':
    main() 

