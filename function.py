# def print_message(name, language):
#     print("Hi, my name is " + name + " and my favorite programming language is " + language)


# print_message("Kadir", "Python")

#####################
#### 1ère façon #####
#####################
# def print_message(name, language):
#     print("Hi, my name is " + name + " and my favorite programming language is " + language)


# print_message(language="Python", name="Kadir")

#####################
#### 2ème façon #####
#####################

# def print_message(name, language="Python"):
#     print("Hi, my name is " + name + " and my favorite programming language is " + language)


# print_message(name="Kadir")


#####################
#### 3ème façon #####
#####################

# def print_message(name, language="Python"):
#     print("Hi, my name is " + name + " and my favorite programming language is " + language)


# print_message("Kadir", "Java")






def print_message(name, language):
    return "Hi, my name is " + name + " and my favorite programming language is " + language


var= print_message("Kadir", "Python")


print(var)