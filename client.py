import tkinter as tk
import threading
import socket
import time

running = True  

def run_program(output_widgets):
    """Simulate a program that produces continuous output."""
    count = 1
    global running
    while running:
        time.sleep(0.1)  
        text = f"Critical error: System failure detected, immediate action required {count} !\n"
        for widget in output_widgets:
            widget.insert(tk.END, text)  
            widget.see(tk.END)  
        count += 1

def receive_message(client_socket):
    global running
    while running:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == "STOP":
                running = False
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def create_dialogs(index):
    if running:  # Continue creating dialogs while the program is running
        dialog = tk.Toplevel(root)
        dialog.title(f"Program Output {index + 1}")
        dialog.geometry("1200x800")
        dialog.resizable(False, False)
        
        output = tk.Text(dialog, wrap=tk.WORD, state=tk.NORMAL)
        output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        output_widgets.append(output)
        
        # Schedule the next dialog creation after 1 second
        root.after(500, create_dialogs, index + 1)


root = tk.Tk()
root.title("Main Window")
root.geometry("1200x800")
root.resizable(False, False)

output_widgets = []


create_dialogs(0)


HOST = "10.22.27.252" # This is the ip address of the server computer connected in a common network with the client. Use relevant command to see the ip address of your pc and keep it here
PORT = 65432        # The port used by the server.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Start the output generation in a separate thread
    thread = threading.Thread(target=run_program, args=(output_widgets,))
    thread.daemon = True
    thread.start()
    
    # Start a thread to listen for messages from the server
    listen_thread = threading.Thread(target=receive_message, args=(s,))
    listen_thread.daemon = True
    listen_thread.start()

    # Run the Tkinter event loop
    root.mainloop()
