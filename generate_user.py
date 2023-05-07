# 1. Feladat - User generálás - 10 pont

import unicodedata

names = [['Kovács', 'Tóth', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]

users = []


def create_users(names):
    for name in names:
        # without a dot character between names in email:
        # full_name: str = ""
        # for i in name:
        #  full_name = full_name + i

        # using the join() to add the dots:
        full_name: str = '.'.join(name)
        full_name = full_name + "@company.hu"
        email = unicodedata.normalize('NFKD',
                                      full_name).encode('ASCII', 'ignore')
        email = email.decode("utf-8").lower()
        password = name[0] + "123Start"
        users.append(({'name': name, 'email': email, 'password': password}))

    with open('nevek.txt', 'w') as f:
        for item in users:
            name_text: str = " ".join(item['name'])
            f.write(f"{name_text} {item['email']} {item['password']}\n")
    print("nevek.txt with all data is created.")


create_users(names)

# print(users)
