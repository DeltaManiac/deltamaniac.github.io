+++
title = "Onigiri: A SSH Tunnel Manager"
date = "2025-02-22T02:13:48.573000+05:30"
tags = ["tools","ssh","rust","egui"]
draft = false
type = "post"
+++

# Building Onigiri: A Tale of SSH Tunnels and Rust Adventures

After years of juggling dozens of SSH tunnels for various databases, caches, and internal services, I finally snapped. You know that moment when you're frantically searching through terminal windows trying to remember which port maps to which staging Redis instance? Yeah, that one.

## The Breaking Point

Picture this: It's 3 AM, production is acting up, and I'm staring at my terminal trying to remember if port 6379 is pointing to the prod Redis or the staging Postgres. Fun times. After the third time of connecting to the wrong database (and nearly running DROP TABLE on staging instead of the local dev environment 😅), I decided enough was enough.

## Enter Onigiri

Why Onigiri? Well, just like how these Japanese rice balls wrap delicious fillings in a neat package, I wanted something to wrap my messy SSH tunnels in a clean GUI. Plus, _Santoryu_, if you know you know.

![](/images/onigiri/onigiri_1.png)

### The Tech Stack

I chose Rust + egui  because I wanted to learn how to build a decent immediate mode GUI app and Rust. Plus, I've always been fascinated by [imgui](https://github.com/ocornut/imgui). Before settling on this stack, I considered not to use electron.

## The Journey

### First Steps: Basic GUI

Starting with egui was surprisingly straightforward. Here's the basic window setup:

```rust
fn main() -> Result<(), eframe::Error> {
    let options = eframe::NativeOptions {
        viewport: eframe::egui::ViewportBuilder::default()
            .with_inner_size([400.0, 500.0])
            .with_resizable(false),
        ..Default::default()
    };

    eframe::run_native(
        "Onigiri",
        options,
        Box::new(|_cc| Box::new(Tunneler::new())),
    )
}
```

### The Data Model

The core of Onigiri is pretty simple. Each tunnel is just a struct:

```rust
struct Tunnel {
    id: i64,
    name: String,
    ssh_server: String,
    local_ip: String,
    local_port: u16,
    remote_ip: String,
    remote_port: u16,
}
```

### Lessons Learned

1. **SQLite is Your Friend**: Initially, I was tempted to use a fancy database. But SQLite with `rusqlite` turned out to be perfect. It's embedded, requires zero setup, and just works and its sooper duper easy.

2. **The Borrow Checker is... Interesting**: Coming from Go, I thought I knew what strict typing was. Oh boy, was I wrong. The Rust borrow checker humbled me real quick. This innocent-looking code:

```rust
fn update_tunnel(&mut self) {
    let tunnel = self.get_tunnel();
    self.save_tunnel(tunnel); // "hold my beer" - borrow checker
}
```

Led to my favorite compiler error message collection. The solution? Understanding ownership and learning to love `clone()` (but not too much).

3. **Process Management is Tricky**: Managing SSH processes taught me a lot about proper cleanup. The `Drop` trait became my best friend:

```rust
impl Drop for Tunneler {
    fn drop(&mut self) {
        info!("Cleaning up tunnel processes...");
        for (id, tunnel) in self.active_tunnels.iter_mut() {
            tunnel.stop_tunnel();
        }
    }
}
```

### The "Fun" Parts

1. **Icon Integration**: Ever tried to add a simple window icon? Here's a fun rabbit hole of image formats, RGBA conversions, and the joy of learning that different platforms expect different things. The solution? Use the `image` crate to handle format conversion and let egui handle platform differences:

```rust
let icon = image::load_from_memory(include_bytes!("../resources/icon.png"))
    .unwrap()
    .to_rgba8();
let icon = Arc::new(egui::IconData {
    rgba: icon.into_raw(),
    width: icon_width,
    height: icon_height,
});
```

2. **Cross-Platform Path Fun**: Windows uses backslashes, Unix uses forward slashes, and somewhere in between, your paths get mangled. The solution was to consistently use the `dirs` crate and `std::path::PathBuf` for all path operations:

```rust
let config_dir = dirs::config_dir()
    .map(|p| p.join("onigiri"))
    .unwrap_or_else(|| PathBuf::from("~/.config/onigiri"));
```

## The Result

After several weekends, countless coffee cups, and one minor incident where I accidentally tunneled to my neighbor's Minecraft server (long story), Onigiri was born. It's not perfect, but it:

- Manages SSH tunnels without me wanting to pull my hair out
- Hasn't deleted production (yet)
- Actually looks decent (thanks, egui!)
- Saves me from the "which port was it again?" dance
- Uses minimal resources (<50MB RAM, <1% CPU when idle)

## A Note on Code Quality

Let's be real here - this is very much a "works on my machine" kind of project right now. The code structure might make seasoned Rust developers cringe a bit (sorry about that massive main.rs file!), and there's definitely room for improvement in terms of:

- Error handling (currently it's a mix of Result, unwrap(), and "hope for the best")
- Code organization (everything is in one file because... reasons)
- Proper logging (println! debugging may have snuck in there)
- Test coverage (what are tests? 😅)

But you know what? It works. And sometimes that's exactly what you need - a working solution that solves your immediate problem. The code might not be the prettiest, but it's a solid foundation to build upon. Think of it as a well-functioning proof of concept that's gradually evolving into something more robust.

## The Distribution Dilemma

Speaking of "works on my machine," let's talk about distribution. Right now, Onigiri is very much a macOS-only affair (because that's what I use), and even that comes with some caveats:

### The Apple Signing Saga

Try distributing an unsigned app on modern macOS, and you'll be greeted with everyone's favorite message: "Cannot open because the developer cannot be verified." Getting a proper Apple Developer Certificate costs $99/year, which feels a bit steep for a free tool that just manages SSH tunnels. Currently, users need to:

1. Right-click the app and select "Open" (instead of double-clicking)
2. Click through a few scary security warnings
3. Possibly run some `xattr` commands to remove quarantine attributes
4. Question their life choices

```bash
# The classic "trust me, I'm a developer" command
xattr -dr com.apple.quarantine /Applications/Onigiri.app
```

### Platform Limitations

While Rust and egui are cross-platform, Onigiri currently:
- Only runs on macOS (tested on Sonoma)
- Assumes a Unix-style SSH setup
- Probably has interesting behaviors on different macOS versions that I haven't tested
- Might explode spectacularly on Linux or Windows (okay, maybe not explode, but you get the idea)

The irony of building a tool to make life easier, then making users jump through hoops to run it, isn't lost on me. It's definitely on the todo list to:
- Set up proper code signing (when I feel like splurging on that Apple Developer Certificate)
- Test on different macOS versions (anyone got a Catalina machine lying around?)
- Maybe explore Linux support (it should work... in theory)
- Create proper installation packages (because raw .app files are so 2010)

## What's Next?

1. Better error handling (because "it broke" isn't very helpful)
2. Tunnel groups for related services
3. Maybe a dark theme (because we all know dark theme makes everything better)
4. Actually writing tests (don't judge, we've all been there)
5. Proper code organization (splitting that monolithic main.rs into modules)
6. Better state management (because global state isn't always evil, but it's not great either)
7. Actual documentation (beyond just the "TODO: document this" comments)

**Current Status**: Active development, with updates roughly every two weeks. The project is stable enough for daily use but expect occasional rough edges. Check out the code at [GitHub](https://github.com/DeltaManiac/onigiri) - contributions welcome!

The beauty of side projects is that they don't have to be perfect from day one. They can grow and evolve as you learn more and as your needs change. Onigiri started as a quick fix for a personal annoyance, and that's exactly what it does - maybe not elegantly, but effectively.

## Conclusion

Building Onigiri taught me more than just Rust. It taught me that sometimes the best tools come from scratching your own itch, that the Rust compiler is both your worst enemy and best friend, and that naming projects while hungry leads to interesting choices.

The code is open source, feel free to check it out, and remember: every time you manually type an SSH tunnel command, somewhere a developer starts writing their own GUI tool.

Happy tunneling!