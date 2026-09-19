"""Core validation primitives."""

from __future__ import annotations


class Field:
    def __init__(self, name, dtype=None, required=False, **constraints):
        self.name = name
        self.dtype = dtype
        self.required = required
        self.constraints = constraints


class SchemaGuard:
    def __init__(self, schema_name, fields):
        self.schema_name = schema_name
        self.fields = {f.name: f for f in fields}

    def validate(self, row):
        # Minimal public surface; full logic lives in the release history.
        for name, field in self.fields.items():
            if field.required and name not in row:
                raise SchemaViolation(f"{self.schema_name}: missing required field '{name}'")
        return row


class SchemaViolation(Exception):
    pass
