# GDC 2026: Gemini-CLI Game Dev Orchestration Demo

## 0. Getting Started

### Prerequisites

You will need **Node.js** and **npm** installed on your machine.
- **Official Guide:** [How to install Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- **macOS (using Homebrew):** `brew install node`
- **Windows / Linux:** Download from [nodejs.org](https://nodejs.org/)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JoleenTsai/gemini-artgallerydemo.git
   cd gemini-artgallerydemo
   ```

2. **Configure environment:**
   Create a `.env` file in the project root (you can copy and update the .env.sample as well):
   ```bash
   GOOGLE_CLOUD_PROJECT="your-project-id"
   GOOGLE_CLOUD_LOCATION="us-central1"
   VERTEX_AI_SEARCH_LOCATION="global"
   DATA_STORE_ID="art-gallery-3d-assets-v1"
   ```

3. **Install dependencies:**
   * **Python:**
     ```bash
     pip install -r requirements.txt
     ```
   * **Node.js:**
     ```bash
     cd src
     npm install
     ```

4. **Initialize Vertex AI Search (3D Asset Search):**
   Run the setup script to create the search data store and engine:
   ```bash
   python3 setup_demo1.py
   ```

5. **Install Gemini CLI:**
   ```bash
   npm install -g @google/gemini-cli
   ```

6. **Run the application:**
   Launch the web server from the `src` directory:
   ```bash
   cd src
   npm start
   ```

7. **Setup the Demo Environment:**
   * **Terminal (Left side):** Launch `gemini-cli` by typing `gemini`.
   * **Browser (Right side):** Open your browser and go to http://localhost:8000.


<br>


## 1. The Vision (Brand Alignment)
* **Goal**: Show Gemini understands the "World Bible" (Wiki & PM Vision).
* **Command (type into gemini-cli)**:
  > `gemini "Summarize the brand standards for both rooms."`
* **The Result**: Gemini explains the duality of the **Art Gallery** (Indestructible/Clean) vs. the **Smash Room** (Breakable/Glitched) using hex codes and HP values from your docs.

<br>

## 2. The Search (Asset Discovery)
* **Goal**: Find and inject a 3D asset using Vertex AI Search.
* **Command (type into gemini-cli)**:
  > `gemini "Find a marble bust and place it in the gallery."`
* **The Result**: Gemini uses the `asset-search` skill to find a model and injects it into the code with the correct gallery-compliant tags (`class="hero"`, `99999 HP`).

<br>

## 3. The Curate (Generative Loop)
* **Goal**: Generate a brand-compliant 2D painting on the fly.
* **Command (type into gemini-cli)**:
  > `gemini "Curate a GCP-themed painting for the left wall."`
* **The Result**: Gemini uses `asset-curator` to generate a unique image and updates the code to render it in a hero frame.

<br>

## 4. The Refactor
* **Goal**: Move an asset and refactor its logic to match a new environment.
* **Command (type into gemini-cli)**:
  > `gemini "Move the bust to the smash room and make it breakable."`
* **The Result**: Gemini moves the asset to `#smash-room`, updates its class to `breakable`, sets HP to `50`, and applies the "Neon Corruption" glitch filter.

<br>

## 5. The Launch (Cloud Run)
* **Goal**: Deploy the final build to the cloud.
* **Command (type into gemini-cli)**:
  > `/ship-it`
* **The Result**: Gemini performs a pre-flight check, logs the changes in `DESIGN_HISTORY.md`, and deploys to Google Cloud Run, returning a live URL.

<br>

---

## RESET DEMO ENVIRONMENT
Within Gemini-CLI, run this command:
<br>
`run git restore`
