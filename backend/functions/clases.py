# Define the Person class, which we will use as a base class
class Person():
    def __init__(self, name, id, ):
        self.name = name
        self.id = id

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    # Added for debugging
    def show(self):
        print(f' Name: {self.name}')
        print(f' ID: {self.id}')
        

# Define a Student subclass that inherits from Person
class Student(Person):
    def __init__(self, name, id, cel = None, email = None):
        self.cel = cel
        self.email = email
        super().__init__(name, id)

    def getCel(self):
        return self.cel

    def getEmail(self):
        return self.email

    def setCel(self, cel):
        self.cel = cel

    def setEmail(self, email):
        self.email = email

    # Added for debugging
    def show(self):
        super().show()
        print(f' Cel: {self.cel}')
        print(f' Email: {self.email}')

# Clase asociada a la encuesta
class Survey():
    def __init__(self, idSurvey, statements = None):
        self.idSurvey = idSurvey
        self.numStatements = 0
        if statements == None: 
            self.statemens = []
        else: 
            self.statemens = statements[:]  # make a copy 
            self.numStatements = len(self.statemens)
    
    def getIdSurvey(self):
        return self.getIdSurvey

    def getNumStatements(self):
        return self.numStatements
    
    def addStatement(self, statement):
        self.statemens.append(statement)
        self.numStatements += 1

    def getStatement(self,num):
        return self.statemens[num]
    
    def show(self):
        print(self.statemens)


if __name__=='__main__': 
    # Test estudiantes
    est1 = Student("Profesor Xavier", "0000", "3001111111","jairo.agudelo.m@gmail.com") 
    est2 = Student("tigarto", "0001", "3002222222","helpu1409@gmail.com") 
    est1.show()
    print()
    est2.show()
    preguntas = [
        "¿Que tal le parecio la materia?",
        "¿Que tal le parecio la metodologia empleada por el profesor?",
    ]
    # Test encuesta
    print()
    encuesta1 = Survey("encuesta-0001",preguntas)
    print(encuesta1.getNumStatements())
    encuesta1.addStatement("¿Que tan pertinente es la materia para su carrera?")
    print(encuesta1.getNumStatements())
    print(encuesta1.getStatement(0))
    encuesta1.show()




 