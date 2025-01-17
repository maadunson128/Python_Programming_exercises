#Program: using file dialogs for some problems

from tkinter.filedialog import askopenfilename , asksaveasfilename

def main()->None:

    infile = askopenfilename()
    outfile = asksaveasfilename()

main()
