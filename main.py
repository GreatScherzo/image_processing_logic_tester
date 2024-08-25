# import img_logic
#
# if __name__ == '__main__':
#
#     img_logic.DynamicThresholdLogic()


# Entrypoint
from form import main_menu
import logging
import wx
# from controller import form_event_methods as forms
enable_debug = False


if __name__ == '__main__':
    app = wx.App()

    # Initialize logging format
    if enable_debug:
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                            level=logging.DEBUG,
                            filename='./log.txt',
                            filemode='a')

    # Enter from main menu frame
    MyMenu = main_menu.frame_MainMenu(parent=None)
    MyMenu.Show()
    logging.debug("Main menu form shown")
    app.MainLoop()