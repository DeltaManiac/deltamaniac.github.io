---
id: wfOGHenRJP9nCVGtK2e5V
title: Reliable TCP Streams
desc: ''
updated: 1640619233740
created: 1640531504058
nav_order: 3
---

# TCP

**Packet Loss**: Occurs when data fails to reach its destination

**Network Congestion**: Occurs when nodes attempt to send more data over a network connections than the connection can handle which causes nodes to discard the excess packets

**Flow Control**: Adaptation of transfer rate to make sure it transmits data as fast as possible while keeping dropped packets to a minimum


### TCP Session

Established with a three-way handshake

<pre>

                   CLIENT                      SERVER
               Dial  |                           | Listen
                     |                           |
                     | ----------SYN-----------> |
                     |                           | Accept
                     | <-------SYN/ACK---------- |
        Established  |                           |
                     | ----------ACK-----------> | Established

</pre>

### Handshake

1. Client sends a packet with the synchronize(SYN) flag to the server which contains client's capabilities and preferred window settings

2. Server responds with both the acknowledgement(ACK) and SYN flag set in the packet

3. Client responds with ac ACK packet to acknowledge the server's SYN packet.


#### Acknowledgin Receipt of Packets by using Sequence Number
<pre>

                 CLIENT                             SERVER
                    |        SYN (Seq = X)            |
                    |-------------------------------->|
                    |                                 | Received
                    |        SYN (Seq = Y)            | Client Seq = X
                    |<--------------------------------|
           Received |        ACK (Seq = X+1)          |
     Server Seq = Y |                                 |
                    |-------------------------------->|
                    |        ACK (Seq = Y+1)          |
                    |                                 |
</pre>

Sequence number is determined by the sender of the message

#### Receive Buffers and Windows Sizes

TCP allows a single ACK packet to acknowledge the receipt of more than one incoming packet.

Receiver must advertise to the sender how much space it have available in its receive buffer before it sends an acknowledgment

**Receive Buffer**: per connection block of memory reserved for incoming data on a network connection

