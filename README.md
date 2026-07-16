[[[FYI - This project was made before I found out about headless browsers so I definitely can make this much more efficient and plan to when I need to use it]]]
# Remote Automation Server

## Brief

The purpose of this project is to implement an API connected to an AI chat client. A remote computer (server) receives requests from a client, communicates with an AI service, and returns results. The goal is to create a free AI client that can be integrated into your own API and used for remote automation.

## Setup

### 1. Server Setup

Navigate to the server directory:

```bash
cd server
```

Install requirements:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Keep the server terminal running.

---

### 2. Client Setup

Open a new terminal.

Navigate to the client directory:

```bash
cd client
```

Install requirements:

```bash
pip install -r requirements.txt
```

Update the `.env` file with the server computer's IP address.

Run the client:

```bash
python main.py
```

### 3. Network Setup

For connections between different networks, install Tailscale on both computers.

Set the client's `.env` file to the server computer's Tailscale IP address.

Example:

SERVER_IP=100.x.x.x
SERVER_PORT=8000

---

### 4. Troubleshooting

If the automation does not work correctly, you may need to modify `automation.py` to match your system configuration.

Different operating systems and browser setups can launch applications in different ways, so the commands used to open a web browser may need to be adjusted for your computer.

By default, the automation is configured to use ChatGPT in a web browser. If you use a different browser, have a custom browser installation, or want to automate a different AI service, update the logic in `automation.py`.
