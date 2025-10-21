"""
memory initialization, allocate and free
"""

class Pointer(object):
    def __init__(self, start=0, end=0):
        self.start = start
        self.size = end        

class Memory(object):
    def __init__(self, capability):
        self.capability = capability
        self.pointer_list = []
        self.free_space = capability
        print('==> total_space: {}'.format(self.free_space))

    def allocate(self, size):
        if self.free_space < size:
            print("==> Error: no space to allocate")
            return -1
        
        if len(self.pointer_list) <= 0:
            new_pointer = Pointer(0, size)
            self.free_space -= size
            self.pointer_list.append(new_pointer)
            print('==> curr_pointer: {}, free_space: {}'.format(new_pointer.start, self.free_space))
            return new_pointer.start
        elif len(self.pointer_list) == 1:
            new_pointer = Pointer(self.pointer_list[0].start + self.pointer_list[0].size, size)
            self.free_space -= size
            self.pointer_list.append(new_pointer)
            print('==> curr_pointer: {}, free_space: {}'.format(new_pointer.start, self.free_space))
            return new_pointer.start
        else:
            for i in range(0, len(self.pointer_list)-2):
                curr_pointer = self.pointer_list[i]
                next_pointer = self.pointer_list[i+1]
                if next_pointer.start - curr_pointer.start - curr_pointer.size >= 0:
                    new_pointer = Pointer(curr_pointer.start + curr_pointer.size, size)
                    self.free_space -= size
                    self.pointer_list.append(new_pointer)
                    print('==> curr_pointer: {}, free_space: {}'.format(new_pointer.start, self.free_space))
                    return new_pointer.start
        
        return -1

    def free(self, start):
        if len(self.pointer_list) <= 0:
            print("==> no operation needed")
            return

        # 1) find the pointer that has the same start position
        hit_index = -1
        for i in range(0, len(self.pointer_list)):
            if self.pointer_list[i].start == start:
                hit_index = i
                break
        # 2) free it
        if hit_index >= 0:            
            self.free_space += self.pointer_list[hit_index].size            
            print('==> free_space: {}, available_space'.format(self.pointer_list[hit_index].size, self.free_space))
            del self.pointer_list[hit_index] # or self.pointer_list.pop(i)

        # or we can direct remove the elem with value
        return

if __name__ == "__main__":
    memory = Memory(100)

    p1 = memory.allocate(20)
    p2 = memory.allocate(30)
    p3 = memory.allocate(60)

    memory.free(p2)

    memory.allocate(60)