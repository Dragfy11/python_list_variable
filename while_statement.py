counter = 0

# while counter < 10:
#     print(counter)
#     counter+=1
### le counter au dessu du if le renvoi jusque 10 sans prendre le 0 mais si on le met en dessou du print il prend en compte le 0 et y va jusque 8
# while counter <10:
#     if counter % 2 ==0:
#         print(counter)
#     counter +=1

###### jeu

# while True:

#     user_input = input("Veuillez me donner un numbre entre 1 et 20 svp ? (appuyez sur la touche 'y' pour quitter):" )

#     number = 7

#     if user_input == 'y':
#         break

#     if int(user_input) == 7:
#         print("Excellent, tu es bon !!!")

#     elif number-5 <= int(user_input) <= number+5:
#         print("Tu es très proche du numbre")

#     elif (number + 5 < int(user_input) <= 20) or (number -5 >int(user_input)> 0):
#         print("Tu es loin d'avoir trouvé")

#     else:
#         print("erreur")


student = {}

active = True

while active:
    userinput = input("Quel est le nom de l'étudiant:  ")
    course = input("Dans quel cours est-il inscrit:  ")
    student[userinput] = course

    exit_continue = input("Appuyez sur y pour continuer svp ")
    if str(exit_continue) != "y":
        active= False
        # break
print("\n {}\t \t \t\t \t{:<20}".format("Student","Course"))
for sname, scourse in student.items():
    # print("{:<20} \t {:<20}".format(sname, scourse))
    print(str(sname + " \t\t\t\t" + str(scourse)))