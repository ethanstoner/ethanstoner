<div align="center">

# Hey, I'm Ethan

**Cloud & Automation Engineer**

I build cloud-ready systems, self-hosted production platforms, and AI-powered workflows.
From GPU inference to deployment infrastructure — I ship real systems that serve real users.

[![Portfolio](https://img.shields.io/badge/Portfolio-ethanstoner.github.io-0A0A0A?style=for-the-badge&logo=github&logoColor=white)](https://ethanstoner.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-eastoner-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/eastoner)
[![Email](https://img.shields.io/badge/Email-ethanstoner08-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ethanstoner08@gmail.com)

</div>

<br>

## About Me

I'm a cloud and automation-focused engineer with hands-on experience building computer vision systems, self-hosting production web applications, running AI inference workloads on local GPU hardware, and managing deployment infrastructure end-to-end. Currently pursuing the **AWS Certified Cloud Practitioner (CLF-C02)** and studying at **Great Oak High School** (graduating June 2026).

<br>

## Tech Stack

<table>
<tr>
<td width="160"><b>Cloud & DevOps</b></td>
<td>
<img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white">
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white">
<img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black">
<img src="https://img.shields.io/badge/Self--Hosted-333?style=flat-square&logo=serverfault&logoColor=white">
</td>
</tr>
<tr>
<td><b>AI & CV</b></td>
<td>
<img src="https://img.shields.io/badge/YOLOv8-111?style=flat-square&logo=yolo&logoColor=00FFFF">
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white">
<img src="https://img.shields.io/badge/Whisper-111?style=flat-square&logo=openai&logoColor=white">
<img src="https://img.shields.io/badge/ComfyUI-333?style=flat-square&logoColor=white">
<img src="https://img.shields.io/badge/GPU_Inference-333?style=flat-square&logo=nvidia&logoColor=76B900">
</td>
</tr>
<tr>
<td><b>Languages</b></td>
<td>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white">
</td>
</tr>
<tr>
<td><b>Backend & Data</b></td>
<td>
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white">
<img src="https://img.shields.io/badge/WebSockets-333?style=flat-square&logo=socketdotio&logoColor=white">
<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white">
<img src="https://img.shields.io/badge/MQTT-660066?style=flat-square&logo=eclipsemosquitto&logoColor=white">
<img src="https://img.shields.io/badge/ffmpeg-007808?style=flat-square&logo=ffmpeg&logoColor=white">
</td>
</tr>
<tr>
<td><b>Testing & QA</b></td>
<td>
<img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white">
<img src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white">
</td>
</tr>
</table>

<br>

# Flagship Projects

## Qorlyt — Image-to-3D Generator &nbsp; [![Live](https://img.shields.io/badge/Live-qorlyt.com-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://qorlyt.com) [![Repo](https://img.shields.io/badge/Code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/3d-generator)

<p align="center">
  <img src="https://raw.githubusercontent.com/ethanstoner/3d-generator/main/docs/screenshots/main-app.png" width="640" alt="Qorlyt 3D generator app">
</p>

> **Live, self-hosted product** at **[qorlyt.com](https://qorlyt.com)**. Upload a single image, get a textured `.glb` 3D model back in ~80 seconds via a local **ComfyUI + Hunyuan3D 2.1** GPU pipeline. A persistent **WebSocket** to ComfyUI maps per-node progress back to each user in real time, an **async job queue** serializes GPU work with live queue position + ETA, and every generation is stored with an in-browser 3D viewer. Shared-password auth, GPU health pings, persistent history.

`Python` · `FastAPI` · `WebSockets` · `ComfyUI` · `Hunyuan3D 2.1` · `GPU Inference` · `Self-Hosted`

---

## Lyric Generator &nbsp; [![CI](https://github.com/ethanstoner/lyric-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/ethanstoner/lyric-generator/actions/workflows/ci.yml) [![Repo](https://img.shields.io/badge/Code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/lyric-generator)

<p align="center">
  <img src="https://raw.githubusercontent.com/ethanstoner/lyric-generator/main/assets/demo.gif" width="230" alt="Lyric video demo: Radiohead - No Surprises">
</p>

> Paste a Spotify link, get a brat-style lyric video. FastAPI pipeline: Spotify metadata → local / yt-dlp audio → **Whisper** word-level timing (LRCLIB fallback) → **Pillow** frame rendering → **ffmpeg** mux. Async job queue, graceful failure handling on every external call, packaged with `pyproject.toml`, MIT-licensed, and **CI-tested on every push**.

`Python` · `FastAPI` · `Whisper` · `Pillow` · `ffmpeg` · `yt-dlp` · `GitHub Actions`

---

## yt2tiktok &nbsp; [![Repo](https://img.shields.io/badge/Code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/yt2tiktok)

<p align="center">
  <img src="https://raw.githubusercontent.com/ethanstoner/yt2tiktok/main/assets/captions-demo.gif" width="260" alt="yt2tiktok animated captions demo">
</p>

> Desktop app that turns any YouTube video into scheduled, captioned TikTok clips. Splits into 60–70s vertical segments (silence-based or LLM cliffhanger cuts), burns in **word-by-word karaoke captions** (6 style presets), and uploads on a schedule. **NVENC GPU encoding** with CPU fallback, parallel encoding (2–4× faster), and hybrid transcription — YouTube captions with automatic local Whisper fill-in for censored words.

`Python` · `CustomTkinter` · `ffmpeg / NVENC` · `faster-whisper` · `yt-dlp`

<br>

## More Featured Work

### CSUSM Campus Monitor &nbsp; [![Tests](https://github.com/ethanstoner/csusm-monitor/actions/workflows/ci.yml/badge.svg)](https://github.com/ethanstoner/csusm-monitor/actions/workflows/ci.yml)
> Real-time occupancy tracker for campus locations using computer vision — live HLS stream capture, YOLOv8 person detection with custom false-positive filtering, dashboard with live counts, weekly heatmaps, and best-times recommendations. Dual backend (local YOLO + Frigate NVR via MQTT), full CI pipeline.

`Python` `FastAPI` `YOLOv8` `OpenCV` `SQLite` `MQTT` `Docker` | [View Repo](https://github.com/ethanstoner/csusm-monitor)

### Senior TV
> Open-source kiosk entertainment and care system for seniors with dementia/Alzheimer's — one mini PC, one TV, one `install.sh`. 6-button remote, self-healing services, HDMI-CEC control, fully remote-managed for caregivers. Built for two 95-year-olds who watch TV 8+ hours a day.

`Python` `Flask` `Linux` `Jellyfin` `HDMI-CEC` | [View Repo](https://github.com/sandbreak80/senior-tv)

### Auto YouTube Pipeline
> Fully automated, zero-human-interaction YouTube content pipeline. Records animated race videos via headless Playwright, encodes + mixes audio with FFmpeg, uploads on a rate-ramped cron schedule via the YouTube API. 76 race types, parallel batch recording.

`Python` `Playwright` `FFmpeg` `YouTube API` `Automation` | [View Repo](https://github.com/ethanstoner/auto-youtube-pipeline)

<br>

## Client / Freelance Work

### GSI Sand & Gravel &nbsp; [![Live](https://img.shields.io/badge/Live-gsi.fluximetry.com-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://gsi.fluximetry.com)
> Designed, built, and deployed a production marketing website for **GSI Sand & Gravel**, a Southern California sand & gravel supplier serving the region for 30+ years. Responsive Next.js site presenting the company's services, coverage area, and contact funnel — shipped and live for a real business.

`Next.js` `React` `Responsive` `Deployed`

<br>

<details>
<summary><b>More Projects</b></summary>

<br>

| Project | What it does | Stack | Link |
|---------|-------------|-------|------|
| **Hunyuan3D-2.1 Install Guide** ⭐9 | Comprehensive step-by-step guide for installing Hunyuan3D-2.1 + ComfyUI on Windows | Docs | [Repo](https://github.com/ethanstoner/Hunyuan3D-2.1-Complete-Install-Guide) |
| **QA Automation Framework** | Reusable, Dockerized QA pipeline: unit tests, static analysis, security scanning, Playwright E2E, HTML/JSON reports | Python, Playwright, Docker | [Repo](https://github.com/ethanstoner/qa-instructions) |
| **Vulture** | Minecraft mod decompiler/deobfuscator with suspicious-pattern security detection, Docker-isolated execution | Python, Java, Docker | [Repo](https://github.com/ethanstoner/vulture) |
| **DelayEdge** | Automated trading bot for the HowTheMarketWorks simulator; real-time scanning, fixed-target exits, market-hours guards | Python | [Repo](https://github.com/ethanstoner/delayedge) |
| **HumanType** | Cross-platform realistic typing emulator — QWERTY-based typos, natural rhythm, packaged Windows app with update checks | C# | [Repo](https://github.com/ethanstoner/humanlike-typer) |
| **Quiz Sorter for TAs** | Wayground quiz organizer with attendance matching, curve caps, multi-quiz merge, sorted CSV/PDF output | Python | [Repo](https://github.com/ethanstoner/Quiz-Sorter-Program) |
| **Exploding Ball Engine** | Web physics sim with collision detection and particle effects | JavaScript, Matter.js | [Repo](https://github.com/ethanstoner/exploding-ball-engine) |
| **Portfolio** | Responsive personal site with animations & Playwright testing | HTML/CSS/JS | [Live](https://ethanstoner.github.io) |

</details>

<br>

## Work Experience

**Collaborator** &nbsp;&middot;&nbsp; Riffyx Labs Mentorship &nbsp;|&nbsp; 2025 – 2026 &nbsp;&middot;&nbsp; 1 yr
> Built hands-on experience with AWS fundamentals, debugging, and real-world technical issues across mentored projects. Used Git-based workflows to make code updates, work across branches, and submit pull requests for review. Worked alongside Cisco professionals on implementation tasks, strengthening troubleshooting, teamwork, and release discipline.

**Co-Founder** &nbsp;&middot;&nbsp; TrashCan Powerwashing &nbsp;|&nbsp; Aug 2025 – Oct 2025 &nbsp;&middot;&nbsp; 3 mos
> Co-founded a residential trash-can power-washing business, working directly with customers from scheduling through service completion. Managed scheduling, customer communication, and cash handling while tracking income and expenses. Delivered services reliably, building hands-on experience with responsibility, time management, and client-facing work.

**Member** &nbsp;&middot;&nbsp; Cheryl's Caramels &nbsp;|&nbsp; 2022 – 2025 &nbsp;&middot;&nbsp; 3 yrs &nbsp;|&nbsp; Oceanside, CA
> Represented the company at markets and events, engaging customers and resolving product questions on the spot. Tested Stripe payment flows for the Cheryl's Caramels e-commerce site before release to verify checkout and payment reliability. Processed cash and digital transactions accurately while maintaining inventory and display readiness. Took ownership of assigned responsibilities, consistently meeting expectations with minimal oversight, and communicated professionally in fast-paced, high-traffic environments.

<br>

## Education & Certifications

| | |
|---|---|
| **Great Oak High School** | Expected Graduation: June 2026 |
| **AWS Cloud Practitioner (CLF-C02)** | In Progress |
| **Coursework** | AP Computer Science Principles, AP Calculus AB, AP Statistics, AP English Lit |

<br>

## Currently Learning

<div align="center">

`AWS CLF-C02` &nbsp; `IAM & EC2` &nbsp; `Infrastructure Patterns` &nbsp; `Cloud Security` &nbsp; `Cost Optimization`

</div>

<br>

---

<div align="center">

**Cloud Engineering** &nbsp;&bull;&nbsp; **Computer Vision** &nbsp;&bull;&nbsp; **DevOps** &nbsp;&bull;&nbsp; **Automation** &nbsp;&bull;&nbsp; **AI Infrastructure**

[![Portfolio](https://img.shields.io/badge/ethanstoner.github.io-000?style=for-the-badge&logo=github&logoColor=white)](https://ethanstoner.github.io)

</div>
