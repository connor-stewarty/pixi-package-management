---
author: Connor Stewart
title: 'Pixi: Package Management Made Easy'
subtitle: Reproducible environments from laptop → CI/CD
date: December 15, 2025
---

## The Problem

- “Works on my machine” syndrome

- Different environment for local vs CI

- Hard-to-reproduce builds

- TODO: Check my slides, something about too many images or harder to update

---

## What is Pixi?

- Fast, modern package & environment manager

- Built on Conda ecosystem (cross-platform)

- One config for:

    - Dependencies

    - Tasks

    - Environments

- Works the same locally and in CI/CD

---

## Conda vs Pixi

- Conda "environments" vs Pixi "workspaces"

- Workspace

    - Manage multiple environments and platforms

    - Tasks and dependencies

    - conda-forge & Pypi

---

## Installation
Linux
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

Windows
```powershell
    irm -useb https://pixi.sh/install.ps1 | iex
```
---

## Create Workspace

```bash
pixi init my-project
```

Creates:  
`pixi.toml` – dependencies, tasks, environments

---

## Add Dependencies

```bash
pixi add numpy pytest ruff
```

Creates:  
`pixi.lock` – lock file for fully reproducible builds

---

## Running Tasks

Define tasks once:
```toml
[tasks]
test = "pytest"
lint = "ruff ."
start = "python app.py"
```
Run anywhere (local, CI, container):
```bash
pixi run test
pixi run start
```

--- 

## Multi-Environment Support
```toml
Combine features (dependencies and tasks) into environments:
[environments]
build = ["deps-build","tasks-build"]
lint = ["deps-lint","tasks-lint"]
test = ["deps-test","tasks-test"]
```
Tasks run in environments
```bash
pixi run lint
```
---

## Why Pixi?

- One tool for deps + tasks

- Reproducible, faster builds

- Same workflow from laptop → pipeline

---

## Takeaway

Pixi streamlines reproducibility and automation from local workstations to CI/CD pipelines with one config, one workflow, everywhere

---
