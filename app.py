import tkinter as tk

class GuiSetup:
    def __init__(self, parent):
        self.parent = parent
        self.main_frame = None
        self.text_area = None
        self.status_label = None
        self.open_button = None
        
    def create_main_container(self):
        self.main_frame = tk.Frame(self.parent)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
    def create_text_area(self):
        self.text_area = tk.Text(
            self.main_frame,
            wrap=tk.WORD,
            padx=10,
            pady=10
        )
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
    def create_status_label(self):
        self.status_label = tk.Label(
            self.parent,
            text="Ready",
            anchor=tk.E,
            padx=5
        )
        self.status_label.pack(side=tk.RIGHT, fill=tk.X)
        
    def create_button_bar(self):
        button_frame = tk.Frame(self.parent)
        button_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.open_button = self._create_button(
            button_frame,
            "Open File",
            self._handle_file_open
        )
        
    def _create_button(self, parent, text, command):
        button = tk.Button(
            parent,
            text=text,
            command=command,
            padx=5,
            pady=3
        )
        button.pack(side=tk.LEFT, fill=tk.X, expand=True)
        return button
        
    def _handle_file_open(self):
        self._update_status("Opening file...")
        # File opening logic would go here
        self._update_status("Ready")
        
    def _update_status(self, message):
        self.status_label.config(text=message)

def main():
    root = tk.Tk()
    gui = GuiSetup(root)
    
    # Setup basic UI components
    gui.create_main_container()
    gui.create_text_area()
    gui.create_status_label()
    gui.create_button_bar()
    
    root.mainloop()

if __name__ == "__main__":
    main()
