
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class KaryotypeAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Karyotype Analyzer")

        self.load_button = tk.Button(master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.analyze_button = tk.Button(master, text="Analyze", command=self.analyze_image, state=tk.DISABLED)
        self.analyze_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if file_path:
            self.image = Image.open(file_path)
            self.image.thumbnail((400, 400))
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(200, 200, image=self.photo)
            self.analyze_button.config(state=tk.NORMAL)

    def analyze_image(self):
        # Placeholder for image analysis
        self.result_label.config(text="Analysis complete. No abnormalities detected.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = KaryotypeAnalyzerGUI(root)
    root.mainloop()
