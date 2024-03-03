from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar
from Basic_code import open_camera_for_duration
from PIL import Image, ImageDraw
import requests
import os
import shutil



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")
IMAGES_PATH = OUTPUT_PATH / Path(r"./png_images")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def relative_to_images(path: str) -> Path:
    return IMAGES_PATH / Path(path)



def convert_images_to_png(input_folder, output_folder):
    # Ensure the output folder exists
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    # Create a new output folder
    os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    for file_name in files:
        # Check if the file is an image
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Build the full path for the input image
            input_path = os.path.join(input_folder, file_name)

            # Load the image
            img = Image.open(input_path)
            target_size = (300,300)

            # Resize the image
            img = img.resize(target_size, Image.LANCZOS)

            # Construct the output file path with a '_cropped.png' extension
            output_file_name = os.path.splitext(file_name)[0] + '.png'
            output_path = os.path.join(output_folder, output_file_name)

            # Save the cropped image in PNG format
            img.save(output_path, 'PNG')

            print(f"Converted, resized, and cropped {file_name} to {output_file_name}")





convert_images_to_png ("./Images", "./png_images")


class FaceRecognitionApp:
    def __init__(self, master):

        self.master = master
        self.master.title("Attenddance App")
        #self.master.iconbitmap("icon.ico")


        self.master.geometry("1000x600")
        self.master.configure(bg = "#344955")

        self.name = "Waiting ..."


        self.canvas = Canvas(
            master,
            bg = "#344955",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1000.0,
            72.0,
            fill="#E5BEEC",
            outline="")

        self.canvas.create_text(
            100.0,
            10.0,
            anchor="nw",
            text="ATTENDANCE SYSTEM",
            fill="#1C1A1A",
            font=("InriaSans Bold", 40 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            54.0,
            36.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            227.0,
            316.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            107.0,
            169.0,
            anchor="nw",
            text="Click the button ",
            fill="#FFFFFF",
            font=("InriaSerif Bold", 32 * -1)
        )

        self.canvas.create_text(
            650.0,
            465.0,
            anchor="nw",
            text= "Waiting ...",
            fill="#FFFFFF",
            font=("InriaSerif Bold", 36 * -1)
        )
        

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            730.0,
            300.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            78.0,
            211.0,
            anchor="nw",
            text="below to mark your ",
            fill="#FFFFFF",
            font=("InriaSerif Bold", 32 * -1)
        )

        self.canvas.create_text(
            135.0,
            255.0,
            anchor="nw",
            text="attendance",
            fill="#FFFFFF",
            font=("InriaSerif Bold", 32 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.person_name,
            relief="flat"
        )

        self.button_1.place(
            x=160.0,
            y=378.0,
            width=100.0,
            height=40.0
        )

    def person_name(self):
        self.name, self.accuracy = open_camera_for_duration(10)



        self.image_image_3 = PhotoImage(
            file=relative_to_images(f"{self.name}.png"))
        self.image_3 = self.canvas.create_image(
            730.0,
            300.0,
            image=self.image_image_3
        )

        self.canvas.create_rectangle(
            650.0,
            465.0,
            900.0,
            520.0,
            fill="#344955",
            outline="")

        self.canvas.create_text(
            750.0,
            465.0,
            anchor="n",
            text= "Hi " +self.name,
            fill="#FFFFFF",
            font=("InriaSerif Bold", 36 * -1)
        )
    


if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionApp(root)
    root.resizable(False, False)
    root.mainloop()
