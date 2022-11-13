
## WASM

- Simple Machine Model 
- Executable Format

Two formats

    - `.wat` -> [[programming.S-Expressions]] Text format

    - `.wasm` -> Binary Format

`.wat` representation of adding two numbers
```scheme
(module
  (func (export "addTwo") (param i32 i32) (result i32)
    local.get 0
    local.get 1
    i32.add))
```


## Linear Memory Model Memory

WebAssembly has a very simple memory model. A wasm module has access to a single "linear memory", which is essentially a flat array of bytes

Wasm cannot access the GC-ed heap memory of JS. However JS can access the Linear Memory of WASM modules as Scalar `ArrayBuffer` type.
