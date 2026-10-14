def find_phone_number(contacts, name):
    contact_book = {}

    for contact_name, phone_number in contacts:
        contact_book[contact_name] = phone_number

    return contact_book.get(name, "Not found")
    
print(find_phone_number([("Ada", "0801"), ("Bola", "0802")], "Ada"))
print(find_phone_number([("Ada", "0801")], "Chidi"))