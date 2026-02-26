# [MASTER SPEC] PROJECT: ART GALLERY & SMASH ROOM
## Technical World-Bible & Asset Orchestration Protocol v2.0

### 1. MISSION & NARRATIVE ARCHITECTURE
This project is a dual-state simulator designed to showcase real-time asset manipulation and deployment via Gemini-CLI.
* **The Art Gallery:** Represents "Immutable State." It is a repository of high-value digital artifacts where brand compliance is strictly enforced.
* **The Smash Room:** Represents "Ephemeral State." It is a testing ground for procedural destruction, physics-based entropy, and digital rebellion.

---

### 2. ARCHITECTURAL SCHEMA: THE ART GALLERY
The gallery is defined by structural rigidity, prestige, and high-fidelity rendering.

#### 2.1 Visual Design Tokens
* **Aesthetic:** Neo-Classical Minimalism / Brutalist Luxury.
* **Surface Shaders:** High-gloss marble, brushed titanium, gold leafing, and volumetric glass.
* **Palette (Primary):** `White: #FFFFFF`, `Grey: #2F2F2F`.
* **Accent Colors:** `GCP Teal: #00FFD1` (Signifying Google Cloud connection), `Sunlight Gold: #D4AF37`.

#### 2.2 DOM Structure & Logic
* **Container ID:** `#gallery`
* **Target Selectors:** `.pedestal`, `.hero-frame`.
* **Physics State:** `static`. All assets in this wing are indestructible and ignore gravity constants.

#### 2.3 Nano Banana (GCP) Prompt Injection Parameters
* **Base Modifiers:** "8k UHD, cinematic museum lighting, ray-traced reflections, symmetrical composition, marble plinth, minimalist background, museum archival quality."
* **Material Weights:** `[Marble: 0.8, Gold: 0.2]`.

---

### 3. ARCHITECTURAL SCHEMA: THE SMASH ROOM
The Smash Room is an unstable, high-energy physics environment.

#### 3.1 Visual Design Tokens
* **Aesthetic:** Industrial Cyberpunk / Digital Glitch.
* **Surface Shaders:** Matte obsidian, glowing plasma textures, spray-painted concrete, and wireframe overlays.
* **Palette (Primary):** `Void Black: #000000`.
* **Accent Colors:** `Neon Pink: #FF00FF`, `Electric Cyan: #00FFFF`, `Glitch Green: #39FF14`.

#### 3.2 DOM Structure & Logic
* **Container ID:** `#smash-room`
* **Target Selectors:** `.spawn-zone`, `.debris-bin`.
* **Physics State:** `dynamic`. Assets here inherit gravity and collision properties from `game.js`.

#### 3.3 Nano Banana (GCP) Prompt Injection Parameters
* **Base Modifiers:** "Low-poly artifacts, chromatic aberration, flickering neon rim lighting, spray-painted grunge, jagged edges, digital noise, internal glowing core, unstable form."
* **Material Weights:** `[Glass: 0.5, Obsidian: 0.3, Neon: 0.2]`.

---

### 4. DATA SCHEMA & METADATA BINDINGS
When the AI injects an asset into `src/index.html`, it **must** attach the following data attributes:

| Attribute | Type | Description |
| :--- | :--- | :--- |
| `data-asset-id` | UUID | Unique identifier for telemetry tracking. |
| `data-hp` | Integer | Health points (Gallery = `99999`, Smash Room = `10-100`). |
| `data-loot-value` | Float | Multiplier for currency drops on smash. |
| `data-shatter-type` | Enum | `[glass, ceramic, digital_glitch, marble_dust]`. |
| `data-prompt-origin` | Base64 | The original Nano Banana prompt for GDC transparency. |

---

### 5. THE TRANSITION PROTOCOL
When an asset is moved from the Art Gallery to the Smash Room via CLI:
1.  **CSS Refactor:** Swap the `.hero` class for `.breakable`.
2.  **Shader Update:** Apply a `hue-rotate(270deg)` and `brightness(1.5)` filter to simulate "Neon Corruption."
3.  **Physics Bind:** The `game.js` must register a new `CollisionListener` for the object's ID.

---

### 6. GDC PERFORMANCE & RESILIENCY GUARDRAILS
* **Wi-Fi Strategy:** If the GCP API latency exceeds 3000ms, inject a "Digital Placeholder" (glitched CSS box) to keep the demo moving.
* **Audit Trail:** Every change must be logged in `logs/DESIGN_HISTORY.md` with the specific rationale: "Aligning with WIKI Section 2.1 for Neo-Classical Compliance."