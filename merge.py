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
    
    # perform merge sort and print after each merge
    def merge_sort(arr):
        if len(arr) <= 1:
            return
        
        # split array into its halves
        mid = len(arr)//2
        left, right = arr[:mid], arr[mid:]
        
        # recursive call on each half
        merge_sort(left)
        merge_sort(right)
        
        # merge the halves
        it_left = iter(left)
        it_right = iter(right)
        # each half should have at least 1 element so calling next here without handling is ok
        curr_left = next(it_left)
        curr_right = next(it_right)
        i = 0
        while i < len(arr):
            arr[i] = min(curr_left, curr_right)
            if arr[i] == curr_left:
                try:
                    curr_left = next(it_left)
                except StopIteration:
                    curr_left = Student('a a 9999') # always evaluates higher than real students
            else:
                try:
                    curr_right = next(it_right)
                except StopIteration:
                    curr_right = Student('a a 9999')
            i += 1
            
        # output
        # because this is actually splitting the array into smaller arrays instead of having the
        # original one exist during all calls, the outputs don't line up but the sort works
        for item in arr:
            print(item)
        print()
        
                    
    merge_sort(students)
