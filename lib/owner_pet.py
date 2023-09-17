class Owner:
    def __init__(self, name):
        self.name = name
        self.allPets = []

    def pets(self):
        return self.allPets
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            self.allPets.append(pet)
            pet.owner = self
        else: 
            raise Exception("not correct pet type")

    def get_sorted_pets(self):
        return sorted(self.allPets, key=lambda pet: pet.name)


class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        
        if pet_type in Pet.PET_TYPES:
            self.name = name
            self.pet_type = pet_type
            Pet.all.append(self)
            if owner:
                if isinstance(owner, Owner):
                    self.owner = owner
                    owner.add_pet(self)
                else:
                    raise Exception("yoo")
        else:
            raise Exception("Pet_type not one of the approved types")



