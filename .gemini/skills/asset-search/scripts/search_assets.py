import os
import sys
import json
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1beta as discoveryengine

# Configuration from environment
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("VERTEX_AI_SEARCH_LOCATION", "global")
DATA_STORE_ID = os.environ.get("DATA_STORE_ID")

def search_assets(query):
    if not PROJECT_ID or not DATA_STORE_ID:
        return {"error": "Missing GOOGLE_CLOUD_PROJECT or DATA_STORE_ID environment variables."}

    try:
        client_options = ClientOptions(api_endpoint=f"{LOCATION}-discoveryengine.googleapis.com")
        client = discoveryengine.SearchServiceClient(client_options=client_options)

        serving_config = client.serving_config_path(
            project=PROJECT_ID,
            location=LOCATION,
            data_store=DATA_STORE_ID,
            serving_config="default_search",
        )

        request = discoveryengine.SearchRequest(
            serving_config=serving_config,
            query=query,
            page_size=5,
        )

        response = client.search(request)
        
        results = []
        for result in response.results:
            data = result.document.struct_data
            results.append({
                "title": data.get("title"),
                "description": data.get("description"),
                "config": data.get("config")
            })
        return results
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No query provided."}))
        sys.exit(1)
    
    query = sys.argv[1]
    results = search_assets(query)
    print(json.dumps(results, indent=2))
