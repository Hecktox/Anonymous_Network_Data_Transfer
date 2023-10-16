# TOR Network Simulator
TOR Network simulator with RSA encryption using Python, Flask, and Socket programming for anonymous data transmission between nodes.

## How does data stay anonymous between nodes
We used a different method than what TOR actually does.
The Tor Browser encrypts the message to be sent on many layers, and each node it passes through will decrypt the body, containing a new message and location to send to. 

Our algorithm encrypts the ips to each nodes that the message must pass through, with the public key of the node it must receive it from. Every node will then try to decrypt the ips in the list, and whichever it's able to decrypt, is the next node in the chain. This way, every node will only konw who they received the message from, and they only know who to send it to next, and only the client knows the full chain of nodes and final destination. 

**The Advantage** is that the message size doesn't grow as multiple layers of encryption are added.

## Encryption method
We used RSA encryption method in order to encrypt the ips and the message to send. Each node makes their public key available by request, but we also have them hard coded in a text file, and should have functionality for a main server in the future, to protect clients identity.

