<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:00ffcc,100:004a99&height=200&section=header&text=Ecosystem%20Command%20Center&fontSize=45&fontColor=ffffff&fontAlignY=40&desc=Central%20Dashboard%20for%20the%20Raphasha27%20GitHub%20Ecosystem&descAlignY=65" width="100%"/>

  [![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-222222?style=for-the-badge&logo=github-pages&logoColor=white)](https://raphasha27.github.io/ecosystem-command-center)
  [![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
  [![Status](https://img.shields.io/badge/Status-Live-00ffcc?style=for-the-badge)](#)
</div>

## Overview

The **Ecosystem Command Center** is a live dashboard that provides real-time visibility into the entire Raphasha27 GitHub ecosystem. It aggregates repository health metrics, contribution analytics, and CI/CD status across all priority repositories.

**Live:** [raphasha27.github.io/ecosystem-command-center](https://raphasha27.github.io/ecosystem-command-center)

## Features

- **Repo Health Overview** — Star counts, forks, language distribution, last updated
- **Priority Repository Tracking** — Focus on the 10 core ecosystem repos
- **Real-time GitHub API Data** — Always up-to-date on page load
- **Dark Theme** — Matches the Kirov Dynamics branding aesthetic
- **Zero Infrastructure** — Fully static site, deployable to GitHub Pages

## Architecture

```
ecosystem-command-center/
├── index.html      # Single-page dashboard (vanilla JS, no build step)
└── README.md       # Documentation
```

The dashboard uses the **GitHub REST API** directly from the browser — no backend, no server, no API keys needed for public repositories.

## Deployment

This dashboard is designed for **GitHub Pages**:

1. Enable GitHub Pages in repo Settings → Pages
2. Set source to `main` branch, root directory
3. Access at `https://raphasha27.github.io/ecosystem-command-center`

## License

MIT License.

---

*Part of the **Kirov Dynamics Technology** ecosystem — built by **Koketso Raphasha (Raphasha27)**.*
