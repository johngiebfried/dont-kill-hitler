# Platformer Spec — "Don't Kill Hitler" (web edition)

Owner: Session A. Folder: `platformer/`. Starting point: `reference/dkh_platformer_v1.html` (the build played in class on March 9, 2026, with every in-chat patch applied; smoke-tested headless with no console errors).

## 1. What it is and what must not change

A single-file HTML5 canvas side-scroller, three to five minutes long, projected by the instructor in class. Five short runs through the Reich Chancellery. Each run ends by reaching the target. The first four targets are Hitler, Himmler, Heydrich, Goebbels; after each, a briefing reports a worse successor. The fifth target is the player's own past self. Killing it closes the loop: Hitler never died, history proceeds as written, and the final screen says "The machine was always the problem."

Fixed by John and not up for redesign without his say: the target sequence, the self-as-final-target paradox ending, the 1933 Chancellery setting for the opening, no player gun ("for now"), guards that shoot, dogs that patrol and charge, short levels, the TID framing, and the CRT green-terminal identity. The argument lives in the text and the sequence (see `01`, section 5), so polish the delivery of that text; do not add systems that try to carry the argument mechanically.

Aesthetic: canvas 640×360 logical pixels, `image-rendering: pixelated`, CSS scanline overlay, all sprites drawn procedurally with `fillRect` (no image files), limited dark palette (`const C`), Courier New throughout, green on black. No swastikas or insignia; banners are an abstract red roundel by design.

## 2. Architecture of v1 (about 650 lines, one `<script>`)

```
PALETTE        const C { ... }
CONSTANTS      FLOOR=296, GRAV=0.52, PSPEED=2.8, JFORCE=-11, TIME_LIM=35, LVL_W=4800, TARGET_X=LVL_W-130
PLATFORMS      const PLATS [[worldX, worldY, width], ...]  (13, same every level)
LEVEL DATA     const LEVELS [{target, lines[]}], const FINAL [], const TARGET_NAMES
SPRITES        r(), sprPlayer(x,y,walkFrame,flip,ghost), sprGuard(x,y,wf,facing), sprDog(x,y,dir,charging), sprTarget(x,y,type)
INPUT          const K (key map), key(...keys)
STATE          state, lvl, frame, camX, timers, p (player), enemies, bullets, parts, MAX_HP=3
INIT           mkPlayer(), mkEnemies(), resetLvl()
HANDLERS       click + keydown advance the state machine
UPDATE         update(): timer, physics, platforms, camera, target check, enemy AI, stomp/hurt, bullets, particles
DAMAGE         hurtP() (−1 HP, 90 iframes, knockback hop), killP() (death state, particles)
DRAW           draw() → dTitle / dBrief / dGame (dBg, dFloor, dPlats, dEnemies, dBullets, dTargetObj, dHUD) / dFinal
LOOP           requestAnimationFrame(loop)
```

State machine: `TITLE → BRIEF → PLAY → (DEAD → PLAY) | (DONE → BRIEF next level) | (level 5: FINAL) → TITLE`.

Briefing text types out four frames per line; lines starting with `>` render as bold prompts; `.`, `..`, `...` render dim; empty strings add space. A click or key skips to the end; once complete, Space/Enter/click deploys.

Player: `{x,y,vx,vy,ground,dead,wf,wt,right,hp,iframes}`. Arrow keys or WASD, jump on Space/W/Up. Three hit points; each hit gives 90 frames (1.5 s) of invincibility with blinking. Death restarts the level with full HP. Landing on an enemy from above (falling, feet above 55% of enemy height) kills it with a bounce. Touching the target ends the level.

Guards: five per level at x = 840, 1640, 2540, 3490, 4380; two of every three patrol ±55 px; always face the player; shoot when within 400 px and the cooldown expires (`st` starts 140–280 frames, then `cd` = max(120, 200 − 10·lvl) + up to 40); bullets travel 1.8 px/frame for 120 frames. Dogs: eight per level at x = 590 … 3890; patrol ±85 px at 1.1·hard; charge when the player is within 135 px horizontally and 55 px vertically at 3.2 + 0.55·lvl px/frame, turning red. `hard = 1 + 0.28·lvl` scales patrol speed only.

Timer: 35 s per level (the brief said about 30), red and blinking under 8 s; running out kills the player. HUD: op counter, target name, timer, progress bar to target, hearts.

## 3. Known problems in v1

The final screen overflows (confirmed by screenshot): sixteen lines starting at y = 62 with 26 px spacing need about 394 px on a 360 px canvas. "from the outside." collides with the "TEMPORAL INTELLIGENCE DIRECTORATE / SIMULATION COMPLETE" footer, and the closing line, "the problem.", is cut off below the canvas. The thesis line of the whole game does not display. Fix this first.

The canvas is fixed at 640×360 CSS pixels. On a classroom projector it is small. Scale to the window with integer scaling where possible (letterboxed, still crisp).

All five levels share one platform layout and nearly identical difficulty; the `hard` multiplier is barely felt.

Particles are stored in screen space, so stomp particles slide with the camera. Cosmetic.

There is no sound at all, no pause, no mute, and no way for an instructor to jump to a given level during a lecture.

The "kill" is walking into the target; the moment has a white flash and particles but no weight. The self-reveal on level 5 is a red copy of the player sprite with a "?" and no animation.

## 4. Roadmap (priority order; commit after each item)

**P0 — Classroom-ready baseline.** Copy v1 into `platformer/index.html` and confirm it runs. Fix the final-screen overflow (smaller type or paging or a slow scroll; keep every line of text). Add projector scaling. Add an instructor layer: `P` pause, `M` mute, number keys `1`–`5` jump straight to that level's briefing (and `0` to the final screen) behind a modifier or a hidden toggle so students do not stumble into it, and `R` restart the current level.

**P1 — Sound.** Synthesized with the Web Audio API, no audio files, NES-style square/noise voices: jump, stomp, hit, death, bullet, dog bark on charge, briefing typewriter tick, a short victory sting on each target kill, and something quiet and wrong for the final screen (a held tone, or silence after the last line). Respect mute. Audio must start only after a user gesture.

**P2 — Make the kill and the reveal land.** A beat on each target kill (freeze frame, sting, the "TARGET ELIMINATED" card). On level 5, the target should be visibly the player: same sprite, same colors, resolving from a silhouette with "?" as the player approaches, and the player's controls perhaps slowing as they close in. The final screen could bring back the title screen's Chancellery silhouette. John's design note from March: "Students will feel it before they can articulate it." Keep it short.

**P3 — Variety.** Per-level platform layouts and enemy placements (data-driven `LEVELS[i].plats` / `.guards` / `.dogs`), and a modest difficulty ramp (more guards or shorter cooldowns in later levels), staying beatable by a non-gamer professor on a projector. Keep each run about 30 seconds; consider setting `TIME_LIM` to 30–40 per level as data.

**P4 — Comfort.** A "Classroom" difficulty toggle on the title screen (five hearts, slower bullets) beside "Standard." Remappable keys or at least both WASD and arrows (already present). Optional on-screen touch controls for tablets. Reduced-flash option.

**P5 — Credits screen (only with John's text).** A short "Sources and inspiration" screen after the final (xkcd #1063, "Wikihistory," the 1941 story) and course credit. Do not write citations yourself; ask John for the exact wording.

## 5. Constraints

Single self-contained HTML file. No libraries, no images, no external fonts (Courier New is fine). US English in all text ("organized," not "organised"; v1 already corrected). No analytics. Runs from `file://`. Sixty frames per second on a mid-range laptop; avoid per-frame allocation in hot loops if you add effects.

Do not change the meaning of any briefing line without John. You may fix line breaks and pacing.

## 6. Open questions to put to John at kickoff (with trade-offs)

Q1. Do the later levels stay in the 1933 Chancellery or move to each successor's world (for example, Himmler at SS headquarters on Prinz-Albrecht-Straße, Heydrich in Prague, Goebbels at the Propaganda Ministry)? Same setting: tighter loop, reads as "the same mistake again." New settings: more variety and more historical texture, but each needs an accurate year and place, and it changes the joke from repetition to escalation.

Q2. Sound style: chiptune stings (playful, risks levity at the end) or sparse, cold terminal sounds (on-tone, less fun). A hybrid is possible: playful during runs, cold in briefings and the finale.

Q3. Difficulty target: should John be able to finish it live on the first try in front of students (Classroom default), or should it be a little hard so students want to play it themselves afterward?

Q4. The player gun was deferred "for now" in March. Still no gun? (Adding one shifts the platformer toward violence-as-fun and away from the "you keep winning and it keeps getting worse" point.)

Q5. Succession accuracy: Himmler is the first successor in the briefing; in 1933 the obvious successor would have been Göring. Leave as deliberate escalation, add a one-line acknowledgment, or insert Göring as an extra loop?
