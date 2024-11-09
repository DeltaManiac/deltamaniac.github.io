+++
title = "NGBG: Cobalt Core"
date = "2024-10-27T23:13:48.573000+05:30"
tags = ["games","savefile","ngbg","json"]
draft = false
type = "post"
+++

# Cobalt Core

![](/images/ngbg/cobalt_core/cobalt_core_1.png)

Steam Link : https://store.steampowered.com/app/2179850/Cobalt_Core/

Savefile Location : _C:\Users\\%PROFILE%\AppData\Roaming\CobaltCore\Slot0_

File Name : _Save.json_

Format : _JSON_

## What is this game about?

Cobalt Core is a 2D indie sci-fi roguelike deckbuilder set in space and a time loop. Its a fun game with a variety of crew memebers to unlock and ships to build.
Each crew member gives a set of cards that can be played with the limited energy thats refunded each turn.

The gameplay loop is simple, fun, and addictive:

    Select a Crew.
    Select a Ship.
    Fight other ships.
    Complete the run.
    Unlock and view the memory for a single crew memeber
    Repeat until all memories are unlocked and reach the finale!

![](/images/ngbg/cobalt_core/cobalt_core_2.png)


## Analyzing the save game

The save game is a plain JSON file, although it's not that large. It contains information like the map, items in the map, ship, artifacts etc.

![](/images/ngbg/cobalt_core/cobalt_core_3.png)

The `ship` node is the most important piece of data in the game. This is where the major modifications would go for an easier game and no heavy grind.

![](/images/ngbg/cobalt_core/cobalt_core_4.png)
`

1. **Step 1:** Open the save file (`Save.json`) in any text editor.

2. **Step 2:** Locate the `ship` entry—these are your major things that make the gameplay easy.

   - `baseEnergy` directly corresponds to the action points you get each turn.

   - `baseDraw` directly corresponds to the number of cards you draw each turn.

   - `hull` represent current health points.

   - `hullMax` represent max health points.

3. **Step 3:** Edit the values to your liking. For example, I’ve changed my hull and hullMax to 69.

Save the file, and voila! You’re all set with maxed-out hp.

![](/images/ngbg/cobalt_core/cobalt_core_5.png)


### A Few Notes on Editing

- Be cautious when modifying baseDraw, as you can only hold a maximum of 10 cards at any given time.

- If you're already in battle, changes to baseEnergy will only take effect on the next turn.

---

Have fun—no more grinding necessary!