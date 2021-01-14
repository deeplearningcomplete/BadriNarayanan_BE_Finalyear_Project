import os
import colors
import sys
var = 1
while var==1:

        with colors.pretty_output(colors.BOLD, colors.FG_GREEN) as out:
                print()
                print()
        with colors.pretty_output(colors.BOLD, colors.FG_RED) as out:
                out.write("WELCOME TO SUMMARIZATION")
                print()
        with colors.pretty_output(colors.BOLD, colors.FG_GREEN) as out:
                #print("THE OPTIONS AVAILABLE ARE SINGLE DOCUMENT SUMMARIZATION",end = " ") 
                #print("and MULTIPLE DOCUMENT SUMMARIZATION")
                print()
                out.write("PRESS 1 FOR SINGLE DOCUMENT SUMMARIZATION")
                print()
                out.write("PRESS 2 FOR MULTIPLE DOCUMENT SUMMARIZATION")
                print()
                out.write("PRESS 3 TO EXIT")
                print()
        methodselection = input()
        print()

        with colors.pretty_output(colors.BOLD, colors.FG_YELLOW) as out:
                print("THANK YOU FOR YOUR SELECTION")
                print()

        if methodselection == "1":
                os.system('python  summarization.py')

        if methodselection == "2":
                 os.system('python ./News-Summarizer/driver.py')

        if methodselection == "3":
                 sys.exit()
        print()
        print()
        takeinput = input("DO YOU WANT ANOTHER SUMMARY TO BE DONE ?  PLEASE GIVE  YES OR NO  ")
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
