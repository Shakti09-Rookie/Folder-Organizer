import tkinter
from tkinter import filedialog
from tkinter import *
import os
import shutil
#formatting
formats = {
    "video_formats" : [".mp4", ".m4a", ".m4v", ".f4v", ".f4a", ".m4b", ".m4r", ".f4b", ".mov", ".3gp", ".wmv", ".avi"],
    "doc_formats" : [".doc", ".docx", ".ppt", ".pptx", ".xlsx", ".xls", ".txt", ".csv", ".dif", ".pdf",".vcf"],
    "image_format" : [".jpg", ".jpeg", ".tiff", ".bmp", ".raw"],
    "executables" : [".exe", ".ini"],
    "codes" : [".c", ".cpp", ".java", ".py",".html", ".css"]
}

def sourcefolder():
    #root.withdraw()
    global folder_selected_source
    folder_selected_source = filedialog.askdirectory()

def destinationfolder():
    #root.withdraw()
    global folder_selected_destination
    folder_selected_destination = filedialog.askdirectory()


# for key,values in formats.items():
#     for value in values:

def searching(fname):
    for key,values in formats.items():
        for value in values:
            if(fname.endswith(value)):
                return key

def Organizing():
    for fname in os.listdir(folder_selected_source):
        fname_path = os.path.join(folder_selected_source, fname)
        which_type = searching(fname)
        if (which_type == "video_formats"):
            path = os.path.join(folder_selected_destination, "Videos")
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                pass
        elif (which_type == "doc_formats"):
            path = os.path.join(folder_selected_destination, "Documents")
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                pass
        elif (which_type == "image_format"):
            path = os.path.join(folder_selected_destination, "Images")
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                pass
        elif (which_type == "executables"):
            path = os.path.join(folder_selected_destination, "Applications")
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                pass
        elif (which_type == "codes"):
            path = os.path.join(folder_selected_destination, "Codes")
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                pass
        else:
            path = os.path.join(folder_selected_destination, "Extras")
            if not os.path.exists(path):
                os.mkdir(path)
            else:
                pass
        file = os.path.isfile(fname_path)
        if(file == True):
            #for complete change copy to move
            shutil.copy(fname_path, path)
        else:
            pass
        # shutil.copy(fname_path, path)
    print("Done")


root=tkinter.Tk()
root.title("File Organizer")
label=tkinter.Label(root,text = "Now Organize folers with ease and make folders clutter free")
label.pack()
source_folder = tkinter.Button(root, text = "Source Folder", command = sourcefolder )
source_folder.pack()
target_destination = tkinter.Button(root, text = "Destination Folder", command = destinationfolder )
target_destination.pack()
organize_n = tkinter.Button(root, text = "Organize", command = Organizing )
organize_n.pack()
root.mainloop()
