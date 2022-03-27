"""
File: student.py
Resources to manage a student's name and test scores.
"""

'''
* Author's Name: Atienza, Abril, Cacanindin, Martin
* Group No.: 1
* Date: March 27, 2022
* Filename: student1.py

''' 

class Student(object): 
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    """METHOD 1"""
    def __eq__(self, student):
        if (self.name == student.name):
            return "Yes"
        else:
            return "No"

    """METHOD 2"""
    def __lt__(self, student):
        if (self.name < student.name):
            return "Yes"
        else:
            return "No"

    """METHOD 3"""
    def __ge__(self, student):
        if (self.name >= student.name):
            return "Yes"
        else:
            return "No"

    def __str__(self):
        """Returns the string representation of the student."""
        return "Student Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    print("\nStudent 1")
    student = Student("Ed", 5)

    for i in range(1, 6):
        student.setScore(i, 100-i)
    print(student)

    print("\nStudent 2")
    student2 = Student("Eddy", 5)

    for j in range(1, 6):
        student2.setScore(j, 95-j)
    print(student2)

    print("\nIs Student 1 equal to Student 2")
    print(student.__eq__(student2))

    print("\nIs Student 1 equal to Student 2")
    print(student.__lt__(student2))

    print("\nIs Student 1 greater than or equal to Student 2")
    print(student.__ge__(student2))

if __name__ == "__main__":
    main()




