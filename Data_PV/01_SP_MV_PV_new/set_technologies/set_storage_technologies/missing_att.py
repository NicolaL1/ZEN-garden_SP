import os
import json
from pathlib import Path


# 📌 Base directory where storage technology JSON files are located
STORAGE_TECH_DIR = r"C:\Users\nicol\GitHub\PV ZEN_garden\Data\01_SP_MV_PV\set_technologies\set_storage_technologies"

# 📌 Default values for missing attributes (matching the nested format)
DEFAULT_VALUES = {
    "energy_to_power_ratio_min": {"default_value": 0, "unit": "h"},
    "energy_to_power_ratio_max": {"default_value": 1, "unit": "h"},
    "flow_storage_inflow": {"default_value": 1.0, "unit": "GWh/h"}
}

def update_json_file(json_path):
    """ Reads a JSON file, forces re-writing with missing attributes, and logs changes """
    try:
        print(f"📌 Processing file: {json_path}")

        if not os.path.exists(json_path):
            print(f"❌ ERROR: File does not exist! {json_path}")
            return

        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        print(f"   📄 BEFORE: {json.dumps(data, indent=2)}")

        added_attributes = []
        for attr, default_struct in DEFAULT_VALUES.items():
            if attr not in data:
                data[attr] = default_struct
                added_attributes.append(f"{attr} = {default_struct}")

        # 🚨 Force write the file even if no changes were detected
        with open(json_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"✅ UPDATED: {json_path}")
        print(f"   ➕ Added attributes: {added_attributes if added_attributes else 'No new attributes added'}")
        print(f"   📄 AFTER: {json.dumps(data, indent=2)}")

    except Exception as e:
        print(f"❌ Error processing {json_path}: {e}")

def process_all_storage_jsons():
    """ Recursively scans storage technology directories and forces updates for all attributes.json files """
    print("\n🔍 Scanning directories inside set_storage_technologies...")

    for root, _, files in os.walk(STORAGE_TECH_DIR):
        print(f"📂 Checking folder: {root}")

        for file in files:
            if file.lower() == "attributes.json":
                json_path = os.path.join(root, file)
                update_json_file(json_path)

# Run the script
process_all_storage_jsons()
print("\n✅ All missing attributes have been forcefully written to JSON files!")
