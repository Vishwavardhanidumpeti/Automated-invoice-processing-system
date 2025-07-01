class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def display(self):
        print(f" Name: {self.name} | Age: {self.age} | Species: {self.species}")

class Clinic:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet: Pet):
        self.pets.append(pet)
        print(f"{pet.name} has been added to the clinic.")

    def remove_pet(self, name: str):
        name = name.lower()
        for pet in self.pets:
            if pet.name.lower() == name:
                self.pets.remove(pet)
                print(f"{pet.name} has been removed from the clinic.")
                return
        print(f"No pet found with the name: {name}")

    def search_pet(self, name: str):
        name = name.lower()
        for pet in self.pets:
            if pet.name.lower() == name:
                print("Pet Found:")
                pet.display_info()
                return
        print(f"No pet found with the name: {name}")

    def display_all(self):
        if not self.pets:
            print("No pets currently in the clinic.")
        else:
            print("All Pet Records:")
            for pet in self.pets:
                pet.display_info()

def main():
    clinic = Clinic()

    while True:
        print("\n--- Clinic Management ---")
        print("1. Add Pet")
        print("2. Remove Pet")
        print("3. Search Pet")
        print("4. Display All Pets")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter pet name: ")
            age = input("Enter pet age: ")
            species = input("Enter pet species: ")
            pet = Pet(name, age, species)
            clinic.add_pet(pet)

        elif choice == '2':
            name = input("Enter pet name to remove: ")
            clinic.remove_pet(name)

        elif choice == '3':
            name = input("Enter pet name to search: ")
            clinic.search_pet(name)

        elif choice == '4':
            clinic.display_all()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
