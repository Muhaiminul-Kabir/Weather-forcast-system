import tkinter as tk

class DynamicTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Text Example")
        self.label = tk.Label(root, font=('Helvetica', 24))
        self.label.pack(pady=20)

        self.update_text()  # Start updating the text
    
     

    def update_text(self):
        with open('C:/Users/ASUS/Desktop/output.txt', 'r') as file:
            content = file.read()  # Read the entire content
            
        current_time = content
        self.label.config(text=current_time)  # Update the label text
        self.root.after(1000, self.update_text)  # Schedule next update in 1000 ms

if __name__ == '__main__':
    root = tk.Tk()
    app = DynamicTextApp(root)
    root.geometry("500x200")
    root.mainloop()
