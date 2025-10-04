import pyautogui as spammer
from time import sleep
from keyboard import is_pressed

timer = list(range(10))
timer.reverse()

if __name__ == "__main__":
    print(" Welcome to SpamBotWabot ".center(100,"-"),end="\n\n")
    text = input("Enter spam text and press 'q' to stop spamming: ")
    for i in timer:
        print(f'Spaming in {i+1} seconds')
        sleep(1)
    while True:
        if is_pressed("q"):
            print("\n\n" + (" Thanks for using ".center(100,"-")))
            break
        spammer.write(text)
        spammer.press("enter")