import json

# Read the countries.json file
with open('frontend/public/countries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total countries: {len(data['features'])}")
print(f"\nFirst country example:")
first = data['features'][0]['properties']
print(f"  ADMIN: {first.get('ADMIN')}")
print(f"  ISO_A3: {first.get('ISO_A3')}")
print(f"  Keys: {list(first.keys())}")

# Check if Cape Verde exists
print("\n\nSearching for Cape Verde...")
for feature in data['features']:
    props = feature['properties']
    admin = props.get('ADMIN', '').lower()
    iso = props.get('ISO_A3', '').upper()
    
    if 'cabo' in admin or 'cape' in admin or 'verde' in admin or iso == 'CPV':
        print(f"Found: {props.get('ADMIN')} ({props.get('ISO_A3')})")
        print(f"Geometry type: {feature['geometry']['type']}")
        break
else:
    print("Cape Verde NOT found in the file")

