import json

class ContactManager:

    def __init__(self, path="-"):
        self.contact_list = []

        if path != "-":
            try:

                print("Loading previous contacts...")
                with open(path, "r") as f:
                    data = f.read()
                    if data.strip(): 
                        self.contact_list = json.loads(data)
                print("LOADED...")

            except FileNotFoundError:
                print("No previous file found. Starting fresh.")

    def add(self, name, number):
        for contact in self.contact_list:
            if contact["number"] == number:
                print("Warning: This number already exists!")
                return

        self.contact_list.append({"name": name, "number": number})
        print("Contact added.")
        

    def search(self, name):
        result = []

        for item in self.contact_list:
            if name.lower() in item["name"].lower():
                result.append(item)

        return result

    def backup(self):
        with open("./contact_list.json", "w") as f:
            json.dump(self.contact_list, f, indent=4)



    def print(self):
        for i in self.contact_list:
            print(f"Name: {i['name']}, Number: {i['number']}")
            

    def run(self):
        while True:
            print("\n1. Add Contact")
            print("2. Search")
            print("3. Show All")
            print("4. Save & Exit")

            choice = input("Choose: ")

            if choice == "1":
                name = input("Name: ")
                number = input("Number: ")
                self.add(name, number)

            elif choice == "2":
                name = input("Search name: ")
                results = self.search(name)

                if not results:
                    print("No contact found with that name.")
                else:
                    for r in results:
                        print(f"Name: {r['name']}, Number: {r['number']}")

            elif choice == "3":
                self.print()

            elif choice == "4":
                self.backup()
                print("Saved. Bye!")
                break

            else:
                print("Error: Enter valid name or number.")


my_contacts = ContactManager(path="./contact_list.json")
my_contacts.run()