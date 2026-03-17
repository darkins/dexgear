---
title: "Ableton Live"
slug: "ableton"
description: "Ableton Live is a digital audio workstation for music production, creation, and performance."
url: "https://www.ableton.com/"
tags:
  - DAW
  - Music Production
---

## Session View vs Arrangement View

Ableton Live 12 operates in two parallel environments. **Session View** is the clip-launching matrix — rows (scenes) hold clips that fire on demand, ideal for improvisation and live performance. **Arrangement View** is a traditional linear timeline for composition and final arrangement. You can freely record Session View performances into the Arrangement View to lock in a structure.

## Hardware Integration Map

<ul class="space-y-4 list-disc pl-6">
  <li><strong>Push 1</strong> — primary hands-on instrument: step sequencing, clip launching, melodic note input, device parameter control via 8 encoders. The most deeply integrated controller in the stack.</li>
  <li><strong>Launchkey 37 Mk3</strong> — 37-key keyboard for melodic and chordal input; direct transport, clip launch, and scene controls built in. Use Scale Mode to restrict output to the current key signature.</li>
  <li><strong>Launch Control XL Mk2</strong> — dedicated mixing surface: 8 faders, 16 assignable knobs (sends A+B), 24-pad mute/solo/arm grid. Handles the mixing layer so Push stays free for performance.</li>
  <li><strong>Knobbler (M4L)</strong> — iPad-based deep parameter control via Max for Live. Endless encoders with auto-labelling, X–Y pads, device shortcuts, and a Channel Strip mixer. Complements all hardware controllers.</li>
  <li><strong>Hydrasynth Explorer</strong> — connected as an External Instrument; audio into MOTU inputs 5/6, MIDI via USB or MOTU 5-pin DIN. Use Live's External Instrument device for zero-latency monitoring.</li>
  <li><strong>ROLI Seaboard M</strong> — USB-C MPE controller. Set MIDI track Input to Seaboard M and enable MPE on the instrument track. Use MPE-capable instruments (Drift, Meld, ROLI Studio Player).</li>
  <li><strong>Yamaha P-225</strong> — USB MIDI class-compliant controller; load virtual piano instruments (NI Noire, Addictive Keys) on the receiving MIDI track.</li>
  <li><strong>Shure SM58</strong> — vocal recording via MOTU input 1; create an Audio Track and set the input to MOTU In 1. Monitor through CueMix FX to avoid latency during tracking.</li>
  <li><strong>Roland VT-3</strong> — processed vocal insert; stereo line out → MOTU inputs 3/4. Record a separate Audio Track for the VT-3 signal simultaneously with the clean SM58 track.</li>
  <li><strong>MOTU UltraLite Mk3</strong> — the audio backbone; all analog audio enters and exits through this interface. Configure in Ableton Preferences → Audio → ASIO → MOTU UltraLite-mk3.</li>
</ul>

## Setting Up External Instruments

Use **Instruments → External Instrument** on a MIDI track to route a hardware synth through Live:

1. Drop the External Instrument device onto a MIDI track.
2. Set the MIDI To field to the synth (e.g. Hydrasynth USB MIDI or MOTU MIDI Out).
3. Set Audio From to the MOTU input channels the synth uses (e.g. 5/6 for the Hydrasynth stereo output).
4. Adjust the Hardware Latency knob to compensate for any analog round-trip delay.

This gives zero-latency hardware monitoring through MOTU while still recording into Ableton.

## Max for Live

Max for Live embeds the Max/MSP visual programming environment directly inside Live. It enables custom MIDI processors, generative sequencers, and deep integration devices like Knobbler that would be impossible with standard MIDI mapping. Open any M4L device's patch by clicking the wrench icon — useful for understanding how data flows. See the [M4L page](/daw/m4l) for curated device links.

## Related Pages

- [Keyboard Shortcuts](/daw/shortcuts)
- [Max for Live Resources](/daw/m4l)
- [Racks Guide](/daw/racks)
