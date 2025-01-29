# Configuration settings for the Code Viewer application

class Config:
    # Basic settings
    TITLE = "Code Viewer"
    WINDOW_SIZE = (800, 600)
    
    # File types
    SUPPORTED_FILES = {
        'cpp': ('.cpp', '.hpp'),
        'header': '.h'
    }
