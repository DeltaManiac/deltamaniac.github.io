+++
title = "Maelstrom: Echo"
date = "2025-09-05T20:20:53.546000+05:30"
tags = ["programming","golang","distributed systems"]
draft = false
type = "post"
+++

# Maelstrom

[Jepsen Maelstrom](https://github.com/jepsen-io/maelstrom) is an educational tool that simulates a distributed system in which nodes communicate with JSON over stdin/stdout. Maelstrom handles the network simulation and we have to handle distributed system logic.

## Echo

This is the first challenge and is a good one to get started.

> Recieve a message with some text and send it back

For the echo message which looks like:

```json
{
  "src": "c1",
  "dest": "n1", 
  "body": {
    "type": "echo",
    "msg_id": 1,
    "echo": "Hello, world!"
  }
}
```

and respond with:
```json
{
  "src": "n1",
  "dest": "c1",
  "body": {
    "type": "echo_ok", 
    "msg_id": 2,
    "in_reply_to": 1,
    "echo": "Hello, world!"
  }
}
```

### Understanding the Fields

- `src/dest`: Message routing - who sent it and who should receive it
- `type`: What kind of message this is (echo request → echo_ok response)
- `msg_id`: Unique identifier for each message sent
- `in_reply_to`: Links the response message back to the original request
- `echo`: The actual payload to echo back

### Implementing the Node

The node needs to be a message-processing loop that:

1. Reads line from stdin
2. Parse JSON message
3. Check message type 
4. Handle the specific message
5. Generate response
6. Write JSON response to stdout
7. Wait for next message from stdin

The `Node` struct holds the handles to stdin and stdout. It also keeps track of the message id to respond with.
```golang
type Node struct {
    id     string
    reader io.Reader
    writer io.Writer
    msgID  int
}
```


#### Handling Message

The message handling implementation has to be decoupled from the processing and parsing of each message.

```golang
func (n *Node) handleMessage(msg Message) error {
    body, ok := msg.Body.(MessageBody)
    if !ok {
        return fmt.Errorf("invalid message body type")
    }

    switch body.GetType() {
    case MsgInit:
        return n.handleInit(msg, body.(*InitBody))
    case MsgEcho:
        return n.handleEcho(msg, body.(*EchoBody))
    default:
        return fmt.Errorf("unhandled message type: %s", body.GetType())
    }
}
```

#### The Init Message

Before handling any messages the node must be initialized. This is done via responding to the `init` message with an `init_ok` which tells Maelstrom that the node is ready to handle requests

Request:
```json
{
  "src": "c1",
  "dest": "n1",
  "body": {
    "type": "init",
    "msg_id": 1,
    "node_id": "n1",
    "node_ids": ["n1", "n2", "n3"]
  }
}
```

Reponse:
```json
{
  "src": "n1", 
  "dest": "c1",
  "body": {
    "type": "init_ok",
    "msg_id": 1,
    "in_reply_to": 1
  }
}
```

### Resources

- [Maelstrom Documentation](https://github.com/jepsen-io/maelstrom/blob/main/doc/01-getting-ready/index.md)

- [Fly.io Distributed Challenge](https://fly.io/dist-sys/)

- [Solution Implementation](https://github.com/DeltaManiac/maelstrom/tree/echo)