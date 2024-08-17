# ALU-AUTO-IP-CHANGER
ALU Auto IP Changer ALU Auto IP Changer is a Python tool designed to automatically change the public IP address of your internet connection at regular intervals using the Tor network. This tool leverages the power of the Tor network to maintain anonymity and enhance privacy by periodically switching to a new IP address.

"FEATURES"
Automated IP Change: Automatically changes the IP address every 2 minutes.
Tor Integration: Uses the Tor network for routing internet traffic, ensuring anonymity.
Simple and Efficient: Lightweight script with minimal dependencies.
Customizable Timing: Easily adjust the interval between IP changes.

"USAGE"
Install Dependencies
Copy code
pip install stem requests
pip install stem requests pyfiglet
Python: Ensure you have Python installed on your system. You can download it from python.org.

Tor: Install the Tor service on your machine. Instructions can be found here.

Python Packages: Install the necessary Python packages using pip.

sh
Copy code
pip install stem requests pyfiglet
Configure Tor
Start Tor: Make sure the Tor service is running. On most systems, you can start it with the following command:

Copy code
tor
Tor Configuration: Ensure that the Tor control port is configured to use port 9051. This is usually set by default. If not, you may need to edit the torrc file located in your Tor installation directory.
sh
Copy code
ControlPort 9051
HashedControlPassword <hashed_password>
To generate the HashedControlPassword, use the tor --hash-password <your_password> command.


Run Tor: Ensure the Tor service is running on your machine. The default Tor control port is 9051 and SOCKS port is 9050.

Configure the Script: Set your Tor password in the get_new_ip function.

Execute the Script: Run the script to start changing your IP address periodically.
