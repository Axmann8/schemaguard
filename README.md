# schemaguard

Lightweight schema-validation guard for data pipelines.

`schemaguard` sits between producers and consumers and enforces that the
data crossing the boundary actually matches the declared contract — before it
becomes a 3 a.m. page. It's deliberately small, dependency-light, and boring
on purpose: it does one thing (validate) and gets out of the way.

## Install

```bash
pip install schemaguard
