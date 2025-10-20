import json
import os

# Check if both files exist
pub_file = 'frontend/public/countries.json'
dist_file = 'frontend/dist/countries.json'

print(f"Public file exists: {os.path.exists(pub_file)}")
print(f"Dist file exists: {os.path.exists(dist_file)}")

if os.path.exists(pub_file):
    pub = json.load(open(pub_file, 'r', encoding='utf-8'))
    print(f"\nPublic file features: {len(pub['features'])}")
    cpv_pub = any(f['properties'].get('ISO_A3') == 'CPV' for f in pub['features'])
    print(f"CPV in public: {cpv_pub}")

if os.path.exists(dist_file):
    dist = json.load(open(dist_file, 'r', encoding='utf-8'))
    print(f"\nDist file features: {len(dist['features'])}")
    cpv_dist = any(f['properties'].get('ISO_A3') == 'CPV' for f in dist['features'])
    print(f"CPV in dist: {cpv_dist}")
    
    # Check file sizes
    pub_size = os.path.getsize(pub_file)
    dist_size = os.path.getsize(dist_file)
    print(f"\nPublic file size: {pub_size:,} bytes")
    print(f"Dist file size: {dist_size:,} bytes")
    print(f"Files are same size: {pub_size == dist_size}")

