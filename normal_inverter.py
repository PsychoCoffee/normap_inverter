from PIL import Image
import os

print("|---------------------|")
print("|   normap_inverter   |")
print("|     by luka beg     |")
print("|      (c) 2023       |")
print("|---------------------|")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def askForLoop():
    a = input("\nDo you wish to continue?\n\n(a)->Yes\n(b)->No\n\nChoice:")
    if(a.lower() == "a"):
        clear()
        loop()
    elif(a.lower() == "b"):
        exit()
    else:
        askForLoop()

def work():
    #Loading
    input_image_path = input("Normal Texture: ").strip('"')
    input_image_path = os.path.normpath(input_image_path)
    input_image = Image.open(input_image_path)

    #Invert the red and green channels of the normal map
    inverted_data = [(255 - r, 255 - g, b) for (r, g, b) in input_image.getdata()]
    inverted_image = Image.new(input_image.mode, input_image.size)
    inverted_image.putdata(inverted_data)

    #Saving
    output_path = os.path.splitext(os.path.basename(input_image_path))[0] + "_inverted.png"
    inverted_image.save(output_path)
    print("-----------------------\nSucessfully saved to", output_path, "\n-----------------------")
    
    #Loop check
    askForLoop()

work()
