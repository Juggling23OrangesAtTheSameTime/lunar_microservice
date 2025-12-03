# this file does not require any editing for file paths

import socket
import json
import ephem


HOST = "127.0.0.1"
PORT = 5000



def cmd_moon_info(params):
    
    date = ephem.now()
    moon = ephem.Moon(date)
    illumination = moon.phase / 100.0

    next_full = ephem.next_full_moon(date)
    next_new = ephem.next_new_moon(date)

    if illumination < 0.01:
        phase = "New Moon"
    elif illumination > 0.99:
        phase = "Full Moon"
    elif moon.phase < 50:
        phase = "Waxing"
    else:
        phase = "Waning"

    return {
        "date": str(date),
        "illumination_percent": round(illumination * 100, 2),
        "phase": phase,
        "next_full_moon": str(next_full),
        "next_new_moon": str(next_new)
    }



COMMANDS = {
    "moon_info": cmd_moon_info
}

def start_server():
    print(f"Starting JSON command server on {HOST}:{PORT}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        while True:
            conn, addr = server.accept()
            handle_client(conn, addr)


def handle_client(conn, addr):
    print(f"Client connected: {addr}")
    with conn:
        data = conn.recv(4096).decode().strip()
        if not data:
            return
        response = handle_request(data)
        conn.sendall(json.dumps(response).encode() + b"\n")


def handle_request(data):
    try:
        request = json.loads(data)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON"}
    command = request.get("command")
    if command not in COMMANDS:
        return {"error": f"Unknown command '{command}'"}
    try:
        return COMMANDS[command]
    except Exception as e:
        return {"error": f"Command failed: {str(e)}"}


if __name__ == "__main__":
    start_server()
