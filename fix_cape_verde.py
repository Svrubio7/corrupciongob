import json

def reverse_polygon_coordinates(coords):
    """Reverse the order of coordinates in a polygon to fix winding order"""
    if isinstance(coords[0][0], list):
        # MultiPolygon - reverse each polygon
        return [[reverse_ring(ring) for ring in polygon] for polygon in coords]
    else:
        # Polygon - reverse each ring
        return [reverse_ring(ring) for ring in coords]

def reverse_ring(ring):
    """Reverse a single ring of coordinates"""
    return list(reversed(ring))

# Read the countries.json file
with open('frontend/public/countries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find and fix Cape Verde
fixed = False
for feature in data['features']:
    props = feature['properties']
    if props.get('ISO_A3') == 'CPV':
        print(f"Found: {props.get('ADMIN')} ({props.get('ISO_A3')})")
        print(f"Original geometry type: {feature['geometry']['type']}")
        
        # Reverse the coordinate order
        feature['geometry']['coordinates'] = reverse_polygon_coordinates(
            feature['geometry']['coordinates']
        )
        
        print("Coordinates have been reversed to fix winding order")
        fixed = True
        break

if fixed:
    # Write back to the file
    with open('frontend/public/countries.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    
    # Also update dist file
    with open('frontend/dist/countries.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    
    print("\nCape Verde geometry has been fixed in both public and dist folders!")
else:
    print("Cape Verde not found in the file!")

