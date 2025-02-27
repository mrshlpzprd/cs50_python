import inflect
p = inflect.engine()

list_of_names = []


while True:
    try:
        name_prompt = input("Name: ")
        list_of_names.append(name_prompt)
        adieu_list = p.join(list_of_names)

    except EOFError:
        print('Adieu, adieu, to ' + adieu_list)
        break
