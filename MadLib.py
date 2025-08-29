#MadLib.py
#Name:Bennett Schulte
#Date:
#Assignment:MadLib

def main():
  print("Madlib")
  #Ask user for words
verb1 = input("Enter a verb: ")
verb2 = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter an adjective: ")


  #Print the story with the user supplied words.

print(f"The {adjective1} {noun1} wanted to {verb1} quickly. Then the {adjective2} {noun2} began to {verb2} suddenly.")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
