import json

# Read the countries.json file
with open('frontend/public/countries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find Cape Verde
for feature in data['features']:
    props = feature['properties']
    if props.get('ISO_A3') == 'CPV':
        print(f"Found: {props.get('ADMIN')} ({props.get('ISO_A3')})")
        print(f"\nGeometry type: {feature['geometry']['type']}")
        print(f"Number of coordinates: {len(feature['geometry']['coordinates'])}")
        
        # Show first polygon coordinates
        if feature['geometry']['type'] == 'MultiPolygon':
            for i, polygon in enumerate(feature['geometry']['coordinates']):
                print(f"\nPolygon {i+1}:")
                print(f"  Number of rings: {len(polygon)}")
                if len(polygon) > 0 and len(polygon[0]) > 0:
                    first_coord = polygon[0][0]
                    print(f"  First coordinate: {first_coord}")
                    last_coord = polygon[0][-1]
                    print(f"  Last coordinate: {last_coord}")
                    print(f"  Total points in outer ring: {len(polygon[0])}")
        
        # Check bounds
        coords_flat = []
        if feature['geometry']['type'] == 'MultiPolygon':
            for polygon in feature['geometry']['coordinates']:
                for ring in polygon:
                    coords_flat.extend(ring)
        
        if coords_flat:
            lons = [c[0] for c in coords_flat]
            lats = [c[1] for c in coords_flat]
            print(f"\nBounds:")
            print(f"  Longitude: {min(lons):.2f} to {max(lons):.2f}")
            print(f"  Latitude: {min(lats):.2f} to {max(lats):.2f}")
        
        break
else:
    print("Cape Verde not found!")

