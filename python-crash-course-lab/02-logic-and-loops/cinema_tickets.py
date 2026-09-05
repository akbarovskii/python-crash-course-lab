cinema = '\nEnter "404" to finish purchasing tickets.'
cinema += "\nHello, please enter your age and we will find the ticket price for you: "

while True:
     
     age = int(input(cinema))

     if age < 3:
         print("Here is your free ticket!")
     elif age < 12:
         print("Here is your ticket for $10!")
     elif age < 18:
         print("Here is your ticket for $15!")
     elif age <= 150:
         print("Here is your ticket for $20!")

     if age == 404:
          break
