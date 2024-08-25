import wx
from form import form as source_form
import os

class dialog_About(source_form.Dialog_About):

    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent)
        # cwd_path = os.getcwd() # returns entrypoint path
        # rel_img_path = r"res\MusoSuppliesLogoAlphaSmall.png"
        # full_img_path = os.path.join(cwd_path, rel_img_path)
        # self.m_bitmap_CompanyLogo.SetBitmap(wx.Bitmap(full_img_path, wx.BITMAP_TYPE_ANY))
        self.Show()


    def Dialog_BuildingNameEditOnClose(self, event):
        self.switchback_to_parent()

    def m_button_OKOnButtonClick(self, event):
        self.switchback_to_parent()

    def switchback_to_parent(self):
        """
        function to do necessary actions before switching back to parent
        Returns:
        """
        self.parent.Show()
        self.Destroy()

