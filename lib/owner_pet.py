class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]  # valid pet types
    all = []  # store all Pet instances

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.pet_type = pet_type

        self.owner = None
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an instance of Owner")
            self.owner = owner
            owner.add_pet(self)  # automatically add the pet to the owner's list

        # Add this instance to the class variable 'all'
        Pet.all.append(self)
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of all pets that belong to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign a pet to this owner, validating the type."""
        if not isinstance(pet, Pet):
            raise Exception("Can only add instances of Pet")
        pet.owner = self  # assign this owner to the pet

    def get_sorted_pets(self):
        """Return a list of the owner's pets sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)
