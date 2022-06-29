class AnimalShelter():
    def __init__(self):
        self.cat = []
        self.dog = []
        
    def enqueue(self, animal, type):
        if type == "cat":
            self.cat.append(animal)
        else:
            self.dog.append(animal)
            
    
    def dequeueCat(self):
        return None if len(self.cat) == 0 else self.cat.pop(0)

    def dequeueDog(self):
        return None if len(self.dog) == 0 else self.dog.pop(0)
    
    def dequeAny(self):
        return self.dog.pop(0) if len(self.cat) == 0 else self.cat.pop(0)
    
custome_shelter = AnimalShelter()
custome_shelter.enqueue("Cat1", "cat")
custome_shelter.enqueue("Cat2", "cat")
custome_shelter.enqueue("Cat3", "cat")
custome_shelter.enqueue("dog1", "dog")
custome_shelter.enqueue("cat4", "cat")
custome_shelter.enqueue("dog2", "dog")

print(custome_shelter.dequeAny())
print(custome_shelter.dequeAny())
print(custome_shelter.dequeueDog())
print(custome_shelter.dequeAny())
