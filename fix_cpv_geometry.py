import json

# Read the countries.json file
with open('frontend/public/countries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Cabo Verde
fixed = False
for feature in data['features']:
    props = feature['properties']
    if props.get('ISO_A3') == 'CPV':
        print(f"Found: {props.get('ADMIN')} ({props.get('ISO_A3')})")
        print(f"Original geometry type: {feature['geometry']['type']}")
        
        # Check current structure
        coords = feature['geometry']['coordinates']
        if len(coords) > 0 and isinstance(coords[0], list) and isinstance(coords[0][0], list) and not isinstance(coords[0][0][0], list):
            # It's [ring1, ring2, ...] where ring = [point, point] and point = [lon, lat] (not list? No, [lon, lat] is list, but lon is float)
            # Actually, check if coords[0][0][0] is number (float/int)
            if isinstance(coords[0][0][0], (int, float)):
                # Incorrect: flat list of rings for MultiPolygon - wrap each in [ring]
                feature['geometry']['coordinates'] = [[ring] for ring in coords]
                print("Fixed structure: Wrapped each ring in an additional array for proper MultiPolygon")
                fixed = True
            else:
                print("Structure already correct")
        else:
            print("Unexpected structure")
        break

if fixed:
    # Write back to public
    with open('frontend/public/countries.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    
    # Also update dist
    with open('frontend/dist/countries.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    
    print("\nCabo Verde MultiPolygon structure has been fixed in both files!")
else:
    print("No changes needed or Cabo Verde not found!")
