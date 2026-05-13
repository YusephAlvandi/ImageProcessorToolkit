"""
Watermark Module - Batch Image Watermarking
Part of ImageProcessor Toolkit
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import os

class WatermarkModule:
    def __init__(self):
        self.window = ctk.CTkToplevel()
        self.window.title("Watermark Images")
        self.window.geometry("800x600")
        self.window.configure(fg_color="#0a0a0a")
        
        self.input_folder = ""
        self.output_folder = ""
        self.watermark_text = ctk.StringVar(value="Sample")
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header = ctk.CTkFrame(self.window, fg_color="transparent")
        header.pack(fill="x", pady=(20, 15), padx=30)
        ctk.CTkLabel(header, text="💧 Watermark Images", font=ctk.CTkFont(size=28, weight="bold"), text_color="#1E90FF").pack()
        
        # Main content
        main = ctk.CTkFrame(self.window, fg_color="#1a1a1a", corner_radius=12)
        main.pack(fill="both", expand=True, padx=30, pady=10)
        
        # Text input
        text_frame = ctk.CTkFrame(main, fg_color="transparent")
        text_frame.pack(fill="x", padx=20, pady=(20, 10))
        ctk.CTkLabel(text_frame, text="Watermark Text:", font=ctk.CTkFont(size=13)).pack(side="left")
        ctk.CTkEntry(text_frame, textvariable=self.watermark_text, width=300).pack(side="left", padx=10)
        
        # Folder selection
        ctk.CTkButton(main, text="Select Input Folder", command=self.select_input, height=35).pack(pady=10)
        self.label_input = ctk.CTkLabel(main, text="Not selected", text_color="#888888")
        self.label_input.pack()
        
        ctk.CTkButton(main, text="Select Output Folder", command=self.select_output, height=35).pack(pady=10)
        self.label_output = ctk.CTkLabel(main, text="Not selected", text_color="#888888")
        self.label_output.pack()
        
        # Process button
        ctk.CTkButton(main, text="Start Watermarking", command=self.process, height=40, fg_color="#1E90FF").pack(pady=20)
        
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
        
        text = self.watermark_text.get()
        supported = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
        count = 0
        
        for filename in os.listdir(self.input_folder):
            if filename.lower().endswith(supported):
                try:
                    img = Image.open(os.path.join(self.input_folder, filename)).convert("RGBA")
                    txt_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
                    draw = ImageDraw.Draw(txt_layer)
                    
                    # Try to load a font
                    try:
                        font = ImageFont.truetype("arial.ttf", 36)
                    except:
                        font = ImageFont.load_default()
                    
                    # Position watermark at bottom-right
                    bbox = draw.textbbox((0, 0), text, font=font)
                    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
                    x, y = img.width - tw - 20, img.height - th - 20
                    
                    draw.text((x, y), text, fill=(255, 255, 255, 180), font=font)
                    result = Image.alpha_composite(img, txt_layer)
                    
                    output_path = os.path.join(self.output_folder, f"wm_{filename}")
                    result.convert("RGB").save(output_path, 'JPEG', quality=95)
                    count += 1
                    self.status_label.configure(text=f"Processed: {filename}")
                    self.window.update()
                except Exception as e:
                    self.status_label.configure(text=f"Skipped: {filename}")
        
        self.status_label.configure(text=f"✅ Done! {count} images watermarked.", text_color="#4CAF50")
        messagebox.showinfo("Complete", f"Watermarked {count} images.")
    
    def run(self):
        self.window.mainloop()