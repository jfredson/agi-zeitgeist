# Not merged: partial traces from the full panel collection

Working copies of traces started on 2026-10-09 for the full collection of the frozen
panel (amendment A18). They are kept here so partial work is not lost. **Nothing in this
folder is part of the dataset.** A member's rows move into `data/statements.csv` and
`data/search_log.csv` only once their trace is finished, and that member's folder is
then removed from here.

Each folder holds the member's statement rows, search rows, any statements by other
panel members found along the way (`incidental.csv`), and the tracer's report, which
says which years are fully searched and which leads are still unread.

A folder that holds only `incidental.csv` belongs to a member whose own trace is already
merged: those rows are statements by *other* panel members found along the way, held
here until that other member's trace is merged too, then added to their rows (and
dropped if their own trace already has the same statement).
