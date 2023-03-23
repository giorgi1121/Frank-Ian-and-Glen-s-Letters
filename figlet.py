#main function which prompts user input text and prints it in appropriate font
def main():
    text = input("Input: ")
    print(figlet(text))

#figlet function which convert str text into appropriate font
def figlet(text):
    #import moduls and define figlet and fonts
    import sys
    import random

    from pyfiglet import Figlet

    figlet = Figlet()

    fonts = figlet.getFonts()

    #check the number of command-line arguments

    #if there is only zero argument program shoulde choose font by random
    if len(sys.argv) == 1:
        figlet.setFont(font= random.choice(fonts))

    #if here is 3 arguments then check if argument on first position is "-f" or "--font"
    #if True then define argumen on second position as desired font
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        desired_font = sys.argv[2]
        #check if desired font is in fonts, if not exit via sys.exit with an error message
        if desired_font in fonts:
            figlet.setFont(font= desired_font)
        else:
            sys.exit("Invalid usage")

    #return value of converted text
    return figlet.renderText(text)

#call main function
main()
