import json

def validate_geojson(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"File is valid JSON")
        print(f"Total features: {len(data.get('features', []))}")
        
        # Check for Cabo Verde
        cpv = None
        for feature in data['features']:
            if feature['properties'].get('ISO_A3') == 'CPV':
                cpv = feature
                break
        
        if cpv:
            print("\nCabo Verde found:")
            print(f"Geometry type: {cpv['geometry']['type']}")
            print(f"Number of coordinates arrays: {len(cpv['geometry']['coordinates'])}")
            # Check if coordinates are lists of lists
            if isinstance(cpv['geometry']['coordinates'][0], list):
                print("Coordinates structure looks valid")
            else:
                print("WARNING: Coordinates structure invalid")
        else:
            print("Cabo Verde not found!")
        
        return True
    
    except json.JSONDecodeError as e:
        print(f"JSON Error: {str(e)}")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

# Validate public
print("Validating frontend/public/countries.json")
validate_geojson('frontend/public/countries.json')
print("\n")

# Validate dist
print("Validating frontend/dist/countries.json")
validate_geojson('frontend/dist/countries.json')
