import sys
from compute import *

class Grades:
    __stInfo = {}
    __asg1Info = {}
    __asg2Info = {}
    __prjInfo = {}
    __test1Info = {}
    __test2Info = {}
    __max_asg1 = None
    __max_asg2 = None
    __max_prj = None
    __max_test1 = None
    __max_test2 = None

    def get_stInfo(self):
        return self.__stInfo

    def get_asg1Info(self):
         return self.__asg1Info

    def get_asg2Info(self):
        return self.__asg2Info

    def get_prjInfo(self):
        return self.__prjInfo

    def get_test1Info(self):
        return self.__test1Info

    def get_test2Info(self):
        return self.__test2Info

    def get_maxasg1(self):
        return self.__max_asg1

    def get_maxasg2(self):
        return self.__max_asg2

    def get_maxprj(self):
        return self.__max_prj

    def get_maxtest1(self):
        return self.__max_test1

    def get_maxtest2(self):
        return self.__max_test2

    def __init__(self):
        class_file = open("class.txt", "r+")
        read_class = class_file.read().splitlines()
        for x in range(len(read_class)):
            mystring = read_class[x].split("|")
            self.__stInfo[mystring[0]] = mystring[1] + "," + mystring[2]

        asg1_file = open("a1.txt", "r+")
        asg1_class = asg1_file.read().splitlines()

        for i in range(len(asg1_class)):
            if i==0:
                self.__max_asg1 = asg1_class[i]
            else:
                mystring = asg1_class[i].split("|")
                self.__asg1Info[mystring[0]] = mystring[1]

        asg2_file = open("a2.txt", "r+")
        asg2_class = asg2_file.read().splitlines()

        for i in range(len(asg2_class)):
            if i==0:
                self.__max_asg2 = asg2_class[i]
            else:
                mystring = asg2_class[i].split("|")
                self.__asg2Info[mystring[0]] = mystring[1]

        prj_file = open("project.txt", "r+")
        prj_class = prj_file.read().splitlines()

        for i in range(len(prj_class)):
            if (i == 0):
                self.__max_prj = prj_class[i]
            else:
                mystring = prj_class[i].split("|")
                self.__prjInfo[mystring[0]] = mystring[1]

        test1_file = open("test1.txt", "r+")
        test1_class = test1_file.read().splitlines()

        for i in range(len(test1_class)):
            if i == 0:
                self.__max_test1 = test1_class[i]
            else:
                mystring = test1_class[i].split("|")
                self.__test1Info[mystring[0]] = mystring[1]

        test2_file = open("test2.txt", "r+")
        test2_class = test2_file.read().splitlines()

        for i in range(len(test2_class)):
            if i == 0:
                self.__max_test2 = test2_class[i]
            else:
                mystring = test2_class[i].split("|")
                self.__test2Info[mystring[0]] = mystring[1]


def main():
    g = Grades()
    c = Compute(g.get_stInfo(), g.get_maxasg1(), g.get_asg1Info(), g.get_maxasg2(), g.get_asg2Info(),
                g.get_maxprj(), g.get_prjInfo(), g.get_maxtest1(), g.get_test1Info(), g.get_maxtest2(),
                g.get_test2Info())
    menu = '''\n\n1> Display individual component
2> Display component average 
3> Display Standard Report 
4> Sort by alternate column 
5> Change Pass/Fail point 
6> Exit'''

    while True:
        print(menu)
        var = input("Enter your option (1-6):")
        if var.isdigit():
            tmp = int(var)
            if tmp == 1:
                Compute.ind_comp(c)
            elif tmp == 2:
                Compute.cal_average(c)
            elif tmp == 3:
                Compute.std_report(c)
            elif tmp == 4:
                Compute.sort_by(c)
            elif tmp == 5:
                Compute.changepf(c)
            elif tmp == 6:
                print("Good Bye", end="")
                exit(0)
            else:
                print("Enter correct option.")
        else:
            print("Enter correct option.")


main()

