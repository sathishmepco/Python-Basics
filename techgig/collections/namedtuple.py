from collections import namedtuple
def main():
    n = int(input().strip())
    students = []
    Student = namedtuple("Student",["name","mark"])
    string = input().strip().split()
    for i in range(n):
        s1, s2 = input().strip().split()
        if string[0] == "marks":
            s1 = int(s1)
            s = Student(s2,s1)
        else:
            s2 = int(s2)
            s = Student(s1,s2)
        students.append(s)
    total = sum(s.mark for s in students)
    print("{:.2f}".format(total/n),end='')
main()

'''
Input
3
marks names
10 arpit
20 anushka
35 rakshita
Output
21.67
'''