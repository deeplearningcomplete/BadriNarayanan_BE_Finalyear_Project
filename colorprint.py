
import colors

with colors.pretty_output(colors.BOLD, colors.FG_RED) as out:
    print()
    out.write("THE AVAILABLE OPTIONS ARE ")
    print()
    out.write("VOTING  GULFWAR  PARLIAMENT  WORLD BANK")
    print()
with colors.pretty_output(colors.BOLD, colors.FG_GREEN) as out:
    out.write("PRESS 1 FOR VOTING INFO")
    print()
    out.write("PRESS 2 FOR GULFWAR INFO")
    print()
    out.write("PRESS 3 FOR PARLIAMENT INFO")
    print()
    out.write("PRESS 4 FOR WORLD-BANK INFO")
    print()
    out.write("PRESS 5 FOR ANY OTHER INFORMATION")
    print()
    out.write("PRESS 6 FOR EXIT")
    print()
domain = input("CHOOSE AN OPTION  ")
print()
