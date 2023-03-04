import tkinter as tk
import tkinter.messagebox as tkmb
# Create the GUI window
root = tk.Tk()
root.title("Scribblespace")
root.configure(bg='light yellow')

# Create a Text widget to display the notes
notes_text = tk.Text(root, bg='light yellow')
notes_text.pack()

# Create a Save button
def save_notes():
    if tkmb.askyesno("Scribblespace", "Are you sure you want to save? This will overwrite existing notes."):
        with open("scribbles.txt", "w") as file:
            file.write(notes_text.get("1.0", "end"))
        tkmb.showinfo("Scribblespace", "Notes saved successfully!")

save_button = tk.Button(root, text="Save", command=save_notes, bg='light yellow')
save_button.pack()

# Create a Load button
def load_notes():
    with open("scribbles.txt", "r") as file:
        notes_text.delete("1.0", tk.END)
        notes_text.insert("1.0", file.read())
    tkmb.showinfo("Scribblespace", "Notes loaded successfully!")

load_button = tk.Button(root, text="Load", command=load_notes, bg='light yellow')
load_button.pack()

root.mainloop()
