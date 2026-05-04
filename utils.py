# This function ensures the user enters a valid number
def get_valid_number(prompt):
   # Keep asking until user enters a valid integer
   while True:
       try:
           return int(input(prompt))  # Convert input to integer
       except ValueError:
           # If conversion fails, user didn't enter a number
           print("❌ Please enter a valid number.")
