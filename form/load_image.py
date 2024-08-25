import cv2

from form import form as source_form
import wx
import cv2 as cv
import numpy as np
class frame_LoadImage(source_form.Frame_LoadImage):
    def __init__(self, parent):
        super().__init__(parent)
        # ###############################################################################
        # Other frame handler
        # ###############################################################################
        self.parent = parent

        # Variable
        self.ImagePath = None
        self.LoadedImage = None
        self.LoadedImageDisplay = None


    # ###############################################################################
    # Load Image Event
    # ###############################################################################

    def m_filePicker_ImageOnFileChanged(self, event):
        self.ImagePath = self.m_filePicker_Image.GetPath()
        try:
            buf = cv.imread(self.ImagePath, cv.IMREAD_GRAYSCALE)
            # self.m_bitmap1.SetBitmap(wx.Bitmap(full_img_path, wx.BITMAP_TYPE_ANY))

            # copied_buf = np.copy(buf)
            # create displaying image
            stacked_grey_buf = np.stack([buf, buf, buf], axis=2)

            # get size of bitmap view
            size_frame_height = self.m_bitmap_LoadImage.GetSize().Height
            size_frame_width = self.m_bitmap_LoadImage.GetSize().Width

            buf_height = buf.shape[0]
            buf_width = buf.shape[1]
            # Resize, but adaptive to maintain aspect ratio of input image
            adaptive_width = int((buf_width/buf_height)*size_frame_height)

            # stacked_grey_buf_resized = cv2.resize(stacked_grey_buf, (size_frame_width, size_frame_height))
            stacked_grey_buf_resized = cv2.resize(stacked_grey_buf, (adaptive_width, size_frame_height))



            # Set buffer
            # buf_height = buf.shape[0]
            # buf_width = buf.shape[1]
            # bmp = wx.Bitmap.FromBuffer(buf_width, buf_height, buf)

            # bmp = wx.Bitmap.FromBuffer(size_frame_width, size_frame_height, stacked_grey_buf_resized)
            bmp = wx.Bitmap.FromBuffer(adaptive_width, size_frame_height, stacked_grey_buf_resized)
            self.m_bitmap_LoadImage.SetBitmap(bmp)
            # wx.DC.DrawBitmap(wx.Bitmap.FromBuffer(iw, ih, cv_image), 0, 0)


            # Store image
            self.LoadedImage = buf
            self.LoadedImageDisplay = bmp

        except Exception as e:
            wx.MessageBox("Failed reading image data.\n {0}".format(str(e)),
                          "Operation Error", wx.ICON_ERROR | wx.OK)
            return


    # ###############################################################################
    # Navigation Events
    # ###############################################################################

    # def m_button_LoadImageOnButtonClick(self, event):
    #     self.Hide()
    #     self.LoadImageFormHandler = patient_manager_form.frame_PatientManager(self)
    #     self.PatientManagerFormHandler.Layout()
    #     self.PatientManagerFormHandler.Show()

    def m_button_OKOnButtonClick(self, event):
        # Store images to parent
        self.parent.LoadedImage = self.LoadedImage
        self.parent.LoadedImageDisplay = self.LoadedImageDisplay

        self.parent.Layout()
        self.parent.Show()
        self.Hide()

    def m_button_CancelOnButtonClick(self, event):
        self.parent.Layout()
        self.parent.Show()
        self.Hide()

    # ###############################################################################
    # Close Event
    # ###############################################################################
    def Frame_LoadImageOnClose(self, event):
        if event.CanVeto():
            if wx.MessageBox("Are you sure you want to exit program?", "Confirm exit",
                             wx.ICON_WARNING | wx.YES_NO) != wx.YES:
                event.Veto()
                return

        self.parent.Destroy()
        self.Destroy()
