
import pandas as pd
import numpy as np
from time import sleep
import pyautogui
import pywinauto
from pywinauto import Desktop, application, keyboard
import warnings
from tkinter.filedialog import askopenfilename
from tkinter import Tk
# pillow
"""
connor
June 2022
"""
    
    
def main():
    ''' main function to prompt the user and pass out task'''
    
    try:
        print("Enter the number of what would you like to do... cntrl c to cancel\n",
          "1) Load an excel doc of tags.\n",
          "2) Open a spec.\n",
          "3) Create a spec. - not implemented yet")
        choice = input("=> ")
        if choice == '1': # load an excel doc
            tag = get_tag_file()
            wd = connect_to('Smart Instrumentation')
            create_tags(wd,tag)
        elif choice == '2': # open a specific spec
            tag = get_tag_input()
            print("Opening tag",tag)
            wd = connect_to('Smart Instrumentation')
            open_spec(wd,tag)
        elif choice == '3': # create a spec
            print("This is not ready yet")
            main()
            quit()
        else:
            print(" ***\n please select a proper choice or press cntrl c to cancel\n ***\n")
            main()
            quit()
    except KeyboardInterrupt:
        print("bye bye")
        quit()


'''=============================================================================
                Option 1: Load an excel doc and create tags
=============================================================================='''

def create_tags(wd,tags):
    # start instrument index module
    click_on('images\\inst_index.png')
    
    for tag in tags:
        # send tag name
        click_on('images\\create_tag.png')
        for t in tag:
            keyboard.send_keys(t)
            keyboard.send_keys('{TAB}')
        keyboard.send_keys('{ENTER}')
        sleep(2)
        keyboard.send_keys('{ENTER}')

'''=============================================================================
                Option 2: 
=============================================================================='''

def open_spec(wd,tag):
    # start the spec module
    click_on('images\\spec_index.png')
    click_on('images\\create_spec.png')
    for t in tag:
        keyboard.send_keys(t)
        keyboard.send_keys('{TAB}')
    keyboard.send_keys('{ENTER}')
    
def get_tag_input():
    tag_type = input("Input tag type (ex PT, TE): ")
    line_num = input("Input line number (ex 1001): ")
    suffix = input("Enter suffix (ex A, 1): ")
    return np.array([tag_type, line_num])    
    
'''=============================================================================
                Option 3: 
=============================================================================='''
    
def create_spec(wd):
    return True


'''=============================================================================
                Helper Functions 
=============================================================================='''
    
def get_tag_file():
    ''' prompts the user to select an excel doc with tags. columns must be PT,1000,A '''
    FILE_NAME = "test_input.xlsx"
    prmpt = input("This will read from "+FILE_NAME+". \nEnter y to continue, c to select a different file, or something else to cancel: ")
    if prmpt == 'c':
        # file prompt for a new xlsx file
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        c_filename = askopenfilename(title='select tag file', filetypes=[
                    ("all excel formats", ".xls"),
                    ("all excel formats", ".xlsx"),
                    ("all excel formats", ".xlsm")]) # show an "Open" dialog box and return the path to the selected file
        if c_filename == '':
            quit() #user hit cancel
        return pd.read_excel(c_filename).to_numpy(dtype=str)
    elif prmpt != 'y':
        quit()
    return pd.read_excel(FILE_NAME).to_numpy(dtype=str)

def connect_to(name):
    ''' wrapper for a window object with the name of the passed string '''
    warnings.simplefilter('ignore', category=UserWarning)
    try:
        w_hnd = pywinauto.findwindows.find_windows(title_re=r''+name+'.*')[0]
    except IndexError:
        print(" ** ERROR: Please open an instance of SPI.")
        quit()
    wd = application.Application(backend="win32").connect(handle=w_hnd).top_window()
    wd.set_focus()
    return wd
    
def click_on(img):
    ''' wrapper to click on a image stored in cur.path\images '''
    try:
        pyautogui.click(pyautogui.locateOnScreen(img))
    except:
        try: # try one more time
            sleep(2)
            pyautogui.click(pyautogui.locateOnScreen(img))
        except:
            print('Image could not be found.')
            quit()

if __name__ == "__main__":
    main()