
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


#### Acknowledging Receipt of Packets by using Sequence Number
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

**Window Size**: Information in the ACK packet which is the number of bytes the sender can transmit to the receiver without requiring an acknowledgement

<pre>
              Client                         Server
                |                               |
                |   ACK (Window size = 3072)    |
Acknowledging   |------------------------------>| Client can Receive 3072 bytes
data            |                               |
                |                               |
                |         (1024 bytes)          |
                |<------------------------------|
                |                               |
                |         (1024 bytes)          |
                |<------------------------------|
                |                               |
                |         (1024 bytes)          |
Buffer full     |<------------------------------|
with 3072 bytes |                               |
                |                               |
                |   ACK (Window size = 2048)    |
Acknowledging   |------------------------------>| Client can Receive 2048 bytes
data            |                               |
                |         (1024 bytes)          |
                |<------------------------------|
                |                               |
                |         (1024 bytes)          |
Buffer full     |<------------------------------|
with 2048 bytes |                               |
</pre>

### Termination TCP Sessions

1. Client connections changes from `ESTABLISHED` to `FIN_WAIT_1`

2. Server acknowledges the client's `FIN` and changes its state from `ESTABLISHED` to `CLOSE_WAIT`

3. Server sends it own `FIN` packet changing its state to `LAST_ACK` and waits for final acknowledgement from client

4. The client acknowledges the server's `FIN` and enters `TIME_WAIT` state and sends the final`ACK`

5. The client waits for the the *maximum segment life-time* then changes its connection state to `CLOSED`

<pre>
              Client                         Server
                |                               |
    Established |                               | Established
                |                               |
                |           FIN                 |
    FIN_WAIT_1  |------------------------------>|
                |           ACK                 | CLOSE_WAIT
                |<------------------------------|
    FIN_WAIT_2  |                               |
                |                               |
                |                               |
                |           FIN                 |
                |<------------------------------| LAST_ACK
     TIME_WAIT  |           ACK                 |
                |------------------------------>|
                |                               | CLOSED
        CLOSED  |                               |
</pre>


### Handling Less Graceful Terminations

When connections are closed/terminated, any connection from the other side of the connection will prompt the closed side of the connection to return  `RST` packet(reset)
