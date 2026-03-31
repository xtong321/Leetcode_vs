"""
https://neetcode.io/problems/dynamicArray
Design Dynamic Array (Resizable Array)

Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.
Your DynamicArray class should support the following operations:

DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
int get(int i) will return the element at index i. Assume that index i is valid.
void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
void pushback(int n) will push the element n to the end of the array.
int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
void resize() will double the capacity of the array.
int getSize() will return the number of elements in the array.
int getCapacity() will return the capacity of the array.
If we call void pushback(int n) but the array is full, we should resize the array first.

Example 1:
Input:
["Array", 1, "getSize", "getCapacity"]
Output:
[null, 0, 1]

Example 2:
Input:
["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]
Output:
[null, null, 1, null, 2]

Example 3:
Input:
["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]
Output:
[null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]
"""

class DynamicArray:    
    def __init__(self, capacity: int):
        if capacity <= 0:
            print(f'Error: capacity should be > 0')
        self._capacity = capacity
        #self._array = []
        # set default val for teh array, and use size to control access/actual size
        self._array = [0] * self._capacity     
        self._size = 0      
    
    # int get(int i) will return the element at index i. Assume that index i is valid.
    def get(self, i: int) -> int:
        if i<0 or i >= self._size:
            return None
        return self._array[i]

    # void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
    def set(self, i: int, n: int) -> None:
        if i >= self._size:
            print(f'Error: invalid index')
        self._array[i] = n
        
    # void pushback(int n) will push the element n to the end of the array.
    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
            #self._capacity *= 2
            #self._array.reverse(self._capacity)
        
        self._array[self._size] = n
        self._size += 1
        #self._array.append(n)
        
    # int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
    def popback(self) -> int:
        if not self._array:
            print(f'Error: array is empty')
        
        #val = self._array[self._size-1]
        #del self._array[self._size-1]
        #self._size -= 1
        #return val

        # new imp, not real delete the last item, keep the index
        if self._size > 0:
            # soft delete the last element
            self._size -= 1
        # return the popped element
        return self._array[self._size]
         
    # void resize() will double the capacity of the array.
    def resize(self) -> None:
        self._capacity *= 2
        new_arr = [0] * self._capacity

        # Copy elements to new_arr
        for i in range(self._size):
            new_arr[i] = self._array[i]
        self._array = new_arr
        
    # int getSize() will return the number of elements in the array.
    def getSize(self) -> int:
        if not self._array:
            return 0
        return self._size
                
    
    def getCapacity(self) -> int:
        return self._capacity
        

## test
if __name__ == "__main__":
    # Input: ["Array", 1, "getSize", "getCapacity"], Output: [null, 0, 1]
    #array_1 = DynamicArray(1)
    #print(array_1.getSize())
    #print(array_1.getCapacity())

    # Input: ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]
    # Output: [null, null, 1, null, 2]
    array2 = DynamicArray(1)
    print(array2.pushback(1))
    print(array2.getCapacity())
    print(array2.pushback(2))
    print(array2.getCapacity())