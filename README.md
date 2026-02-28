# GDC 2026: Gemini-CLI Game Dev Orchestration Demo

## 1. The Setup (The "Context" Story)
* **Goal**: Prove Gemini understands non-code business logic (Wiki & PM Vision).
* **Action**: 
  > `gemini "Designer, Summary our brand standards for the Art Gallery vs the Smash Room."`
* **The Wow**: The AI explains that the **Art Gallery** is Neo-Classical/Indestructible, while the **Smash Room** is Cyberpunk/Breakable, citing specific HEX codes and HP values from your docs.

  > `gemini "Thanks Designer, can you tell me what I'm missing based on the PM vision?"`
* **The Wow**: The AI explains that the **Art Gallery** is Neo-Classical/Indestructible, while the **Smash Room** is Cyberpunk/Breakable, citing specific HEX codes and HP values from your docs.

## 2. The "Corrupt & Move" (Technical Refactor)
* **Goal**: Show real-time code manipulation and gameplay logic assignment.
* **Action**:
  > `gemini "Move that sculpture to the Smash Room. Update its aesthetic to be 'Glitched' and make it breakable with 50HP."`
* **The Wow**: The AI understands the code and moves the scultpure to `#smash-room`, swaps the CSS class to `breakable` with `health points`.

## 3. The Creative Loop (Nano Banana Integration)
* **Goal**: Generate a brand-compliant asset texture on the fly.
* **Action**:
  > `gemini "Add a green felt sculpture to the main room."` May need to look around to find the sculpture. 
  > `gemini "Curate a modern art painting and place within one of the canvas location on the left wall."`
* **The Wow**: Gemini-CLI understand the code base, uses Nano Banana to generate the image asset, then places it within the code so that it renders within the art gallery.

## 4. The Global Launch (Cloud Run)
* **Goal**: Show the transition from local dev to a live cloud environment.
* **Action**:
  > `gemini "Coding-buddy, ship-it."`
* **The Wow**: The CLI runs pre-flight path checks and deploy the game to Cloud Run within GCP.

