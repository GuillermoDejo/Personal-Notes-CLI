import os
import argparse
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

def view_notes():
    notes = read_notes()
    if not notes:
        print("No notes found.")
        return
    for idx, note in enumerate(notes, 1):
        print(f"{idx}. {note}")

def add_note(note_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    full_note = f"[{timestamp}] {note_text}"
    notes = read_notes()
    notes.append(full_note)
    write_notes(notes)
    print("Note added.")

def add_note_interactive():
    note = input("Write your note: ")
    add_note(note)

def search_notes(query):
    notes = read_notes()
    found = False
    for idx, note in enumerate(notes, 1):
        if query in note.lower():
            print(f"{idx}. {note}")
            found = True
    if not found:
        print("No matching notes found.")

def delete_note_by_number(num):
    notes = read_notes()
    if 1 <= num <= len(notes):
        deleted = notes.pop(num - 1)
        write_notes(notes)
        print(f"Deleted note: {deleted}")
    else:
        print("Invalid note number.")

def delete_note_interactive():
    view_notes()
    try:
        num = int(input("Enter note number to delete: "))
        delete_note_by_number(num)
    except ValueError:
        print("Please enter a valid number.")

def main():
    parser = argparse.ArgumentParser(description="Personal Notes CLI App")
    parser.add_argument("--add", help="Add a new note")
    parser.add_argument("--view", action="store_true", help="View all notes")
    parser.add_argument("--search", help="Search notes by keyword")
    parser.add_argument("--delete", type=int, help="Delete note by number")
    args = parser.parse_args()

    if args.add:
        add_note(args.add)
    elif args.view:
        view_notes()
    elif args.search:
        search_notes(args.search.lower())
    elif args.delete:
        delete_note_by_number(args.delete)
    else:
        # Interactive menu if no arguments are given
        while True:
            print("\n--- Personal Notes App ---")
            print("1. Add Note")
            print("2. View Notes")
            print("3. Search Notes")
            print("4. Delete Note")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                add_note_interactive()
            elif choice == "2":
                view_notes()
            elif choice == "3":
                query = input("Enter keyword to search: ").lower()
                search_notes(query)
            elif choice == "4":
                delete_note_interactive()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

if __name__ == "__main__":
    main()