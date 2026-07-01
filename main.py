import asyncio


class variables:
    def __init__(self):
        self.path = (
            "./settings/settings.yaml"
            or "./settings/settings.json"
            or "./settings/settings.toml"
        )
        self.sunrise = 6
        self.sunset = 20
        self.degree = 0
        self.degree_default = 0
        self.sunrise_default = 6
        self.sunset_default = 20


async def calculate(x):
    if x.sunrise != "default" or x.degree != "default" or x.sunset != "default":
        time = x.sunrise + x.degree / 180 * (x.sunset - x.sunrise)
        return time + x.sunrise
    if x.sunrise == "default":
        if x.degree == "default":
            if x.sunset == "default":
                print("")


async def decide(x):
    if x.path.endswith(".yaml"):
        await yaml(x)
    elif x.path.endswith(".json"):
        await json(x)
    elif x.path.endswith(".toml"):
        await toml(x)
    else:
        raise "Error: requiring valid & supported file"


async def json(x):
    import json

    with open(x.path) as file:
        x.cfg = json.load(file)
        x.sunrise = x.cfg.get("world", "default").get("sunrise", "default")
        x.degree = x.cfg.get("world", "default").get("degree", "default")
        x.sunset = x.cfg.get("world", "default").get("sunset", "default")


async def toml(x):
    import toml

    with open(x.path) as file:
        x.cfg = toml.load(file)
        x.sunrise = x.cfg["world"]["sunrise"]
        x.degree = x.cfg["world"]["degree"]
        x.sunset = x.cfg["world"]["sunset"]


async def yaml(x):
    import yaml

    with open(x.path) as file:
        x.cfg = yaml.safe_load(file)
        x.sunrise = x.cfg["world"]["sunrise"]
        x.degree = x.cfg["world"]["degree"]
        x.sunset = x.cfg["world"]["sunset"]


async def main(STATE=False):
    launch = True
    while launch:
        if STATE:
            print("Main Loaded")
        x = variables()
        dec = await decide(x)
        if dec != "Error: requiring valid & supported file" and STATE:
            print("done Deciding File type")
        answer = await calculate(x)
        print(answer)
        return True


asyncio.run(main(STATE=False))
