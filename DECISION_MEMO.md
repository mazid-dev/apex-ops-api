# Decision Memo
- FastAPI: minimal, testable, small image
- Postgres in compose: meets "database dependency" requirement
- Versioned images by git SHA / semver for rollback safety
- Metrics as proposal only (assessment asks for proposal)
- Trade-off: no HA / no managed cloud (assessment forbids paid resources)