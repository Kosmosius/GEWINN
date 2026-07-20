# ADR 0003: Generated and raw artifact policy

## Status

Accepted during repository bootstrap.

## Decision

Do not edit generated manuscript tables. Keep large reproducible raw outputs outside Git in ignored `artifacts/raw/`; track only small reviewable summaries, metadata, hashes, provenance, and regeneration commands.

## Consequences

The working tree stays reviewable and avoids duplicate numerical sources. A raw artifact can be reproduced and verified without committing a large generated blob or applying Git LFS migration.
