import tkinter as tk
from tkinter import messagebox
import ApiKey

def on_entry_click(event):
    if entry_box.get() == "Enter your question...":
        entry_box.delete(0, tk.END)
        entry_box.insert(0, '')
        entry_box.config(fg='black')

def on_focusout(event):
    if entry_box.get() == '':
        entry_box.insert(0, "Enter your question...")
        entry_box.config(fg='grey')

def send_question(event=None):
    question = entry_box.get()
    if question == "Enter your question...":
        messagebox.showwarning("Warning", "Please enter a question.")
        return

    entry_box.delete(0, tk.END)

    prompt_parts = [question]
    response = ApiKey.model.generate_content(prompt_parts)

    response_area.config(state=tk.NORMAL)  # Make response_area editable
    response_area.insert(tk.END, "You: " + question + "\n")

    # Check if the response text is surrounded by triple backticks
    if response.text.startswith("```") and response.text.endswith("```"):
        response_area.insert(tk.END, f"{response.text}\n", "code")
    else:
        response_area.insert(tk.END, f"{response.text}\n")

    response_area.insert(tk.END,
                         "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
                         + "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")

    response_area.config(state=tk.DISABLED)  # Disable editing after inserting text
    response_area.yview(tk.END)


root = tk.Tk()
root.title("Chatbox")
root.configure(background="lightgray")

# Define a tag for the code (red color and bold)
response_area = tk.Text(root, width=80, height=30, wrap=tk.WORD, background="white", state=tk.DISABLED)
response_area.tag_configure("code", foreground="red", font=("Arial", 12, "bold"))

response_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Entry box customization
entry_box = tk.Entry(root, width=60, font=("Arial", 13), fg='grey')
entry_box.pack(side=tk.TOP, padx=10, pady=(10, 5), ipadx=5, ipady=5)  # Adjust pady as per your preference
entry_box.insert(0, "Enter your question...")
entry_box.bind('<FocusIn>', on_entry_click)
entry_box.bind('<FocusOut>', on_focusout)

submit_button = tk.Button(
    root, text="→", width=8, height=2, bg="gray", fg="white", font="Arial 14",
    command=send_question
)
submit_button.pack(side=tk.TOP, padx=10, pady=10)

# Bind Enter key to send_question function
root.bind("<Return>", send_question)

# Pencere boyutu ve konumu
window_width = max(800, root.winfo_screenwidth() // 2)
window_height = max(610, root.winfo_screenheight() // 2)

root.minsize(width=window_width, height=window_height)

x_coordinate = (root.winfo_screenwidth() - window_width) // 2
y_coordinate = (root.winfo_screenheight() - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

root.mainloop()
