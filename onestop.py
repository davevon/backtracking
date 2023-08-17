import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Define modern colors
PRIMARY_COLOR = "#3498db"
SECONDARY_COLOR = "#e74c3c"
BG_COLOR = "#2c3e50"
FG_COLOR = "#ecf0f1"

class HomePage(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master, bg=BG_COLOR)
        self.master = master
        self.switch_frame = switch_frame
        
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        
    def create_widgets(self):
        label = tk.Label(self, text="Welcome to the Home Page", bg=BG_COLOR, fg=FG_COLOR, font=("Helvetica", 16))
        label.pack(padx=10, pady=10)
        
        button_product = ttk.Button(self, text="Go to Product Page", command=lambda: self.switch_frame(ProductPage), style="Primary.TButton")
        button_product.pack(padx=10, pady=10)
        
        # Display time
        self.time_label = tk.Label(self, text="", bg=BG_COLOR, fg=FG_COLOR, font=("Helvetica", 12))
        self.time_label.pack(padx=10, pady=5)
        self.update_time()
        
        # New feature: Display a random quote
        self.quote_label = tk.Label(self, text="", bg=BG_COLOR, fg=FG_COLOR, font=("Helvetica", 14), wraplength=300)
        self.quote_label.pack(padx=10, pady=10)
        self.update_quote()
        
    def update_time(self):
        import time
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text="Current Time: " + current_time)
        self.time_label.after(1000, self.update_time)
        
    def update_quote(self):
        import random
        quotes = [
            "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Innovation distinguishes between a leader and a follower. - Steve Jobs",
            "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
        ]
        random_quote = random.choice(quotes)
        self.quote_label.config(text=random_quote)
        self.quote_label.after(15000, self.update_quote)  # Update quote every 15 seconds

class ProductPage(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master, bg=BG_COLOR)
        self.master = master
        self.switch_frame = switch_frame
        
        self.products = []  # List to store added products
        
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
        
    def create_widgets(self):
        label = tk.Label(self, text="Welcome to the Product Page", bg=BG_COLOR, fg=FG_COLOR, font=("Helvetica", 16))
        label.pack(padx=10, pady=10)
        
        button_home = ttk.Button(self, text="Go to Home Page", command=lambda: self.switch_frame(HomePage), style="Primary.TButton")
        button_home.pack(padx=10, pady=10)
        
        # New feature: Add Product
        entry_label = tk.Label(self, text="Product Name:", bg=BG_COLOR, fg=FG_COLOR)
        entry_label.pack(padx=10, pady=5)
        
        self.product_entry = ttk.Entry(self)
        self.product_entry.pack(padx=10, pady=5)
        
        add_button = ttk.Button(self, text="Add Product", command=self.add_product, style="Primary.TButton")
        add_button.pack(padx=10, pady=5)
        
        # Display added products
        products_label = tk.Label(self, text="Added Products:", bg=BG_COLOR, fg=FG_COLOR, font=("Helvetica", 14))
        products_label.pack(padx=10, pady=5)
        
        self.products_listbox = tk.Listbox(self, bg=BG_COLOR, fg=FG_COLOR)
        self.products_listbox.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        # New feature: Clear Products button
        clear_button = ttk.Button(self, text="Clear Products", command=self.clear_products, style="Primary.TButton")
        clear_button.pack(padx=10, pady=10)
        
    def add_product(self):
        product_name = self.product_entry.get()
        if product_name:
            self.products.append(product_name)
            self.products_listbox.insert(tk.END, product_name)
            self.product_entry.delete(0, tk.END)
            
    def clear_products(self):
        self.products = []
        self.products_listbox.delete(0, tk.END)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Modern Tkinter Application")
        
        self.geometry("400x500")
        self.configure(bg=BG_COLOR)
        
        # Set up themed style for buttons
        style = ttk.Style(self)
        style.configure("Primary.TButton", foreground=FG_COLOR, background=PRIMARY_COLOR, borderwidth=0, relief="flat")
        style.map("Primary.TButton", foreground=[('pressed', SECONDARY_COLOR), ('active', SECONDARY_COLOR)])
        
        self.switch_frame(HomePage)
        
    def switch_frame(self, frame_class):
        new_frame = frame_class(self, self.switch_frame)
        
        if hasattr(self, "current_frame"):
            self.current_frame.destroy()
            
        self.current_frame = new_frame
        self.current_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()

