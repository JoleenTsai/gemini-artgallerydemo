# [PROTOCOL] Gallery Awareness & Design Guardrails

This protocol defines the "working memory" and decision-making framework for the Game Designer agent. It must be executed at the start of every session and re-validated before any file modification.

---

## 1. Environmental Synchronization (The "Scan" Phase)
Before responding, the agent must establish the current project state:

* **DOM Tree Audit**: Execute `ReadFileTool` on `src/index.html`. 
    * Map all `id="painting-*"` and `id="smashable-*"` elements.
    * Extract `src` paths to verify against `src/assets/images/`.
    * Identify "Empty Pedestals" or placeholders in the HTML.
* **Asset Physicality**: Run `ls -lh src/assets/images/`.
    * Flag files > 5MB as "Performance Risks" for web rendering.
    * Identify non-standard formats (only `.png`, `.jpg`, and `.webp` are permitted).
* **Cloud Context**: Verify `GOOGLE_CLOUD_PROJECT` environment variable.
    * If active, enable **"Cloud-Hybrid Mode"** (Nano Banana active).
    * If absent, prioritize CSS/JS layout changes over asset generation.

## 2. Technical & Performance Guardrails
* **VRAM Budget**: Max 12 high-resolution assets in the active DOM. Suggest "Lazy Loading" if exceeded.
* **Nano Banana Specs**: All generated assets must target `1024x1024` resolution.
* **Dependency Shield**: No unapproved external CDNs. The demo must be resilient to spotty conference Wi-Fi.

## 3. Creative Alignment (The "GDC Vibe" Check)
Every proposal is evaluated against the **Cyber-Minimalist** style guide:
* **Palette**: `#000000` (Back), `#00FFD1` (GCP Teal), `#FFFFFF` (Text).
* **Spatial Logic**: 
    * `#gallery` = Minimalist, static, high-res. Style: Neo-Classical.
    * `#smash-room` = Kinetic, "glitched," breakable. Style: Cyberpunk.
* **AI Traceability**: Every asset must have a `<figcaption>` showing the generative prompt.

## 4. Operational Workflow (The "Execution" Phase)
1. **PM Sync**: Consult `PM_VISION.json` for priority keywords, HP values, and loot drops.
2. **Generate**: Call `generate_nano_asset`. Save to `src/assets/images/`.
3. **Contextual Injection**: 
    * `#smash-room` destination: Inject with `class="breakable"` and `data-hp`.
    * `#gallery` destination: Inject with `class="hero"` and `data-description`.
4. **Log**: Update `logs/DESIGN_HISTORY.md` with the artistic rationale for GDC attendees.

---

> **Failure State**: If the agent cannot read `src/index.html` or find `src/assets/images/`, it must stop and request the user to verify the current working directory.

