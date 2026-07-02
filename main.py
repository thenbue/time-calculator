import asyncio


class variables:
    def __init__(self):
        self.sunrise = None
        self.degree = None
        self.sunset = None
        self.state = False
        self.path = "./settings/settings.json"
        self.dec = "0"


async def calculate(x):
    try:
        if x.sunrise is None:
            x.sunrise = 6
        if x.degree is None:
            x.degree = 0
        if x.sunset is None:
            x.sunset = 20
        time = x.sunrise + x.degree / 180 * (x.sunset - x.sunrise)
        return time + x.sunrise
    except Exception as e:
        print(f"Error: {e}: line 25")


async def decide(x):
    try:
        if x.path.endswith(".yaml"):
            await yaml(x)
        elif x.path.endswith(".json"):
            await json(x)
        elif x.path.endswith(".toml"):
            await toml(x)
        else:
            x.dec = "Requiring valid & supported file; Error"
    except Exception as e:
        print(f"Error: {e}: line 39")


async def json(x):
    try:
        import json

        with open(x.path) as file:
            cfg = json.load(file)
        x.sunrise = cfg.get("sunrise", None)
        x.degree = cfg.get("degree", None)
        x.sunset = cfg.get("sunset", None)
    except Exception as e:
        print(f"Error: {e}: line 52")


async def toml(x):
    try:
        import toml

        with open(x.path) as file:
            x.cfg = toml.load(file)
            x.sunrise = x.cfg["sunrise"]
            x.degree = x.cfg["degree"]
            x.sunset = x.cfg["sunset"]
    except Exception as e:
        print(f"Error: {e}: line 65")


async def yaml(x):
    try:
        import yaml

        with open(x.path) as file:
            x.cfg = yaml.safe_load(file)
            x.sunrise = x.cfg["sunrise"]
            x.degree = x.cfg["degree"]
            x.sunset = x.cfg["sunset"]
    except Exception as e:
        print(f"Error {e}: line 78")


async def main():
    launch = True
    try:
        while launch:
            print("Main Loaded")
            x = variables()
            await decide(x)
            if x.dec.endswith("; Error"):
                print("File Not found, quitting")
                return True
            else:
                print("done Deciding File type")
                answer = await calculate(x)
                print(answer)
                return True
    except Exception as e:
        print(f"Error:{e}: line 97")
        return True


try:
    asyncio.run(main())
except Exception as Error:
    print(f"Error: {Error}")
