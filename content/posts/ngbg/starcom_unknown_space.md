+++
title = "NGBG: Starcom Unknown Space"
date = "2025-12-27T23:13:48.573000+05:30"
tags = ["games","savefile","ngbg","json"]
draft = false
type = "post"
+++

# Cobalt Core

![](/images/ngbg/starcom_unknown_space/starcom_unknown_space_1.png)

Steam Link : https://store.steampowered.com/app/1750770/Starcom_Unknown_Space/

Savefile Location : _C:\Users\Hari\AppData\LocalLow\Wx3 Labs, LLC\Starcom Unknown Space\saves_

File Name : _<save_name>.json_

Format : _JSON_

## What is this game about?

Starcom: Unknown Space is an action RPG of space exploration and adventure. Build your own starship while discovering an epic story in a universe of strange mysteries, alien factions and uncharted worlds. variety of crew memebers to unlock and ships to build.

The gameplay loop is simple, fun, and addictive:

    You have a ship and a crew.
    You do mission and exploration.
    You most of the time fight other ships.
    Progress the story and upgrade your ship/crew/research


![](/images/ngbg/starcom_unknown_space/starcom_unknown_space_2.png)

The image above does not do the game justice. **IT IS SUPER FUN.**

## Analyzing the save game

The save game is a plain JSON file, although it's a bit large. It contains information like the world, anomalies on the map, ship, artifacts player data etc.

![](/images/ngbg/starcom_unknown_space/starcom_unknown_space_3.png)

The `playerData` node is the most important piece of data in the game regarding your ship. This is where the major modifications would go for an easier game and no heavy grind.

![](/images/ngbg/starcom_unknown_space/starcom_unknown_space_4.png)

Modify the `researchPoints` and `totalResearchPoints` nodes to give yourself points to unlock the items on the research tree.

![](/images/ngbg/starcom_unknown_space/starcom_unknown_space_5.png)

![](/images/ngbg/starcom_unknown_space/starcom_unknown_space_6.png)

Modify the `playerResources` node for gifting yourself ingame materials.

![](/images/ngbg/starcom_unknown_space/starcom_unknown_space_7.png)

![](/images/ngbg/starcom_unknown_space/starcom_unknown_space_8.png)

In order to give your crew more XP youll have to modify the `crewData` node. Just update the value of the `unspentPoints` and assign those values to the crew members once in the game.

![](/images/ngbg/starcom_unknown_space/starcom_unknown_space_9.png)

![](/images/ngbg/starcom_unknown_space/starcom_unknown_space_10.png)

![](/images/ngbg/starcom_unknown_space/starcom_unknown_space_11.png)

---

Have fun—no more grinding necessary!