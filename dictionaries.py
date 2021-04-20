breakfast = {"Ham":"yes", "Eggs":"yes", "Spam":"no"}

# game_object = {"Icon":["blue", "Speed", "Points"]}

# print(game_object["Icon"])

### \n permet de passer àla ligne suivante

###ajout d'un élément
# breakfast["Grits"]= "no"


###supression d'un élément

# del(breakfast["Spam"])

print("Breakfast Menu \n")

### ici 2 variable utiliser 1 pour la key = k, l'autre valeur = v 
### on oublie pas de mettre la fonction sorted -> trier devant le dictionnaire
for k,v in sorted(breakfast.items()):

###\t permet d'ajouter un onglet

    print("{} \t {}".format(k,v))

### déclaration d'un dictionnaire 
# icon = {}
### ajoute un paire de valeur clef
# icon['Name'] = "Alien"
#### ajoute une clef avec liste pour les valeurs
# icon['Speed'] = ["fast", "medium", "slow"]
#### montre comment on peut imbriquer un dictionnaire dans les valeurs d'un autre disctionnaire
# icon["points"] = {"top":200, "bottom":300, "middle":1200}