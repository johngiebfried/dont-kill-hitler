# Context and Design History

Read this before touching either game. It explains why the games exist, what argument they make, what was tried and rejected, and the sensitivity rules that govern every design decision.

## 1. The course

*Game Design and Interactive Storytelling* (University of Vienna, MA Digital Humanities, course 070172, Summer Semester 2026; 25 Vienna students meeting in the GameLab, plus a small Tel Aviv University cohort). Instructor: John Giebfried, a historian (medieval diplomatic history, Reacting to the Past designer). Co-instructor: Dr. Ahuva Liberles, TAU.

The course's thesis: games are arguments; design decisions are scholarly decisions; and AI collapses the production gap but not the design gap. The consistent session structure is play first, debrief second, theory third.

The two Don't Kill Hitler games were the subject of the March 9, 2026 session ("games as arguments / essential experience"). The week before had introduced MDA (Hunicke, LeBlanc and Zubek 2004) and procedural rhetoric. The session after these games turned the two into a case study of where MDA works and where it breaks (see section 5).

A note on the Holocaust constraint. The partnered TAU course *Reacting to a Jewish Past* explicitly avoided the National Socialist period, because neither instructor specializes in it and because of the period's weight for both Israeli and Austrian students. John knowingly made an exception for these games and said so in the planning chat: the games are about the time-travel trope and historiography, not about depicting the Holocaust, and Vienna students carry enough background knowledge to play. That exception is the reason the sensitivity rules below are strict.

## 2. Origin story (in John's framing for students)

John remembered a comic he had seen a decade earlier in which someone goes back to kill Hitler and things get worse. Looking for it, he found more: xkcd #1063 (the agent who arrives in the bunker just as Hitler shoots himself), a 1941 pulp story, "I Killed Hitler" (described in John's notes as from *Weird Tales*), the short story "Wikihistory" (time travelers on a forum trying to stop newcomers from killing Hitler; usually credited to Desmond Warzel, 2009, though the planning chat calls it "the Abrams story," so check the Google Doc before citing it in any credits screen), and a cultural-history essay tracing the "kill Hitler" trope through Great Man theory, structuralism, the Baby Hitler thought experiment, and the Novikov self-consistency principle. He gathered these in a Google Doc for students (not included here). The "first rule of time travel: don't kill Hitler" is the joke and the thesis.

He built two games from this. The platformer is the direct response to the comic and was presented honestly to students as a few-hours proof of concept, a show-piece of what can now be made quickly. The card game is the real design work.

## 3. The argument both games make

The core historiographical debate is Great Man theory against structural explanation. Would removing Hitler have changed anything, or would the conditions that produced him have produced someone else, possibly worse? A secondary debate runs through the card game: nature against nurture (was the monster made or born?). A third, the card game's moral axis, asks what the agent personally has to do and whether they can defend it.

The two games argue this in opposite ways, and that contrast is pedagogically deliberate.

The platformer argues it through content. Its mechanics are generic platformer verbs (run, jump, stomp, timer). The thesis lives in the briefing text, the succession of replacement targets, and the bootstrap-paradox ending. John's own line for class: it is "an illustrated lecture with jumping in it," and that is the point of comparison.

The card game argues it through mechanics. The cross-examination question, the two voting criteria, and the comparative ranking force players to construct the structuralist counterargument against each other in real time. Remove the rules and there is no argument.

Any web adaptation must preserve this contrast. Do not bolt a lecture onto the card game, and do not try to make the platformer's mechanics "carry" the argument by adding systems; that would erase the comparison John teaches with.

## 4. Design history and decision log

### 4.1 Card game

The chat that produced it ran from late February to mid-March 2026. The key decisions, in order:

The first concepts were a platformer in which you play Hitler's bodyguards (rejected: players identifying with Hitler would distract from the learning and create friction, especially with Israeli students) and a social-deduction game with "temporal police" against agents on secret missions. Claude pitched three alternatives ("Baby Hitler" party game, "Wikihistory" forum social-deduction game, "The Competent Dictator" strategy game). John chose a competitive debate party game in the Baby Hitler vein: a central deck, everyone draws, everyone tries to convince the table their plan is best, judged on probability of success and on the quality of the resulting timeline. The second, digital game was deferred.

Scoring went through three versions. A bidding-token system (players wager 1–5 on each pitch) was dropped as too fiddly. Simple fund/reject votes were considered. John settled on ranked voting: after each round every player ranks their top three other pitches, 3/2/1 points, no self-voting.

Framing became a spy dossier. LLM-generated card brainstorms (John ran the same prompt across several models) were clustered; the spy-dossier tone won over academic, informal, and Cards-Against-Humanity registers. Everyone is a field agent of the Temporal Intelligence Directorate (TID) competing for one remaining insertion. Sequential reveal (each mission revealed when argued) was chosen over simultaneous reveal. A "Structuralism veto" was proposed and rejected by John.

Organizing principle: phases of Hitler's life, not tone categories. John's hard rule: every plan must either kill Hitler directly or prevent him from consolidating power. He cut cards he disliked (the Reichstag vote, the Polish Corridor). Popular targets get two or three variants that imply different theories of causation (three Cradle variants: kill the infant, extract him to a Jewish family in Vienna's Leopoldstadt, stay and raise him yourself since the machine is one way; three art-school variants). He later added "world cards" that change Hitler's environment rather than Hitler (Sarajevo, the sealed train, Versailles, Lueger, the 1848 crown).

Card format: only MISSION and COMPLICATION, each short. The challenge question lives inside the complication. Earlier "classification" tags (ALPHA/BETA/GAMMA) and asset/window fields were dropped as too wordy for a printed card. Titles must be playful, not "too seriously German." No duplicate operation names. The agent can never replace a historical person; they can only persuade, bribe, or position themselves (for example, you brief Jesse Owens; you are not Jesse Owens; you persuade Georg Elser; you are not Elser).

Ten cards per phase for version one (forty total). The bunker card, Operation Götterdämmerung, was rewritten at John's insistence into a meta-card: its mission is to make sure nothing changes, and its complication puts the whole evening's exercise on trial.

External review: John sent the full deck to several other LLMs for fact-checking and design review. The consolidated changes he accepted produced v3 (replace the portfolio-sabotage card with a Buenos Aires scholarship ticket; replace the Reichstag-fire "inside job" variant with Versailles/Keynes; reframe Jesse Owens away from personal sacrifice toward the propaganda showcase; reframe Ballot Box as advising Schuschnigg to move the vote up; nuance the two France cards; keep Schicklgruber as "a joke with an air of seriousness"). Some of the reviewers' "corrections" were themselves wrong; see the flags in `03_CARD_DECK.md`.

Voting criteria: John reduced three proposed criteria to two. (1) Which plan successfully stops Hitler without producing an equal or greater catastrophe? (2) Which plan requires the least moral compromise from the agent carrying it out?

Visual design: five mockups (Cold War Classified, OSS Field Manual, Teletype, Diplomatic Dispatch, Weimar Document). John chose Design 4, Diplomatic Dispatch: cream paper `#faf7f0`, navy `#1a2744`, dark red `#8b0000` complication rule, Playfair Display / Libre Baskerville / Oswald, faint crosshair watermark, phase color strip and badge (Phase I `#6b4c2a`, II `#1a4a6b`, III `#2a5c3a`, IV `#6b1a1a`). Printed 2×2 on US Letter. A one-page rules handout ("Mission Briefing & Field Protocols") uses the same system and ends with the let-go line: "The machine is one way. Once you argue it, it's argued. Leave it on the table when you walk out."

### 4.2 Platformer

Claude pitched three digital projects doable in about a day (a CRT text adventure, a side-scroller "where winning is the problem," and an AI-powered dossier console). John chose the side-scroller and specified the plot himself: 1933, Hitler has just taken power; run the Reich Chancellery, dodge guards who shoot and dogs that patrol and charge; kill Hitler; Himmler took over; kill Himmler; Heydrich, worse, rules; kill Heydrich; Goebbels rules; then go back and kill your past self, so Hitler comes back. Levels around thirty seconds. No player gun.

Playtesting with John drove the difficulty changes: bullets slowed from 4.6 to 1.8 px/frame, guards cut from ten to five, shooting cooldown roughly tripled, platforms recolored for visibility, Mario-style stomping added after John kept dying, and finally three hit points with invincibility frames. A syntax error introduced during patching was fixed. A handoff document for Opus was written but, as far as the record shows, no further development happened. The v1 in `reference/` is that final state.

The CRT green-on-black terminal look is the platformer's own identity and differs from the card game's paper dossier look on purpose. Both share the TID fiction.

## 5. How John teaches with the pair (MDA framing)

This shapes what the web versions must preserve. In class he planned to play the card game first without theory, then introduce MDA, then run MDA on both games. The card game's mechanics produce dynamics (players pre-building counterarguments, cross-examination exposing what the pitcher suppressed, alliance calculus around the pass-off) and an aesthetic John calls "productive argumentative failure," which is not in MDA's eight-aesthetic taxonomy. The platformer's MDA analysis stops at Challenge and Fantasy; strip the text and it is a generic runner. MDA's claim that "the content of a game is its behavior, not the media that streams out of it" fits the card game and fails the platformer. His closing line for students: "If the argument only works when you explain it, it isn't in the game yet."

So: the web platformer should get better at being a platformer and at delivering its text, but it should not quietly acquire mechanics that encode the argument. The web card game should be a facilitation tool for humans arguing, not a substitute for arguing.

## 6. Sensitivity rules (non-negotiable)

No swastikas, SS runes, or other Nazi insignia in any asset. Uniforms and banners stay abstract. Nazi leaders appear only as small, non-heroic pixel targets in the platformer and by name in card text; no portraits, no photographs, no speeches or slogans.

No depiction of Holocaust victims, camps, deportations, or atrocity imagery. Cards that name the Holocaust (Wannsee, Briefcase, Last Train-type arguments) do so in text the players read; the software never illustrates them.

Humor targets the agents, the plans, and bureaucracy. Never victims. Never Jewish characters as props.

The Jesse Owens card was flagged by an external reviewer for burdening a Black athlete with stopping the Holocaust. John kept it after the reframe to the propaganda showcase. The web version presents it exactly as the text reads, with no illustration of Owens.

Player-facing content must not drift into glorifying any intervention as "the right answer." The game never scores historical correctness; humans vote.

No external analytics, tracking, or data collection. Classroom use only.

## 7. Voice and tone

TID flavor text is dry, bureaucratic, faintly funny, never winking. The recurring lines ("The machine is one way. Plan accordingly." / "The Temporal Intelligence Directorate accepts no responsibility for paradoxes, alternative timelines, or the personal consequences of spending thirty years raising Adolf Hitler.") are approved and can be reused. New UI copy should be short and in that register. Avoid AI-sounding filler.

## 8. Known stale sources

The Moodle post written in March describes the deck with the wrong phase names ("Pre-WWI, Weimar/Interwar, Early Nazi Rule, War/Holocaust") and quotes card titles that do not exist in the final deck. Ignore it. The canonical sources are `cards.json` and `02_CARD_GAME_SPEC.md`.
