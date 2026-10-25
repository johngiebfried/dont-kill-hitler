# Don't Kill Hitler — web edition

A scrolling essay on game-based learning, with two playable games and a debrief. Built from the March 2026 classroom materials for *Game Design and Interactive Storytelling* (University of Vienna, 070172).

```
index.html              The essay: the question → why this topic → two comics, two stories → four questions → play → debrief → theory
assets/                 Comics and cover from the class source packet (see credits in the essay footer). doubt-creeps-in-vertical.jpg is a stand-in until the Tapas file arrives
platformer/index.html   The platformer, single self-contained file (built from index.src.html)
card-game/index.html    Mission Dossiers walkthrough (built from index.src.html + data/cards.json + tools/ce_mapdata.json)
card-game/data/cards.json   Canonical card text (approved copy; edit only with John's approval)
tools/inline_cards.py   Rebuilds card-game/index.html (inlines the card text and the table-mat map grid)
tools/build_platformer.py   Rebuilds platformer/index.html (inlines the conquest-map data)
docs/                   The March handoff, verbatim
REVIEW_NOTES.md         Decisions made on John's behalf, open questions, things to verify
```

## Run it

Double-click `index.html`. Everything works from `file://`, from GitHub Pages, or as a published claude.ai artifact. No build step is needed to play. The only external requests are Google Fonts (essay and card game); without a connection the pages fall back to system serif and sans fonts.

The games open in an overlay on the essay and send the reader back to the debrief when they finish. Each also runs on its own.

## Platformer (`platformer/`)

Version 3 (October 2026). Five runs, each a decade later and a world worse:

| Run | Year | Target | World |
|---|---|---|---|
| 1 | 1933 | Hitler | The Reich Chancellery, the Reichstag burning in the windows (placed there ahistorically, by choice) |
| 2 | 1943 | Himmler | Prinz-Albrecht-Straße 8: a vertical climb through card-index floors, with a paternoster lift |
| 3 | 1953 | Goebbels | The Babelsberg film lot: painted London, New York and countryside sets, flats that topple, a cardboard moon |
| 4 | 1963 | Speer | Germania finished, the von Braun rocket port, a launch, then a low-gravity moon base |
| 5 | 1933 | Agent 001 or Hitler | The Chancellery again, silent and frozen. Go left to stop your first self, or right to kill Hitler again |

Between runs: **Standing Order 1147** (the rules: the Directorate stands outside time, the machine is one way, every insertion leaves a ten-year wake), **Temporal Analysis** (a conquest map flickering between the real 1942 high-water mark and the new timeline, plus a ledger that grows a row each run), **Insertion Windows** (the wake diagram), and the **recovered lunar machine** that can reach 1933. Each exit of the last run ends in a short post-script of questions for the debrief. Nothing the player chooses is recorded.

- **Build:** edit `platformer/index.src.html`, then run `python3 tools/build_platformer.py`, which inlines the land-mask map data from `tools/mapdata.json`. The built `index.html` is still one self-contained file. `tools/make_mapdata.py` regenerates the map grid (needs the `global-land-mask` package).
- **Classroom layer:** Classroom mode is the default (five hearts, slower bullets, more time); Standard is the March difficulty. Instructor keys: `P` pause, `M` sound, `R` restart the run, `Shift+1`–`Shift+5` jump to a briefing, `Shift+6` the rocket launch, `Shift+0` the ending. After three deaths on a run, `S` skips ahead.
- **Carried over from v2:** procedural pixel sprites, dynamic lighting, crisp HTML text, synthesized sound, projector scaling, touch controls, fixed-step physics.

## Card game (`card-game/`)

Version 2 of the walkthrough (October 2026) plays a whole game at a table of four: four qualifying rounds, the field, the final, and card 40.

- **Cards lie face up, name side showing.** The mission and complication are on the other side. You choose by name and only read a card once you've picked it up.
- **Snake draft.** Picks go around the table and back (1-2-3-4, 4-3-2-1). Your first pick is in your hand; on your second you read both, keep one, and put the other back face up for the agents after you. First pick moves one seat each round, so at a table of four everyone goes first once. With seven agents ten cards still suffice, because every second pick returns a card.
- **Nothing is secret.** The table sees every pick and every put-back.
- **Card 40 is held back.** After the Round IV draft, GÖTTERDÄMMERUNG is offered to one agent at random, who may swap it for the card they kept.
- **One look per round, with a table mat that maps the round's places:** I Vienna Secession (Central Europe, 1848–1913), II field telegram (Vienna to the Western Front, 1907–1919), III Bauhaus (Munich to Berlin, 1919–1933), IV Allied intelligence file (Europe, 1933–1945). Round IV borrows the opponents' look on purpose.
- **Round I is played in full** (draft, pitch with an advisory clock, cross-examination, all pitches, your ballot, the count). Rounds II–IV go draft → ballot → count. Then the field (round winners, the wildcard, the pass-off, with your own choices if you won more than one round), the final ballot, and the result.
- The other agents' picks and ballots are random and labeled as samples. "Let the table play this round" and "Sample ballot for me" skip ahead. The software never judges an argument.

To change card text: edit `card-game/data/cards.json`, then run `python3 tools/inline_cards.py`. Card text on screen is checked byte-for-byte against the JSON in testing. The table-mat land grid is `tools/ce_mapdata.json` (regenerate with `tools/make_mapdata.py`).

**Card data changelog.** October 2026: duplicate names split for the face-up draft (John approved the split; the names are mine and need his OK). Card 2 CRADLE → FOUNDLING, card 3 CRADLE → LODGER, card 13 STILL LIFE → BUENOS AIRES, card 14 STILL LIFE → COMMISSION. Cards 1 and 12 keep their names. A new `series` field keeps the family on all six. No mission, complication, or variant text changed.

Not built yet: the Table Host mode for running a real class (pass-and-play, undo), print pages for a face-up deck, phone ballots. The spec for those is in `docs/02_CARD_GAME_SPEC.md`.
