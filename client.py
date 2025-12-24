import tkinter as tk
import threading
import socket
import time
import random
import os
import sys


def play_beep():
    
    try:
        if sys.platform.startswith("win"):
            import winsound
            winsound.Beep(1200, 200)  
        else:
            # Linux / macOS fallback
            os.system('printf "\\a"')
    except Exception:
        pass


running = True
output_widgets = []


def run_program(output_widgets):
    
    count = 1
    global running

    while running:
        time.sleep(0.1)

        remaining = max(0, 100 - count)
        text = (
            f"[!!] KERNEL PANIC #{count}\n"
            f"     › Memory corruption detected\n"
            f"     › Unauthorized process escalation\n"
            f"     › Data integrity compromised\n"
            f"     › Encrypting disk sectors... {remaining}% remaining\n"
            f"     › DO NOT TURN OFF YOUR COMPUTER\n\n"
        )

        for widget in output_widgets:
            try:
                widget.insert(tk.END, text)
                widget.see(tk.END)
            except tk.TclError:
                pass

        count += 1


def receive_message(client_socket):
    
    global running

    while running:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message == "STOP":
                for widget in output_widgets:
                    widget.insert(
                        tk.END,
                        "\n[✔] Remote override detected.\n"
                        "[✔] System stabilized.\n"
                        "[✔] Threat neutralized.\n"
                    )
                running = False
                break
        except Exception as e:
            print(f"Error receiving message: {e}")
            break


def flash_title(dialog, state=True):
    
    if not running:
        return

    dialog.title(
        "⚠ SYSTEM BREACH DETECTED ⚠"
        if state
        else "!!! DATA LOSS IMMINENT !!!"
    )
    dialog.after(300, flash_title, dialog, not state)


def create_dialogs(index):
    
    if not running:
        return

    #Beep Sound 
    play_beep()

    dialog = tk.Toplevel(root)
    dialog.configure(bg="black")

    x = random.randint(0, 400)
    y = random.randint(0, 200)
    dialog.geometry(f"1200x800+{x}+{y}")
    dialog.resizable(False, False)

    output = tk.Text(
        dialog,
        wrap=tk.WORD,
        bg="black",
        fg="red",
        insertbackground="red",
        font=("Courier New", 12, "bold"),
    )
    output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    output_widgets.append(output)

    flash_title(dialog)

    #EXTRA panic beep 
    root.after(150, play_beep)

    # Create next dialog after xx ms
    root.after(3000, create_dialogs, index + 1) #Change 3000 to 500 for speed 


#MAIN 

root = tk.Tk()
root.title("System Monitor")
root.geometry("1200x800")
root.configure(bg="black")
root.resizable(False, False)

create_dialogs(0)

HOST = "10.22.23.212"  # Server IP: look using ip addr show OR ipconfig 
PORT = 65432           # Server port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    output_thread = threading.Thread(
        target=run_program, args=(output_widgets,), daemon=True
    )
    output_thread.start()

    listen_thread = threading.Thread(
        target=receive_message, args=(s,), daemon=True
    )
    listen_thread.start()

    root.mainloop()
