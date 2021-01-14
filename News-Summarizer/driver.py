# driver.py
# Luke Reichold - CSCI 4930
import colors
import sys
import os
from summarize import Summarizer

argentina_articles = ["argentina/argentina-guardian.txt", "argentina/argentina-nyt.txt"]
china_articles = ["china/china-cnn.txt", "china/china-nyt.txt"]
climate_articles = ["climate/climate-npr.txt", "climate/climate-nyt.txt"]
VW_articles = ["VW/VW-ars.txt", "VW/VW-nyt.txt"]
other_articles = ["otherdomain/otherdomain_one.txt", "otherdomain/otherdomain_two.txt"]

print()
with colors.pretty_output(colors.BOLD, colors.FG_RED) as out:
    out.write("THE AVAILABLE OPTIONS ARE")
    print()
    out.write("ARGENTINA CHINA CLIMATE-CHANGE VOLKS-WAGEN ")
with colors.pretty_output(colors.BOLD, colors.FG_GREEN) as out:
    print()
    out.write("PRESS 1 FOR ARGENTINA ARTICLES")
    print()
    out.write("PRESS 2 FOR CHINA ARTICLES")
    print()
    out.write("PRESS 3 FOR CLIMATE CHANGE ARTICLES")
    print()
    out.write("PRESS 4 FOR VOLKS WAGEN CAR EMISSION STARNDARDS ARTICLES")
    print()
    out.write("PRESS 5 FOR OTHER ARTICLES")
    print()
    out.write("PRESS 6 FOR EXIT")
    print()

yourinput = input()
if yourinput == "1":
    magic = Summarizer(argentina_articles)
if yourinput == "2":
    magic = Summarizer(china_articles)
if yourinput == "3":
    magic = Summarizer(climate_articles)
if yourinput == "4":
    magic = Summarizer(VW_articles)
if yourinput == "5":
    magic = Summarizer(other_articles)
if yourinput == "6":
    sys.exit()

#magic = Summarizer(yourvariable)
#print(magic.generate_summaries())
f =  open("demofile2.txt", "a")
fp = open("demofile2.pdf", "a")
f.write(magic.generate_summaries())
f.close()
fp.close()
os.system('python scriptone.py')
