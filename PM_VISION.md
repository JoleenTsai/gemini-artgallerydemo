# [PRODUCT VISION] PROJECT: ART GALLERY & SMASH ROOM
## Game Design Requirements & Logic Specifications v2.0

### 1. STRATEGIC OBJECTIVE
The goal of this demo is to showcase a seamless "Vibe-to-Code" pipeline. The system must bridge the gap between high-level brand standards and functional game mechanics using Gemini-CLI as the primary orchestrator.

---

### 2. CORE PHILOSOPHY: THE DUALITY ENGINE
The project is split into two distinct operational "States." The AI must identify which state it is modifying based on the Parent Container ID in `src/index.html`.

#### 2.1 The Art Gallery (State: IMMUTABLE)
* **Target Audience**: High-end digital art collectors.
* **UX Goal**: Evoke feelings of prestige, permanence, and reverence.
* **Technical Constraints**:
    * **Class Binding**: All assets MUST be assigned `class="hero"`.
    * **Physics Interaction**: Assets are static. They must NOT respond to gravity or collision events.
    * **Durability**: Health Points (HP) must be set to `99999` to simulate invulnerability.
    * **Visual Filter**: Maintain a clean, high-fidelity look with no glitched textures.

#### 2.2 The Smash Room (State: EPHEMERAL)
* **Target Audience**: High-energy players seeking tactile feedback and destruction.
* **UX Goal**: Evoke feelings of rebellion, digital entropy, and kinetic satisfaction.
* **Technical Constraints**:
    * **Class Binding**: All assets MUST be assigned `class="breakable"`.
    * **Physics Interaction**: Assets must inherit the global gravity constant defined in `game.js`.
    * **Durability**: Standard Health Points (HP) are set to `50` (2-3 hit kill).
    * **Visual Filter**: Assets should receive "Neon Corruption" (CSS hue-rotation or saturation boosts).

---

### 3. ASSET TIER & ECONOMY SPECIFICATIONS
The AI should use these tiers when generating `data-loot-value` attributes for assets:

| Tier | Environment | HP | Loot Multiplier | Shatter Style |
| :--- | :--- | :--- | :--- | :--- |
| **Common** | Smash Room | 25 | 1.0x | `glass` |
| **Elite** | Smash Room | 100 | 2.5x | `ceramic` |
| **Heroic** | Art Gallery | 99999 | 0.0x | `none` |
| **Artifact** | Art Gallery | 99999 | 0.0x | `marble_dust` |

---

### 4. TELEMETRY & AUDIT REQUIREMENTS
To ensure GDC-grade transparency, every asset modification must be logged:
1.  **Origin Tracking**: Every `<img>` tag must include a `data-prompt-origin` attribute containing the Base64 encoded prompt.
2.  **Logic Rationale**: The AI must update `logs/DESIGN_HISTORY.md` explaining why it chose a specific Tier for a new asset.
3.  **Performance Check**: No asset can be deployed if it exceeds the 5.0MB VRAM budget defined in the Technical Standards.

---

### 5. DEPLOYMENT CRITERIA
* **Zero-Downtime**: The `ship-it` command must verify that `index.html` is well-formed before triggering the Google Cloud Run deployment.
* **Live Feedback**: The terminal must output the final Cloud Run URL in a formatted block for immediate audience scanning.
