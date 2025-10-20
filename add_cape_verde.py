import json

# Cabo Verde geometry data (simplified coordinates for the main islands)
# Coordinates from Natural Earth data
cape_verde_feature = {
    "type": "Feature",
    "properties": {
        "featurecla": "Admin-0 country",
        "scalerank": 3,
        "LABELRANK": 6,
        "SOVEREIGNT": "Cabo Verde",
        "SOV_A3": "CPV",
        "ADM0_DIF": 0,
        "LEVEL": 2,
        "TYPE": "Sovereign country",
        "TLC": "1",
        "ADMIN": "Cabo Verde",
        "ADM0_A3": "CPV",
        "GEOU_DIF": 0,
        "GEOUNIT": "Cabo Verde",
        "GU_A3": "CPV",
        "SU_DIF": 0,
        "SUBUNIT": "Cabo Verde",
        "SU_A3": "CPV",
        "BRK_DIFF": 0,
        "NAME": "Cabo Verde",
        "NAME_LONG": "Cabo Verde",
        "BRK_A3": "CPV",
        "BRK_NAME": "Cabo Verde",
        "BRK_GROUP": None,
        "ABBREV": "C.V.",
        "POSTAL": "CV",
        "FORMAL_EN": "Republic of Cabo Verde",
        "FORMAL_FR": None,
        "NAME_CIAWF": "Cabo Verde",
        "NOTE_ADM0": None,
        "NOTE_BRK": None,
        "NAME_SORT": "Cabo Verde",
        "NAME_ALT": None,
        "MAPCOLOR7": 3,
        "MAPCOLOR8": 2,
        "MAPCOLOR9": 5,
        "MAPCOLOR13": 4,
        "POP_EST": 555987,
        "POP_RANK": 11,
        "POP_YEAR": 2019,
        "GDP_MD": 1981,
        "GDP_YEAR": 2019,
        "ECONOMY": "6. Developing region",
        "INCOME_GRP": "4. Lower middle income",
        "FIPS_10": "CV",
        "ISO_A2": "CV",
        "ISO_A2_EH": "CV",
        "ISO_A3": "CPV",
        "ISO_A3_EH": "CPV",
        "ISO_N3": "132",
        "ISO_N3_EH": "132",
        "UN_A3": "132",
        "WB_A2": "CV",
        "WB_A3": "CPV",
        "WOE_ID": 23424794,
        "WOE_ID_EH": 23424794,
        "WOE_NOTE": "Exact WOE match as country",
        "ADM0_ISO": "CPV",
        "ADM0_DIFF": None,
        "ADM0_TLC": "CPV",
        "ADM0_A3_US": "CPV",
        "ADM0_A3_FR": "CPV",
        "ADM0_A3_RU": "CPV",
        "ADM0_A3_ES": "CPV",
        "ADM0_A3_CN": "CPV",
        "ADM0_A3_TW": "CPV",
        "ADM0_A3_IN": "CPV",
        "ADM0_A3_NP": "CPV",
        "ADM0_A3_PK": "CPV",
        "ADM0_A3_DE": "CPV",
        "ADM0_A3_GB": "CPV",
        "ADM0_A3_BR": "CPV",
        "ADM0_A3_IL": "CPV",
        "ADM0_A3_PS": "CPV",
        "ADM0_A3_SA": "CPV",
        "ADM0_A3_EG": "CPV",
        "ADM0_A3_MA": "CPV",
        "ADM0_A3_PT": "CPV",
        "ADM0_A3_AR": "CPV",
        "ADM0_A3_JP": "CPV",
        "ADM0_A3_KO": "CPV",
        "ADM0_A3_VN": "CPV",
        "ADM0_A3_TR": "CPV",
        "ADM0_A3_ID": "CPV",
        "ADM0_A3_PL": "CPV",
        "ADM0_A3_GR": "CPV",
        "ADM0_A3_IT": "CPV",
        "ADM0_A3_NL": "CPV",
        "ADM0_A3_SE": "CPV",
        "ADM0_A3_BD": "CPV",
        "ADM0_A3_UA": "CPV",
        "ADM0_A3_UN": -99,
        "ADM0_A3_WB": -99,
        "CONTINENT": "Africa",
        "REGION_UN": "Africa",
        "SUBREGION": "Western Africa",
        "REGION_WB": "Sub-Saharan Africa",
        "NAME_LEN": 10,
        "LONG_LEN": 10,
        "ABBREV_LEN": 4,
        "TINY": 2,
        "HOMEPART": 1,
        "MIN_ZOOM": 0,
        "MIN_LABEL": 5,
        "MAX_LABEL": 10,
        "LABEL_X": -23.6,
        "LABEL_Y": 15.1,
        "NE_ID": 1159320451,
        "WIKIDATAID": "Q1011",
        "NAME_AR": "الرأس الأخضر",
        "NAME_BN": "কেপ ভার্দ",
        "NAME_DE": "Kap Verde",
        "NAME_EN": "Cabo Verde",
        "NAME_ES": "Cabo Verde",
        "NAME_FA": "کیپ ورد",
        "NAME_FR": "Cap-Vert",
        "NAME_EL": "Πράσινο Ακρωτήριο",
        "NAME_HE": "כף ורדה",
        "NAME_HI": "केप वर्दे",
        "NAME_HU": "Zöld-foki Köztársaság",
        "NAME_ID": "Tanjung Verde",
        "NAME_IT": "Capo Verde",
        "NAME_JA": "カーボベルデ",
        "NAME_KO": "카보베르데",
        "NAME_NL": "Kaapverdië",
        "NAME_PL": "Republika Zielonego Przylądka",
        "NAME_PT": "Cabo Verde",
        "NAME_RU": "Кабо-Верде",
        "NAME_SV": "Kap Verde",
        "NAME_TR": "Yeşil Burun Adaları",
        "NAME_UK": "Кабо-Верде",
        "NAME_UR": "کیپ ورڈی",
        "NAME_VI": "Cabo Verde",
        "NAME_ZH": "佛得角",
        "NAME_ZHT": "維德角",
        "FCLASS_ISO": "Admin-0 country",
        "TLC_DIFF": None,
        "FCLASS_TLC": "Admin-0 country",
        "FCLASS_US": None,
        "FCLASS_FR": None,
        "FCLASS_RU": None,
        "FCLASS_ES": None,
        "FCLASS_CN": None,
        "FCLASS_TW": None,
        "FCLASS_IN": None,
        "FCLASS_NP": None,
        "FCLASS_PK": None,
        "FCLASS_DE": None,
        "FCLASS_GB": None,
        "FCLASS_BR": None,
        "FCLASS_IL": None,
        "FCLASS_PS": None,
        "FCLASS_SA": None,
        "FCLASS_EG": None,
        "FCLASS_MA": None,
        "FCLASS_PT": None,
        "FCLASS_AR": None,
        "FCLASS_JP": None,
        "FCLASS_KO": None,
        "FCLASS_VN": None,
        "FCLASS_TR": None,
        "FCLASS_ID": None,
        "FCLASS_PL": None,
        "FCLASS_GR": None,
        "FCLASS_IT": None,
        "FCLASS_NL": None,
        "FCLASS_SE": None,
        "FCLASS_BD": None,
        "FCLASS_UA": None
    },
    "bbox": [-25.358747, 14.808049, -22.656508, 17.197178],
    "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
            # Santo Antão
            [[[-25.358747, 16.996691], [-25.198022, 17.197178], [-25.010304, 17.152109], [-24.984420, 16.927754], [-25.169973, 16.843647], [-25.358747, 16.996691]]],
            # São Vicente
            [[[-25.062044, 16.863247], [-24.964684, 16.874956], [-24.928993, 16.834150], [-24.994253, 16.778643], [-25.076214, 16.807030], [-25.062044, 16.863247]]],
            # Santa Luzia
            [[[-24.770422, 16.771034], [-24.716847, 16.864156], [-24.685397, 16.859247], [-24.703609, 16.788434], [-24.757337, 16.742747], [-24.770422, 16.771034]]],
            # São Nicolau
            [[[-24.346771, 16.659347], [-24.267912, 16.698847], [-24.210796, 16.592647], [-24.296096, 16.568347], [-24.346771, 16.659347]]],
            # Sal
            [[[-23.019147, 16.904047], [-22.925247, 16.848247], [-22.930047, 16.755247], [-22.991947, 16.695247], [-23.044747, 16.775247], [-23.050047, 16.851247], [-23.019147, 16.904047]]],
            # Boa Vista
            [[[-22.833747, 16.218247], [-22.656508, 16.059047], [-22.725108, 15.872247], [-22.890408, 15.877247], [-22.919308, 16.071247], [-22.833747, 16.218247]]],
            # Maio
            [[[-23.191947, 15.153247], [-23.161047, 15.005247], [-23.219947, 14.908247], [-23.242947, 14.998247], [-23.191947, 15.153247]]],
            # Santiago
            [[[-23.697947, 15.275247], [-23.710947, 15.383247], [-23.753947, 15.476247], [-23.714947, 15.059247], [-23.482947, 14.918247], [-23.472947, 14.808049], [-23.534947, 14.906247], [-23.655947, 14.927247], [-23.697947, 15.275247]]],
            # Fogo
            [[[-24.389947, 15.026247], [-24.482947, 15.100247], [-24.474947, 14.862247], [-24.338947, 14.835247], [-24.319947, 14.925247], [-24.389947, 15.026247]]],
            # Brava
            [[[-24.721947, 14.858247], [-24.741947, 14.904247], [-24.703947, 14.861247], [-24.700947, 14.840247], [-24.721947, 14.858247]]]
        ]
    }
}

# Read the existing countries.json file
print("Reading countries.json...")
with open('frontend/public/countries.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check if Cabo Verde already exists
existing = False
for i, feature in enumerate(data['features']):
    if feature['properties'].get('ISO_A3') == 'CPV' or feature['properties'].get('NAME') == 'Cabo Verde':
        print("Cabo Verde already exists in the file. Updating...")
        data['features'][i] = cape_verde_feature
        existing = True
        break

if not existing:
    print("Adding Cabo Verde to the file...")
    data['features'].append(cape_verde_feature)

# Write the updated file
print("Writing updated countries.json...")
with open('frontend/public/countries.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)

print("Cabo Verde has been added successfully!")
print(f"Total countries in file: {len(data['features'])}")

