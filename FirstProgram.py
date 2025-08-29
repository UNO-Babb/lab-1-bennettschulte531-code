#FirstProgram.py
#Name:Bennett Schulte
#Date:8/26/25
#Assignment:Lab 1

def main():
  print("First Program")
  #Say hello
  print("hello")
  #Ask for the user's name
username = input("What is your name?")
  #Use the user's name in the program.
print("Nice to meet you",(username)+"!")
  #Ask the user for their age.
user_age = int(input("How old are you?"))
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
current_year = 2025
birth_year = current_year - user_age
print("You were born in" , (birth_year))
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
