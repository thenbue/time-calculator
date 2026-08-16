# v1
class variables:
    def __init__(self):
        self.sunrise = None
        self.degree = None
        self.sunset = None
        self.path = "./../usage/main.json"  # .yaml, .toml works too.


def json():
    import json

    with open(x.path, "r", encoding="utf-8-sig") as file:
        cfg = json.load(file)
        x.sunrise = cfg.get("sunrise")
        x.sunset = cfg.get("sunset")
        x.degree = cfg.get("degree")
        del cfg
    return 0


def toml():
    import toml

    with open(x.path, "r") as file:
        cfg = toml.load(file)
        x.sunrise = cfg.get("sunrise")
        x.degree = cfg.get("degree")
        x.sunset = cfg.get("sunset")
        del cfg
    return 0


def yaml():
    import yaml

    with open(x.path, "r") as file:
        cfg = yaml.safe_load(file)
        x.sunrise = cfg.get("sunrise")
        x.degree = cfg.get("degree")
        x.sunset = cfg.get("sunset")
        del cfg
    return 0


def calculate():
    if x.sunrise is None:
        x.sunrise = 6
    if x.degree is None:
        x.degree = 0
    if x.sunset is None:
        x.sunset = 20
    time = x.sunrise + x.degree / 180 * (x.sunset - x.sunrise)
    return time


def decide():
    print(f"PATH: {x.path}")
    if x.path.endswith(".yaml"):
        yaml()
    elif x.path.endswith(".json"):
        json()
    elif x.path.endswith(".toml"):
        toml()
    else:
        return 1


x = variables()
print("file not found, qutting") if decide() == 1 else print("file found")
t = calculate()
print(f"{int(t)}:{int(t * 60) % 60}")
