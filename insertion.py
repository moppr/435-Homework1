class Student:
    '''A student with a first and last name and graduation year'''
    
    def __init__(self, line):
        self.first, self.last, self.year = line.split()
    
    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.first < other.first:
                return True
            elif self.first == other.first:
                return True if self.last < other.last else False
        return False
    
    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.first > other.first:
                return True
            elif self.first == other.first:
                return True if self.last > other.last else False
        return False
    
    def __str__(self):
        return self.first + ' ' + self.last + ' ' + self.year

if __name__ == '__main__':

    # parsing inputs
    num_students = int(input())
    students = [Student(input()) for _ in range(num_students)]
    
    # perform insertion sort and print after each pass
    for i in range(1, len(students)):
        next = students[i]
        j = i-1
        while j >= 0 and next < students[j]:
            students[j+1] = students[j]
            j -= 1
        students[j+1] = next
        
        for student in students:
            print(student)
        print()
