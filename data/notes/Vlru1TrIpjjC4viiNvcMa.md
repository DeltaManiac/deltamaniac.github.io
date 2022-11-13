# Intro

**Computer Network** : Connection between two or more devices/nodes that allow each node to share data

# Network Topologies

**Topology** : Organization of nodes in a network

### Point to Point

![](/assets/images/2021-12-22-06-51-39.png)

### Daisy Chain

**Hop**: Intermediate Node between source and destination node

![](/assets/images/2021-12-22-06-52-01.png)

### Bus

![](/assets/images/2021-12-22-06-55-34.png)

Most common in wireless networks

### Ring

![](/assets/images/2021-12-22-06-58-10.png)

Traffic travels in a single direction

Speed can be limited by slowest node in the network

### Star

![](/assets/images/2021-12-22-07-21-27.png)

Most common in wireless networks

Central node is mostly a network switch

Data can traverse on a single hop

### Mesh

![](/assets/images/2021-12-22-07-27-34.png)

### Hybrid

![](/assets/images/2021-12-22-07-30-29.png)


# Open Systems Interconnection Reference Model

OSI Model standardizes networking

**Protocols**: Rules and procedures that determine the format and order of data sent over a network

![](/assets/images/2021-12-22-20-11-06.png)

## Layer 7 - Application

Responsible for identifying hosts and retrieving resources

e.g. Browsers, Torrent Client

## Layer 6 - Presentation

Prepares data for the network layer when data moves down the stack and for application layer when data moves up the stack

Functions: Encryption/Decryption Encoding

## Layer 5 - Session

Manages connection lifecycle between nodes on a network

Functions: Connection establishment, managing connection timeouts, coordinating the mode of operation and connection termination

## Layer 4 - Transport

Controls and coordinates transfer of data between nodes while maintaining the reliability

Functions: Correcting errors, speed control, chunking data, ack-ing received data

## Layer 3 - Network

Transmits data between nodes without having a direct point to point connection to the remote node

Functions: Network management protocols for routing, addressing, multicasting and traffic control

## Layer 2 - Data Link

Handles data transfers between two directly connected nodes

Function: Error detection and Error Correction

## Layer 1 - Physical

Converts bits from the network stack to the physical medium

Controls bit rate

# Sending Traffic by Using Data Encapsulation

**Payload**: Data travelling down the stack

**Horizontal Communication**: Communication between client and server on the same layer

![](/assets/images/2021-12-22-21-08-28.png)

![](/assets/images/2021-12-22-21-09-23.png)

# TCP/IP Model

**End-to-End Principle**: Each network segment includes only enough functionality to properly transmit and route bits; all other functionality belongs to the endpoints.

![](/assets/images/2021-12-22-21-30-48.png)

## Application Layer

Interacts directly with software applications

Encompasses three OSI layers

Protocols: FTP, HTTP, SMTP

Function: DHCP, DNS

## Transport Layer

Handles transfer of data between two node

Ensures data integrity

Protocols: TCP, UDP

## Internet Layer

Responsible for routing packets of data

Protocols: IPv4, IPv6, BGP, ICMP, IGMP, IPsec

Function: Data Delivery

## Link Layer

ARP Translates nodes IP address to MAC address of network interface
