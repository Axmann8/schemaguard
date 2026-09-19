# Changelog

## 1.4.2
- Fix false-positive on nullable decimal fields with trailing zeros.

## 1.4.0
- Add `one_of` constraint support for string fields.
- Tighten error messages to include the schema name and field path.

## 1.3.x
- Performance pass on hot validation path (avoid per-call allocations).

## 1.2.x
- Initial stable release; core `SchemaGuard` API frozen for this major version.
