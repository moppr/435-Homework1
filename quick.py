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
    
    
    # perform quick sort and print after each partition
    def quick_sort(arr,l,r):
        if l >= r:
            return
        
        # midpoint for recursive call        
        i = partition(arr,l,r)
            
        for item in arr:
            print(item)
        print()
            
        quick_sort(arr,l,i)
        quick_sort(arr,i+1,r)
        

    def partition(arr,l,r):
        # using first element in range as the pivot point
        i = l+1
        
        for j in range(l+1,r):
            if arr[l] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                i = i + 1
                
        arr[i-1],arr[l] = arr[l],arr[i-1]
        return i-1           
            

    quick_sort(students, 0, len(students))
