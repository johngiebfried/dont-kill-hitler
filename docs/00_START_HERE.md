# Don't Kill Hitler — Web Build Handoff (start here)

This folder hands two related games to Claude Code so they can be rebuilt as web games, in parallel, by two separate sessions. Both games were designed in February–March 2026 by John Giebfried (University of Vienna, Digital Humanities) for his graduate course *Game Design and Interactive Storytelling* (co-taught with Dr. Ahuva Liberles, Tel Aviv University). Both were played in class on March 9, 2026. The card game existed only on paper; the platformer existed as a rough single-file demo. The job now is to turn both into polished, shareable web games.

Read this file first, then `01_CONTEXT_AND_DESIGN_HISTORY.md`. After that, each session reads only its own spec.

## The two games in one paragraph each

**The platformer ("Don't Kill Hitler" side-scroller).** A three-to-five-minute browser game. You are a temporal agent sent to 1933 Berlin. You run through the Reich Chancellery past guards and dogs and kill Hitler. Himmler takes over. Go back, kill Himmler. Heydrich takes over. Kill Heydrich. Goebbels. Then the briefing says the paradox has been traced to its source: the target is you. You kill your past self, the loop closes, Hitler never died, history proceeds as written. The ending is the argument. Spec: `04_PLATFORMER_SPEC.md`. Working v1: `reference/dkh_platformer_v1.html`.

**The card game ("Don't Kill Hitler: Mission Dossiers").** A competitive debate party game for 4–7 players (3 playable). Everyone is a temporal agent with a one-way, one-use time machine; one mission gets funded. Four qualifying rounds, one per phase of Hitler's life (Childhood, Young Adulthood, Rise to Power, In Power), ten mission cards per phase. Each player draws, picks a mission, pitches it for two minutes, survives one hostile question, and the table ranks the pitches 3/2/1. Round winners plus a wildcard reach the final. The last card in the deck, Operation Götterdämmerung, asks the player to argue that the timeline should not be changed at all. Spec: `02_CARD_GAME_SPEC.md`. Card text: `03_CARD_DECK.md` and `cards.json`. Print reference: `reference/dkh_printable_cards.html`, `reference/dkh_rules_sheet.html`.

## File index

| File | What it is | Who reads it |
|---|---|---|
| `00_START_HERE.md` | This file: plan, repo layout, shared rules, kickoff prompts | Both sessions |
| `01_CONTEXT_AND_DESIGN_HISTORY.md` | Course, thesis, origin story, decision log for both games, tone rules, sensitivity rules | Both sessions |
| `02_CARD_GAME_SPEC.md` | Canonical rules, scoring edge cases, web adaptation spec, UI flow, open questions | Card-game session |
| `03_CARD_DECK.md` | All 40 cards, human-readable, plus fact-check flags awaiting John's decision | Card-game session (and John) |
| `cards.json` | Same 40 cards as data. Canonical text. | Card-game session |
| `04_PLATFORMER_SPEC.md` | Architecture of v1, constants, known bugs, prioritized roadmap | Platformer session |
| `reference/dkh_platformer_v1.html` | The playable March build (all in-chat patches applied, smoke-tested) | Platformer session |
| `reference/dkh_printable_cards.html` | Printable deck in the approved "Diplomatic Dispatch" style; renders from the same JSON | Card-game session |
| `reference/dkh_rules_sheet.html` | One-page rules handout as students saw it | Card-game session |

## What "in parallel" means here

Two Claude Code sessions, one per game, running at the same time on separate branches (git worktrees work well), each owning exactly one directory. They share nothing at runtime. The only shared things are this documentation and the visual vocabulary (the Temporal Intelligence Directorate fiction), and neither session edits the other's folder. A third, tiny step at the end adds a hub page linking both, so John can open them side by side in class.

Suggested repository layout:

```
dont-kill-hitler-web/
  index.html            ← hub page, written last (two big buttons: "Platformer", "Card Game")
  docs/                 ← this handoff folder, copied in verbatim (read-only for both sessions)
  platformer/           ← owned by Session A
    index.html
    README.md
  card-game/            ← owned by Session B
    index.html
    data/cards.json
    print/cards.html    ← print deck (port of reference/dkh_printable_cards.html)
    print/rules.html
    README.md
```

## Rules that bind both sessions

Each game ships as a static site with no server, no build step required to play, and no external runtime dependencies beyond Google Fonts. It must open by double-clicking `index.html` (so no `fetch()` of local JSON on `file://`; inline the data or use a script that writes it into the HTML). It must also run unchanged from GitHub Pages or as a published claude.ai artifact.

The classroom is the target. That means it must work on a projector at 1920×1080 and on a laptop at 1366×768, keyboard-first, with a visible way to reset. Mobile is nice to have for the card game and optional for the platformer.

Write all player-facing text in US English (organized, honor, color, authorized). The March files had UK spellings in places; the reference files in this folder have already been corrected, so do not reintroduce them.

Historical accuracy outranks convenience. John is a historian and will check. Do not invent facts in flavor text. Card text in `cards.json` is approved copy: do not rewrite it, shorten it, or "improve" it. Where you believe a card is wrong, the fix goes through the flags in `03_CARD_DECK.md`, which John decides.

No swastikas or other Nazi insignia anywhere, in sprites, banners, or UI. The platformer's banners are deliberately an abstract red roundel. No Holocaust imagery, no victims depicted, no humor at the expense of victims. The comedy in both games comes from the absurdity of the agents' plans and from bureaucracy, never from the persecuted. The full sensitivity rules are in `01`.

The argument is the product. When a mechanic, polish feature, or difficulty choice competes with the argument landing, the argument wins. For the platformer, the ending must stay legible to someone who has never played a video game. For the card game, the software must never decide who argued best; humans vote.

Before building anything substantive, each session should present John with two or three options and their trade-offs for its open questions (listed at the end of each spec) and wait for his choice, unless he has told you to proceed on the defaults. This is how he works.

## Kickoff prompt — Session A (platformer)

> You are rebuilding the "Don't Kill Hitler" platformer as a polished web game. Read `docs/00_START_HERE.md`, `docs/01_CONTEXT_AND_DESIGN_HISTORY.md`, and `docs/04_PLATFORMER_SPEC.md`, then open `docs/reference/dkh_platformer_v1.html` and play it in a browser. You own only `platformer/`. Start by copying v1 into `platformer/index.html` unchanged and confirming it runs. Then present the open questions at the end of the spec to me as options with trade-offs. After I answer, work through the roadmap in priority order, committing after each item, and keep the game a single self-contained HTML file. Do not touch `card-game/`.

## Kickoff prompt — Session B (card game)

> You are building a web version of the "Don't Kill Hitler" debate card game. Read `docs/00_START_HERE.md`, `docs/01_CONTEXT_AND_DESIGN_HISTORY.md`, `docs/02_CARD_GAME_SPEC.md`, and `docs/03_CARD_DECK.md`. Card text comes from `docs/cards.json` and must not be edited. Visual style comes from `docs/reference/dkh_printable_cards.html`. You own only `card-game/`. Before writing game code, present me the open questions at the end of `02_CARD_GAME_SPEC.md` as options with trade-offs, and list the rules ambiguities with the defaults you intend to use. After I answer, build the Table Host mode first, then the print pages, then anything optional. Do not touch `platformer/`.

## Definition of done (both)

The game runs from `file://`, GitHub Pages, and as an artifact. A full playthrough works start to finish with no console errors. John can reset at any point. Every player-facing string is US English and matches the approved text. A short `README.md` in each folder explains how to run it, how to change content, and what was changed from the March version and why.
