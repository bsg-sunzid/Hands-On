from configparser import ConfigParser
import pickle

config = ConfigParser()

config["Default"] = {
    "numberdigits": 6,
    "numbertries": 8,
    "playername": "Player"
}

config["NeuralNine"] = {
    "numberdigits": 6,
    "numbertries": 8,
    "playername": "Florian"
}

config["Sudo"] = {
    "numberdigits": 6,
    "numbertries": 8,
    "playername": "cheater",
    "cheats": "on"
}

with open("number_guessing.txt", "wb") as f:
    pickle.dump(config, f)


with open("number_guessing.txt", "rb") as f:
    loaded_config = pickle.load(f)

print("✅ Pickle file loaded successfully!")
print(loaded_config["Sudo"]["playername"])
