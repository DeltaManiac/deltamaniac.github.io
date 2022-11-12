---
id: de9dmvtq24un4eg7t18os7y
title: JavaScript
desc: ''
updated: 1668235261910
created: 1668232329484
---

# Array Buffer

The ArrayBuffer object is used to represent a generic, fixed-length raw binary data buffer.
Synonymous to Byte Buffer

```js
const buffer = new ArrayBuffer(8); // 8 Bytes = 8*8bits = 64bits
const view = new Int32Array(buffer); // can store 2 elements of 32bit in buffer
console.log(view)
>    int32Array [ 0, 0 ]
>      0: 0
>      1: 0
>      buffer: ArrayBuffer { byteLength: 8 }
>      byteLength: 8
>      byteOffset: 0
>      length: 2
>      <prototype>: Int32Array.prototype { … }

const view2 = new Int16Array(buffer); // can store 4 elments of 16bit in buffer
console.log(view2)
>    int16Array [ 0, 0, 0, 0 ]
>      0: 0
>      1: 0
>      2: 0
>      3: 0
>      buffer: ArrayBuffer { byteLength: 8 }
>      byteLength: 8
>      byteOffset: 0
>      length: 4
>      <prototype>: Int16Array.prototype { … }
```

# Shared Array Buffer

The SharedArrayBuffer object is used to represent a generic, fixed-length raw binary data buffer, similar to the ArrayBuffer object, but in a way that they can be used to create views on shared memory. A SharedArrayBuffer is not a Transferable Object, unlike an ArrayBuffer which is transferable.