class Animal:
    def __init__(self,name: str,age: int,species: str) -> None:
        self.name = name
        self.age = age
        self.species = species

    def walk(self):
        print(f"{self.name} is walking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print("animal sound")

    def display_info(self):
        print(f"this is an {self.species}, and got the name as {self.name}, with an age of {self.age}.")



class Dog(Animal):
    def __init__(self, name, age, species,breed,has_shots: bool) -> None:
        super().__init__(name, age, species)
        self.breed = breed
        self.has_shots = has_shots

    def make_sound(self):
        print("WOOF")
    def go_for_walk(self):
        print(f"{self.name} is going for a walk")

class Cat(Animal):
    def __init__(self, name, age, species,fur_color: str, is_vaccinated: bool) -> None:
        super().__init__(name, age, species)
        self.fur_color = fur_color
        self.is_vaccinated = is_vaccinated

    def make_sound(self):
        print("MEOW")
    def scratch(self):
        print(f"{self.name} is scratching the sofa")

class AnimalShelter:
    def __init__(self) -> None:
        self.animals = []

    def add_animal(self,animal_obj):
        self.animals.append(animal_obj)
        print(f"{animal_obj.name} added to shelter.")
    
    def admit_animal(self,animal):
        self.animals.append(animal)

    def list_all_animals(self):
        for animal in self.animals:
            animal.display_info()

    def make_all_animals_sound(self):
        for animal in self.animals:
            animal.make_sound()

    def adopt_animal(self,name):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                print(f"{name} has been adopted!")
                return
        print(f"No animal name {name} found.")


shelter = AnimalShelter()

# Admit Dogs
shelter.admit_animal(Dog("Kevin", 7, "Dog", "Bulldog", True))
shelter.admit_animal(Dog("Lassa", 12, "Dog", "Beagle", True))
shelter.admit_animal(Dog("Thor", 7, "Dog", "Dobermann", False))

# Admit Cats
shelter.admit_animal(Cat("Oliver", 5, "Cat", "Black", False))
shelter.admit_animal(Cat("Leo", 1, "Cat", "Orange", True))
shelter.admit_animal(Cat("Milo", 3, "Cat", "Tortoiseshell", False))

def main_menu(shelter):
    while True:
        print("\n=== Animal Shelter Menu ===")
        print("1 - Admit a new animal")
        print("2 - List all animals")
        print("3 - Make all animals sound")
        print("4 - Adopt an animal")
        print("5 - Exit")

        choice = input("Choose an option: ")

        # ADMIT AN ANIMAL
        if choice == "1":
            print("\n--- Admit Animal ---")
            animal_type = input("Dog or Cat? ").strip().lower()

            name = input("Name: ")
            age = int(input("Age: "))
            
            if animal_type == "dog":
                breed = input("Breed: ")
                shots = input("Has shots? (yes/no): ").strip().lower() == "yes"
                new_animal = Dog(name, age, "Dog", breed, shots)

            elif animal_type == "cat":
                color = input("Color: ")
                shots = input("Has shots? (yes/no): ").strip().lower() == "yes"
                new_animal = Cat(name, age, "Cat", color, shots)

            else:
                print("Invalid animal type!")
                continue  # return to menu

            shelter.admit_animal(new_animal)
            print(f"{name} has been admitted!")

        # LIST ANIMALS
        elif choice == "2":
            print("\n--- Animals in Shelter ---")
            shelter.list_all_animals()

        # MAKE ALL SOUND
        elif choice == "3":
            print("\n--- The Shelter Gets Noisy ---")
            shelter.make_all_animals_sound()

        # ADOPT AN ANIMAL
        elif choice == "4":
            print("\n--- Adopt Animal ---")
            name = input("Enter animal name to adopt: ")
            shelter.adopt_animal(name)

        # EXIT
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    shelter = AnimalShelter()
    main_menu(shelter)
