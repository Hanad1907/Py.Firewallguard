import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont

class FirewallGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Py.Firewallguard")

        # Set a colorful background
        self.master.configure(bg="#2C3E50")

        # Logo Label
        self.logo_label = tk.Label(self.master, text=self.get_logo(), font=("Courier New", 12), fg="#ECF0F1", bg="#2C3E50", justify="center")
        self.logo_label.pack(pady=20)

        # Title label
        self.title_label = tk.Label(self.master, text="Welcome to Py.Firewallguard", 
                                     font=("Arial", 20, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.title_label.pack(pady=10)

        # Block port frame
        self.block_frame = tk.Frame(self.master, bg="#34495E")
        self.block_frame.pack(pady=10)

        self.block_label = tk.Label(self.block_frame, text="Block Ports:", 
                                     font=("Arial", 16), fg="#ECF0F1", bg="#34495E")
        self.block_label.pack(side=tk.LEFT, padx=10)

        self.port_entry = tk.Entry(self.block_frame, width=10)
        self.port_entry.pack(side=tk.LEFT, padx=10)

        self.block_button = tk.Button(self.block_frame, text="Block", 
                                       command=self.block_port, bg="#E74C3C", fg="#ECF0F1")
        self.block_button.pack(side=tk.LEFT, padx=10)

        # Allow port frame
        self.allow_frame = tk.Frame(self.master, bg="#34495E")
        self.allow_frame.pack(pady=10)

        self.allow_label = tk.Label(self.allow_frame, text="Allow Ports:", 
                                     font=("Arial", 16), fg="#ECF0F1", bg="#34495E")
        self.allow_label.pack(side=tk.LEFT, padx=10)

        self.allow_entry = tk.Entry(self.allow_frame, width=10)
        self.allow_entry.pack(side=tk.LEFT, padx=10)

        self.allow_button = tk.Button(self.allow_frame, text="Allow", 
                                      command=self.allow_port, bg="#2ECC71", fg="#ECF0F1")
        self.allow_button.pack(side=tk.LEFT, padx=10)

    def get_logo(self):
        return """ 
██████╗ ██╗   ██╗██████╗  ██████╗ ██╗     ██╗██╗     ██╗      ███████╗
██╔══██╗██║   ██║██╔══██╗██╔════╝ ██║     ██║██║     ██║      ██╔════╝
██████╔╝██║   ██║██████╔╝██║  ███╗██║     ██║██║     ██║      █████╗  
██╔═══╝ ██║   ██║██╔═══╝ ██║   ██║██║     ██║██║     ██║      ██╔══╝  
██║     ╚██████╔╝██║     ╚██████╔╝███████╗██║███████╗███████╗███████╗
╚═╝      ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝╚═╝╚══════╝╚══════╝╚══════╝
        """

    def block_port(self):
        port = self.port_entry.get()
        # Logic to block the port would go here
        messagebox.showinfo("Blocked", f"Port {port} has been blocked.")

    def allow_port(self):
        port = self.allow_entry.get()
        # Logic to allow the port would go here
        messagebox.showinfo("Allowed", f"Port {port} has been allowed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FirewallGUI(root)
    root.mainloop()
