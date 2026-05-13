"""
Optimizer Module - Smart Image Compression
Part of ImageProcessor Toolkit
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os

class OptimizerModule:
    def __init__(self):
        self.window = ctk.CTkToplevel()
        self.window.title("Optimize Images")
        self.window.geometry("800x600")
        self.window.configure(fg_color="#0a0a0a")
        
        self.input_folder = ""
        self.output_folder = ""
        self.quality = ctk.IntVar(value=70)
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header = ctk.CTkFrame(self.window, fg_color="transparent")
        header.pack(fill="x", pady=(20, 15), padx=30)
        ctk.CTkLabel(header, text="🗜️ Optimize Images", font=ctk.CTkFont(size=28, weight="bold"), text_color="#1E90FF").pack()
        
        # Main content
        main = ctk.CTkFrame(self.window, fg_color="#1a1a1a", corner_radius=12)
        main.pack(fill="both", expand=True, padx=30, pady=10)
        
        # Quality slider
        qual_frame = ctk.CTkFrame(main, fg_color="transparent")
        qual_frame.pack(fill="x", padx=20, pady=(20, 10))
        ctk.CTkLabel(qual_frame, text="Quality:", font=ctk.CTkFont(size=13)).pack(side="left")
        ctk.CTkSlider(qual_frame, from_=10, to=95, variable=self.quality, width=250, command=self.update_label).pack(side="left", padx=10)
        self.qual_label = ctk.CTkLabel(qual_frame, text="70%", font=ctk.CTkFont(size=13, weight="bold"))
        self.qual_label.pack(side="left")
        
        # Folder selection
        ctk.CTkButton(main, text="Select Input Folder", command=self.select_input, height=35).pack(pady=10)
        self.label_input = ctk.CTkLabel(main, text="Not selected", text_color="#888888")
        self.label_input.pack()
        
        ctk.CTkButton(main, text="Select Output Folder", command=self.select_output, height=35).pack(pady=10)
        self.label_output = ctk.CTkLabel(main, text="Not selected", text_color="#888888")
        self.label_output.pack()
        
        # Process button
        ctk.CTkButton(main, text="Start Optimization", command=self.process, height=40, fg_color="#E67E22").pack(pady=20)
        
        # Status
        self.status_label = ctk.CTkLabel(main, text="Ready", text_color="#4CAF50")
        self.status_label.pack(pady=10)
    
    def update_label(self, value):
        self.qual_label.configure(text=f"{int(float(value))}%")
    
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
        
        quality_val = self.quality.get()
        supported = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
        total_orig = 0
        total_comp = 0
        count = 0
        
        for filename in os.listdir(self.input_folder):
            if filename.lower().endswith(supported):
                try:
                    input_path = os.path.join(self.input_folder, filename)
                    orig_size = os.path.getsize(input_path)
                    total_orig += orig_size
                    
                    img = Image.open(input_path)
                    if img.mode == 'RGBA':
                        img = img.convert('RGB')
                    
                    output_path = os.path.join(self.output_folder, f"opt_{filename}")
                    img.save(output_path, 'JPEG', quality=quality_val, optimize=True)
                    
                    comp_size = os.path.getsize(output_path)
                    total_comp += comp_size
                    count += 1
                    self.status_label.configure(text=f"Processed: {filename}")
                    self.window.update()
                except Exception as e:
                    self.status_label.configure(text=f"Skipped: {filename}")
        
        reduction = ((total_orig - total_comp) / total_orig * 100) if total_orig > 0 else 0
        self.status_label.configure(text=f"✅ Done! {count} images optimized ({reduction:.0f}% smaller).", text_color="#4CAF50")
        messagebox.showinfo("Complete", f"Optimized {count} images.\nSpace saved: {reduction:.0f}%")
    
    def run(self):
        self.window.mainloop()