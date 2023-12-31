import tkinter as tk
from tkinter import messagebox
import ApiKey

# GUI setup
def send_question(event=None):
    question = entry_box.get()
    if question == "":
        messagebox.showwarning("Warning", "Please enter a question.")
        return

    entry_box.delete(0, tk.END)

    prompt_parts = [question]
    response = ApiKey.model.generate_content(prompt_parts)
    response_area.config(state=tk.NORMAL)  # Make response_area editable
    response_area.insert(tk.END, "You: " + question + "\n")
    response_area.insert(tk.END, "Chatbot: \n" + response.text + "\n")
    response_area.insert(tk.END, "------------------------------------------------------------------------------------------------------------------\n")
    response_area.config(state=tk.DISABLED)  # Disable editing after inserting text
    response_area.yview(tk.END)

root = tk.Tk()
root.title("Chatbox")
root.configure(background="lightgray")

response_area = tk.Text(root, width=80, height=20, wrap=tk.WORD, background="white", state=tk.DISABLED)
response_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

entry_box = tk.Entry(root, width=60, font="Arial 16")
entry_box.pack(side=tk.TOP, padx=10, pady=10)
entry_box.focus_set()  # Set focus on entry_box

submit_button = tk.Button(
    root, text="→", width=8, height=1, bg="gray", fg="white", font="Arial 14",
    command=send_question
)
submit_button.pack(side=tk.TOP, padx=10, pady=10)

# Bind Enter key to send_question function
root.bind("<Return>", send_question)

# Pencere boyutunu ve konumunu ayarla
window_width = max(800, root.winfo_screenwidth() // 2)
window_height = max(500, root.winfo_screenheight() // 2)

root.minsize(width=window_width, height=window_height)

x_coordinate = (root.winfo_screenwidth() - window_width) // 2
y_coordinate = (root.winfo_screenheight() - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

root.mainloop()
