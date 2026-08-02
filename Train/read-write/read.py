phone_book = open("Train/read-write/phone_book.txt", "r")

print(phone_book.readlines())

for person in phone_book.readlines():
    print(person)
    
phone_book.close()
