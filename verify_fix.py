import json

def check_winding_order(coords):
    """Check if polygon coordinates are clockwise or counterclockwise"""
    # Get the first ring of the first polygon
    if isinstance(coords[0][0][0], list):
        # MultiPolygon
        ring = coords[0][0]
    else:
        # Polygon
        ring = coords[0]
    
    # Calculate signed area (Shoelace formula)
    area = 0
    for i in range(len(ring) - 1):
        x1, y1 = ring[i][:2]
        x2, y2 = ring[i + 1][:2]
        area += (x2 - x1) * (y2 + y1)
    
    return "clockwise" if area > 0 else "counterclockwise"

# Check public file
print("=" * 60)
print("Checking frontend/public/countries.json")
print("=" * 60)

with open('frontend/public/countries.json', 'r', encoding='utf-8') as f:
    public_data = json.load(f)

public_cpv = None
for feature in public_data['features']:
    if feature['properties'].get('ISO_A3') == 'CPV':
        public_cpv = feature
        break

if public_cpv:
    print(f"[OK] Found: {public_cpv['properties'].get('ADMIN')}")
    print(f"  Geometry type: {public_cpv['geometry']['type']}")
    print(f"  Number of polygons: {len(public_cpv['geometry']['coordinates'])}")
    
    # Check first few coordinates of first polygon
    first_polygon = public_cpv['geometry']['coordinates'][0][0]
    print(f"  First 3 coordinates:")
    for i, coord in enumerate(first_polygon[:3]):
        print(f"    {i+1}. {coord}")
    
    winding = check_winding_order(public_cpv['geometry']['coordinates'])
    print(f"  Winding order: {winding}")
else:
    print("[ERROR] Cape Verde NOT found!")

print()

# Check dist file
print("=" * 60)
print("Checking frontend/dist/countries.json")
print("=" * 60)

with open('frontend/dist/countries.json', 'r', encoding='utf-8') as f:
    dist_data = json.load(f)

dist_cpv = None
for feature in dist_data['features']:
    if feature['properties'].get('ISO_A3') == 'CPV':
        dist_cpv = feature
        break

if dist_cpv:
    print(f"[OK] Found: {dist_cpv['properties'].get('ADMIN')}")
    print(f"  Geometry type: {dist_cpv['geometry']['type']}")
    print(f"  Number of polygons: {len(dist_cpv['geometry']['coordinates'])}")
    
    # Check first few coordinates of first polygon
    first_polygon = dist_cpv['geometry']['coordinates'][0][0]
    print(f"  First 3 coordinates:")
    for i, coord in enumerate(first_polygon[:3]):
        print(f"    {i+1}. {coord}")
    
    winding = check_winding_order(dist_cpv['geometry']['coordinates'])
    print(f"  Winding order: {winding}")
else:
    print("[ERROR] Cape Verde NOT found!")

print()

# Compare if both files match
if public_cpv and dist_cpv:
    coords_match = (public_cpv['geometry']['coordinates'] == 
                   dist_cpv['geometry']['coordinates'])
    print("=" * 60)
    print(f"Both files have identical coordinates: {'[OK] YES' if coords_match else '[ERROR] NO'}")
    print("=" * 60)

