# Advocate Diary System

## Overview

The **Advocate Diary System** is a structured case and hearing management system designed for legal practitioners.
Its primary goal is to replace fragile paper diaries and ad-hoc spreadsheets with a **reliable, auditable, and future-extendable digital system**.

The project is being developed **backend-first**, with a CLI-driven architecture initially, followed by a web-based GUI.

This approach ensures:

* correctness before appearance
* stable data models
* predictable business logic
* easy future expansion (GUI, auth, sync, analytics)

---

## Core Design Philosophy

* **Separation of Concerns**

  * Database schema ≠ CRUD ≠ business logic ≠ GUI
* **No hidden magic**

  * Explicit paths, explicit models, explicit actions
* **Append-only audit**

  * Legal data should be traceable, not mutable
* **Diary-forwarding as first-class logic**

  * Hearings move forward; history is never overwritten

---

## Project Structure

```
AdvocateDiarySystem/
│
├── README.md
├── requirements.txt
├── config.py
│
├── gui/                        # Web GUI (added after backend stabilizes)
│   ├── templates/
│   ├── static/
│   └── app.py
│
├── backend/                    # Backend (CLI-first)
│   ├── main.py                 # CLI entry point
│   │
│   ├── commands/               # CLI command modules
│   │   ├── add_hearing.py
│   │   ├── view_day.py
│   │   └── update_status.py
│   │
│   ├── db/                     # Local development databases
│   │   ├── advocatedb.sqlite       # Advocate registry
|   │   │   ├── advocates tables
|   |   ├── clientdb.sqlite
|   │   │   ├── clients table
│   │   ├── casedb.sqlite
|   │   │   ├── cases table
|   │   │   ├── hearings table
|   │   │   ├── client_case_assignments table
│   │   └── auditdb.sqlite      # Append-only audit log
|   │       ├── audit_trail table
│   │
│   ├── models/                 # Table structure only
│   │   ├── __init__.py         # Initializes engine and session
│   │   ├── advocate.py         # Advocate table class
│   │   ├── client.py           # Client table class
│   │   ├── case.py             # Case table class
│   │   ├── hearing.py          # Hearing table class
│   │   └── audit.py            # Audit table class
│   │
│   ├── crud/                   # CRUD operations per table
│   │   ├── advocate_crud.py
│   │   ├── client_crud.py
│   │   ├── case_crud.py
│   │   ├── hearing_crud.py
│   │   └── audit_crud.py
│   │
│   ├── adapter/                # Database adapter / single access point
│   │   └── db_adapter.py
│   │
│   └── utils/                  # Helper functions (date parsing, validation, logging)
│       ├── logger.py
│       └── validators.py
│
└── tests/                      # Optional unit tests for backend
    ├── test_cases.py
    └── test_clients.py

```

---

## Development Phases

### Phase 1 – Backend (Current)

* Define database schemas
* Implement CRUD operations
* Implement diary-forwarding logic
* Validate via CLI commands

### Phase 2 – GUI

* Web interface over existing backend
* No direct DB access from GUI
* Backend remains the single source of truth

### Phase 3 – Enhancements (Future)

* Authentication & roles
* Notifications
* Search & analytics
* Sync / backup strategies

---

## Status

🟡 **Backend in active development**
🔴 GUI intentionally frozen until backend stabilizes

---

## License

Private / Educational / Internal Use
(Not intended for public distribution at this stage)
