import json

def get_first_ring(coords):
    if isinstance(coords[0][0][0], list):  # MultiPolygon
        return coords[0][0]  # First polygon's exterior
    elif isinstance(coords[0][0], list):  # Polygon
        return coords[0]     # Exterior ring
    else:
        return None

def check_winding_order(ring):
    total = 0
    n = len(ring)
    for i in range(n):
        x1, y1 = ring[i]
        x2, y2 = ring[(i + 1) % n]
        total += (x1 * y2) - (x2 * y1)
    return "counterclockwise" if total > 0 else "clockwise", total

# Load data
with open('frontend/public/countries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Countries to check
countries = [('CPV', 'Cabo Verde'), ('SEN', 'Senegal')]

for code, name in countries:
    for feature in data['features']:
        if feature['properties'].get('ISO_A3') == code:
            ring = get_first_ring(feature['geometry']['coordinates'])
            if ring:
                winding, sum_val = check_winding_order(ring)
                print(f"\n{name} ({code}):")
                print(f"Geometry type: {feature['geometry']['type']}")
                print(f"Winding: {winding} (sum: {sum_val})")
                print("First 5 coordinates:")
                for coord in ring[:5]:
                    print(f"  {coord}")
                print("Last 5 coordinates:")
                for coord in ring[-5:]:
                    print(f"  {coord}")
            break
