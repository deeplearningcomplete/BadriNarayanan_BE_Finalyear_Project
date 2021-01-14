import colors

with colors.pretty_output(colors.BOLD, colors.FG_RED) as out:
    out.write("This is a bold red text")

with colors.pretty_output(colors.BG_GREEN) as out:
    out.write("This output have a green background but you " + 
               colors.BOLD + colors.FG_RED + "can" + colors.END + " mix styles")
