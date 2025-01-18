## ForkBombSimulator (A Client-Server based program)

This project is a customized version of the traditional ForkBomb bash script with some added GUI. It consists of a client-server application built with Python. The client, when executed, connects to the server and displays simulated program output in real-time through a graphical user interface (GUI) built with Tkinter. The program continuously displays a "Critical error" message with incremental count numbers in separate dialog windows.

The server sends a "STOP" message to the client, at which point the client stops displaying output and terminates the program.

## Features
- **Real-time Output Display**: The client displays continuous program output in separate Tkinter windows.
- **Simulated Program Output**: The client simulates a program that produces output with a "Critical error" message.
- **Multiple Output Windows**: Each output window receives real-time program messages.
- **Client-Server Communication**: The client and server communicate over a socket, where the server can send commands to control the client's behavior.
- **Graceful Termination**: The client gracefully stops displaying output when the server sends the "STOP" message.

## Disclaimer⚠️❗
The program continously generates random dialogue boxes in 500ms time intervel which can be modified by the user and can be stopped only by sending the STOP message by the server. Continously ruunning the script may slow down your PC. It is created just for fun with your friends and doesnot amplify any malicious activity.

### To modify the time interval
Change 500 to your desired time interval
```bash
root.after(500, create_dialogs, index + 1)
```

## Installation

### Prerequisites

Make sure you have Python 3.x installed on your system.

You can download Python from the official website: https://www.python.org/downloads/

### Required Libraries

The following libraries are required for the client-server communication and Tkinter GUI:

- **Tkinter** (for GUI): Tkinter is usually included by default with Python installations.
- **Socket** (for networking): The socket library is also included in Python by default.
- **Threading** (for concurrent execution): Threading is included in Python by default.

To check if Tkinter is installed, run the following in your terminal:

```bash
python -m tkinter
```

 
