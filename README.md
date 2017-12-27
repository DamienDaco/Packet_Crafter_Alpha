# Packet Crafter Alpha
Experimental version of Packet Crafter.

DISCLAIMER: This app was made for ethical hacking labs.
Please use responsibly. Improper usage of this kind of tool can get you prosecuted and/or fired.

This is a GUI app to automate ARP spoofing/poisonning attacks.
With this app, it is extremely simple to poison both the victim and the gateway.
All the user has to do is to input the victim's IP, and the app will take care of the rest.

![alt text](http://i.imgur.com/WvJLYVe.png)

Features:

-Selectable network interface (Defaults to loopback interface)

-Automatic gateway IP and MAC discovery

-Automatic victim's MAC discovery

-Automatic host IP and MAC discovery

-Man in the Middle mode: sends ARP replies to the victim AND the gateway. (1Hz frequency)

-Normal mode: Manual ARP queries. Lets you specify all the ARP options for fun. Experiment with weird ARP options and check the results with Wireshark ;)


