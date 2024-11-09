+++
title = "NGBG: Nightmare: The Lunatic"
date = "2024-11-08T23:13:48.573000+05:30"
tags = ["games","savefile","ngbg","json","encoding"]
draft = false
type = "post"
+++

# Nightmare: The Lunatic

![](/images/ngbg/nightmare_the_lunatic/nightmare_the_lunatic_1.png)

Steam Link : https://store.steampowered.com/app/1842730/Nightmare_The_Lunatic/ 

Savefile Location : _C:\Users\micro\AppData\LocalLow\MaetdolGames\Nightmare The Lunatic

File Name : _SAVE_1.dat_

Format : _Base64-encoded JSON_

## What is this game about?

Nightmare: The Lunatic is a fast-paced, rogue-lite platformer with a focus on precise parrying mechanics. You play as a silent protagonist trapped in a nightmare, attempting to escape its clutches. Each run strengthens your character with items and upgrades to aid your next attempt, creating an addictive gameplay loop. As you progress, you gather resources to unlock items and power-ups, making each run more rewarding.

The gameplay loop is simple, fun, and addictive:

    Select 3 Weapons.
    Fight your way to the levels.
    Complete the run or die.
    Unlock cool stuff.

![](/images/ngbg/nightmare_the_lunatic/nightmare_the_lunatic_2.png)


## Analyzing the save game

For those who’d like to skip the grind and tweak their save file, the process is fairly simple. The save file for Nightmare: The Lunatic is in Base64-encoded JSON format, which can be edited after decoding. Here’s a step-by-step guide to modify the save file.

1. **Step 1:** Open the save file (`SAVE_1.dat`) in any text editor.

![](/images/ngbg/nightmare_the_lunatic/nightmare_the_lunatic_3.png)

2. **Step 2:** Copy and paste the contents into a base64 decoder, here we use  [base64decode.org](https://www.base64decode.org/) 

![](/images/ngbg/nightmare_the_lunatic/nightmare_the_lunatic_4.png)

3. **Step 3:** Copy the decoded value into a text editor and modify the values. The key resources that can be modified are `ArtifactFragment`, `DreamCrystal` and `DreamShard`.
![](/images/ngbg/nightmare_the_lunatic/nightmare_the_lunatic_5.png)

4. **step 4:** Copy and paste the modified contents into a base64 encoder, here we use  [base64encode.org](https://www.base64encode.org/) 

5. **step 5:** Copy the newly encoded text back into your SAVE_1.dat file and save it.

![](/images/ngbg/nightmare_the_lunatic/nightmare_the_lunatic_6.png)

---

Have fun—no more grinding necessary!