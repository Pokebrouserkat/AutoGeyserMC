# Dockerized auto-updating Minecraft Java Edition server and GeyserMC-Standalone
Skins don't work right now, I don't know how to get Java and Bedrock players to both be able to log in without sacrificing compatibility with default configuration in both the client and its launcher.
The client can use any render distance the vanilla client supports. Anything higher than that is ignored, but this does mean the server can send an entire 32 chunk radius around the player.
It's a vanilla server.jar and server.properties and eula.txt. This means no third-party plugins (including [Floodgate](https://geysermc.org/wiki/floodgate/setup)) and no PaperMC-style optimizaitons/further configs.
Comes with resource packs from [Vanilla Tweaks](https://vanillatweaks.net) and the [GeyserOptionalPack](https://download.geysermc.org/v2/projects/geyseroptionalpack/versions/latest/builds/latest/downloads/geyseroptionalpack) for better cross-platform continuity/parity.
`autoserver.py` will work regardless of where it is, it just expects it's in a volume and has a network connection.
`/stop` will stop the server, not restart it. This behaviour is controlled by `docker-compose.yml`, for example, to make `/stop` restart the server rather than stopping it, you would replace `restart: on-failure` with `restart: unless-stopped` (stopped by Docker, that is).
Xbox achievements are enabled, commands on Bedrock are not. You can change these in `config.yml`.
I have it set to not log IPs, you can change that.
Auto-update occurs when the server restarts, it will not automatically restart if an update is available.
When changing the max players, remember to change `server.properties` AND `config.yml`, one for Java and one for Bedrock (the former being the real limit)
If enabling online mode, do so in `server.properties` and then change `auth-type` to `online` in `config.yml`


*I would generally recommend running this once, quitting it instanly, then looking at all the files to see what you want to change.*


I'll probably get ChatGPT to update this file
