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
        return time
    except Exception as e:
        print(f"Error: {e}: fn calculate")
        x.dec = "file load; Error"


async def decide(x):
    print(f"PATH: {x.path}")
    try:
        if x.path.endswith(".yaml"):
            await yamle(x)
        elif x.path.endswith(".json"):
            await jeason(x)
        elif x.path.endswith(".toml"):
            await toelo(x)
        else:
            x.dec = "Requiring valid & supported file; Error"
    except Exception as e:
        print(f"Error: {e}: fn decide")


async def jeason(x):
    try:
        import json

        with open(x.path, "r", encoding="utf-8-sig") as file:
            cfg = json.load(file)
        x.sunrise = cfg.get("sunrise")
        x.sunset = cfg.get("sunset")
        x.degree = cfg.get("degree")
    except Exception as e:
        print(f"Error: {e}: fn json")


async def toelo(x):
    try:
        import toml

        with open(x.path, "r") as file:
            x.cfg = toml.load(file)
            x.sunrise = x.cfg.get("sunrise")
            x.degree = x.cfg.get("degree")
            x.sunset = x.cfg.get("sunset")
    except Exception as e:
        print(f"Error: {e}: fn toml")


async def yamle(x):
    try:
        import yaml

        with open(x.path, "r") as file:
            x.cfg = yaml.safe_load(file)
            x.sunrise = x.cfg.get("sunrise")
            x.degree = x.cfg.get("degree")
            x.sunset = x.cfg.get("sunset")
    except Exception as e:
        print(f"Error {e}: fn yaml")


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
                t = await calculate(x)
                print(f"{int(t)}:{ int(t * 60) % 60}")
                return True
    except Exception as e:
        print(f"Error:{e}: fn main")
        return True


try:
    asyncio.run(main())
except Exception as Error:
    print(f"Error: {Error}")
