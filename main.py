"""
ImageProcessor Toolkit - All-in-One Image Processing Suite
Author: Yuseph Alvandi
GitHub: https://github.com/YusephAlvandi
Description: A modular toolkit combining watermarking, resizing, and compression.
Version: 1.0.0
"""

import customtkinter as ctk
from tkinter import messagebox

# Import our modules
from watermark import WatermarkModule
from resizer import ResizerModule
from optimizer import OptimizerModule

# ============ GLOBAL SETTINGS ============
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
# =========================================

class ImageProcessorToolkit:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("ImageProcessor Toolkit")
        self.window.geometry("900x600")
        self.window.configure(fg_color="#0a0a0a")
        
        self.setup_ui()
    
    def setup_ui(self):
        # Header
        header = ctk.CTkFrame(self.window, fg_color="transparent")
        header.pack(fill="x", pady=(30, 20), padx=40)
        
        ctk.CTkLabel(
            header,
            text="🧰 ImageProcessor Toolkit",
            font=ctk.CTkFont(size=36, weight="bold"),
            text_color="#1E90FF"
        ).pack()
        
        ctk.CTkLabel(
            header,
            text="Select the tool you need:",
            font=ctk.CTkFont(size=14),
            text_color="#AAAAAA"
        ).pack(pady=5)
        
        # Button frame
        btn_frame = ctk.CTkFrame(self.window, fg_color="#1a1a1a", corner_radius=16, border_width=1, border_color="#333333")
        btn_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Tool 1: Watermark
        self.create_tool_button(
            btn_frame,
            "💧 Watermark Images",
            "Add text watermarks to multiple images",
            self.open_watermark,
            pady=(40, 10)
        )
        
        # Tool 2: Resizer
        self.create_tool_button(
            btn_frame,
            "📐 Resize Images",
            "Resize images to specific dimensions",
            self.open_resizer,
            pady=10
        )
        
        # Tool 3: Optimizer
        self.create_tool_button(
            btn_frame,
            "🗜️ Optimize Images",
            "Compress images with smart quality control",
            self.open_optimizer,
            pady=10
        )
        
        # Status bar
        status_frame = ctk.CTkFrame(self.window, fg_color="#1a1a1a", corner_radius=12, height=40)
        status_frame.pack(fill="x", padx=40, pady=(0, 20))
        status_frame.pack_propagate(False)
        
        self.status_label = ctk.CTkLabel(
            status_frame,
            text="● Ready",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#4CAF50"
        )
        self.status_label.pack(pady=10)
    
    def create_tool_button(self, parent, title, subtitle, command, pady=10):
        """Create a styled tool selection button"""
        btn = ctk.CTkButton(
            parent,
            text=f"{title}\n{subtitle}",
            command=command,
            height=80,
            font=ctk.CTkFont(size=16),
            fg_color="#252525",
            hover_color="#1E90FF",
            corner_radius=12,
            border_width=1,
            border_color="#404040"
        )
        btn.pack(fill="x", padx=30, pady=pady)
    
    def open_watermark(self):
        """Open Watermark module"""
        self.status_label.configure(text="🔄 Opening Watermark tool...", text_color="#FFAA33")
        self.window.update()
        try:
            wm = WatermarkModule()
            wm.run()
            self.status_label.configure(text="✅ Watermark tool closed", text_color="#4CAF50")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Watermark tool:\n{e}")
            self.status_label.configure(text="⚠️ Error opening tool", text_color="#FF5555")
    
    def open_resizer(self):
        """Open Resizer module"""
        self.status_label.configure(text="🔄 Opening Resizer tool...", text_color="#FFAA33")
        self.window.update()
        try:
            rz = ResizerModule()
            rz.run()
            self.status_label.configure(text="✅ Resizer tool closed", text_color="#4CAF50")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Resizer tool:\n{e}")
            self.status_label.configure(text="⚠️ Error opening tool", text_color="#FF5555")
    
    def open_optimizer(self):
        """Open Optimizer module"""
        self.status_label.configure(text="🔄 Opening Optimizer tool...", text_color="#FFAA33")
        self.window.update()
        try:
            opt = OptimizerModule()
            opt.run()
            self.status_label.configure(text="✅ Optimizer tool closed", text_color="#4CAF50")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Optimizer tool:\n{e}")
            self.status_label.configure(text="⚠️ Error opening tool", text_color="#FF5555")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ImageProcessorToolkit()
    app.run()