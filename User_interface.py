import tkinter as tk
from phone_directory import *


# Create the main window
Interface = tk.Tk()
Interface.geometry("600x400")
Interface.title("My App")

# Create the three frames
search_frame = tk.Frame(Interface, padx=20, pady=20)
search_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

input_frame = tk.Frame(Interface, padx=20, pady=20)
input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

delete_frame = tk.Frame(Interface, padx=20, pady=20)
delete_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Add labels to the frames
search_label = tk.Label(search_frame, text="Searching", font=("Arial", 24))
search_label.pack(pady=(20, 10))

input_label = tk.Label(input_frame, text="Input", font=("Arial", 24))
input_label.pack(pady=(20, 10))

delete_label = tk.Label(delete_frame, text="Delete", font=("Arial", 24))
delete_label.pack(pady=(20, 10))

# Create a function to change the screen
def change_screen(frame_name):
    Interface.geometry("800x600")
    search_frame.pack_forget()
    input_frame.pack_forget()
    delete_frame.pack_forget()
    new_frame = tk.Frame(Interface, padx=50, pady=50)
    new_frame.pack(fill=tk.BOTH, expand=True)
    new_label = tk.Label(new_frame, text=f"You pressed the {frame_name} button!", font=("Arial", 28))
    new_label.pack()
    if frame_name == "Input":
        def add_name():
            name_label.config(text="Enter a name:")
            name_entry.pack(side=tk.LEFT, padx=(10, 0))
            add_button.pack(side=tk.LEFT, padx=(10, 0))

        name_frame = tk.Frame(new_frame, pady=10)
        name_frame.pack()
        name_label = tk.Label(name_frame, font=("Arial", 18))
        name_entry = tk.Entry(name_frame, font=("Arial", 18))
        add_button = tk.Button(name_frame, text="Add", font=("Arial", 18), command=lambda: [make_trie(name_entry.get()), name_entry.delete(0, tk.END), name_label.config(text="")])

        new_label = tk.Label(new_frame, text="Click the button to add a name to the trie", font=("Arial", 28))
        new_label.pack(pady=(20, 10))
        input_button = tk.Button(new_frame, text="Add Name", command=add_name, font=("Arial", 18))
        input_button.pack(pady=(0, 20))
    elif frame_name == "Searching":
        def perform_search():
            query = search_entry.get()
            results = search_trie(root, query)
            output_label.config(text="\n".join(results))
        search_label = tk.Label(new_frame, text="Enter your search query:", font=("Arial", 18))
        search_label.pack(pady=(20, 10))
        search_entry = tk.Entry(new_frame, font=("Arial", 18))
        search_entry.pack(pady=(0, 10))
        search_button = tk.Button(new_frame, text="Search", command=perform_search, font=("Arial", 18))
        search_button.pack()
        output_label = tk.Label(new_frame, text="", font=("Arial", 18))
        output_label.pack(pady=(10, 0))
# Create buttons for each frame
search_button = tk.Button(search_frame, text="Search", command=lambda: change_screen("Searching"), font=("Arial", 18))
search_button.pack(pady=(0, 20))

input_button = tk.Button(input_frame, text="Input", command=lambda: change_screen("Input"), font=("Arial", 18))
input_button.pack(pady=(0, 20))

delete_button = tk.Button(delete_frame, text="Delete", command=lambda: change_screen("Delete"), font=("Arial", 18))
delete_button.pack(pady=(0, 20))

def close_ui():
    Interface.destroy()

terminate_button = tk.Button(Interface, text="Terminate", command=close_ui, bg="red", fg="white", font=("Arial", 16), padx=10, pady=5)
terminate_button.pack(side=tk.BOTTOM, pady=20)

# Start the main loop
Interface.mainloop()
