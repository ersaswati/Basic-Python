import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

print("Learning rate:", config["training"]["lr"])
print("Epochs:", config["training"]["epochs"])