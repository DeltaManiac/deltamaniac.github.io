---
id: qeciETQdP6y5coUZpEL1W
title: Resource Locating and Traffic Routing
desc: ''
updated: 1640612909137
created: 1640232890111
nav_order: 2
---

# Internet Protocol

Set of rules that dictate the format of the data send over a network

## IPv4 Addressing

32-bit numbers as 4 octets

### Network and Host IDs

IPv4 address represents two component : networkID and host ID

**NetworkID**: informs the network devices(routers) responsible for shuttling packets toward their destination about the the next appropriate hop in the transmission

**HostID**: router uses the hostID to deliver data to a specific recipient

For a 32-bit IPv4 address depending on the network size the networkID is computed and the remaining bits compute the hostID

e.g. in a 16-bit Network the first two octets determine the networkID and the remaining two octets determine the hostID

For address 192.168.212.056 in a 16-bit network

<pre>

       IPv4 Address
     ---------------
     192.168.212.056
            |
            |
192.168.0.0 | 0.0.212.056
------------|------------
NetworkID   | HostID
</pre>

### Subdividing IPv4 Addresses into Subnets

**Subnets**: Nodes that have same NetworkID but unique HostID

**CIDR**: Classless Inter-Domain Routing

Indicate number of bits in the networkID by appending a network prefix for each IP address. It consists of a forward slash and an integer

Network IP derived by applying a subnet mask

e.g. 192.168.15.69/16 -> 16 bit network and the first 16 bits are the networkID


CIDR Prefix length | Subnet Mask     | Available Networks | Hosts/Network
-------------------|-----------------|--------------------|--------------
8                  | 255.0.0.0       | 1                  | 16,777,214
9                  | 255.128.0.0     | 2                  | 8,388,606
10                 | 255.192.0.0     | 4                  | 4,194,302
11                 | 255.224.0.0     | 8                  | 2,097,150
12                 | 255.240.0.0     | 16                 | 1,048,574
13                 | 255.248.0.0     | 32                 | 524,286
14                 | 255.252.0.0     | 64                 | 262,142
15                 | 255.254.0.0     | 128                | 131,070
16                 | 255.255.0.0     | 256                | 65,534
17                 | 255.255.128.0   | 512                | 32,766
18                 | 255.255.192.0   | 1,024              | 16,382
19                 | 255.255.224.0   | 2,048              | 8,190
20                 | 255.255.240.0   | 4,096              | 4,094
21                 | 255.255.248.0   | 8,192              | 2,046
22                 | 255.255.252.0   | 16,384             | 1,022
23                 | 255.255.254.0   | 32,768             | 510
24                 | 255.255.255.0   | 65,536             | 254
25                 | 255.255.255.128 | 131,072            | 126
26                 | 255.255.255.192 | 262,144            | 62
27                 | 255.255.255.224 | 524,288            | 30
28                 | 255.255.255.240 | 1,048,576          | 14
29                 | 255.255.255.248 | 2,097,152          | 6
30                 | 255.255.255.252 | 4,194,304          | 2

<pre>
<b>
e.g. For address 192.168.1.1/9 the mask is the first 9 bits
    192  |    168   |   1      |     1
11000000 | 10101000 | 00000001 | 00000001

Mask the first 9 bits

11111111 | 10000000 | 00000000 | 00000000
 255     |    0     |     0    |     0

 Network IP -> Ip Address & Mask
11000000 | 10101000 | 00000001 | 00000001
                AND
11111111 | 10000000 | 00000000 | 00000000
-------------------------------------------
11000000 | 10000000 | 00000000 | 00000000
    192  |     1    |     0    |     0

so the possible IP addresses could be 192.1.0.0 and 192.0.0.0
</b>
</pre>

Each network has 2 reserved host addresses.

The first Ip address in e.g. 192.168.0.0/16 is 192.168.0.0 is the network address and the last address 192.168.255.255 is the broadcast address

### Allocating Networks that don't break at an Octet Boundary

IpAddr: 192.168.156.97/19
<pre>
<b>
            192  |    168   |   156    |    97
        11000000 | 10101000 | 10011100 | 01100001

Network ID

    |         19-Bits       |
    -------------------------
    11000000 | 10101000 | 10000000 | 00000000
        192  |   168    |    128   |    0


Host ID
                                 |    13-Bits   |
                                 ----------------
        00000000 | 00000000 | 00011100 | 01100001
           0     |     0    |  28      |   97
</b>
</pre>

### Network Address Translation

**Network Address Translation**: Process that allows numerous nodes to share the same public address

Devices: Firewall, Load Balancer, Router

![](/assets/images/2021-12-23-17-53-46.png)

##### Steps

1. NAT Capable device receives a connection from the client socket 10.0.0.3:50926

2. NAT requests the destination with its own IP 1.2.3.4:50926 and port being mapped to the internal client

3. The response received is then sent to the client

### Unicast, Multicast and Broadcast

**Unicast**: Sending packets from one IP address to another IP address

**Multicast**: Sending a singe message to a group of nodes

**Broadcast**: Concurrently deliver a message to all IP addresses in a network (Achieved via sending messages to the broadcast address of its subnet)

### Resolving MAC Address to a Physical Network Connection

The MAC address is relevant to only the local network.


## IPv6 Addressing

128-bit numbers arranged in colon-separated groups of 16bits(hextets)

e.g. 4d61 : 6e64 : 792c : 2042 : 656e : 2c20 : 4c69 : 6c79

#### Simplifying IPv6

To simplify an IPv6 address e.g. `fd00:4700:0010:0000:0000:0000:6814:d10`

1. Safely remove all leading zeros in each hextet

    `fd00:4700:10:0:0:0:6814:d103`

2. Replace leftmost group of consecutive zero-valued hextets with double colons

    `00:4700:10::6814:d103`

#### IPv6 Network and Host Addresses

**Network Address**: 0-64Bits

**Global Routing Prefix**: 0-48 bits

**Subnet Id**: 49-64 bits

<pre>
+------Network Address-----+
|                          |
|4d61 : 6e64 : 792c : 2042 : 656e : 2c20 : 4c69 : 6c79|
|_________GRP_______|      | |                        |
                    |______| |                        |
                    SubnetID +-----Interface ID-------+
</pre>

#### IPv6 Address Categories

##### Unicast

Uniquely identifies a node. Enables 1:1 communication

##### Multicast

Multicast addresses represents a group of nodes. Enables 1:n communication

#### Anycast

Anycast addresses represents a group of node listening to the same address.
