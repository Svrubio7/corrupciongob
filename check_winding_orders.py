import json

def check_winding_order(coords):
    """Determine winding order of the first exterior ring using shoelace formula"""
    if isinstance(coords[0][0][0], list):  # MultiPolygon
        ring = coords[0][0]  # First polygon's exterior
    elif isinstance(coords[0][0], list):  # Polygon
        ring = coords[0]     # Exterior ring
    else:  # LineString or something, skip
        return "unknown"

    total = 0
    n = len(ring)
    for i in range(n):
        x1, y1 = ring[i]
        x2, y2 = ring[(i + 1) % n]
        total += (x1 * y2) - (x2 * y1)

    return "counterclockwise" if total > 0 else "clockwise"

# Load data
with open('frontend/public/countries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Countries to check: code, expected name
countries = [
    ('CPV', 'Cabo Verde'),
    ('SEN', 'Senegal'),
    ('ESP', 'Spain'),
    ('MDV', 'Maldives'),
    ('JPN', 'Japan')
]

print("=" * 60)
for code, name in countries:
    found = False
    for feature in data['features']:
        if feature['properties'].get('ISO_A3') == code:
            winding = check_winding_order(feature['geometry']['coordinates'])
            geom_type = feature['geometry']['type']
            print(f"{name} ({code}): {geom_type} - Winding: {winding}")
            found = True
            break
    if not found:
        print(f"{name} ({code}): NOT FOUND")
print("=" * 60)
