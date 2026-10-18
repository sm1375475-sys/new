class student:
    def __init__(self, name, id, grade):
        self.name=name
        self.id=id
        self.__grade=grade

    def get_grade(self):
        return self.__grade 
    
    def add_grade(self, grade):
        return self.__grade.append(grade)
    
    def average_calculate(self):
        return sum(self.__grade)/len(self.__grade)
    
    def calculate_grade(self):
        if self.calculate_average() >= 50:
            return"pass"
        else:
            return"fail"
        
        def display_info(self):
            print("name:", self.name) 
            print("id:", self.id)
            print("grade:", self.get_grade())
            print("average:", self.calculate_average())  
            print("grade:", self.calculate_grade())
        
