---
title: "ROLI Seaboard M"
slug: "block-m"
description: "ROLI Seaboard M — 24-key MPE controller with a silicone Keywave surface enabling 5 dimensions of expressive touch."
url: "https://roli.com/eu/product/seaboard-m"
tags:
  - Controller
  - ROLI
  - MPE
---

## Keywave Surface

The Seaboard M features 24 miniature Keywaves — continuous silicone keys approximately 25% narrower than standard piano keys. The soft surface deforms under finger pressure, enabling the sensor array to detect continuous gesture data impossible on a rigid keybed. There are no moving parts in the traditional sense; the key response comes entirely from the silicone compliance and pressure sensitivity.

## MPE — 5 Dimensions of Touch

<ul class="space-y-4 list-disc pl-6">
  <li><strong>Strike (Note-On velocity):</strong> how fast the key is pressed downward — controls initial brightness, volume, or any velocity-mapped parameter on the receiving instrument.</li>
  <li><strong>Press (per-note channel pressure / poly aftertouch):</strong> push deeper into the key after the initial strike. Maps to channel pressure or a dedicated MPE dimension. Use for vibrato, filter opening, or a slow swell into a note.</li>
  <li><strong>Slide (CC74 / timbre):</strong> move the finger up or down the vertical length of a key while held. Commonly routed to timbral morphing — wavetable position on the Hydrasynth, or filter cutoff on any MIDI instrument.</li>
  <li><strong>Glide (per-note pitch bend):</strong> move horizontally between or across keys while sustaining a note. Creates portamento, pitch slides between adjacent notes, and seamless legato transitions.</li>
  <li><strong>Lift (Note-Off velocity):</strong> how quickly the finger leaves the key. Controls the tail character — a fast lift creates an abrupt release; a slow lift produces a soft decay fade.</li>
</ul>

## Setting Up MPE in Ableton Live 12

1. Connect the Seaboard M via USB-C — it appears as a class-compliant MIDI device, no driver needed.
2. In Live's Preferences → MIDI, enable Track and Remote for the Seaboard M input.
3. Create a MIDI track. In the track's MIDI From dropdown, select **Seaboard M**.
4. On the instrument in the track, enable **MPE mode** (look for an MPE toggle in the instrument header or device settings).
5. Use MPE-capable instruments: **Ableton Drift**, **Ableton Meld**, **ROLI Studio Player**, or third-party MPE synths.

## ROLI Studio Player

Included with the Seaboard M. Contains 200+ MPE-designed presets that respond expressively to all 5 dimensions out of the box. Notable features:

- **Smart Chords:** hold one note, trigger a full chord voicing. Change chord type via the instrument UI.
- **3-layer MPE arpeggiator:** independent layers each with their own rate, pattern, and MPE dimension routing.
- **Voice slots:** up to 24 simultaneous voices (one per Keywave).

## Connectivity

- **USB-C** to computer: class-compliant, no driver required, works on Windows and macOS.
- **Bluetooth MIDI** with up to 10-hour battery life — play wirelessly while connected to a laptop or iPad.
- **DNA magnetic connectors** on left and right ends for chaining a second Seaboard M or a Piano M without cables.

## Using with the Hydrasynth Explorer

The Hydrasynth supports polyphonic aftertouch natively, making it an ideal MPE companion:

1. Set the Seaboard M MIDI output to the Hydrasynth's USB MIDI input (or via MOTU 5-pin MIDI Out if USB is occupied).
2. On the Hydrasynth, enable poly aftertouch in the MIDI settings.
3. **Press** (poly AT) → Hydrasynth per-voice filter opening, vibrato, or macro routing.
4. **Slide** (CC74) → assign in the Hydrasynth modulation matrix to wavetable morph position or second filter cutoff.
5. **Glide** (pitch bend range) → set the Hydrasynth pitch bend range to match the Seaboard's glide range (typically ±48 semitones for wide pitch slides).

## Playing Techniques

<ul class="space-y-4 list-disc pl-6">
  <li><strong>Vibrato:</strong> oscillate the Press dimension on a sustained note — the rate and depth of pressure oscillation maps directly to pitch modulation speed on most MPE instruments.</li>
  <li><strong>Pitch slides:</strong> hold a note and glide horizontally to a new pitch — creates a smooth portamento that standard MIDI cannot achieve per-voice.</li>
  <li><strong>Filter swells:</strong> sustain a pad sound and slowly increase Press — the filter opens gradually over 2–4 seconds for dramatic tension-and-release.</li>
  <li><strong>Timbral evolution:</strong> slowly move a held finger up and down the Keywave (Slide dimension) to morph wavetable position on the Hydrasynth in real time.</li>
  <li><strong>Expressive chords:</strong> strike a chord and independently Press each finger at different rates — each note gets its own modulation, creating complex polyphonic expression from a chord.</li>
</ul>
