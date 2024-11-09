
import tkinter as tk
from src.gui import KaryotypeAnalyzerGUI
from src.image_processor import analyze_karyotype
from src.database import Database

class KaryotypeAnalyzer:
    def __init__(self):
        self.root = tk.Tk()
        self.gui = KaryotypeAnalyzerGUI(self.root)
        self.db = Database()

        # Override the analyze_image method
        self.gui.analyze_image = self.analyze_image

    def analyze_image(self):
        if hasattr(self.gui, 'image'):
            image_path = self.gui.image.filename
            result = analyze_karyotype(image_path)
            
            # Update GUI
            self.gui.result_label.config(text=f"Chromosome count: {result['chromosome_count']}, Result: {result['analysis_result']}")
            
            # Save to database
            self.db.insert_result(image_path, result['chromosome_count'], result['analysis_result'])
        else:
            self.gui.result_label.config(text="Please load an image first.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = KaryotypeAnalyzer()
    app.run()
