import json

def print_structure(name, coords, indent=0):
    print("  " * indent + f"{name}:")
    if isinstance(coords, list):
        print("  " * indent + f"Type: list, length: {len(coords)}")
        if len(coords) > 0:
            print_structure("First item", coords[0], indent + 1)
    else:
        print("  " * indent + f"Type: {type(coords)}")

# Load data
with open('frontend/public/countries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

countries = [('CPV', 'Cabo Verde'), ('DOM', 'Dominican Republic')]

for code, name in countries:
    found = False
    for feature in data['features']:
        if feature['properties'].get('ISO_A3') == code:
            print(f"\n{name} ({code}):")
            print(f"Geometry type: {feature['geometry']['type']}")
            print_structure("Coordinates", feature['geometry']['coordinates'])
            found = True
            break
    if not found:
        print(f"{name} ({code}) not found!")
