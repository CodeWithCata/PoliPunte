# PoliPunte — MASTER BUILD PROMPT (paste this into a new Claude chat, with the attachments)

> How to use: open a new chat, attach the files listed in the README of this pack, then paste everything below the line.
> Everything the website shows to users must be in **ROMANIAN**. This prompt is in English only for you (Claude).

---

# ROLE

You are a senior product designer + front-end engineer + conversion-copy writer building a contest-winning web prototype. You care equally about (1) a flawless, polished user experience, (2) strict factual and ethical correctness, and (3) a prototype that works on the first try on a phone. You write excellent Romanian.

# THE CONTEST (why this matters)

I am competing in the **AI-Powered Business Challenge 2026** (Start Your StartUP, POLITEHNICA București), high-school (Elevi) section. The team has **3 hours in total** to deliver a web prototype + strategy + financial model + promo material + AI journal + pitch. I am **Member 1 — Product & Development Lead**: I deliver the web prototype. Two teammates handle strategy/finance and marketing/pitch.

The challenge theme is "AI for Good — Un loc în cămin poate schimba un destin!" for **Fundația HIPOLITECH** (POLITEHNICA București foundation), which wants to attract **private funding for a new student dormitory**.

How we are judged:
- Preselection: AI-assisted scoring + a human committee that verifies "proof of functioning". Rubric: **App & user experience 35**, Strategy & financial model 25, Critical use of AI 15, Promo material 15, Pitch 10. Minimum 60 points, top 10 teams advance.
- Tie-break: the **application score decides first**.
- Final: 3 minutes pitch + live demo, 2 minutes of jury questions (5 business jurors). Final rubric: App & demo 30, Strategy & model 30, AI understanding 20, Presentation 20.
- The app does **not** need runtime AI. The organizers also evaluate how AI was used to build it.
- **Presenting features or results that do not exist is forbidden** and can lead to disqualification. Never claim in the UI, README or comments anything that is not actually implemented and working.

# ATTACHMENTS (read ALL of them before writing code)

1. The official challenge PDF (source of truth for the requirements).
2. My concept/specification PDF for the product, called PoliPunte (detailed spec: flow, fields, validations, brief structure, role matrix, Claims Guard, scale lens, ledger, test cases).
3. A file with the official facts about the campaign (use ONLY these for facts about the dormitory/campaign).
4. The contest regulation PDF, if attached.

If two documents conflict, the official challenge PDF and the regulation win over my concept PDF. Tell me about any conflict you find. Do not silently "fix" things.

# THE PRODUCT: PoliPunte

**One-line pitch:** PoliPunte helps a person inside a company (the "champion") turn interest in the HIPOLITECH campaign into a one-page internal brief that they can forward to the decision maker — with official facts, correct context for any amount, and no promises.

**Why this idea:** in the contest's reference scenario, 200,000 of the 250,000 lei target (80%) comes from 20 corporate sponsors. The user of the tool is usually NOT the decision maker; the brief is the bridge. This is the single "main web function" the contest allows.

**What it is NOT:** not a payment page, not a donation form, not a chatbot, no login, no backend, no real data. It is a clearly labeled **DEMO**.

# NON-NEGOTIABLE RULES (from the organizers — violating any costs points)

- Never say an amount "buys" a room, bed, place or square meter. Approved phrasing: "o contribuție la obiectivul comun de finanțare".
- Never promise or imply accommodation rights, reservations or priority. Donations do not grant housing.
- Never promise tax deductibility or any fiscal treatment; say it must be verified with the Foundation / a tax advisor.
- Never invent sponsors, partners, beneficiaries, testimonials or numbers. Use only fictional company names typed by the user.
- Never turn estimates/sketches into firm promises. The Foundation says technical details may evolve.
- Never confuse "pledged/committed" with "received". Never confuse ad views with donations.
- No payment processor, no card fields, no bank data, no personal IDs, nothing that imitates a real payment.
- Do not use official logos of the Foundation or the University as if they endorse the app. Include a footer note: prototype made for the contest, not officially affiliated.
- Link to the official Foundation page whenever relevant; never build a donate button of our own.
- Every number must carry a source badge (see "Source badges").

# OFFICIAL FACTS (put them in ONE config object in the code; nothing else may hard-code them)

- Initiator: Fundația Universității Politehnica din București – HIPOLITECH
- Campaign: „Un loc în cămin poate schimba un destin!"
- Goal: supporting the construction of a student dormitory through private contributions
- First stage estimate: **1.250.000 lei** — design, approvals and permits (estimate published by the Foundation)
- Total investment estimate: **100.000.000 lei** (estimate published by the Foundation)
- Priority beneficiaries: students with outstanding academic results and students who need financial support (per the public presentation)
- Official page: https://fundatia.upb.ro/proiecte-si-evenimente/un-loc-in-camin-poate-schimba-un-destin/
- If the attached facts file contains text copied from the official page, prefer that wording (paraphrase lightly, never present AI wording as official).

Contest assumptions (NOT Foundation commitments): fundraising target in the exercise **250.000 lei gross**; campaign budget **max 15.000 lei**; **6 months**. Reference scenario: 500 donors × 100 lei = 50.000; 20 sponsors × 10.000 lei = 200.000; gross 250.000; cost 15.000; remaining 235.000.

# SOURCE BADGES (visible everywhere a number or claim appears)

- 🟢 **OFICIAL** — from the official source / the Foundation's published estimates
- 🟡 **IPOTEZĂ CONCURS** — value imposed by the contest rules (250.000, 15.000, 6 luni, reference scenario)
- 🔵 **ESTIMARE ECHIPĂ** — our own judgement (role arguments, warning thresholds)

Implement as small pills with color + text label (never color alone). Include a legend on the intro screen.

# FUNCTIONAL SPEC

Single page, three states (Intro → Form → Result), no routing library. Target: a first-time evaluator understands it and gets a result in **under 60 seconds**.

## Persistent elements
- Top ribbon, always visible: **"DEMO — nu se efectuează nicio donație sau plată. Datele rămân în browser."**
- Footer: prototype for the contest, not officially affiliated; link to the official Foundation page; the source-badge legend.
- A collapsible box **"Cum testezi în 1 minut"** with 3–4 short steps and the two example buttons (so human and AI evaluators can verify instantly).

## Screen 0 — Intro
Title PoliPunte, one clear sentence of purpose, primary button "Începe", secondary link to the official page, legend of badges. A short "official facts" card (see config) with badge 🟢 and a note that estimates may evolve.

## Screen 1 — Form (all labels in Romanian)
Fields: 
1. **Numele companiei (fictive)** — required, 2–60 chars, at least one letter. Helper: "Folosește o companie fictivă. Nu introduce date reale."
2. **Domeniu** — optional select: IT, Industrie, Construcții, Servicii financiare, Retail, Energie, Altul.
3. **Persoana de convins** — required: Administrator / CEO, Responsabil CSR, Director financiar, Resurse umane.
4. **Interes principal** — optional, max 2 of: Educație și acces, Comunitate, Talente, Reputație.
5. **Contribuția orientativă (lei)** — required, integer.
Buttons: "Generează brief-ul", "Încarcă exemplu valid", "Încarcă exemplu invalid", "Resetează".

Valid example: company "Alfa Demo SRL", domain IT, role Director financiar, interest Talente, amount 10000.
Invalid example: empty name, no role, amount "zece mii".

### Validation (never produce a fake result from invalid input; show inline errors with aria-live; move focus to first error)
Amount: accept "10000", "10 000", "10.000" (strip separators).
- empty → „Introdu o sumă orientativă în lei."
- not a number → „Scrie suma ca număr întreg, de exemplu 10000."
- ≤ 0 → „Suma trebuie să fie mai mare decât 0."
- decimals → „Folosește un număr întreg de lei."
- > 100.000.000 → „Suma depășește valoarea totală estimată a proiectului (100.000.000 lei). Verifică cifra."
- > 1.250.000 and ≤ 100.000.000 → VALID + visible warning: „Suma depășește estimarea pentru prima etapă. Brief-ul se generează; modul în care ar fi folosită o astfel de contribuție se clarifică direct cu Fundația."
- < 1.000 → VALID + warning: „Pentru o sponsorizare corporate, suma este mică. Poate fi mai potrivită o donație individuală — vezi pagina oficială."
Other required-field messages: „Introdu numele unei companii fictive (minimum 2 caractere)." / „Alege rolul persoanei care decide." / more than 2 interests → „Alege cel mult două interese."
If optional fields are empty, still generate, with a visible note that arguments are general.

## Screen 2 — Result: "Brief intern" (one printable page, looks like a real document)
Sections (badges where relevant):
1. Header: "Brief intern: contribuție la campania „Un loc în cămin poate schimba un destin!"", company (fictive), date, DEMO mark.
2. Pe scurt (3 lines).
3. Fapte oficiale 🟢 (from config) + note: details may evolve during design.
4. De ce se potrivește companiei 🔵 — built from domain + interests; phrase as hypotheses to discuss ("poate fi relevant pentru că…"), never as facts about the company.
5. Argumentul pentru [rol ales] 🔵 — see role matrix.
6. Contribuția în context — the **scale lens** (below).
7. Obiecții probabile și răspunsuri factuale (3 for the chosen role).
8. Ce nu știm încă — to verify with the Foundation: tax treatment, forms of recognition (if any), contribution procedure, timeline.
9. Pași următori: 1) discuție internă, 2) cerere de discuție către Fundație prin pagina oficială, 3) clarificarea condițiilor în scris.
10. Notă de responsabilitate: demonstrativ; nu este angajament, nu este donație, nu conferă drept de cazare sau rezervare.
Actions: "Copiază textul", "Printează / Salvează PDF", "Copiază linkul testului", "Înapoi la formular", "Mergi la pagina oficială a Fundației" (opens official URL in a new tab, rel="noopener").

### Role matrix (write polished Romanian; all items are 🔵 hypotheses)
- **Administrator / CEO** — cares about reputation, coherence with values, risk. Core argument: campaign has a clear purpose (dormitory for high-performing students and students needing support) and a public, verifiable source. Objection "Ce primim în schimb?" → the prototype promises no benefits or rights; whether and what recognition exists is clarified directly with the Foundation.
- **Responsabil CSR** — strategy fit, reporting. Core: education and access as an involvement direction; public information to cite. Objection "Cum raportăm?" → ask the Foundation for the document confirming the contribution; the prototype issues no real documents.
- **Director financiar** — cost, structure, tax treatment, certainty. Core: clear official figures, the amount in context, an explicit list of unknowns. Objection "Se deduce fiscal?" → we do not claim it; verify with the Foundation and a tax advisor.
- **Resurse umane** — talent, relationship with the university. Core: link to POLITEHNICA as a source of graduates; shared interest in high-performing students. Objection "Angajații primesc ceva?" → no; a contribution grants no housing or other rights.
Each role gets 3 objections with factual answers; none may contain a forbidden claim.

### Scale lens (pure arithmetic, never called "impact")
For amount S compute: S/1.250.000 (🟢 base), S/100.000.000 (🟢 base), S/250.000 (🟡 base), S/200.000 (🟡 base, reference corporate target).
Display with Romanian formatting (dot thousands, comma decimals), 2 decimals; below 0,01% show "sub 0,01%"; above 100% show the real value with the note "peste baza de comparație". Always write the base next to each percentage. Wording: "reprezintă X% din estimarea publicată", NEVER "acoperă", "finanțează", "echivalează". Visual bars are allowed only with labeled bases.
Required check values: S=10.000 → 0,80% / 0,01% / 4,00% / 5,00%; S=50.000 → 4,00% / 0,05% / 20,00% / 25,00%; S=250.000 → 20,00% / 0,25% / 100,00% / 125,00%.

### Pledge vs received ledger
A small stepper: 1 Interes exprimat (demo) · 2 Discuție cu Fundația · 3 Acord semnat · 4 Sumă încasată. The prototype can only activate step 1 (button "Exprimă interes (demo)" — it just marks the state; no data is collected or sent). Steps 2–4 are greyed out with the label "în afara prototipului". Include the sentence: „Interesul exprimat nu este o promisiune și nu este o donație."

## Claims Guard (the differentiator — must really work)
A panel in the result with two modes:
1. **Auto-check of the generated brief**: runs the 7 rules over the brief text and shows "7/7 reguli respectate" (or lists violations). Rules: R1 no sum↔object equivalence; R2 no housing/reservation/priority promises; R3 no fiscal promises; R4 no invented sponsors/partners/beneficiaries; R5 no guarantees/superlatives; R6 no emotional pressure; R7 official source attached and figures labeled.
2. **"Verifică-ți propriul text"**: textarea where the user pastes a message. Normalize text (lowercase, strip diacritics) and match pattern families; highlight flagged expressions and show a suggested rewrite for each. Pattern families (extend sensibly):
 - R1: cameră/camere, pat, un loc, metru pătrat/mp, cumperi/cumpara, achiziționezi → „Suma reprezintă o contribuție la obiectivul comun de finanțare."
 - R2: rezervi, loc garantat, prioritate la cazare → remove; donations grant no housing rights.
 - R3: deductibil/deductibilitate, scutire, reducere de impozit, recuperezi taxe → „Tratamentul fiscal se verifică cu Fundația."
 - R5: garantăm, sigur, 100%, fiecare leu ajunge → „Contribuie la…"
 - R6: ultima șansă, fără tine, vor rămâne pe drumuri, dacă nu donezi → neutral factual tone.
 - R4: partener oficial, sponsor oficial, în parteneriat cu → „Parteneriatele se confirmă direct cu Fundația."
 It is lexical pattern matching, NOT AI; label it "verificator de formulări" and never call it AI. Show the empty-input case gracefully ("Lipește un text pentru a-l verifica").
Test: „Cu 10.000 lei cumperi o cameră și garantăm deductibilitate" must flag at least cumperi, o cameră, garantăm, deductibilitate.

## Other behaviors
- **Shareable test state in the URL query** (company, domain, role, interests, amount) so an evaluator can repeat the exact test; loading such a URL pre-fills and auto-generates if valid. Only fictional data is expected.
- **Built-in self-test**: opening `?selftest=1` runs assertions (parseAmount, validation cases, the three scale-lens check rows, Claims Guard test sentence) and shows PASS/FAIL clearly. Keep it small and real.
- **Print stylesheet**: hide ribbon/buttons, print only the brief on one A4 page.
- `<noscript>` message in Romanian.
- Language: `<html lang="ro">`, proper title/meta description/Open Graph title+description, inline SVG favicon.

# LANGUAGE & COPY (Romanian)

- All UI copy and generated brief text in natural, correct Romanian **with proper diacritics (ă â î ș ț)**. Use ș/ț (comma-below), not ş/ţ.
- UI addressed informally with "tu", short sentences, no jargon. The brief text itself is written in neutral, professional third person (it will be forwarded to a boss).
- Tone: factual, calm, warm. No emotional pressure, no exaggeration, no marketing superlatives.
- Use "Lucrurile de predat"-style plain Romanian; avoid odd calques ("livrabil", "glosar"); say "dicționar" if needed.
- Number format: 1.250.000 lei; percentages with comma (0,80%).
- Write the strings yourself, but run a red-team pass: search ALL user-visible text for forbidden claims (outside the Claims Guard pattern list and its tests).

# DESIGN DIRECTION (this is where the 35 points are won)

Goal: it must look like a polished, trustworthy product from a real design team — institutional credibility with modern editorial craft. Not a template, not a gradient-blob startup page.

- **Concept:** "the bridge" (puntea) between champion and decision maker. Use one elegant inline-SVG bridge/arch motif in the hero and as a subtle divider; no stock images, no external assets.
- **Palette (CSS variables):** deep navy primary (#14284B-ish), warm off-white paper background, one warm accent for the primary button (amber/coral), neutral grays. Badge colors: green / amber / blue pills exactly as above. Meet WCAG AA contrast.
- **Typography:** system font stack only (`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`) — no external fonts, no CDN, no libraries. Make it feel designed through scale, weight, tight letter-spacing on headings, generous line-height, `font-variant-numeric: tabular-nums` for figures.
- **Layout:** a 3-step progress indicator (Despre campanie · Datele tale · Brief-ul tău); cards with generous spacing and soft borders; on desktop the result is a two-column layout: the brief as a "paper document" on the left, a sticky side panel on the right with the scale lens (labeled bars), ledger and Claims Guard; on mobile everything stacks in a logical order.
- **Details that signal quality:** animated count-up for percentages, smooth section transitions, a subtle toast on copy, clear focus rings, hover/active states, a sticky bottom action bar on mobile, skeleton-free instant rendering. Respect `prefers-reduced-motion`.
- **Mobile-first:** perfect at 360×740 and 390×844; no horizontal scroll; tap targets ≥ 44px; form inputs use appropriate `inputmode` (numeric for the amount); no zoom-on-focus issues (inputs ≥ 16px).
- **Trust cues:** the DEMO ribbon, badges, official-source button, "Ce nu știm încă" section — make these look intentional and premium, not like disclaimers.
- Light theme is the priority; do not add a dark theme unless everything else is done and it is risk-free.

# TECHNICAL CONSTRAINTS

- **One file: `index.html`** (HTML + CSS + vanilla JS). No frameworks, no npm, no build step, no CDN, no external fonts or images, no network requests of any kind, no analytics, no localStorage/sessionStorage (state lives in memory and the URL query).
- Code structure inside the file: a `CONFIG` object (official facts, URLs, numbers, badge definitions), a `RULES` object (Claims Guard patterns + rewrites), a `TEMPLATES` object (roles, domains, interests, objections), and **pure functions** (`parseAmount`, `validate`, `scaleLens`, `buildBrief`, `checkClaims`, `encodeState`/`decodeState`) separate from rendering. Comment the code in English briefly.
- Semantic, accessible HTML: landmarks, labels tied to inputs, `aria-live` for errors/results, keyboard operable, visible focus, text content readable without JS interaction where possible (evaluators may be AI/automated). Don't draw text in canvas.
- Robust: handle weird input (very long names, emoji, pasted numbers with spaces, negative numbers, huge numbers) without breaking the layout or throwing errors. Escape all user input before inserting into HTML (no XSS).
- Must work when opened directly from disk and when hosted statically (Vercel).
- Performance: instant load, under ~100 KB.

# PROCESS

1. Read all attachments. Reply first with a **short confirmation (max 12 lines)**: what you will build, any conflicts or ambiguities you found between documents, and any assumptions you are making. Do not ask more than 2 questions, and only if truly blocking; otherwise assume and list the assumptions. Then continue immediately in the same message.
2. Build the **complete working `index.html`** in your first full response: core first (intro, facts, form, validation, brief, scale lens, example buttons, mobile layout, DEMO ribbon, official link) AND the differentiators (badges, Claims Guard both modes, role matrix, ledger, URL state, print, self-test). No TODOs, no placeholders, no "lorem ipsum". If you must cut something to guarantee a flawless result, cut visual extras first and tell me.
3. Self-review before delivering: (a) run the acceptance tests below mentally or with code execution if available; (b) verify the scale-lens numbers; (c) search the user-visible Romanian text for forbidden phrases; (d) check for console errors, unescaped input, broken layout at 360px; (e) confirm that every claim in the UI is actually implemented.
4. Deliver: the `index.html` as a downloadable file/artifact, plus a short Romanian `README.md` (how to open, how to test in 5 steps, how to deploy statically on Vercel, and the warning that the deployment must be public — no login/protection). Then list in ≤10 lines what is implemented and anything not implemented (honest).

# ACCEPTANCE TESTS (all must pass)

- T1 valid example → full brief; lens 0,80% / 0,01% / 4,00% / 5,00%; Claims Guard 7/7.
- T2 empty name + no role + empty amount → inline errors on all required fields; no brief.
- T3 amount "zece mii", then -500, then 0, then 1500,50 → correct specific messages; no brief.
- T4 amount 150000000 → error (exceeds total).
- T5 amount 2000000 → brief + visible warning (above first stage).
- T6 amount 300 → brief + warning (small amount).
- T7 Claims Guard text „Cu 10.000 lei cumperi o cameră și garantăm deductibilitate" → at least 4 flags with rewrites.
- T8 reload with the shareable URL → same result.
- T9 viewport 360px → no horizontal scroll, usable controls.
- T10 no payment-like element anywhere; DEMO ribbon always visible; footer disclaimer present.
- `?selftest=1` → all assertions PASS.
- Print preview shows one clean A4 page of the brief.

# WHAT NOT TO BUILD

Payments, login, backend, runtime AI/API calls, chatbot, analytics, multi-language switch, dark mode (unless free), a separate fundraising simulator (the financial model lives in the team's spreadsheet), anything not listed above. Do not add features just because they look impressive; a smaller flawless product scores higher than a larger fragile one.

# FINAL REMINDER

Honesty beats flash: every number sourced and badged, every claim real, every forbidden phrase absent. The Romanian must be natural and correct. The first 60 seconds of use must feel effortless on a phone.

---

# FOLLOW-UP PROMPTS (paste one at a time after the first build)

**A — Romanian red-team pass:**
"Do a red-team pass over every user-visible Romanian string in index.html. Flag and fix: forbidden claims (room/bed/place equivalence, housing rights, tax promises, invented partners, guarantees, emotional pressure), awkward Romanian, wrong diacritics (use ș/ț comma-below), inconsistent terminology, and any claim not backed by the official facts config. Show me a table of what you changed and why, then give the full updated file."

**B — Mobile & accessibility audit:**
"Audit index.html at 360×740, 390×844 and 1280×800. Check horizontal overflow, tap target sizes, input zoom on iOS, keyboard navigation, focus order, aria-live announcements, color contrast (AA), prefers-reduced-motion. List the issues found, fix them, and give the full updated file."

**C — Design polish:**
"Raise the visual quality of index.html without adding dependencies or risk: refine spacing/type scale, hero bridge illustration, cards, result 'paper' document, side panel bars, micro-interactions, toast, sticky mobile action bar. Keep all behavior and tests passing. Give the full updated file."

**D — Evaluator experience:**
"Simulate a first-time external evaluator (human and automated) with the 1-minute test. List every friction point, unclear label or missing hint, fix them, make sure the 'Cum testezi în 1 minut' box is perfect, and give the full updated file."

**E — Demo script:**
"Write a 90-second Romanian demo script for the live final (valid case, invalid case, Claims Guard, what the app does NOT do), plus 5 likely jury questions with short, honest answers (including: why no runtime AI, where the figures come from, what we would test first)."

**F — Final check before submission:**
"Final pre-submission check of index.html and README.md: run the acceptance tests T1–T10 and ?selftest=1 logically, verify the scale-lens numbers, scan for forbidden phrases outside the Claims Guard list, confirm no external requests, no storage APIs, no console errors, and confirm every feature mentioned in README exists. Report pass/fail per item and fix anything failing."
