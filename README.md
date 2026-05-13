ImageProcessor Toolkit

A modular all-in-one desktop suite for batch image processing.

Built with Python and CustomTkinter.


WHAT THIS TOOLKIT DOES

This toolkit combines three essential image processing tools into one clean interface:

1. Watermark — Add text watermarks to multiple images at once
2. Resizer — Resize images to target dimensions in bulk
3. Optimizer — Compress images with smart quality control and size reporting


WHY THIS IS BETTER THAN SINGLE-FILE SCRIPTS

Most freelancers deliver one long script that does everything in one file. This toolkit uses a professional modular design. Here is why that matters:

1. Each tool lives in its own file. If you need to fix a bug in the Watermark tool, you only touch watermark.py. The other tools stay safe and untouched.

2. You can reuse any module in other projects. Need just the Optimizer for another client? Import optimizer.py and it works independently.

3. You can deliver individual tools to different clients. You do not have to expose your entire codebase to every client.

4. Adding a new tool in the future is easy. Just create a new .py file and add one button to main.py. Everything else stays the same.

5. This structure shows employers that you understand software architecture, not just scripting.


PROJECT STRUCTURE

ImageProcessorToolkit/
    main.py           (Main launcher with tool selection menu)
    watermark.py      (Watermark module - standalone capable)
    resizer.py        (Resize module - standalone capable)
    optimizer.py      (Compression module - standalone capable)
    README.md         (This file)


HOW TO RUN

1. Install the required libraries:

pip install customtkinter pillow

2. Launch the toolkit:

python main.py

3. Select the tool you need from the main menu.


TECH STACK

Python 3.x — Core programming language
CustomTkinter — Modern desktop UI
Pillow (PIL) — Image processing engine
Modular OOP Architecture — Clean separation of concerns


AUTHOR

Yuseph Alvandi
PhD in Atomic and Molecular Physics (Optics and Laser)
Python Developer and Image Processing Specialist

GitHub: https://github.com/YusephAlvandi
Cryptotask: Available on Cryptotask


LICENSE

MIT License