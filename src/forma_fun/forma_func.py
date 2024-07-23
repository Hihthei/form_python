def calculatrice_addition() -> None:
    while True:
        a = input("Entrez un premier nombre : ")
        b = input("Entrez un deuxième nombre : ")

        if not (a.isdigit() and b.isdigit()):
            print("Veuillez entrer deux nombres valides !")
            continue

        break

    print(f"{a} + {b} = {int(a) + int(b)}")


def list_append(grocery_list: list = None, grocery_name: str = None) -> list or None:
    if grocery_name is None:
        return grocery_list

    if grocery_list is None:
        grocery_list = []

    current_len = len(grocery_list)

    tmp_list = grocery_name.split(" ")
    grocery_list.extend(
        element.lower().title() for element in tmp_list if element not in grocery_list and element.isalpha())

    if len(grocery_list) > current_len:
        elements_str = " ".join(f"{element.lower().title()}" for element in tmp_list if element.isalpha())
        print(f"[ {elements_str} ], bien ajouté avec succès !")

    return grocery_list


def list_remove(grocery_list: list = None, grocery_name: str = None) -> None:
    if grocery_list is None or grocery_name is None:
        return None

    tmp_list = grocery_name.split(" ")
    for element in tmp_list:
        try:
            grocery_list.remove(element.lower().title())
            print(f"{element.lower().title()}, a bien été retiré de la liste.")
        except ValueError:
            pass


def list_print(grocery_list: list = None) -> None:
    if grocery_list is None:
        return None

    for i, element in enumerate(grocery_list, start=1):
        print(f"{i} {element}")


def list_empty(grocery_list: list = None) -> None:
    if grocery_list is None:
        return None

    grocery_list.clear()

    if len(grocery_list) == 0:
        print("La liste a été vidé avec succès !")


def list_main_ui(grocery_list: list = None) -> list:
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

    return grocery_list
