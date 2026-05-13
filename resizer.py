"""
Resizer Module - Batch Image Resizing
Part of ImageProcessor Toolkit
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os

class ResizerModule:
    def __init__(self):
        self.window = ctk.CTkToplevel()
        self.window.title("Resize Images")
        self.window.geometry("800x600")
        self.window.configure(fg_color="#0a0a0a")
        
        self.input_folder = ""
        self.output_folder = ""
        self.target_width = ctk.IntVar(value=800)
        self.target_height = ctk.IntVar(value=600)
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header = ctk.CTkFrame(self.window, fg_color="transparent")
        header.pack(fill="x", pady=(20, 15), padx=30)
        ctk.CTkLabel(header, text="📐 Resize Images", font=ctk.CTkFont(size=28, weight="bold"), text_color="#1E90FF").pack()
        
        # Main content
        main = ctk.CTkFrame(self.window, fg_color="#1a1a1a", corner_radius=12)
        main.pack(fill="both", expand=True, padx=30, pady=10)
        
        # Size settings
        size_frame = ctk.CTkFrame(main, fg_color="transparent")
        size_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        ctk.CTkLabel(size_frame, text="Width:", font=ctk.CTkFont(size=13)).pack(side="left")
        ctk.CTkEntry(size_frame, textvariable=self.target_width, width=80).pack(side="left", padx=(5, 20))
        
        ctk.CTkLabel(size_frame, text="Height:", font=ctk.CTkFont(size=13)).pack(side="left")
        ctk.CTkEntry(size_frame, textvariable=self.target_height, width=80).pack(side="left", padx=5)
        
        # Folder selection
        ctk.CTkButton(main, text="Select Input Folder", command=self.select_input, height=35).pack(pady=10)
        self.label_input = ctk.CTkLabel(main, text="Not selected", text_color="#888888")
        self.label_input.pack()
        
        ctk.CTkButton(main, text="Select Output Folder", command=self.select_output, height=35).pack(pady=10)
        self.label_output = ctk.CTkLabel(main, text="Not selected", text_color="#888888")
        self.label_output.pack()
        
        # Process button
        ctk.CTkButton(main, text="Start Resizing", command=self.process, height=40, fg_color="#1E90FF").pack(pady=20)
        
        # Status
        self.status_label = ctk.CTkLabel(main, text="Ready", text_color="#4CAF50")
        self.status_label.pack(pady=10)
    
    def select_input(self):
        self.input_folder = filedialog.askdirectory()
        if self.input_folder:
            self.label_input.configure(text=f"✓ {os.path.basename(self.input_folder)}", text_color="#4CAF50")
    
    def select_output(self):
        self.output_folder = filedialog.askdirectory()
        if self.output_folder:
            self.label_output.configure(text=f"✓ {os.path.basename(self.output_folder)}", text_color="#4CAF50")
    
    def process(self):
        if not self.input_folder or not self.output_folder:
            messagebox.showerror("Error", "Please select both folders!")
            return
        
        target = (self.target_width.get(), self.target_height.get())
        supported = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
        count = 0
        
        for filename in os.listdir(self.input_folder):
            if filename.lower().endswith(supported):
                try:
                    img = Image.open(os.path.join(self.input_folder, filename))
                    img.thumbnail(target, Image.Resampling.LANCZOS)
                    
                    output_path = os.path.join(self.output_folder, f"resized_{filename}")
                    if img.mode == 'RGBA':
                        img = img.convert('RGB')
                    img.save(output_path, 'JPEG', quality=90)
                    count += 1
                    self.status_label.configure(text=f"Processed: {filename}")
                    self.window.update()
                except Exception as e:
                    self.status_label.configure(text=f"Skipped: {filename}")
        
        self.status_label.configure(text=f"✅ Done! {count} images resized.", text_color="#4CAF50")
        messagebox.showinfo("Complete", f"Resized {count} images.")
    
    def run(self):
        self.window.mainloop()