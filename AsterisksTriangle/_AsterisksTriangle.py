#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    user_input = input("Enter a number (or press Enter to exit): ")
    
    if user_input == "":
        break  # Exit the loop if the user enters a blank line
    
    try:
        n = int(user_input)  # Convert the input to an integer
        if n > 0:
            for i in range(1, n + 1):
                print("*" * i)  # Print the asterisks in increasing order
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

