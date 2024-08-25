"""
Python file that holds mains menu form

"""
import os

# Import all forms here
from form import form as source_form
from form import load_image
from form import wood_knot_logic
from form import help
from form import about_dialog

import wx



class frame_MainMenu(source_form.Frame_MainMenu):
    def __init__(self, parent):
        super().__init__(parent)
        # ###############################################################################
        # Other frame handler
        # ###############################################################################
        self.parent = parent
        self.LoadImageFormHandler = None
        self.WoodKnotLogicFormHandler = None
        self.HelpDialogHandler = None
        self.AboutDialogHandler = None

        # Loaded image variable
        self.LoadedImage = None
        self.LoadedImageDisplay = None

        # Set image of the main menu
        # root_path = os.path.dirname(os.path.realpath(__file__)) # returns current python file path it is currently running
        cwd_path = os.getcwd() # returns entrypoint path
        rel_img_path = r"res\dental_clinic_img_final_600.jpg"
        full_img_path = os.path.join(cwd_path, rel_img_path)
        # self.m_bitmap1.SetBitmap(wx.Bitmap( full_img_path, wx.BITMAP_TYPE_ANY ))


    # ###############################################################################
    # Navigation Events
    # ###############################################################################
    # def m_button_PatientManagerOnButtonClick(self, event):
    #     self.Hide()
    #     self.PatientManagerFormHandler = patient_manager_form.frame_PatientManager(self)
    #     self.PatientManagerFormHandler.Layout()
    #     self.PatientManagerFormHandler.Show()
    #
    # def m_button_AboutOnButtonClick(self, event):
    #     self.Hide()
    #     self.AboutDialogHandler = about_dialog.dialog_About(self)
    #     self.AboutDialogHandler.Layout()
    #     self.AboutDialogHandler.Show()

    def m_button_LoadImageOnButtonClick(self, event):
        self.Hide()
        if self.LoadImageFormHandler is None:
            self.LoadImageFormHandler = load_image.frame_LoadImage(self)
        self.LoadImageFormHandler.Layout()
        self.LoadImageFormHandler.Show()

    def m_button_WoodKnotLogicOnButtonClick(self, event):
        self.Hide()
        # Destroyed form
        self.WoodKnotLogicFormHandler = wood_knot_logic.frame_LoadImage(self)
        self.WoodKnotLogicFormHandler.Layout()
        self.WoodKnotLogicFormHandler.Show()

    def m_button_HelpOnButtonClick(self, event):
        self.Hide()
        self.HelpDialogHandler = help.dialog_About(self)
        self.HelpDialogHandler.Layout()
        self.HelpDialogHandler.Show()

    def m_button_AboutOnButtonClick(self, event):
        self.Hide()
        self.AboutDialogHandler = about_dialog.dialog_About(self)
        self.AboutDialogHandler.Layout()
        self.AboutDialogHandler.Show()




    # ###############################################################################
    # Close Event
    # ###############################################################################
    def Frame_MainMenuOnClose(self, event):
        if event.CanVeto():
            if wx.MessageBox("Are you sure you want to exit program?", "Confirm exit",
                             wx.ICON_WARNING | wx.YES_NO) != wx.YES:
                event.Veto()
                return
        self.Destroy()

    # def m_button_ExitOnButtonClick( self, event ):
    #     if wx.MessageBox("Are you sure you want to exit program?", "Confirm exit",
    #                      wx.ICON_WARNING | wx.YES_NO) != wx.YES:
    #         return
    #     self.Destroy()

    # def _exit_functions(self, event):
    #     if event.CanVeto():
    #         if wx.MessageBox("Are you sure you want to exit program?", "Confirm exit",
    #                          wx.ICON_WARNING | wx.YES_NO) != wx.YES:
    #             event.Veto()
    #             return
    #
    #     self.Destroy()
