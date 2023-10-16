import sys
import pyfiglet

if len(sys.argv) not in [1, 3] or (len(sys.argv) == 3 and sys.argv[1] not in ['-f', '--font']):
    sys.exit("Invalid usage")

if len(sys.argv) == 3:
    font_name = sys.argv[2]
    try:
        pyfiglet.Figlet(font=font_name)
    except pyfiglet.FontNotFound:
        sys.exit("font not found")
    custom_figlet = pyfiglet.Figlet(font=font_name)
else:
    custom_figlet = pyfiglet.Figlet()

text = input("Input: ")
print(custom_figlet.renderText(text))
