# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:27:51 2024

@author: Tatenda Marimo 20114731
@description:The code allows users to create, add, delete, sort, and search 
within dictionary categorized as Actors, Movies, or Games.
@version: 1.0

"""

# Establishing dictionaries for each category.
Actors = {}
Movies = {}
Games = {}

# Function to add a value to a dictionary.
def add_value(dictionary, key, value):
    dictionary[key] = value
    return dictionary

# Function to delete a value from a dictionary.
def delete_value(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    else:
        print("Key does not exist")
    return dictionary

# Function to sort a dictionary by keys.
def sort_dict(dictionary, sort_order='ascending'):
    if sort_order == 'ascending':
        sorted_dict = dict(sorted(dictionary.items()))
    elif sort_order == 'descending':
        sorted_dict = dict(sorted(dictionary.items(), reverse=True))
    else:
        raise ValueError("Order must be either 'ascending' or 'descending'")
    return sorted_dict

# Function to list values in the dictionary.
def list_values(category):
    values = {}
    for i in range(12):
        key = input("Please enter " + category[:-1] + "'s name " + str(i+1) + ": ")
        value = input("Please enter additional information for " + key + ": ")
        values[key] = value
    return values

# Function to perform binary search in a dictionary.
def binary_search_dict(dictionary, key):
    keys = sorted(dictionary.keys())
    begin_index = 0
    end_index = len(keys) - 1
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_key = keys[midpoint]
        if midpoint_key == key:
            return midpoint_key, dictionary[midpoint_key]
        elif key < midpoint_key:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

# Main program loop, prompts users to choose a category and edit the dictionary.
def main():
    while True:
        # Ask the user to select a category.
        category_type = input("Please select the category of your choice (Actors, Movies, or Games) or type 'End' to stop the program: ").strip().lower()
        
        # End the program if the user types 'end'.
        if category_type == 'end':
            print("Program has ended")
            break
        elif category_type in ['actors', 'movies', 'games']:
            # Initialize or retrieve the selected dictionary.
            if category_type == 'actors':
                selected_dict = Actors
            elif category_type == 'movies':
                selected_dict = Movies
            elif category_type == 'games':
                selected_dict = Games
            else:
                print("Invalid category. Please choose from Actors, Movies, or Games.")
                continue
            
            # Populate the selected dictionary.
            selected_dict = list_values(category_type)
            print(category_type + " dictionary:", selected_dict)
        else:
            print("Invalid input. Please choose from Actors, Movies, or Games.")
            continue

        # Inner loop for modifying the selected dictionary.
        while True:
            # Ask the user to select a function to edit the dictionary.
            instruction_type = input("Please select function type to edit the dictionary (Add, Delete, Search, or Sort). Type 'End' to stop: ").strip().lower()
            
            # End the inner loop if the user types 'end'.
            if instruction_type == 'end':
                print("Exiting to category selection...")
                break
            elif instruction_type == 'add':
                key = input("Please enter " + category_type[:-1] + "'s name: ")
                value = input("Please enter additional information for " + key + ": ")
                selected_dict = add_value(selected_dict, key, value)
                print("Updated dictionary:", selected_dict)
            elif instruction_type == 'delete':
                key = input("Please enter " + category_type[:-1] + "'s name to delete: ")
                selected_dict = delete_value(selected_dict, key)
                print("Updated dictionary:", selected_dict)
            elif instruction_type == 'search':
                key = input("Please enter " + category_type[:-1] + "'s name to search: ")
                result = binary_search_dict(selected_dict, key)
                if result is not None:
                    print("Your search item: " + result[0] + " - " + result[1])
                else:
                    print("Item not found.")
            elif instruction_type == 'sort':
                sort_order = input("Please enter sorting order ('Ascending' or 'Descending'): ").strip().lower()
                if sort_order in ['ascending', 'descending']:
                    selected_dict = sort_dict(selected_dict, sort_order)
                    print("Sorted dictionary:", selected_dict)
                else:
                    print("Invalid sorting order. Please enter 'Ascending' or 'Descending'.")
            else:
                print("Invalid function type. Please choose from Add, Delete, Search, or Sort.")
            
#for unit testing       
if __name__ == '__main__':
    main() 
