try:
    marks = int(input("Enter your marks: "))
    marks2 = marks/0
    print("With bonus:", marks2)
except ZeroDivisionError as e:
    print("DONT DIVIDE BY ZERO")
    print(e.)
    print(f"Exception Type: {type(e).__name__}")
#except ValueError:
#    print("Only Numbers are supported")
#finally:
#print("*************** Sorry an exception occured, try again")


'''
except Exception as e:
    # Fallback for any other unexpected exception
    #print(f"An unexpected error occurred: {e}")
    print ("I dont know how to handle your input")
'''

# multiple exceptions