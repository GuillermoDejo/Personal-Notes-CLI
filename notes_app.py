import os
from datetime import datetime

FILENAME = "notes.txt"

def read_notes():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return f.read().splitlines()

def write_notes(notes):
    with open(FILENAME, "w") as f:
        f.write("\n".join(notes))

def add_note():
    note = input("Escribe tu nota: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    full_note = f"[{timestamp}] {note}"
    
    notes = read_notes()
    notes.append(full_note)
    write_notes(notes)
    print("¡Nota guardada con fecha y hora!")

def view_notes():
    notes = read_notes()
    if not notes:
        print("No notes yet.")
        return
    for idx, note in enumerate(notes, 1):
        print(f"{idx}. {note}")

def delete_note():
    view_notes()
    try:
        num = int(input("Enter note number to delete: "))
        notes = read_notes()
        if 1 <= num <= len(notes):
            deleted = notes.pop(num - 1)
            write_notes(notes)
            print(f"Deleted: {deleted}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def search():
    query = input("Enter a word to search: ").lower()
    notes = read_notes()
    found = False

    for idx, note in enumerate(notes, 1):
        if query in note.lower():
            print(f"{idx}. {note}")
            found = True

    if not found:
        print("No results found.")
        

def menu():
    while True:
        print("\n--- Personal Notes App ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Search Notes")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            search()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
