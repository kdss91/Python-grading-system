import sys

class Compute:
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

    def __init__(self, stinfo, max_asg1, asg1info, max_asg2, asg2info, max_prj, prjinfo, max_test1, test1info,
                 max_test2, test2info):
        self.__stInfo = stinfo
        self.__max_asg1 = max_asg1
        self.__max_asg2 = max_asg2
        self.__max_prj = max_prj
        self.__max_test1 = max_test1
        self.__max_test2 = max_test2
        self.__asg1Info = asg1info
        self.__asg2Info = asg2info
        self.__prjInfo = prjinfo
        self.__test1Info = test1info
        self.__test2Info = test2info

    def std_report(self):
        print("ID    LN     FN     A1  A2  PR  T1  T2  GR    FL")
        keys = self.__stInfo.keys()
        for x in sorted(keys):
            sys.stdout.write("%-6s" % x)
            mystring = self.__stInfo.get(x).split(",")
            sys.stdout.write("%-6s %-7s" % (mystring[1], mystring[0]))
            asg1_marks = self.__asg1Info.get(x)
            asg2_marks = self.__asg2Info.get(x)
            prj_marks = self.__prjInfo.get(x)
            test1_marks = self.__test1Info.get(x)
            test2_marks = self.__test2Info.get(x)
            if asg1_marks is None:
                sys.stdout.write("    ")
            else:
                sys.stdout.write("%-4s" % asg1_marks)
            if asg2_marks is None:
                sys.stdout.write("    ")
            else:
                sys.stdout.write("%-4s" % asg2_marks)
            if prj_marks is None:
                sys.stdout.write("    ")
            else:
                sys.stdout.write("%-4s" % prj_marks)
            if test1_marks is None:
                sys.stdout.write("    ")
            else:
                sys.stdout.write("%-4s" % test1_marks)
            if test2_marks is None:
                sys.stdout.write("    ")
            else:
                sys.stdout.write("%-4s" % test2_marks)
            sum1 = 0
            if asg1_marks is not None and asg1_marks.isdigit():
                sum1 += int(asg1_marks)/int(self.__max_asg1) * 7.5

            if asg2_marks is not None and asg2_marks.isdigit():
                sum1 += int(asg2_marks)/int(self.__max_asg2) * 7.5

            if prj_marks is not None and prj_marks.isdigit():
                sum1 += int(prj_marks)/int(self.__max_prj) * 25

            if test1_marks is not None and test1_marks.isdigit():
                sum1 += int(test1_marks)/int(self.__max_test1) * 30

            if test2_marks is not None and test2_marks.isdigit():
                sum1 += int(test2_marks)/int(self.__max_test2) * 30

            sys.stdout.write("%-6s" % float("{0:.2f}".format(sum1)))
            if sum1 >= 94:
                sys.stdout.write("A+")
            elif sum1 >= 87:
                sys.stdout.write("A")
            elif sum1 >= 80:
                sys.stdout.write("A-")
            elif sum1 >= 73:
                sys.stdout.write("B+")
            elif sum1 >= 66:
                sys.stdout.write("B")
            elif sum1 >= 59:
                sys.stdout.write("B-")
            elif sum1 >= 50:
                sys.stdout.write("C")
            else:
                sys.stdout.write("F")

            print("\n", end="")

    def ind_comp(self):
        while True:
            print("Enter component name (A1, A2, PR, T1, T2):")
            tmp = sys.stdin.readline().upper().strip()
            if tmp == "A1":
                print("A1 grades (" + self.__max_asg1 + ")")
                keys = self.__asg1Info.keys()
                for x in sorted(keys):
                    sys.stdout.write("%-8s" % x)
                    stud_info = self.__stInfo.get(x).split(",")
                    sys.stdout.write("%-7s" % (stud_info[1] + ","))
                    sys.stdout.write(stud_info[0].rjust(7))
                    sys.stdout.write("   " + self.__asg1Info.get(x))
                    print("")

                break

            elif tmp == "A2":
                print("A2 grades (" + self.__max_asg2 + ")")
                keys = self.__asg2Info.keys()
                for x in sorted(keys):
                    sys.stdout.write("%-8s" % x)
                    stud_info = self.__stInfo.get(x).split(",")
                    sys.stdout.write("%-7s" % (stud_info[1] + ","))
                    sys.stdout.write(stud_info[0].rjust(7))
                    sys.stdout.write("   " + self.__asg2Info.get(x))
                    print("")

                break

            elif tmp == "PR":
                print("Project grades (" + self.__max_prj + ")")
                keys = self.__prjInfo.keys()
                for x in sorted(keys):
                    sys.stdout.write("%-8s" % x)
                    stud_info = self.__stInfo.get(x).split(",")
                    sys.stdout.write("%-7s" % (stud_info[1] + ","))
                    sys.stdout.write(stud_info[0].rjust(7))
                    sys.stdout.write("   " + self.__prjInfo.get(x))
                    print("")

                break

            elif tmp == "T1":
                print("T1 grades (" + self.__max_test1 + ")")
                keys = self.__test1Info.keys()
                for x in sorted(keys):
                    sys.stdout.write("%-8s" % x)
                    stud_info = self.__stInfo.get(x).split(",")
                    sys.stdout.write("%-7s" % (stud_info[1] + ","))
                    sys.stdout.write(stud_info[0].rjust(7))
                    sys.stdout.write("   " + self.__test1Info.get(x))
                    print("")

                break

            elif tmp == "T2":
                print("T2 grades (" + self.__max_test2+ ")")
                keys = self.__test2Info.keys()
                for x in sorted(keys):
                    sys.stdout.write("%-8s" % x)
                    stud_info = self.__stInfo.get(x).split(",")
                    sys.stdout.write("%-7s" % (stud_info[1] + ","))
                    sys.stdout.write(stud_info[0].rjust(7))
                    sys.stdout.write("   " + self.__test2Info.get(x))
                    print("")

                break

            else:
                print("Enter a valid component.")


    def cal_average(self):
        while True:
            print("Enter component name (A1, A2, PR, T1, T2):")
            tmp = sys.stdin.readline().upper().strip()
            sum1 = 0
            num = 0
            if tmp == "A1":
                print("A1 average: ", end="")
                keys = self.__asg1Info.keys()
                for x in sorted(keys):
                    num += 1
                    sum1 += int(self.__asg1Info.get(x))

                print(float("{0:.2f}".format(sum1/num)), end="")
                print("/" + self.__max_asg1)

                break

            elif tmp == "A2":
                print("A2 average: ", end="")
                keys = self.__asg2Info.keys()
                for x in sorted(keys):
                    num += 1
                    sum1 += int(self.__asg2Info.get(x))

                print(float("{0:.2f}".format(sum1/num)), end="")
                print("/" + self.__max_asg2)

                break

            elif tmp == "PR":
                print("PR average: ", end="")
                keys = self.__prjInfo.keys()
                for x in sorted(keys):
                    num += 1
                    sum1 += int(self.__prjInfo.get(x))

                print(float("{0:.2f}".format(sum1/num)), end="")
                print("/" + self.__max_prj)

                break

            elif tmp == "T1":
                print("T1 average: ", end="")
                keys = self.__test1Info.keys()
                for x in sorted(keys):
                    num += 1
                    sum1 += int(self.__test1Info.get(x))

                print(float("{0:.2f}".format(sum1/num)), end="")
                print("/" + self.__max_test1)

                break

            elif tmp == "T2":
                print("T2 average: ", end="")
                keys = self.__test2Info.keys()
                for x in sorted(keys):
                    num += 1
                    sum1 += int(self.__test2Info.get(x))

                print(float("{0:.2f}".format(sum1/num)), end="")
                print("/" + self.__max_test2)

                break

            else:
                print("Enter a valid component.")

    def sort_by(self):
        tmpd = {}
        tmpg = {}
        keys = self.__stInfo.keys()
        for x in keys:
            fname = self.__stInfo.get(x).split(",")
            tmpd[x] = fname[1]

        for x in keys:
            asg1_marks = self.__asg1Info.get(x)
            asg2_marks = self.__asg2Info.get(x)
            prj_marks = self.__prjInfo.get(x)
            test1_marks = self.__test1Info.get(x)
            test2_marks = self.__test2Info.get(x)
            sum1 = 0
            if asg1_marks is not None and asg1_marks.isdigit():
                sum1 += int(asg1_marks)/int(self.__max_asg1) * 7.5

            if asg2_marks is not None and asg2_marks.isdigit():
                sum1 += int(asg2_marks)/int(self.__max_asg2) * 7.5

            if prj_marks is not None and prj_marks.isdigit():
                sum1 += int(prj_marks)/int(self.__max_prj) * 25

            if test1_marks is not None and test1_marks.isdigit():
                sum1 += int(test1_marks)/int(self.__max_test1) * 30

            if test2_marks is not None and test2_marks.isdigit():
                sum1 += int(test2_marks)/int(self.__max_test2) * 30

            tmpg[x] = sum1

        while True:
            print("Enter the criteria for sorting (LT <last name> or GR <numeric grade>):")
            tmp = sys.stdin.readline().upper().strip()
            if tmp == "LT":
                print("ID    LN     FN     A1  A2  PR  T1  T2  GR    FL")
                for x in sorted(tmpd.items(), key=lambda y: (y[1].upper(), y[1].islower())):
                    sys.stdout.write("%-6s" % x[0])
                    mystring = self.__stInfo.get(x[0]).split(",")
                    sys.stdout.write("%-6s %-7s" % (mystring[1], mystring[0]))
                    asg1_marks = self.__asg1Info.get(x[0])
                    asg2_marks = self.__asg2Info.get(x[0])
                    prj_marks = self.__prjInfo.get(x[0])
                    test1_marks = self.__test1Info.get(x[0])
                    test2_marks = self.__test2Info.get(x[0])
                    if asg1_marks is None:
                        sys.stdout.write("    ")
                    else:
                        sys.stdout.write("%-4s" % asg1_marks)
                    if asg2_marks is None:
                        sys.stdout.write("    ")
                    else:
                        sys.stdout.write("%-4s" % asg2_marks)
                    if prj_marks is None:
                        sys.stdout.write("    ")
                    else:
                        sys.stdout.write("%-4s" % prj_marks)
                    if test1_marks is None:
                        sys.stdout.write("    ")
                    else:
                        sys.stdout.write("%-4s" % test1_marks)
                    if test2_marks is None:
                        sys.stdout.write("    ")
                    else:
                        sys.stdout.write("%-4s" % test2_marks)
                    sum1 = 0
                    if asg1_marks is not None and asg1_marks.isdigit():
                        sum1 += int(asg1_marks) / int(self.__max_asg1) * 7.5

                    if asg2_marks is not None and asg2_marks.isdigit():
                        sum1 += int(asg2_marks) / int(self.__max_asg2) * 7.5

                    if prj_marks is not None and prj_marks.isdigit():
                        sum1 += int(prj_marks) / int(self.__max_prj) * 25

                    if test1_marks is not None and test1_marks.isdigit():
                        sum1 += int(test1_marks) / int(self.__max_test1) * 30

                    if test2_marks is not None and test2_marks.isdigit():
                        sum1 += int(test2_marks) / int(self.__max_test2) * 30

                    sys.stdout.write("%-6s" % float("{0:.2f}".format(sum1)))
                    if sum1 >= 94:
                        sys.stdout.write("A+")
                    elif sum1 >= 87:
                        sys.stdout.write("A")
                    elif sum1 >= 80:
                        sys.stdout.write("A-")
                    elif sum1 >= 73:
                        sys.stdout.write("B+")
                    elif sum1 >= 66:
                        sys.stdout.write("B")
                    elif sum1 >= 59:
                        sys.stdout.write("B-")
                    elif sum1 >= 50:
                        sys.stdout.write("C")
                    else:
                        sys.stdout.write("F")

                    print("\n", end="")

                break

            elif tmp == "GR":
                print("ID    LN     FN     A1  A2  PR  T1  T2  GR    FL")
                for x in sorted(tmpg.items(), key=lambda y: y[1], reverse=True):
                    sys.stdout.write("%-6s" % x[0])
                    mystring = self.__stInfo.get(x[0]).split(",")
                    sys.stdout.write("%-6s %-7s" % (mystring[1], mystring[0]))
                    asg1_marks = self.__asg1Info.get(x[0])
                    asg2_marks = self.__asg2Info.get(x[0])
                    prj_marks = self.__prjInfo.get(x[0])
                    test1_marks = self.__test1Info.get(x[0])
                    test2_marks = self.__test2Info.get(x[0])
                    agg = tmpg[x[0]]
                    if asg1_marks is None:
                        sys.stdout.write("    ")
                    else:
                        sys.stdout.write("%-4s" % asg1_marks)
                    if asg2_marks is None:
                        sys.stdout.write("    ")
                    else:
                        sys.stdout.write("%-4s" % asg2_marks)
                    if prj_marks is None:
                        sys.stdout.write("    ")
                    else:
                        sys.stdout.write("%-4s" % prj_marks)
                    if test1_marks is None:
                        sys.stdout.write("    ")
                    else:
                        sys.stdout.write("%-4s" % test1_marks)
                    if test2_marks is None:
                        sys.stdout.write("    ")
                    else:
                        sys.stdout.write("%-4s" % test2_marks)
                    sys.stdout.write("%-6s" % float("{0:.2f}".format(agg)))
                    if agg >= 94:
                        sys.stdout.write("A+")
                    elif agg >= 87:
                        sys.stdout.write("A")
                    elif agg >= 80:
                        sys.stdout.write("A-")
                    elif agg >= 73:
                        sys.stdout.write("B+")
                    elif agg >= 66:
                        sys.stdout.write("B")
                    elif agg >= 59:
                        sys.stdout.write("B-")
                    elif agg >= 50:
                        sys.stdout.write("C")
                    else:
                        sys.stdout.write("F")

                    print("\n", end="")

                break

            else:
                print("Enter a valid label.")

    def changepf(self):
        while True:
            print("Enter a new Pass/Fail point:")
            pf = sys.stdin.readline().strip()
            if pf.replace('.', '', 1).isdigit():
                if float(pf) <= 0 or float(pf) >= 100:
                    print("Enter a number between 0 and 100")
                    continue
                else:
                    newp = float(pf)
                    print("ID    LN     FN     A1  A2  PR  T1  T2  GR    FL")
                    keys = self.__stInfo.keys()
                    for x in sorted(keys):
                        sys.stdout.write("%-6s" % x)
                        mystring = self.__stInfo.get(x).split(",")
                        sys.stdout.write("%-6s %-7s" % (mystring[1], mystring[0]))
                        asg1_marks = self.__asg1Info.get(x)
                        asg2_marks = self.__asg2Info.get(x)
                        prj_marks = self.__prjInfo.get(x)
                        test1_marks = self.__test1Info.get(x)
                        test2_marks = self.__test2Info.get(x)
                        if asg1_marks is None:
                            sys.stdout.write("    ")
                        else:
                            sys.stdout.write("%-4s" % asg1_marks)
                        if asg2_marks is None:
                            sys.stdout.write("    ")
                        else:
                            sys.stdout.write("%-4s" % asg2_marks)
                        if prj_marks is None:
                            sys.stdout.write("    ")
                        else:
                            sys.stdout.write("%-4s" % prj_marks)
                        if test1_marks is None:
                            sys.stdout.write("    ")
                        else:
                            sys.stdout.write("%-4s" % test1_marks)
                        if test2_marks is None:
                            sys.stdout.write("    ")
                        else:
                            sys.stdout.write("%-4s" % test2_marks)
                        sum1 = 0
                        if asg1_marks is not None and asg1_marks.isdigit():
                            sum1 += int(asg1_marks) / int(self.__max_asg1) * 7.5

                        if asg2_marks is not None and asg2_marks.isdigit():
                            sum1 += int(asg2_marks) / int(self.__max_asg2) * 7.5

                        if prj_marks is not None and prj_marks.isdigit():
                            sum1 += int(prj_marks) / int(self.__max_prj) * 25

                        if test1_marks is not None and test1_marks.isdigit():
                            sum1 += int(test1_marks) / int(self.__max_test1) * 30

                        if test2_marks is not None and test2_marks.isdigit():
                            sum1 += int(test2_marks) / int(self.__max_test2) * 30

                        sys.stdout.write("%-6s" % float("{0:.2f}".format(sum1)))
                        range1 = (100-newp)/7
                        if sum1 >= 100 - range1:
                            sys.stdout.write("A+")
                        elif sum1 >= 100 - (2 * range1):
                            sys.stdout.write("A")
                        elif sum1 >= 100 - (3 * range1):
                            sys.stdout.write("A-")
                        elif sum1 >= 100 - (4 * range1):
                            sys.stdout.write("B+")
                        elif sum1 >= 100 - (5 * range1):
                            sys.stdout.write("B")
                        elif sum1 >= 100 - (6 * range1):
                            sys.stdout.write("B-")
                        elif sum1 >= newp:
                            sys.stdout.write("C")
                        else:
                            sys.stdout.write("F")

                        print("\n", end="")
                break
            else:
                print("Enter a valid number.")
