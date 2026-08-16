# v2

# Uncomment the path for your settings, or use input.
path = None
# path = "./../usage/main.toml"
# path = "./../usage/main.yaml"
# path = "./../usage/main.json"
if path is None:
    print("file.type supported by default: main.yaml, main.toml, main.json")
    path = input("enter path (./../usage/main.type): ")
if path.endswith((".json", ".yaml", ".toml")):
    try:
        with open(path, "r", encoding="utf-8") as file:
            if path.endswith(".json"):
                import json

                cfg = json.load(file)
            elif path.endswith(".yaml"):
                import yaml

                cfg = yaml.safe_load(file)

            else:
                import toml

                cfg = toml.load(file)
    except FileNotFoundError:
        raise ValueError(f"{path} doesn't exist")

    if cfg is None:
        raise ValueError("Config file is empty")
    sunrise = cfg.get("sunrise")
    sunset = cfg.get("sunset")
    degree = cfg.get("degree")
    if sunrise is None or sunset is None or degree is None:
        raise ValueError(
            "one or more inputs not found. verify: https://github.com/thenbue/time-calculator"
        )
    t = sunrise + degree / 180 * (sunset - sunrise)
    print(f"{int(t)}:{int(t * 60) % 60}")

else:
    raise ValueError(f"{path} doesn't work with this file.")
