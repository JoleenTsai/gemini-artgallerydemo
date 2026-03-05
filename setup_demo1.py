import os
import time
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1beta as discoveryengine
from google.api_core import exceptions

# --- Configuration ---
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
VERTEX_AI_SEARCH_LOCATION = os.environ.get("VERTEX_AI_SEARCH_LOCATION")
DATA_STORE_ID = os.environ.get("DATA_STORE_ID")
APP_ID = "art-gallery-search-v1"

GAME_ASSETS = [
    {
        "name": "Decorative Indoor Tree",
        "desc": "A tall potted plant with a low-poly trunk and lush canopy.",
        "js_snippet": "{ 'type': 'tree', 'mass': 10, 'isBreakable': false, 'geom': 'cylinder', 'dim': [0.2, 0.2, 4.0], 'mat': 'ceramic' }"
    },
    {
        "name": "Marble End Table",
        "desc": "A heavy minimalist table made of white flecked marble.",
        "js_snippet": "{ 'type': 'table', 'mass': 40, 'isBreakable': false, 'geom': 'box', 'dim': [1.5, 1.0, 1.5], 'mat': 'marble' }"
    },
    {
        "name": "Fragile Glass Cube",
        "desc": "A delicate glass sculpture that shatters easily.",
        "js_snippet": "{ 'type': 'sculpture', 'mass': 2, 'isBreakable': true, 'shatterType': 'glass', 'geom': 'box', 'dim': [0.8, 0.8, 0.8], 'mat': 'glass' }"
    },
    {
        "name": "Neon Obelisk",
        "desc": "A glowing pillars that pulses with pink light.",
        "js_snippet": "{ 'type': 'light', 'mass': 0, 'isBreakable': false, 'geom': 'cylinder', 'dim': [0.3, 0.3, 3.0], 'mat': 'neon' }"
    },
    {
        "name": "Surveillance Camera",
        "desc": "A small black plastic camera for the gallery corners.",
        "js_snippet": "{ 'type': 'prop', 'mass': 1, 'isBreakable': true, 'shatterType': 'ceramic', 'geom': 'box', 'dim': [0.2, 0.2, 0.4], 'mat': 'blackPlastic' }"
    },
    {
        "name": "Vintage Radio",
        "desc": "An old retro-plastic radio that can be thrown.",
        "js_snippet": "{ 'type': 'prop', 'mass': 5, 'isBreakable': true, 'shatterType': 'ceramic', 'geom': 'box', 'dim': [0.6, 0.4, 0.3], 'mat': 'retroPlastic' }"
    },
    {
        "name": "Large Ceramic Urn",
        "desc": "A massive white urn perfect for smashing.",
        "js_snippet": "{ 'type': 'vase', 'mass': 15, 'isBreakable': true, 'shatterType': 'ceramic', 'geom': 'cylinder', 'dim': [0.8, 0.8, 1.5], 'mat': 'ceramic' }"
    },
    {
        "name": "Security Barrier",
        "desc": "A velvet rope stand with a gold post.",
        "js_snippet": "{ 'type': 'post', 'mass': 8, 'isBreakable': false, 'geom': 'cylinder', 'dim': [0.1, 0.1, 1.2], 'mat': 'gold' }"
    }
]

def setup_vertex_search():
    client_options = ClientOptions(api_endpoint=f"{VERTEX_AI_SEARCH_LOCATION}-discoveryengine.googleapis.com")
    ds_client = discoveryengine.DataStoreServiceClient(client_options=client_options)
    engine_client = discoveryengine.EngineServiceClient(client_options=client_options)
    doc_client = discoveryengine.DocumentServiceClient(client_options=client_options)

    parent = f"projects/{PROJECT_ID}/locations/{VERTEX_AI_SEARCH_LOCATION}/collections/default_collection"
    
    # 1. Create Data Store
    print(f"Checking Data Store: {DATA_STORE_ID}...")
    ds = discoveryengine.DataStore(
        display_name="Art Gallery 3D Assets",
        industry_vertical=discoveryengine.IndustryVertical.GENERIC,
        content_config=discoveryengine.DataStore.ContentConfig.NO_CONTENT,
        solution_types=[discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH],
    )
    try:
        operation = ds_client.create_data_store(parent=parent, data_store=ds, data_store_id=DATA_STORE_ID)
        operation.result()
        print(f"Data Store '{DATA_STORE_ID}' created successfully.")
    except exceptions.AlreadyExists:
        print(f"Data Store '{DATA_STORE_ID}' already exists. Skipping.")

    # 2. Create Search Engine
    print(f"Checking Search Engine: {APP_ID}...")
    engine = discoveryengine.Engine(
        display_name="Art Gallery Search",
        data_store_ids=[DATA_STORE_ID],
        solution_type=discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH,
    )
    try:
        operation = engine_client.create_engine(parent=parent, engine=engine, engine_id=APP_ID)
        operation.result()
        print(f"Search Engine '{APP_ID}' created successfully.")
    except exceptions.AlreadyExists:
        print(f"Search Engine '{APP_ID}' already exists. Skipping.")

    # 3. Load 3D-Oriented Documents
    parent_ds = f"{parent}/dataStores/{DATA_STORE_ID}/branches/0"
    print(f"Loading {len(GAME_ASSETS)} assets into Data Store...")
    for asset in GAME_ASSETS:
        doc_id = asset["name"].lower().replace(" ", "-")
        document = discoveryengine.Document(
            struct_data={
                "title": asset["name"],
                "description": asset["desc"],
                "config": asset["js_snippet"]
            }
        )
        try:
            doc_client.create_document(parent=parent_ds, document=document, document_id=doc_id)
            print(f"  [+] Created document: {doc_id}")
        except exceptions.AlreadyExists:
            print(f"  [.] Document already exists: {doc_id}")
    
    print("Setup Complete.")

if __name__ == "__main__":
    setup_vertex_search()

