# Uncomment the path for your settings, or use input.
# path = "./prefrences/settings.json"
# path = "./prefrences/settings.yaml"
# path = "./prefrencessettings.toml"
path = None
if path == None:
    path = input("enter path")


with open(path, "r", encoding="utf-8") as f:
    passed = False
    if path.endswith("json"):
        import json

        cfg = json.load(f)
        passed = True
    elif path.endswith("yaml"):
        import yaml

        cfg = yaml.load(f)
        passed = True

    elif path.endswith("toml"):
        import toml

        cfg = toml.load(f)
        passed = True
    if passed is False:
        print("Warning: no file given, supported formats: json, yaml, toml")
    else:
        sunrise = cfg.get("sunrise", None)

        sunset = cfg.get("sunset", None)

        degree = cfg.get("degree", None)
        if sunrise == None:
            print("sunrise not given, using average {}")
        if sunset == None:
            print("sunrise not given, using average {}")
        if degree == None:
            raise TypeError("No Input For degrees, can't calculate.")

print(sunrise + degree / 180 * (sunset - sunrise))
