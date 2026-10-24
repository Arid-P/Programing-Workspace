# 07 — Progress Log (append-only)

Rules: never rewrite old entries; add corrections as new lines ("Correction <date>: ...").
Update procedure: `06` §9.

---

## 1. Log entries (newest at the bottom)

### 2026-09 (before 28th) — Profile audit (68-statement true/false check)
- Purpose: replace an over-optimistic AI audit with the learner's own facts.
- Outcome summary is in §2 below and in `01_LEARNER_PROFILE.md` §4.
- Key discoveries: the four "big projects" were AI-written; Flask and APIs were unknown; JSON was a blocker; DSA and Python core were solid.

### 2026-09 (before 28th) — Milestone 00 (uv) completed
- **Atoms achieved:** M00.01–M00.14 (all).
- **Built:** uv project with `requests` and `rich`; a PEP 723 inline script (`inline_demo.py`, depends on `rich`); project files `pyproject.toml`, `.python-version`, `.venv`, `uv.lock`.
- **Tooling reported by the teacher AI:** uv v0.12.17 and CPython 3.14 on Ubuntu (not independently checked by the planner).
- **Evidence provided:** learner-written README (own words, accurate), AI-written `notes.md` (mental models: grocery list vs receipt, blueprint vs construction, chauffeur, backpack), teacher-AI "final report".
- **What clicked (learner):** `uv init` outputs; `uv add` auto-creates `.venv` and lockfile; `uv.lock` pins exact versions so `uv sync` elsewhere gives the same environment; `uv run` needs no activation and auto-syncs; `uv remove`; `uv sync`; PEP 723 scripts; `uv python list/install/pin`.
- **Struggled:** `uv lock` (why it exists). **Resolved 2026-09-28:** learner stated "`uv lock` creates the blueprint; `uv sync` creates and applies it" (correct: lock resolves without installing; sync installs so `.venv` matches). Original README line "didn't understand" was left in place; add "resolved 2026-09-28" to it.
- **Technical fact-checks by planner:** grocery-list/receipt, blueprint/construction, `uv run`, PEP 723 all accurate. The pitfall "`uv add datetime` installs an unrelated legacy package" was verified (a real PyPI package named `DateTime` exists; PyPI names are case-insensitive).
- **Discrepancy:** the teacher report claimed "Conventional Commits" history not visible in the learner's notes. Learner says he committed after every topic and told the AI to write per-milestone commit messages, so the AI was confused. **Open:** confirm with `git log --oneline`.
- **Hours:** not recorded. (Start recording from M01: see §5.)

### 2026-09-28 — Planning session outputs
- Frozen milestone list 00–04 (learner request).
- Chose C++ over C; dropped Flutter/FLUX; simulators only; math just-in-time.
- Inserted CBSE Class 11 (by 31 Dec 2026) and Class 12 (by 31 Mar 2027).
- Produced this 8-file document set (v1.0).
- **Pending:** Class 11/12 diagnostic; `git log` check; repo creation and links.

### 2026-09-30 — Milestone 01 — substantially complete
- Atoms achieved: M01.01-03,05-20,22 (19 of 24)
- Atoms partial: M01.04, M01.21, M01.23, M01.24
- Built: process_todos.py, todo_tool.py (argparse CLI, atomic writes, verified under
  corruption/10-rapid-add/double-run stress tests with real terminal output)
- Evidence provided: real git log --graph with actual commit hashes (6213621 fast-forward,
  7781706 three-way merge), real branch-delete-safety error message, real git rm --cached
  output, real git revert output. Missing: reset --soft/mixed/hard terminal proof, diff
  variant terminal proof.
- Discrepancy found: json.dump() code example in learner's own README still has an
  unfixed bug (dumps() called with a file arg) — flagged twice now, not yet fixed.
- Correction accepted: learner's own README had 'git switch -c' backwards (said it
  creates-if-missing; actually it only creates, errors if branch exists already).
- Next action: fix+test json.dump() bug; get reset --soft terminal proof; start M02
  in parallel.
- Hours: not recorded (still pending — start logging from M02).

### 2026-10-19 — CBSE Class 11 Unit 1 — COMPLETE
- Atoms achieved: C11-U1-01 through C11-U1-10 (10 of 10, all verified)
- C11-U1-10 retest: passed cold (3 bytes UTF-8, 2 bytes UTF-16 for Devanagari)
- Evidence quality: raw Q&A file with verbatim student answers, explicit grading
  showing real corrections — independently spot-checked by the planner across
  all 10 topics, conversions and Boolean algebra reverified by hand
- No pre-unit diagnostic was run (acceptable for Unit 1 — content was new;
  MANDATORY before Unit 2, which overlaps proven Python skill)
- Next action: new agy chat generates the Class 11 diagnostic as a fillable md
  file before any Unit 2 teaching begins

*(Add new entries below this line using the format at the bottom of this file.)*

### 2026-10-24 — Milestone 01 (JSON + Git) — completed (24/24)
- Atoms achieved: M01.04, M01.21, M01.23, M01.24 (closing the last four; all others verified 2026-09-30)
- Evidence provided: 16-statement check, 16/16 (reset soft/mixed/hard, restore, revert, amend, diff variants, dump vs dumps); git log -n 10 shows 9 of 10 commits in Conventional Commits form (one typo "eat(...)"; learner says other typos were fixed with reset before pushing)
- Not provided: terminal output of git reset --soft (learner reports real use; accepted on the statement result)
- Struggled: README json.dump/dumps mix-up (resolved)
- Hours: not recorded
- Next action: start M02

### 2026-10-24 — CBSE Class 11 Unit 2 — completed (28/28)
- Atoms achieved: C11-U2-01..28
- Built: 12 note sets, 20-program lab file (CBSE_CS/Class11/programs/), viva bank, project brief + AI-written reference solution (not skill evidence)
- Evidence provided: verbatim Q&A bank; cold diagnostic 24/36; 24-statement retest 23/24 (miss: range step arithmetic, an addition slip); mini-check passed (2 of 3 exact, one addition slip); tree and git log; planner re-ran all 20 programs and ran randomized tests on P09–P16 and P20 (0 mismatches)
- Struggled: setdefault (diagnostic miss, wrong again in Unit 2 trace, passed retest), negative-divisor modulo, tuple-with-list as dict key, exception-type recall, range step arithmetic
- Discrepancies between AI report and evidence: completion report said "all 28 mastered" before any retest; lab-file samples for P08/P17/P18 not real runs (P17 chi-square 0.05, impossible for a genuine run); P18 sample contradicted its own code; diagnostic score mis-added (25 vs 24); Q&A grading lines rewrote wrong answers; Topic 22–24 section duplicated; report said P02 uses for...else (it does not)
- Lab-file authorship: unverified, not counted as skill evidence (cold-write waived at learner's request)
- Hours: ~9.3 (learner-reported, whole unit) vs ~14 planned
- Next action: Unit 3 (C11-U3-01..10), sample papers, teach-back, M02

---

## 2. Audit and diagnostic records

### 2.1 The 68-statement audit (statement numbers by topic)
Topics: 1–9 Python core · 10–13 classes · 14–18 files/JSON · 19–26 APIs/HTTP · 27–32 FastAPI · 33–35 Flask · 36–41 databases/SQL · 42–45 NumPy/Matplotlib · 46–49 Git · 50–57 DSA · 58–61 web basics · 62–65 general dev practice · 66–68 environment.

**True:** 1–6, 10, 12, 13, 14, 27, 29, 31, 36–39, 41, 42, 43, 45, 46, 47, 50–57 (52–54 as stated; 55–57 confirm *zero* practical understanding of trees, graphs, DP), 59, 60, 61, 62, 63, 65.
**False:** 8 (venv understanding; since addressed by M00), 15–18 (JSON write/read/use/persist), 19–26 (all APIs/HTTP), 30 (uvicorn), 32 (`async def`), 33–35 (Flask), 44 (write Matplotlib plot from memory), 48 (resolved merge conflict), 58 (i.e., he *has* written some HTML), 64 (never deployed anything).
**Partial:** 7 (multi-file imports; circular imports with SQLAlchemy models), 9 (pip works, mechanics unclear), 11 (inheritance understood, not used well), 28 (path/query parameters: theory yes, practice needs effort), 40 (relationships mostly conceptual), 49 (pull vs fetch; corrected: pull = fetch + merge).
**Ambiguity:** the learner wrote "28" as partial twice; the second may have referred to another FastAPI item (29 or 31), which he also listed as True. Recheck during M03.
**Environment (66–68):** now Ubuntu + VS Code on a laptop (item 66 "primarily Termux" no longer true); laptop available (67 true); understands Termux vs Linux differences "somewhat" (68).

### 2.2 Diagnostics scheduled
| Diagnostic | Where | When | Status |
|---|---|---|---|
| CBSE Class 11 (statements 1–36) | `03` §7 | 2026-10 | Done: 24/36 cold (weak: string/list/dict methods, setdefault, mode, del) |
| CBSE Class 12 (statements 37–66) | `03` §7 | Before Class 12 starts (Jan 2027) | Pending |
| M01 verification statements | `02` M01 | 2026-10-24 | Done: 16/16 |
| Math diagnostic (20–30 statements) | `05` §2 | ~Jul 2027 | Pending |
| Web basics diagnostic | M04 start | ~Jun 2027 | Pending |

---

## 3. Decision log

| ID | Date | Decision | Reason |
|---|---|---|---|
| D01 | 2026-09 | Use **uv** instead of pip/venv | Modern, faster, matches how his projects are already set up; taught in M00 |
| D02 | 2026-09 | Add **Milestone 00** (environment) before topic milestones | Tooling underpins everything; learn once, reuse per milestone |
| D03 | 2026-09 | One uv project + one `.venv` **per milestone**, not one shared venv | Isolation habit; uv makes it nearly free |
| D04 | 2026-09 | Remove the venv section from M01; keep folder name `01_JSON_Environments_Git` | Content moved to M00; renaming optional |
| D05 | 2026-09 | Ignore **FLUX** (Flutter apps) for the whole journey | Learner wants a CS-student-style foundation instead |
| D06 | 2026-09 | Study like a CS student (systems, DSA, math), tailored to EE | Degree is Electrical Engineering, admissions mid-2028 |
| D07 | 2026-09 | **C++** instead of C as the systems language | Learner's choice; Arduino is C++; C still read later |
| D08 | 2026-09 | No purchases; **simulators only** | No budget for components |
| D09 | 2026-09 | Math learned **just-in-time** or in college | Learner's choice; avoids a standalone math phase |
| D10 | 2026-09 | Phases run **in parallel lanes**, not one topic at a time | Learner prefers a mix to connect ideas |
| D11 | 2026-09-28 | Insert **CBSE CS Class 11 (by 31 Dec 2026) and Class 12 (by 31 Mar 2027)** | To teach his brother and to fill gaps (networks, SQL, file handling) |
| D12 | 2026-09-28 | Milestones 00–04 **frozen** (no structural changes) | Learner request |
| D13 | 2026-09-28 | C++ paused Jan–Mar 2027; Phase 3 compressed to 5 blocks | Time budget (4.5 h/week) |
| D14 | 2026-09-28 | Use MySQL/MariaDB (not SQLite) for CBSE SQL practice | Board syllabus is MySQL-style |
| D15 | 2026-09-28 | TEACHER reports need an evidence bundle | Prior AI over-claims (see `01` §9) |
| D18 | 2026-09-30 | Milestones/Journey_Docs/ is an UNTRACKED working copy (gitignored) that agy edits directly, since agy's access is scoped to Milestones/ only. The learner periodically copies Milestones/Journey_Docs/* over the canonical, git-tracked Programing-Workspace/Journey_Docs/ to sync. | agy cannot reach the root workspace repo |
| D19 | 2026-10-24 | Phase 2 has no personal README; verbatim Q&A banks are the evidence | Learner decision; banks hold his own words and errors |
| D20 | 2026-10-24 | Root Journey_Docs is canonical; Milestones/Journey_Docs is a copy refreshed FROM root. Supersedes D18. | Root-access agy chats edit root directly; a stale Milestones copy caused a mismatch |
| D21 | 2026-10-24 | Phase 2 lives in the root workspace repo (CBSE_CS/), not a separate repo | Existing setup; commits already pushed |

D16 and D17 were never assigned.

---

## 4. Repositories (fill in as created)

| Phase | Repo | URL | Created | Last push | Notes |
|---|---|---|---|---|---|
| Docs | `journey-docs` | <TBD> | | | This document set |
| 1 | milestones | https://github.com/Arid-P/Fixing_Fundamentals | | | Real remote confirmed via git_notes.md, 2026-09-30 |
| 2 | `cbse-cs-11-12` | (root workspace repo; URL TBD) | | | D21 |
| 3 | `cpp-electronics-path` | <TBD> | | | |

Phase completion links (add when each phase finishes): _none yet_.

---

## 5. Hours and pace tracker (start from M01)

| Week of | Lane | Hours | Atoms cleared | Notes |
|---|---|---|---|---|
| 2026-10 (~4 wks) | CBSE C11-U2 | ~9.3 (learner-reported, whole unit) | 28 | ~0.33 h/atom; plan was ~14 h |

**Pace rule:** after 4 weeks of data, compute hours per atom for each lane and compare with the plan (`00` §3 and `04` blocks). If the actual pace differs by more than 25%, re-plan dates only (not scope) and log a decision (D-number).

---

## 6. Entry format (copy for new entries)

```
### <YYYY-MM-DD> — <Milestone/Block/Topic> — <status: started/in progress/completed>
- Atoms achieved: <IDs>
- Atoms partial: <IDs>
- Built: <what, with paths>
- Evidence provided: <tree, git log, tests, README>
- What clicked (learner's words): ...
- Struggled: ...
- Correction / resolved: ...
- Discrepancies between AI report and learner evidence: ...
- Hours: <n>
- Next action: ...
```
