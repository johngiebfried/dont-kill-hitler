# Card Game Spec — "Don't Kill Hitler: Mission Dossiers" (web edition)

Owner: Session B. Folder: `card-game/`. Card text: `cards.json` (do not edit). Look and feel: `reference/dkh_printable_cards.html` and `reference/dkh_rules_sheet.html`.

## 1. What the web version is for

The physical game is a debate. People talk; the cards prompt them; the table votes. The web version exists to make that easy to run in a classroom without printed cards: dealing, private hands, timers, secret ranked ballots, scoring, advancement to the final, the pass-off rule, and a clean results screen that John can project for the debrief. It also replaces the print run with a printable deck generated from the same data.

The software never judges arguments, never suggests which plan is better, and never adds historical commentary to cards. It is a game master, not a participant.

## 2. Canonical rules (as decided by John, March 2026)

**Premise.** Every player is a field agent of the Temporal Intelligence Directorate. Each has built a one-use, one-way time machine. There is one funding slot. You must convince the room your mission deserves it.

**Players.** Ideal 4–7. Playable with 3, in which case each voter ranks only one pitch (a single vote worth 1 point; see 2.6). Above 7 is out of scope for v1.

**Structure.** Four qualifying rounds, then a final. Round 1 uses only Phase I cards (Childhood, 1848–1913), Round 2 only Phase II (Young Adulthood, 1907–1919), Round 3 only Phase III (Rise to Power, 1919–1933), Round 4 only Phase IV (In Power, 1933–1945). Each phase deck has ten cards. Phases are kept separate so players compare like with like.

**2.1 Draw.**
Groups of 3–5: at the start of the round every player draws 2 from that phase's deck, chooses 1 to play, and discards the other face-down (out of the round).
Groups of 6–7: ten cards cannot cover everyone's two-card draw, so players draw in turn around the circle. Each player draws 2, keeps 1, and the discard is shuffled back into the phase deck before the next player draws.
Cards a player keeps are hidden from others until that player pitches (sequential reveal).

**2.2 Pitch.** In seating order, each player reveals their mission and has 2 minutes to argue it: why it works, and what the resulting timeline looks like. No notes. Improvised.

**2.3 Cross-examination.** After each pitch, any one other player may ask the presenter one question (hostile is fine). The presenter must answer. Budget 1 minute.

**2.4 Voting criteria** (shown on screen during voting, wording exact):
1. Which plan successfully stops Hitler without producing an equal or greater catastrophe?
2. Which plan requires the least moral compromise from the agent carrying it out?

**2.5 Ranking.** Each player ranks the other players' pitches: 3 points to first, 2 to second, 1 to third. No self-voting. A strong plan on only one criterion should not win; that guidance appears on the voting screen.

**2.6 Small tables.** With 3 players each voter has only two others to rank; John's rule is "rank 1": each voter picks a single favorite. Default scoring for that case: 1 point (see open question Q4). With 4 players each voter ranks all three others (3/2/1).

**2.7 Advancement.** The highest scorer of each qualifying round advances to the final with the card they won with. After Round 4, the highest-scoring non-qualifier (cumulative across all four rounds) advances as the wildcard, with the card from their best-scoring round. Target: five finalist slots.

**2.8 Ties.** If two players tie for a round's top score, both preliminarily advance. When the final field is settled, the final cut is made so that as many different players as possible have a card in the final. Last resort: coin flip (the app does a visible, animated random draw).

**2.9 Multiple qualifiers and the pass-off.** A player who won more than one round holds more than one qualifying card but may argue only one in the final. For each extra card they choose: discard it from contention, or pass it to any player who is not otherwise in the final. If a passed card wins the final, the original holder scores half the winner's final points and is credited as co-architect.

**2.10 The final.** Each finalist re-argues their qualifying mission (same pitch and cross-exam timings unless John sets otherwise). All players vote, finalists included, ranking the finalists 3/2/1 with no self-voting. Highest total wins.

**2.11 Let-go.** End screen carries the rules sheet's footer: "The machine is one way. Once you argue it, it's argued. Leave it on the table when you walk out."

## 3. Rules ambiguities and the defaults to use

These came up in the March chat and were never fully closed. Use the default, make it a setting where noted, and list your choices for John at kickoff.

| # | Ambiguity | Default | Setting? |
|---|---|---|---|
| A1 | Rank after each pitch, or after all pitches in the round? The rules sheet says "after each pitch," but ranking 3/2/1 requires seeing all pitches. | Vote once, after all pitches in the round. | No |
| A2 | Number of rounds. The rules sheet and John's later rules say four qualifying rounds plus a final. Card 40's complication says "three rounds of your fellow agents," and one chat message said "after three rounds." | Four qualifying rounds plus final. Flag card 40's wording to John (it is in `03`). | Yes: 3 or 4 qualifying rounds |
| A3 | Wildcard basis: cumulative points across all rounds, or best single-round score? | Cumulative. | Yes |
| A4 | Who may receive a passed card? | Any player not already arguing in the final. | No |
| A5 | Can finalists vote in the final? | Yes, with no self-vote (the rules sheet says "all players"). | No |
| A6 | Cross-exam: who asks? | The app shows "Any agent may ask one question"; optionally a "random interrogator" button picks someone. | Toggle |
| A7 | Timers: enforced or advisory? | Advisory: visible countdown, soft chime at zero, presenter can be cut off with one click. Never auto-skips. | Durations editable (default 2:00 / 1:00) |
| A8 | Are discarded cards public? | No. Show only the played card. Reveal all hands in the post-game debrief view. | No |
| A9 | Card 40 (Götterdämmerung) is a meta-card. Dealt normally or treated specially? | Dealt normally from Phase IV. Optional setting "Guarantee Götterdämmerung in Round 4" deals it to a random player as a third option. | Toggle |

## 4. Modes to build

**4.1 Table Host (required, build first).** One device, usually John's laptop on the projector, sometimes passed around. This is the whole game in v1.

Flow:
1. Setup: enter 3–7 agent names (code names encouraged; offer a "generate code names" button with TID-style names), seating order, settings (A2, A3, A6, A7, A9).
2. Round intro: phase title, years, a one-line TID briefing note per phase (write new copy in the established register; keep it short).
3. Private draw: for each player, a privacy screen ("Pass the device to Agent X. Others look away.") then their two cards side by side; they tap one to keep. For 6–7 players, implement the sequential shuffle-back rule exactly.
4. Pitch loop: presenter's card shown full-screen in the dossier style, large enough to read on a projector; 2:00 timer; then cross-exam 1:00 timer; next.
5. Ballot: pass-and-play secret ballot. Each voter sees all pitched cards for the round except their own and orders their top three (drag or tap 1st/2nd/3rd). Criteria visible on the ballot. Confirmation, then privacy screen for the next voter.
6. Round results: points per player this round, cumulative standings, round winner(s), tie handling.
7. After the last qualifying round: wildcard reveal, tie resolution (A-rule then coin flip), pass-off decisions for any multi-qualifier, final roster.
8. Final: same pitch and ballot loop with finalists' cards.
9. End: winner, co-architect credit if a passed card won, full scoreboard, and a debrief view listing every card played by round with who played it and its points (the thing John projects for discussion). The let-go line.

State must survive an accidental reload (persist to `localStorage`, wrapped in try/catch) and there must be "Undo last ballot" and "Abandon game" controls in a discreet menu.

**4.2 Deck Browser (required, small).** Browse all forty cards by phase, open any card large. Useful for teaching and for John to project a single card.

**4.3 Print (required, port).** Port `reference/dkh_printable_cards.html` and `reference/dkh_rules_sheet.html` into `card-game/print/`, rendering from the same card data. Keep the 2×2 Letter layout; add an A4 option (Vienna prints on A4) and optional cut marks. Update the rules sheet text to the canonical rules above where they differ (A1 in particular: "After all pitches in the round, rank the missions you did not argue").

**4.4 Phone Ballots (optional, later; ask John first).** Each student votes on their own phone via a room code. This needs shared state, so it means either a small backend or a hosting environment with shared storage (a published claude.ai artifact can keep shared state through its runtime capabilities). Out of scope until John asks; design the ballot component so it can be reused.

## 5. Visual and interaction design

Use the Diplomatic Dispatch system from the print reference: cream `#faf7f0`, navy `#1a2744`, dark red `#8b0000`, tan rule `#c8b89a`, muted brown text `#8b7355`, phase colors I `#6b4c2a`, II `#1a4a6b`, III `#2a5c3a`, IV `#6b1a1a`. Fonts: Playfair Display (operation names, headings), Libre Baskerville (body), Oswald (labels, small caps, buttons). Card anatomy: "Temporal Intelligence Directorate / Field Operations Division — Mission Dossier" header, "Operation" label, operation name, variant line, phase badge, MISSION section, COMPLICATION block with red left rule, footer "Series Γ · Card NN of 40 · For Authorized Eyes Only," faint crosshair watermark.

On screen the card must scale up. At projector size the mission and complication text should be readable from the back of a seminar room (roughly 28–32 px body text on a 1920-wide display). Provide a dark "projector" variant of the page background (the card itself stays cream).

Keyboard: Space starts/pauses timers, N advances, Esc opens the menu. Everything also works by mouse/touch.

Accessibility: sufficient contrast (the tan-on-cream labels in the print version are too faint for screens; darken them on screen only), visible focus, reduced-motion respected.

## 6. Data

Use `cards.json` as the single source. Fields: `id` (1–40, stable), `phase` (1–4), `op` (operation name, all caps), `variant`, `mission`, `complication`, optional `meta: true` (card 40). Phase labels and colors are in `_meta.phases`. Inline the JSON into `index.html` at build or by a tiny script so the game runs from `file://`. Keep a copy in `card-game/data/cards.json` as the editable source.

When John approves fixes from `03_CARD_DECK.md`, they are made in the JSON only, with a changelog entry in `card-game/README.md` naming the card id and the change.

## 7. Testing checklist

Simulate full games at 3, 4, 5, 6, and 7 players, including: a player winning two rounds (pass-off path, including the passed card winning and half-credit math); a three-way tie for a round; a tie for the wildcard; reload mid-ballot; undo last ballot. With 6–7 players, verify the phase deck never runs out under the shuffle-back rule. Verify card text on screen is byte-identical to `cards.json`. No console errors. Print preview of both print pages on Letter and A4 with no text overflow (the March deck fit at 6.8 pt body text; the longest cards are 13, 28, 30, and 40).

## 8. Open questions to put to John at kickoff (with trade-offs)

Q1. Primary mode. (a) Table Host only, pass-and-play ballots: zero infrastructure, works offline, slower with 7 players. (b) Table Host plus phone ballots: much faster voting and fully secret, but needs shared state or a server and adds failure points in class. (c) Display-only "facilitator board" (timers, scoring entered by hand after paper ballots): simplest, least immersive. Default: (a), designed so (b) can be added.

Q2. Hosting. GitHub Pages under John's account, a published claude.ai artifact, or both. Default: both, since the build is a single static file.

Q3. Round count (A2) and the card 40 wording: keep four qualifying rounds and edit card 40 to "four rounds," or keep the card and move to three qualifying rounds with Phase IV as the final's deck.

Q4. Three-player scoring: a single vote worth 1 point, or worth 3 so scores look comparable to larger tables.

Q5. Whether to show the TID briefing notes between phases (new copy) or keep the interface silent and let John narrate.
