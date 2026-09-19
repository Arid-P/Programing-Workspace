```
backend/db/
├── advocatedb.sqlite
│   └── advocates
│       ├── advocate_id (PK)
│       ├── name
│       ├── phone
│       ├── role (senior / junior)
│       ├── parent_advocate_id (nullable)
│       └── status
│
├── clientdb.sqlite
│   └── clients
│       ├── client_id (PK)
│       ├── name
│       ├── phone
│       └── created_at
│
├── casedb.sqlite
│   ├── cases
│   │   ├── case_id (PK)
│   │   ├── advocate_id (FK logical)
│   │   ├── court
│   │   ├── status
│   │   ├── is_closed
│   │   └── created_at
│   │
│   ├── hearings
│   │   ├── hearing_id (PK)
│   │   ├── case_id (FK logical)
│   │   ├── hearing_date
│   │   ├── is_future
│   │   └── notes
│   │
│   └── client_case_assignments
│       ├── id (PK)
│       ├── client_id
│       ├── case_id
│       └── role_label   # "Mother side", "Brother 1", etc.
│
└── auditdb.sqlite
    └── audit_trail
        ├── audit_id (PK)
        ├── actor_id
        ├── actor_role
        ├── action
        ├── entity_type
        ├── entity_id
        ├── old_value
        ├── new_value
        └── timestamp
```


| Column      | Type             | Description                                        |
| ----------- | ---------------- | -------------------------------------------------- |
| advocate_id | TEXT PRIMARY KEY | Unique ID (can be phone-based or system-generated) |
| name        | TEXT             | Advocate’s name                                    |
| senior_id   | TEXT NULL        | If junior, points to senior advocate ID            |
| phone       | TEXT             | Contact info                                       |
| created_at  | DATETIME         | Account creation timestamp                         |


| Column     | Type             | Description                |
| ---------- | ---------------- | -------------------------- |
| client_id  | TEXT PRIMARY KEY | System-generated unique ID |
| name       | TEXT             | Client’s full name         |
| phone      | TEXT             | Contact info               |
| created_at | DATETIME         | Account creation timestamp |


| Column      | Type             | Description                            |
| ----------- | ---------------- | -------------------------------------- |
| case_id     | TEXT PRIMARY KEY | Unique case identifier                 |
| case_number | TEXT             | Official legal case number             |
| court_name  | TEXT             | Court/venue name                       |
| party_names | TEXT             | ‘Petitioner vs Respondent’             |
| advocate_id | TEXT             | Foreign key → `advocates(advocate_id)` |
| status      | TEXT             | ‘active’ or ‘completed’                |
| created_at  | DATETIME         | Record creation timestamp              |


| Column        | Type             | Description                    |
| ------------- | ---------------- | ------------------------------ |
| hearing_id    | TEXT PRIMARY KEY | Unique hearing record ID       |
| case_id       | TEXT             | Foreign key → `cases(case_id)` |
| hearing_date  | DATE             | Date of the hearing            |
| previous_date | DATE NULL        | Derived from last hearing      |
| next_date     | DATE NULL        | Next hearing date assigned     |
| status        | TEXT             | Hearing status / stage         |
| notes         | TEXT             | Optional notes for advocate    |
| created_at    | DATETIME         | Timestamp of creation          |


| Column        | Type             | Description                        |
| ------------- | ---------------- | ---------------------------------- |
| assignment_id | TEXT PRIMARY KEY | Unique record ID                   |
| client_id     | TEXT             | Foreign key → `clients(client_id)` |
| case_id       | TEXT             | Foreign key → `cases(case_id)`     |
| created_at    | DATETIME         | Timestamp                          |


| Column      | Type             | Description                           |
| ----------- | ---------------- | ------------------------------------- |
| audit_id    | TEXT PRIMARY KEY | Unique audit record ID                |
| entity_type | TEXT             | e.g., ‘case’, ‘hearing’, ‘client’     |
| entity_id   | TEXT             | ID of entity edited                   |
| action      | TEXT             | e.g., ‘UPDATE’                        |
| changed_by  | TEXT             | User ID (senior/junior advocate)      |
| timestamp   | DATETIME         | When change occurred                  |
| old_value   | TEXT             | JSON/text snapshot of previous values |
| new_value   | TEXT             | JSON/text snapshot of updated values  |
