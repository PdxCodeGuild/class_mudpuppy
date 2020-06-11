from random import choice as rc



print(rc(eyes) + rc(noses) + rc(mouths))

class FacePart:
    def __init__(self, name, options):
        self.name = name
        self.options = options
    
    def rand_face_part(self):
        print(f'Making an {self.name}')
        return rc(self.options)

eyes = FacePart('eyes', ':;B')
print(eyes.name, eyes.options)
print(eyes.rand_face_part())

noses = FacePart('noses','->')
mouths = FacePart('mouths', ')(D')