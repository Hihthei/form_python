
# exercice liste de course

from src.forma_fun.forma_func import list_append, list_remove, list_print, list_empty

grocery_list = []

while True:
    print("Choisissez parmi les 5 options suivantes :\n"
          "1_ Ajouter un ou plusieurs éléments à la liste\n"
          "2_ Retirer un ou plusieurs éléments à la liste\n"
          "3_ Afficher la liste\n"
          "4_ Vider la liste\n"
          "5_ Quitter le programme\n")

    user_choice = input("Veuillez saisir votre réponse : ")

    if user_choice == "1":
        grocery_list = list_append(grocery_list, input("Quel(s) ingrédient(s) souhaitez-vous ajouter ?\n"))
    elif user_choice == "2":
        list_remove(grocery_list, input("Quel(s) ingrédient(s) souhaitez-vous retirer ?\n"))
    elif user_choice == "3":
        list_print(grocery_list)
    elif user_choice == "4":
        list_empty(grocery_list)
    elif user_choice == "5":
        break
    else:
        continue

    print("\n")
