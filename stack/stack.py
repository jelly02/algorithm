class stack(list):

    push = list.append();

    def peek(self):
        return self[-1]  #마지막 값 가져오기 self[len(self)-1]


s = stack()

s.push(1)
s.push(5)
s.push(10)

print("my stack is :", s)
print("popped value is : ", s.pop)
print("my stack is :", s)
