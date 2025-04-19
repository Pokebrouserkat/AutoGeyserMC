# Dockerized auto-updating Minecraft Java Edition server and GeyserMC-Standalone

> **Skins currently do not work.**
> I don't know how to allow Bedrock and Java accounts to log in without mods that cause problems, particularly with automatic updates.

## Features or limitations depending on perspective
 - Vanilla `server.jar` and all the files that entails (`server.properties`, `eula.txt`
 - [Vanilla Tweaks](https://vanillatweaks.net) and [GeyserOptionalPack](https://download.geysermc.org/v2/projects/geyseroptionalpack/versions/latest/builds/latest/downloads/geyseroptionalpack) to make Java and Bedrock behave the same.
 - Supports all vanilla render distances, not modded ones though, sorry Optifine users!
 - Auto-updates, though you do need to manually restart when an update is available and depending on the update you may not be informed
 - Xbox achievements work!
 - relative paths are used
 - `/stop` stops the server and shuts down the docker container, this is controlled in `docker-compose.yml`
 - Remember that some settings exist twice, once for Java and once for Bedrock, try to keep them in sync unless you have a reason not to.
   - online mode must be enabled in both locations, for example, `auth-type: offline` -> `auth-type: online` + `online-mode=false` -> `online-mode=true`

## Setup
I'd recommend just running it directly and seeing what files you want to mess with.


*This file was made with the help of [a ChatGPT chat](https://chatgpt.com/share/6803fe41-bcd4-8009-a134-707a31fc4076) what's actual README I did not actually use*
