# Automatically install the server

import subprocess
import os
import sys
import urllib.request
if os.path.exists("geyser.jar"):
    # remove it
    os.remove("geyser.jar")
urllib.request.urlretrieve("https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/standalone", "geyser.jar")
# start Geyser
stopgeyser = subprocess.Popen(["java", "-jar", "geyser.jar", "nogui"]).kill
import json

jarpath = os.path.join(os.path.dirname(__file__), "server.jar")

versions = json.loads(urllib.request.urlopen("https://launchermeta.mojang.com/mc/game/version_manifest.json").read().decode("utf-8"))
snapshot = versions["latest"]["release"] # change to ["latest"]["snapshot"] for snapshot. Snapshot may be the same as release if the game just updated

print("Auto-Update: Downloading " + snapshot + " server")

versions = versions["versions"]
for version in versions:
    if version["id"] == snapshot:
        if os.path.exists(jarpath):
            os.remove(jarpath)
        urllib.request.urlretrieve(json.loads(urllib.request.urlopen(version["url"]).read().decode("utf-8"))["downloads"]["server"]["url"], jarpath)
os.chmod(jarpath, 0o644)


# Run the server
# while run_server() != 0:
#     print("Server crashed, restarting...")
#     if not download_server():
#         print("Failed to download server, using potentially outdated version")
exitcode = subprocess.run([
    "java",
    "-Xms2G",
    "-XX:+UseG1GC",
    "-XX:+UnlockExperimentalVMOptions",
    "-Xmx4G",
    "-Djava.net.preferIPv4Stack=true",
    "-jar",
    jarpath,
    "nogui"
]).returncode
stopgeyser()
sys.exit(exitcode)