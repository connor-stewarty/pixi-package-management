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

## Installation
Linux
```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

Windows

    irm -useb https://pixi.sh/install.ps1 | iex

---

## Project Setup (Demo)

    pixi init my-project
    cd my-project
    pixi add python pytest ruff

Creates:  
`pixi.toml` – dependencies & tasks  
`pixi.lock` – fully reproducible builds

---

## Running Tasks

Define tasks once:
```toml
[tasks]
test = "pytest"
lint = "ruff ."
start = "python app.py"
```
Run anywhere:

    pixi run test
    pixi run start

Same commands:

- Local dev

- CI runners

- Containers

--- 

## Multi-Environment Support

    [environments]
    build = ["python"]
    lint = ["ruff"]
    test = ["pytest"]

Run tasks in environment

    pixi run build

---

## Why Pixi?

- Bruh

---

## Takeaway

- Bruh

---
