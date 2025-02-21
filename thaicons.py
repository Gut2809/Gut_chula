import tkinter as tk
from tkinter import font

# List of Thai consonants with their names
thai_consonants = [
    ("ก", "ก - Gor Gai"),
    ("ข", "ข - Khor Khai"),
    ("ค", "ค - Khor Khuat"),
    ("ง", "ง - Ngor Ngu"),
    ("จ", "จ - Jor Jaan"),
    ("ฉ", "ฉ - Chor Ching"),
    ("ช", "ช - Chor Chang"),
    ("ซ", "ซ - Sor So"),
    ("ญ", "ญ - Yor Ying"),
    ("ฐ", "ฐ - Thor Thahan")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcard Game")
        self.index = 0
        self.showing_name = False
        
        self.custom_font = font.Font(family="Arial", size=50, weight="bold")
        
        self.label = tk.Label(root, text=thai_consonants[self.index][0], font=self.custom_font, width=10, height=5)
        self.label.pack(pady=20)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
        self.flip_button.pack(pady=5)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card)
        self.next_button.pack(side=tk.RIGHT, padx=10)
        
        self.prev_button = tk.Button(root, text="Previous", command=self.prev_card)
        self.prev_button.pack(side=tk.LEFT, padx=10)

    def flip_card(self):
        if self.showing_name:
            self.label.config(text=thai_consonants[self.index][0])
        else:
            self.label.config(text=thai_consonants[self.index][1])
        self.showing_name = not self.showing_name

    def next_card(self):
        self.index = (self.index + 1) % len(thai_consonants)
        self.label.config(text=thai_consonants[self.index][0])
        self.showing_name = False

    def prev_card(self):
        self.index = (self.index - 1) % len(thai_consonants)
        self.label.config(text=thai_consonants[self.index][0])
        self.showing_name = False

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
