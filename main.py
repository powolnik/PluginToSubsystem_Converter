import os
import tkinter as tk
from tkinter import ttk, filedialog, Text

def create_app():
    root = tk.Tk()
    root.title("Windowed C++ App Viewer")
    
    # Main container
    main_frame = ttk.Frame(root)
    main_frame.pack(expand=True, fill='both')
    
    # Create tabbed interface
    notebook = ttk.Notebook(main_frame)
    
    # File list tab
    file_list_frame = ttk.Frame(notebook)
    file_label = ttk.Label(file_list_frame, text="Directory:")
    file_label.pack(anchor='w', padx=5, pady=5)
    
    directory_entry = ttk.Entry(file_list_frame, width=40)
    directory_entry.pack(anchor='w', padx=5, fill=tk.X)
    
    browse_button = ttk.Button(
        file_list_frame,
        text="Browse",
        command=lambda: set_directory(directory_entry)
    )
    browse_button.pack(anchor='w', padx=5, pady=5)
    
    files_listbox = tk.Listbox(file_list_frame, selectmode=tk.SINGLE)
    files_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    # Editor tab
    editor_frame = ttk.Frame(notebook)
    code_text = Text(editor_frame, wrap=tk.WORD)
    code_text.pack(expand=True, fill='both', padx=5, pady=5)
    
    # Line numbers
    line_numbers = ttk.Label(editor_frame, text="1")
    line_numbers.pack(anchor='w', padx=5, side=tk.LEFT, fill='y')
    
    notebook.add(file_list_frame, text="File List")
    notebook.add(editor_frame, text="Editor")
    
    def on_file_selected(event):
        selected_file = files_listbox.get(files_listbox.curselection())
        if not selected_file:
            return
            
        directory = os.path.dirname(selected_file)
        filename = os.path.basename(selected_file)
        
        try:
            with open(selected_file, 'r', encoding='utf-8') as f:
                content = f.read()
                code_text.delete(1.0, tk.END)
                code_text.insert(tk.END, content)
                
                # Update line numbers
                line_numbers.config(text=f"Lines: {len(content.split('/n'))}")
        except Exception as e:
            print(f"Error reading file: {e}")
    
    files_listbox.bind('<<ListboxSelect>>', on_file_selected)
    
def set_directory(entry):
    directory = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, directory)
    
if __name__ == "__main__":
    create_app()
