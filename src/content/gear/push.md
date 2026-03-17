---
title: "Push 1"
slug: "push"
description: "Ableton Push 1 — hands-on instrument for step sequencing, melodic note input, clip launching, and deep device control inside Ableton Live."
url: "https://www.ableton.com/en/manual/using-push-1/"
tags:
  - Controller
  - Ableton
---

## Setup

Connect Push 1 via USB — Ableton detects it automatically with no additional drivers. Push appears immediately as a control surface in Live's Preferences under the MIDI/Surfaces tab.

## Browse Mode

Press **Browse** to load instruments, drum kits, samples, and effects without touching the mouse. The display shows your Live library. Use the **In** and **Out** buttons to navigate folders, the touch encoder to scroll, and the grid pads to load a selection directly onto the currently selected track.

## Session Mode

Press **Session** to enter the clip-launching grid. Each pad maps to a clip slot — lit pads contain clips, unlit pads are empty. Launch clips, stop tracks, and trigger scenes from the hardware. Hold **Shift** + any pad to enter the **Session Overview** — a zoomed-out 64×64 map of the entire Session View, allowing fast navigation across large sets.

## Note Mode — Beats

<ul class="space-y-4 list-disc pl-6">
  <li><strong>Loop Selector layout (default):</strong> 16 bottom pads = drum playback; 16 top pads = step sequencer positions; bottom row pads control loop length. Tap a step pad to add or remove that drum hit.</li>
  <li><strong>16 Velocities layout:</strong> hold a drum pad and press <strong>Select</strong> to enter 16 Velocities mode — the 16 pads become 16 velocity levels for that pad. Useful for humanising drum programming.</li>
  <li><strong>64-Pad Mode:</strong> press <strong>Note</strong> twice to get an 8×8 drum pad grid for large kits with up to 64 pads visible at once.</li>
  <li><strong>Step sequencing:</strong> in Loop Selector layout, tap step pads to place or remove notes. Hold a placed step to edit its note and velocity. Hold <strong>Mute</strong> + a step pad to mute that individual step without deleting it.</li>
  <li><strong>Real-time recording:</strong> press <strong>Record</strong> to start recording; after one loop, push automatically enters Overdub. Press <strong>Record</strong> again to exit overdub. Use <strong>Fixed Length Recording</strong> to commit clips of a set bar length.</li>
  <li><strong>Repeat:</strong> hold a drum pad to stream a continuous stream of notes at the rate set by the <strong>Scene</strong> / <strong>Grid</strong> buttons. Turn the <strong>Swing</strong> knob to add groove.</li>
  <li><strong>Quantize:</strong> press <strong>Quantize</strong> to snap all notes in the clip to the current grid; hold <strong>Quantize</strong> to access quantize settings. Hold <strong>Quantize</strong> + a drum pad to quantize only that pad's notes.</li>
</ul>

## Note Mode — Melodies

<ul class="space-y-4 list-disc pl-6">
  <li><strong>Default layout:</strong> the 8×8 grid plays notes in 4th intervals across rows. Blue pads = root note, white pads = in-scale, green pads = currently playing. Familiar to guitar players; layout shifts by scale.</li>
  <li><strong>Scale Mode:</strong> hold <strong>Shift</strong> + <strong>Note</strong> to access Scale settings. Change the root key, scale type (Major, Minor, Dorian, etc.), toggle In Key vs Chromatic, and enable or disable Fixed Y (locks root note positions).</li>
  <li><strong>Melodic Step Sequencer:</strong> press <strong>Select</strong> while in Note mode to switch to the Melodic Step Sequencer. 8 rows correspond to pitch; 8 columns correspond to steps. The top row pads control loop length. Step through 32-note sequences by advancing loop position.</li>
  <li><strong>32-Note Mode:</strong> in the Melodic Step Sequencer, the bottom half (rows 5–8) plays notes live for input, while the top half (rows 1–4) shows the sequence steps.</li>
  <li><strong>Octave navigation:</strong> press the <strong>Octave Up/Down</strong> buttons or swipe the touch strip to shift the visible pitch range up and down the keyboard.</li>
</ul>

## Device Mode

Press **Device** to control the currently selected Live instrument or effect. Eight encoders map to the eight main parameters of the device. Press the **In** button to navigate into Rack chains or reveal additional parameter banks. Press the **Out** button to step back up. The four **State Control** buttons at the top right toggle the device on/off and navigate between parameters pages.

## Mixing

<ul class="space-y-4 list-disc pl-6">
  <li><strong>Volume Mode:</strong> press <strong>Volume</strong> — the 8 encoders control track volume; the touch strip becomes the Master volume control.</li>
  <li><strong>Pan &amp; Send Mode:</strong> press <strong>Pan &amp; Send</strong> — first press controls pan; subsequent presses cycle through each available send return.</li>
  <li><strong>Track Mode:</strong> press <strong>Track</strong> to control all parameters of the currently selected track at once — volume, pan, and all sends visible simultaneously.</li>
</ul>

## Automation

<ul class="space-y-4 list-disc pl-6">
  <li>Press <strong>Automation</strong> to begin recording parameter movements into the clip. Any encoder change is written as clip automation.</li>
  <li>Press <strong>Delete</strong> + touch an encoder to erase the automation for that single parameter.</li>
  <li>Press <strong>Shift + Automation</strong> to re-enable automation overrides after manually moving a value.</li>
  <li><strong>Per-step automation:</strong> in Device or Volume Mode, hold a step pad in the sequencer with one hand and tweak an encoder with the other — that step gets a unique parameter value independent of the rest of the clip.</li>
</ul>

## User Preferences

- **Velocity curves:** adjustable from Linear to Logarithmic in Push's Preferences (hold **Setup**). Logarithmic makes soft playing easier; Linear gives max dynamic range.
- **Aftertouch threshold:** set how much pressure is required before aftertouch activates — useful if accidental pressure triggering occurs during performance.
- **Fixed Length Recording:** set the default clip length (1, 2, 4, 8 bars) so that clips always commit at the same length.

## Footswitches

- **Port 1 (Sustain):** standard sustain pedal behaviour for melodic playing.
- **Port 2:** single press = toggle record on/off; double-tap = **New** (creates a new clip and starts recording). Ideal for hands-free punch-in recording while playing keys on the Launchkey 37 or P-225.

## Integration Tips

<ul class="space-y-4 list-disc pl-6">
  <li>Run Push 1 alongside the <strong>Launch Control XL</strong> on separate MIDI ports simultaneously — LCX handles fader/send mixing while Push handles note input and step sequencing with no MIDI conflict.</li>
  <li>Use <strong>Knobbler</strong> alongside Push for deeper device parameter control. Push's 8 Device Mode encoders are excellent for top-8 parameters; open Knobbler on iPad for the remaining deep parameters without interrupting the playing surface.</li>
  <li>Use the <strong>footswitch port 2</strong> for hands-free punch-in while playing melodic parts on the Launchkey 37 or P-225 — no need to reach for the computer or Push's Record button.</li>
  <li>In <strong>Scale Mode</strong>, match the root key and scale to whatever the Hydrasynth patch is tuned to — the Push grid highlights available notes, preventing wrong-note mistakes in live jams.</li>
</ul>
