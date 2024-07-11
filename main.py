#CyHelp Starter Code
cybersecurityBirthYear = 1970

#Greets user
print("\t\t\t\t\t\tHello! I'm CyHelp.\n")
userName = input("What is your name?:  ")
print("\t\t\t\t\t\tNice to meet you " + userName +"!\n")

#Recounts start of Cybersecurity
todaysYear = input("What year is it?:  ")
int(todaysYear)
timePassed = int(todaysYear) - cybersecurityBirthYear
print("\n"+"#"*70)
print("\nWow! That means it has been " + str(timePassed) +" years since Cybersecurity began!")
print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")
input("Press enter to continue.\n")

#Describes Cybersecurity
print("Cybersecurity refers to the practices that people use to protect computer system and networks from digital threats.")
print("These people can be government, nations, companies, community, organizations, and individuals. \n")

#Introduces CIA Triad
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for confidentiality, integrity, and availability.")
print("Would you like to learn about the CIA Triad?")
giveInfo = input("\n\t\t\t\t\t\tType 'yes' or 'no'\n--")
print("\n"+"#"*70+"\n")
    

#Explains pillars of CIA Triad
while giveInfo.lower() != "no":
  if giveInfo.lower() == "yes":
    print("What would you like to learn more about? Enter the lowercase letter of the following options:\n\n (a)confidentiality, (b) integrity, (c) availability, or (d) none.")
    topic = input("\n--")
    
    if topic.lower() == "a":
      print("Confidentiality makes sure data is private.\n")
    elif topic.lower() == "b":
      print("Intergrity makes sure data has not been tampered with and can be trusted.\n")
    elif topic.lower() == "c":
      print("Availability makes sure authorized people can access the data.\n")
    elif topic.lower() == "d":
      print("Okay!\n")
      break
    else:
      print("Sorry, I didn't catch that. Choose one of the options listed.")
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
    giveInfo = input("\n\t\t\t\t\t\tType 'yes' or 'no'\n--")
    print("\n"+"#"*70+"\n")

  

#Chatbot ends conversation
print("\n"+"#"*70+"\n")
print("Thanks for chatting with me, and I hope you learned something new!")