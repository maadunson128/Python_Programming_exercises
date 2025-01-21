###Program: Set Objec creation using dictionaries and lists


class Set:
    def __init__(self, elements):
        '''Creates a set'''
        self.set_dict = {}
        for element in elements:
            self.set_dict[element] = True

    def display(self):
        '''Display the set'''
        print(self.set_dict)

    def addElement(self, element):
        '''Add elements to the set'''
        self.set_dict[element] = True

    def deleteElement(self, element):
        '''Deletes the element from the set'''
        del self.set_dict[element]

    def member(self, x):
        '''Returns True if the element is present else False'''
        return self.set_dict.get(x, False)
    
    def intersection(self, set2):
        '''Returns a new set containing just those elements 
            that are common to this set and set2'''
        inter_list = {}

        for element in set2:
            if element in self.set_dict.keys():
                inter_list[element] = True

        return inter_list

    def union(self, set2):
        '''Returns a new set containing all of elements that are in this 
            set, set2, or both.'''
        
        union_list = {}
        for element in self.set_dict.keys():
            union_list[element] = True

        for element in set2:
            union_list[element] = True

        return union_list

    def subract(self, set2):
        '''Returns a new set containing all the elements of this set 
            that are not in set2. '''
        subract_set = {}
        for element in self.set_dict.keys():
            if element not in set2:
                subract_set[element] = True

        return subract_set
    
