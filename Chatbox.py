import ApiKey
import tkinter as tk
from tkinter import messagebox, Menu

def copy_text(event):
    if response_area.tag_ranges(tk.SEL):
        selected_text = response_area.get(tk.SEL_FIRST, tk.SEL_LAST)
        root.clipboard_clear()
        root.clipboard_append(selected_text)

def show_context_menu(event):
    context_menu.post(event.x_root, event.y_root)

def copy_text_entry_box():
    selected_text = entry_box.get()
    root.clipboard_clear()
    root.clipboard_append(selected_text)

def paste_text_entry_box():
    entry_box.delete(0, tk.END)
    entry_box.insert(0, root.clipboard_get())

def on_entry_click(event):
    if entry_box.get() == "Enter your question...":
        entry_box.delete(0, tk.END)
        entry_box.insert(0, '')
        entry_box.config(fg='black')

def on_focusout(event):
    if entry_box.get() == '':
        entry_box.insert(0, "Enter your question...")
        entry_box.config(fg='grey')

def clear_response_area():
    response_area.config(state=tk.NORMAL)
    response_area.delete(1.0, tk.END)
    response_area.config(state=tk.DISABLED)

def send_question(event=None):
    question = entry_box.get()
    if question == "Enter your question...":
        messagebox.showwarning("Warning", "Please enter a question.")
        return

    entry_box.delete(0, tk.END)

    prompt_parts = [question]
    response = ApiKey.model.generate_content(prompt_parts)

    response_area.config(state=tk.NORMAL)  # Make response_area editable
    response_area.insert(tk.END, "You: " + question + "\n\n")

    in_code_block = False
    response_lines = response.text.split('\n')

    for line in response_lines:
        if line.startswith("```") and line.endswith("```"):
            response_area.insert(tk.END, f"{line}\n", "code")
            in_code_block = not in_code_block
        elif in_code_block:
            response_area.insert(tk.END, f"{line}\n", "code")
        else:
            response_area.insert(tk.END, f"{line}\n", "default")  # Default tag for non-code lines

    response_area.insert(tk.END,
                         "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
                         + "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")

    response_area.config(state=tk.DISABLED)  # Disable editing after inserting text
    response_area.yview(tk.END)

# Main Window
root = tk.Tk()
root.title("Chatbox")
root.configure(background="white")

# Window icon
# root.iconbitmap('gemini.ico')
# pyinstaller.exe --onefile --windowed --icon=gemini.ico Chatbox.py #"EXPORT EXE FILE"

# Define a tag for the code (red color and bold)
response_area = tk.Text(root, width=80, height=30, wrap=tk.WORD, background="white", state=tk.DISABLED,
                        highlightbackground="black", highlightcolor="yellow", insertbackground="red")
response_area.tag_configure("code", foreground="red", font=("Courier New", 13, "bold"))
response_area.tag_configure("default", foreground="black", font=("Courier New", 13))  # Default tag for non-code lines
response_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
response_area.tag_configure("code", foreground="black", font=("Courier New", 13))
response_area.tag_configure("default", foreground="black", font=("Courier New", 13))

# Create a context menu
context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Copy", command=copy_text)

# Bind right-click event to show_context_menu function
response_area.bind("<Button-3>", show_context_menu)

# Entry box customization
entry_box = tk.Entry(root, width=60, font=("Arial", 13), fg='grey', relief=tk.GROOVE, bd=2,
                     highlightcolor="#4CAF50", highlightthickness=2, borderwidth=2, selectborderwidth=2, insertborderwidth=2,
                     selectbackground="#4CAF50", selectforeground="white", insertbackground="#4CAF50", insertwidth=4)
entry_box.pack(side=tk.LEFT, padx=10, pady=(10, 5), ipadx=5, ipady=5)  # Adjust pady as per your preference
entry_box.insert(0, "Enter your question...")
entry_box.bind('<FocusIn>', on_entry_click)
entry_box.bind('<FocusOut>', on_focusout)

# Create a context menu for entry_box
entry_box_context_menu = Menu(root, tearoff=0)
entry_box_context_menu.add_command(label="Copy", command=copy_text_entry_box)
entry_box_context_menu.add_command(label="Paste", command=paste_text_entry_box)

def show_entry_box_context_menu(event):
    entry_box_context_menu.post(event.x_root, event.y_root)

# Bind right-click event to show_entry_box_context_menu function
entry_box.bind("<Button-3>", show_entry_box_context_menu)

# Submit button customization
submit_button = tk.Button(
    root, text="Ask", width=5, height=1, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"),
    command=send_question
)
submit_button.pack(side=tk.LEFT, padx=5, pady=5)

# Clear button customization
clear_button = tk.Button(
    root, text="Clear", width=5, height=1, bg="#ff3333", fg="white", font=("Arial", 14, "bold"),
    command=clear_response_area
)
clear_button.pack(side=tk.LEFT, padx=5, pady=5)

# Bind Enter key to send_question function
root.bind("<Return>", send_question)

# Windows size
window_width = max(800, root.winfo_screenwidth() // 2)
window_height = max(610, root.winfo_screenheight() // 2)

root.minsize(width=window_width, height=window_height)

x_coordinate = (root.winfo_screenwidth() - window_width) // 2
y_coordinate = (root.winfo_screenheight() - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

root.mainloop()
