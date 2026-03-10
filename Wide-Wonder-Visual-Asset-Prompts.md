## A: 
# Image Generation Prompts: Wide Wonder App

_Instructions: Copy and paste these directly into your preferred image generator. For Flux/Sora/Midjourney, use the Aspect Ratio (AR) flags provided._

## A. App Icon / Favicon (The Wonder Catcher)

**Settings:** AR 1:1 (Square) **Prompt:**

> A modern, glowing 3D app icon. The central icon is a squishy, magical glass jar slightly tipped open, with glowing bioluminescent firefly-green and warm peach stardust swirling out of it. High-end 3D render, soft rounded edges, glossy texture, vibrant bioluminescence, UI element, isolated focus on a dark twilight blue background, Studio Ghibli meets modern Apple design, very cute and inviting. --ar 1:1

## B. User Engagement Icon (The "Why" Firefly)

**Settings:** AR 1:1 (Square) | _Isolated for Layering_ **Prompt:**

> A 3D render of a friendly, glowing, cartoon firefly hovering in the air. The firefly has a very soft, squishy, rounded body. Its tail is glowing brilliantly with neon yellow-green light, leaving a small trail of magical pixel-dust. Isolated on a solid, deep midnight-purple background for easy transparency masking. High-quality Pixar-style 3D render, soft lighting, UI engagement icon, magical. --ar 1:1

## C. The Wonder Guide (Companion Avatar)

**Settings:** AR 1:1 (Square) | _Isolated for Layering_ **Prompt:**

> A cute, floating, 3D character made entirely of soft, glowing twilight clouds. Big, friendly, expressive eyes and a small, happy mouth. The cloud body is a gradient of soft midnight purple, warm peach, and glowing cyan. Isolated on a solid, deep midnight-purple background. Pixar and Studio Ghibli style, ultra-soft textures, fluffy, inviting, magical companion. --ar 1:1

## D. Worldbuilder Mode (The Treasure Map)

**Settings:** AR 4:3 (Tablet) or 16:9 (Web) **Prompt:**

> A top-down, stylized fantasy map designed for a 5-year-old. A magical world with a glowing marshmallow castle, a forest made of giant blue mushrooms, and a winding river of sparkling juice. 2D vector art mixed with soft 3D elements. Glowing UI lines connect locations like a constellation. Dark twilight background, bioluminescent accents, whimsical children's book illustration style. --ar 16:9

## E. Storybook Mode (The Two-Page Spread)

**Settings:** AR 16:9 (Landscape) **Prompt:**

> An open children's storybook lying flat with glowing, magical pages. Left page: vibrant illustration of a purple cat driving a bulldozer. Right page: clean, readable, glowing geometric text. The book rests on a dark, starry night background. Warm ambient lighting, magical atmosphere, high contrast, UI mockup for a reading app. --ar 16:9

## F. The Wonder Catcher Microphone (In-App Interface)

**Settings:** AR 1:1 (Square) | _Isolated for Layering_ **Prompt:**

> A massive, squishy, 3D magical artifact shaped like a rounded microphone. Made of semi-translucent, glowing jelly in a vibrant bioluminescent firefly-green. Organic and soft texture. Surrounding it are floating particles of peach and cyan stardust. Isolated on a solid, deep midnight-purple background. High-end 3D render, tactile, inviting, whimsical, and magical. --ar 1:1

## G. Master Background Layer (Main App Atmosphere)

**Settings:** AR 16:9 (Landscape) and 9:16 (Portrait) **Prompt:**

> An immersive, expansive twilight sky background for a children's app. A gradient of deep midnight blue at the top to a soft, warm peach and violet glow at the horizon. Very subtle, twinkling "living" stars and faint, drifting stardust clouds. Ample empty space in the center for UI elements. Dreamy, calm, magical, Studio Ghibli aesthetic, high-quality digital painting, ultra-soft focus. --ar 16:9

## H. The Constellation Vault (Gallery Background)

**Settings:** AR 16:9 (Landscape) **Prompt:**

> A "Deep Space" version of the twilight sky. Darker midnight purple tones with a high density of glowing, connected star-constellations in the shapes of animals and toys. The background feels vast and magical, like looking through a telescope into a world of dreams. Bioluminescent cyan and violet nebula clouds. High-end 3D depth, soft focus, dreamy atmosphere for a gallery of memories. --ar 16:9

**NOTES FOR ASSEMBLY WHEN VIBE CODING**

### Expert Guidance for your "Vibe Coding" session:

*   **For the Backgrounds (G & H):** I recommend generating both a **16:9** (for your desktop/web view) and a **9:16** (for mobile/tablet portrait). This allows the app to feel native no matter how your grandson holds the device.
    
*   **The "Isolated" Trick:** By asking for a "solid, deep midnight-purple background" for the characters (B, C, and F), you ensure that if your removal tool misses a few pixels around the edges, they will simply blend into your Master Background (G) because the colors match.
    
*   **Layers in CSS:** In your React code, you'll want to stack them using `z-index`:
    
    *   `z-0`: The Master Background (G).
        
    *   `z-10`: The Wonder Guide (C) - _Floating/Animating_.
        
    *   `z-20`: The Captions/Text.
        
    *   `z-30`: The Wonder Catcher (F) - _Pulsing/Interacting_.

