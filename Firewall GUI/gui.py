import tkinter as tk
from tkinter import messagebox
from firewall import Firewall

firewall = Firewall()

def block_port():
    try:
        port = int(entry_port.get())
        firewall.block_port(port)
        messagebox.showinfo("Success", f"Blocked port {port}")
        entry_port.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid port number.")

def show_blocked_ports():
    firewall.display_blocked_ports()

def run_gui():
    global entry_port
    root = tk.Tk()
    root.title("Simple Firewall")

    tk.Label(root, text="Enter Port to Block:").pack(pady=10)
    entry_port = tk.Entry(root)
    entry_port.pack(pady=10)

    block_button = tk.Button(root, text="Block Port", command=block_port)
    block_button.pack(pady=10)

    show_button = tk.Button(root, text="Show Blocked Ports", command=show_blocked_ports)
    show_button.pack(pady=10)

    root.mainloop()
