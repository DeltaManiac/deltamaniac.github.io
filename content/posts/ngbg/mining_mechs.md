+++
title = "NGBG: Mining Mechs"
date = "2024-09-16T23:13:48.573000+05:30"
tags = ["games","savefile","ngbg","json"]
draft = false
type = "post"
+++

# Mining Mechs

![](/images/ngbg/mining_mechs/1.png)

Steam Link : https://store.steampowered.com/app/1603180/Mining_Mechs/

Savefile Location : _C:\Users\\%PROFILE%\AppData\Local\Mining_Mechs_

File Name : _save_data_0.sav_

Format : _JSON_

## What is this game about?

Mining Mechs is a 2D indie game where you control a mech to mine for resources.

The gameplay loop is simple, fun, and addictive:

    Mine for materials.
    Sell those materials for in-game currency.
    Upgrade your mech to mine faster and carry more materials.
    Repeat!

## Analyzing the save game

The save game is a plain JSON file, although it's quite large. It contains information like the map, items in the map, player stats, etc. Based on the screenshot from the game, the in-game currency value is displayed in the top-right corner:

![](/images/ngbg/mining_mechs/2.png)

Open the file in a text editor of your choice, I've used VS Code here.
To quickly find which field to modify, search for that value in the save file. Open your favorite text editor, hit `Ctrl+F`, and paste the value. In my case, it was __5370__, and I found it under `root.player_<id>.money`. I changed it to an arbitrary value __69420__ and the next time I launched the game, the change was reflected.

![](/images/ngbg/mining_mechs/3.png)


![](/images/ngbg/mining_mechs/4.png)

---

Have fun—no more grinding necessary for materials!