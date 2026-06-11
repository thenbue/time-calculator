import yaml

try:
    with open("settings.yaml", "r") as file:
        config = yaml.safe_load(file)
    print(f"{config}")
    time = config["Sunrise"] + config["Degree"] / 180 * (
        config["Sunset"] - config["Sunrise"]
    )
    print(time + config["Sunrise"])

except Exception as error:
    print(f"Error: {error}")
