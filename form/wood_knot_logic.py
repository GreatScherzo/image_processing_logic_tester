from form import form as source_form
import wx
import img_logic
import numpy as np
import cv2 as cv

class frame_LoadImage(source_form.Frame_WoodKnotLogic):
    def __init__(self, parent):
        super().__init__(parent)
        # ###############################################################################
        # Other frame handler
        # ###############################################################################
        self.parent = parent

        # Display loaded image and enable run button
        if self.parent.LoadedImageDisplay != None:
            self.m_bitmap_InputImage.SetBitmap(self.parent.LoadedImageDisplay)
            self.m_button_Run.Enable()

    # ###############################################################################
    # Image Processing Events
    # ###############################################################################

    def m_button_RunOnButtonClick(self, event):

        # Get every parameter
        mean_filter_size = self.m_spinCtrl_MeanFilterSize.GetValue()
        adaptive_threshold_offset = self.m_spinCtrl_AdaptThreshOffset.GetValue()
        light_dark_selection = self.m_choice_LightDarkPart.Selection
        if light_dark_selection == 0:
            dark_flag = True
        else:
            dark_flag = False

        erode_kernel_size = self.m_spinCtrl_ErodeKernelSize.GetValue()
        opening_kernel_size = self.m_spinCtrl_OpeningKernelSize.GetValue()

        try:
            result = img_logic.DynamicThresholdLogic(self.parent.LoadedImage,
                                                     MeanImgKernelSize=[mean_filter_size, mean_filter_size],
                                                     DynamicThresholdOffset=adaptive_threshold_offset,
                                                     IsDark=dark_flag,
                                                     ErosionKernelSize=[erode_kernel_size, erode_kernel_size],
                                                     OpeningKernelSize=[opening_kernel_size, opening_kernel_size]
                                                     )

            # Do the usual preprocessing to show in result staticbitmapview
            stacked_grey_buf = np.stack([result, result, result], axis=2)

            # get size of bitmap view
            # for some weird reason, the size increases when run is pressed immediately without any parameter change
            size_frame_height = 200
            size_frame_width = 266
            # size_frame_height = self.m_bitmap_ResultImage.GetSize().height
            # size_frame_width = self.m_bitmap_ResultImage.GetSize().width

            buf_height = result.shape[0]
            buf_width = result.shape[1]
            # Resize, but adaptive to maintain aspect ratio of input image
            adaptive_width = int((buf_width/buf_height)*size_frame_height)

            # stacked_grey_buf_resized = cv2.resize(stacked_grey_buf, (size_frame_width, size_frame_height))
            stacked_grey_buf_resized = cv.resize(stacked_grey_buf, (adaptive_width, size_frame_height))

            bmp = wx.Bitmap.FromBuffer(adaptive_width, size_frame_height, stacked_grey_buf_resized)
            self.m_bitmap_ResultImage.SetBitmap(bmp)

        except Exception as e:
            wx.MessageBox("Failed processing image.\n {0}".format(str(e)),
                          "Operation Error", wx.ICON_ERROR | wx.OK)
            return

    # ###############################################################################
    # Navigation Events
    # ###############################################################################
    def m_button_BackOnButtonClick(self, event):
        self.parent.Layout()
        self.parent.Show()
        self.Destroy()

    # ###############################################################################
    # Close Event
    # ###############################################################################
    def Frame_WoodKnotLogicOnClose(self, event):
        if event.CanVeto():
            if wx.MessageBox("Are you sure you want to exit program?", "Confirm exit",
                             wx.ICON_WARNING | wx.YES_NO) != wx.YES:
                event.Veto()
                return
        self.parent.Destroy()
        self.Destroy()

    # def m_button_ExitOnButtonClick( self, event ):
    #     if wx.MessageBox("Are you sure you want to exit program?", "Confirm exit",
    #                      wx.ICON_WARNING | wx.YES_NO) != wx.YES:
    #         return
    #     self.Destroy()
