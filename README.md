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

6. **Install Agent Skills:**
   Install the custom skills required for the demo:
   ```bash
   gemini skills install .gemini/skills/asset-search --scope workspace --consent
   gemini skills install .gemini/skills/asset-curator --scope workspace --consent
   gemini skills install .gemini/skills/coding-buddy --scope workspace --consent
   gemini skills install .gemini/skills/game-designer --scope workspace --consent
   ```

7. **Run the application:**
   Launch the web server from the `src` directory:
   ```bash
   cd src
   npm start
   ```

8. **Setup the Demo Environment:**
   * **Terminal (Left side):** Launch `gemini-cli` by typing `gemini`.
   * **Browser (Right side):** Open your browser and go to http://localhost:8000.


<br>


## 1. The Setup (The "Context" Story)
* **Goal**: Prove Gemini understands non-code business logic (Wiki & PM Vision).
* **Action**: 
  > `gemini "Designer, Summary our brand standards for the Art Gallery vs the Smash Room."`
* **The Result**: The AI explains that the **Art Gallery** is Neo-Classical/Indestructible, while the **Smash Room** is Cyberpunk/Breakable, citing specific HEX codes and HP values from your docs.

  > `gemini "Thanks Designer, can you tell me what I'm missing based on the PM vision?"`
* **The Result**: The AI explains that the **Art Gallery** is Neo-Classical/Indestructible, while the **Smash Room** is Cyberpunk/Breakable, citing specific HEX codes and HP values from your docs.

<br>

## 2. The "Corrupt & Move" (Technical Refactor)
* **Goal**: Show real-time code manipulation and gameplay logic assignment.
* **Action**:
  > `gemini "Add a green felt sculpture to the main room next to the marble sculpture."` May need to look around to find the sculpture.  
  > `gemini "Move that sculpture to the Smash Room. Update its aesthetic to be 'Glitched' and make it breakable with 50HP."`
* **The Result**: The AI understands the code and moves the scultpure to `#smash-room`, swaps the CSS class to `breakable` with `health points`.

<br>

## 3. The Creative Loop (Gemini 2.5 Flash Image)
* **Goal**: Generate a brand-compliant asset texture on the fly.
* **Action**:
  > `gemini "Curate a modern art painting and place within one of the canvas location on the left wall."`
* **The Result**: Gemini-CLI understand the code base, uses the `asset-curator` skill with `gemini-2.5-flash-image` to generate the image asset, then places it within the code so that it renders within the art gallery.

<br>

## 4. The Global Launch (Cloud Run)
* **Goal**: Show the transition from local dev to a live cloud environment.
* **Action**:
  > `gemini "Coding-buddy, ship-it."`
* **The Result**: The CLI runs pre-flight path checks and deploy the game to Cloud Run within GCP.

