# ============================================
# DATABASE-LEVEL VALIDATION — SQLALCHEMY NOTES
# ============================================

# 1. Database validation is NON-OPTIONAL
#    UI validation can fail, DB must protect data integrity.

# 2. NOT NULL
#    nullable=False ensures mandatory fields.
#    DB raises IntegrityError if violated.

# 3. UNIQUE
#    unique=True prevents duplicates at DB level.
#    Always catch IntegrityError and rollback.

# 4. CHECK CONSTRAINT
#    Enforces domain rules directly in database.
#    Example use-cases:
#    - Valid grade format
#    - Valid ranges (1–12)
#    - Allowed sections (A–D)

# 5. LENGTH CONSTRAINTS
#    Use String(length) to prevent oversized data.
#    Important for performance and data hygiene.

# 6. ENUM-like rules
#    SQLite has no ENUM, simulate using CHECK.

# 7. Error Handling Rule
#    - Always rollback after DB error
#    - Log full error with exc_info=True
#    - Show clean message to user

# 8. Golden Rule
#    Python validates intent
#    Database validates truth
