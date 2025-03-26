# Packet Capture and Filtering Script with Scapy

This Python script is designed to use a machine as a **gateway** in a network, intercepting and analyzing the packets passing through it. The script utilizes the `Scapy` library to capture and analyze network packets and the `NetfilterQueue` library to interact with Netfilter queues, redirecting traffic.

The script allows the machine running it to act as a gateway for other devices on the network, redirecting packets through a handler that can be customized to perform actions such as traffic analysis or filtering.

## Requirements

- **Python 3.x**: The script is written in Python and requires Python version 3 or higher.
- **Dependencies**:
  - `scapy`: For analyzing and manipulating network packets.
  - `netfilterqueue`: For interacting with Netfilter queues and capturing network packets.

You can install the dependencies with the following command:
  
```bash
pip install scapy netfilterqueue
```

* **Root privileges**: The script requires root privileges to modify `iptables` rules and process network packets.

## Script Description

The script performs the following tasks:

1. **Root privilege check**: If the script is not run with root privileges, it will terminate and display an error message.

2. **Packet redirection with `iptables`**: The script configures `iptables` rules so that all network traffic is routed through a Netfilter queue. The traffic is processed by the script before being forwarded to its destination.

   - Redirects all network traffic to queue number 1.
   - Sets up a NAT (Masquerading) rule to allow outgoing traffic to pass through the `ens33` network interface, enabling the machine to act as a gateway.

3. **Packet handling**: When packets arrive at the Netfilter queue, they are processed by the `packet_handler` function. Here, they can be analyzed and modified using the `Scapy` library. In this example script, packets are accepted without modification, but the code can be extended to perform specific actions on the packets.

4. **Graceful exit**: If the script is interrupted (e.g., with `Ctrl+C`), the `iptables` rules are restored, and the script terminates gracefully.

## Usage

1. **Running the script as root**: Since the script interacts with `iptables` to modify traffic rules, it must be run with root privileges. You can execute the script with the following command:

```bash
sudo python3 script.py
```

2. Interrupting and stopping the script

The script can be stopped at any time by pressing `Ctrl+C`, which will remove the iptables rules and terminate the script safely.