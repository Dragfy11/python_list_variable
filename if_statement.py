# list

#my_list = ["Batgirl", "Batman", "Supergirl", "Superman", "Aquaman"]



#for superhero in my_list:
#     if superhero.lower() == "supergirl":
#         print("oui, tu as "+ superhero + " comme hero(ïne) dans ta liste")


# for superhero in my_list:
#     if superhero.lower() != "supergirl":
#         print("non, tu ne l'as pas dans ta liste")


# my_int = [2, 3, 4, 5, 3, 2, 4, 5]

# for num in my_int:
#     if num == 3:
#         num = num *10
#     print(num)

# for num in my_int:
#     if num != 3:
#         num = num *10
#     print(num)

# for num in my_int:
#     if num == 3:
#         num = num *10
#     elif num == 4:
#         num = num *100
#     else: 
#         num = num * 1000
#     print(num)

# user_input = input("Veuillez me donner un numbre entre 1 et 20 svp ?")

# number = 7

# if int(user_input) == 7:
#     print("Excellent, tu es bon !!!")

# elif number-5 <= int(user_input) <= number+5:
#     print("Tu es très proche du numbre")

# elif (number + 5 < int(user_input) <= 20) or (number -5 >int(user_input)> 0):
#     print("Tu es loin d'avoir trouvé")

# else:
#     print("erreur")


my_list = ["Batgirl", "Batman", "Supergirl", "Superman", "Aquaman"]

my_int = [2, 3, 4, 5, 3, 2, 4, 5]

# if "Robin" not in my_list:
#     my_list.append("Robin")

# for hero in my_list:
#     print(hero)

my_list1 = []

# for num in my_int:
#     num = num * 10
#     my_list1.append(num)

####### simplification #######

my_list1 = [x*10 for x in my_int]    

for num in my_list1:
    print(num)