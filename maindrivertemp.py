import os
import colors
import sys
var = 1
while var==1:

        with colors.pretty_output(colors.BOLD, colors.FG_GREEN) as out:
                print()
                print()
        with colors.pretty_output(colors.BOLD, colors.FG_RED) as out:
                out.write("WELCOME TO THE BE CSE FINAL YEAR PROJECT ON SUMMARIZATION")
                print()
        with colors.pretty_output(colors.BOLD, colors.FG_YELLOW) as out:
                out.write("PROJECT GUIDE:  PARAMESH R")
                print()
        with colors.pretty_output(colors.BOLD, colors.FG_RED) as out:
                out.write("THE GROUP MEMBERS ARE")
                print()
                out.write("ABHIRATH G")
                out.write("ABHUVAN M")
                out.write("AKSHAY ACHARYA H R")
                out.write("BADRI NARAYANAN G")
                print()
        with colors.pretty_output(colors.BOLD, colors.FG_GREEN) as out:
                #print("THE OPTIONS AVAILABLE ARE SINGLE DOCUMENT SUMMARIZATION",end = " ") 
                #print("and MULTIPLE DOCUMENT SUMMARIZATION")
                print()
                out.write("PRESS 1 for SINGLE DOCUMENT Summarization")
                print()
                out.write("PRESS 2 for MULTIPLE DOCUMENT Summarization")
                print()
                out.write("PRESS 3 to EXIT")
                print()
        methodselection = input()
        print()

        with colors.pretty_output(colors.BOLD, colors.FG_YELLOW) as out:
                print("Thank you for your selection")
                print()

        if methodselection == "1":
                os.system('python  summarization.py')

        if methodselection == "2":
                 os.system('python ./News-Summarizer/driver.py')

        if methodselection == "3":
                 sys.exit()
        print()
        print()
        takeinput = input("DO YOU WANT ANOTHER SUMMARY TO BE DONE ?  Please Give yes or no  ")
        print()
        if takeinput == "yes":
                continue;
        else:
                with colors.pretty_output(colors.BOLD, colors.FG_YELLOW) as out:
                        out.write("THANK YOU FOR USING OUR SUMMARIZATION PROJECT")
                        print()
                        out.write("HAVE A GREAT DAY")
                        print()
                        sys.exit()
