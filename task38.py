# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных

# информация в файле
def selectAllReadPhoneNumber(filename):
    print("\nПП | full name | Tel")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

# Записывает новую инфу в файл
def selectSomethingReadPhoneNumber(filename):
    with open(filename, "r", encoding="utf-8") as data:
        phoneBook = data.read()
    num = len(phoneBook.split("\n"))
    with open(filename, "a", encoding="utf-8") as data: 
        fio = input("Enter full name: ")
        phone_number = input("Enter your phone number: ")
        data.write(f"{num} | {fio} | {phone_number}\n")
        print(f"Добавлена запись : {num} | {fio} | {phone_number}\n")

# Редактирует инфу из файла
def addPerson(filename):
    print("\nПП | full name | Tel")
    with open(filename, "r", encoding='utf-8') as data:
        phoneBook = data.read()
    print(phoneBook)
    print("")
    index_delete_data = int(input("Enter the line number to edit: ")) - 1
    phoneBook_lines = phoneBook.split("\n")
    edit_phoneBook_lines = phoneBook_lines[index_delete_data]
    elements = edit_phoneBook_lines.split(" | ")
    fio = input("Enter full: ")
    phone = input("Enter your phone number: ")
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    phoneBook_lines[index_delete_data] = edited_line
    print(f"Record - {edit_phoneBook_lines}, changed to - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(phoneBook_lines))

# Удаляет инфу из файла
def delete_data(filename):
    print("\nПП | full name | Tel")
    with open(filename, "r", encoding="utf-8") as data:
        phoneBook = data.read()
        print(phoneBook)
    print("")
    index_delete_data = int(input("Enter the line number to delete: ")) - 1
    phoneBook_lines = phoneBook.split("\n")
    del_phoneBook_lines = phoneBook_lines[index_delete_data]
    phoneBook_lines.pop(index_delete_data)
    print(f"Record deleted: {del_phoneBook_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(phoneBook_lines))

def main():
    my_choice = -1
    file_tel = "tel.txt"

    # Создает файл если его нет в папке
    with open(file_tel, "a", encoding="utf-8") as file:
         file.write("")

    while my_choice != 0:
        print("Choose one of the actions:")
        print("1 - press for SHOW ALL")
        print("2 - press for SELECT")
        print("3 - press for ADD DATA")
        print("4 - press for deleting Information ")
        print("0 - press for EXITING THE PROGRAM")
        enteredNum = int(input("Action: "))
        if enteredNum == 1:
            selectAllReadPhoneNumber(file_tel)
        elif enteredNum == 2:
            selectSomethingReadPhoneNumber(file_tel)
        elif enteredNum == 3:
            addPerson(file_tel)
        elif enteredNum == 4:
            delete_data(file_tel)
        else:
            my_choice = 0

    print("Goodbye! See you later!")

if __name__ == "__main__":
    main()
