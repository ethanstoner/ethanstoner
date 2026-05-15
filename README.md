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
<img src="https://img.shields.io/badge/GitHub_Actions_CI-2088FF?style=flat-square&logo=githubactions&logoColor=white">
</td>
</tr>
</table>

<br>

## Featured Projects

### CSUSM Campus Monitor &nbsp; [![Tests](https://github.com/ethanstoner/csusm-monitor/actions/workflows/ci.yml/badge.svg)](https://github.com/ethanstoner/csusm-monitor/actions/workflows/ci.yml)
> Real-time occupancy tracker for campus locations using computer vision. Captures live HLS camera streams, runs YOLOv8 person detection with custom false-positive filtering, and serves a dashboard with live counts, weekly heatmaps, and best-times recommendations. Dual detection backend (local YOLO + Frigate NVR via MQTT), SQLite time-series storage, full CI pipeline.

`Python` `FastAPI` `YOLOv8` `OpenCV` `SQLite` `MQTT` `Docker` | [View Repo](https://github.com/ethanstoner/csusm-monitor)

---

### 3D Generator
> Full-stack web app that turns a single image into a textured `.glb` 3D model in ~80 seconds via a local ComfyUI + Hunyuan3D 2.1 GPU pipeline. Persistent WebSocket to ComfyUI maps per-node progress back to each user, an async job queue serializes GPU work with live queue position + ETA, and every result is stored with an in-browser 3D viewer.

`Python` `FastAPI` `WebSockets` `ComfyUI` `GPU Inference` `Self-Hosted` | [View Repo](https://github.com/ethanstoner/3d-generator)

---

### Senior TV
> Open-source kiosk entertainment and care system for seniors with dementia/Alzheimer's — one mini PC, one TV, one `install.sh`. 6-button remote, self-healing services, HDMI-CEC control, and fully remote-managed for caregivers. Built for two 95-year-olds who watch TV 8+ hours a day.

`Python` `Flask` `Linux` `Jellyfin` `HDMI-CEC` `Kiosk` | [View Repo](https://github.com/ethanstoner/senior-tv)

---

### Lyric Generator &nbsp; [![CI](https://github.com/ethanstoner/lyric-generator/actions/workflows/ci.yml/badge.svg)](https://github.com/ethanstoner/lyric-generator/actions/workflows/ci.yml)
> Paste a Spotify link, get a brat-style lyric video. FastAPI pipeline: Spotify metadata → local/yt-dlp audio → Whisper word-level timing (LRCLIB fallback) → Pillow frame rendering → ffmpeg mux. Async job queue, graceful failure handling on every external call, CI-tested.

`Python` `FastAPI` `Whisper` `Pillow` `ffmpeg` `yt-dlp` | [View Repo](https://github.com/ethanstoner/lyric-generator)

---

### Auto YouTube Pipeline
> Fully automated, zero-human-interaction YouTube content pipeline. Records animated race videos via headless Playwright, encodes + mixes audio with FFmpeg, and uploads on a rate-ramped cron schedule through the YouTube API. 76 race types, parallel batch recording.

`Python` `Playwright` `FFmpeg` `YouTube API` `Automation` | [View Repo](https://github.com/ethanstoner/auto-youtube-pipeline)

---

<details>
<summary><b>More Projects</b></summary>

<br>

| Project | What it does | Stack | Link |
|---------|-------------|-------|------|
| **yt2tiktok** | Desktop app: YouTube → vertical TikTok clips with word-by-word burned captions, GPU/NVENC encoding, hybrid Whisper transcription | Python, CustomTkinter, ffmpeg | [Repo](https://github.com/ethanstoner/yt2tiktok) |
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

**Cheryl's Caramels** &nbsp;-&nbsp; Team Member &nbsp;|&nbsp; Oceanside, CA
> Customer-facing role at markets and events. Processed transactions, maintained inventory, and communicated professionally in fast-paced, high-traffic environments.

**TrashCan Powerwashing** &nbsp;-&nbsp; Co-Founder
> Co-founded a residential cleaning business. Handled scheduling, customer outreach, marketing, and day-to-day service operations.

<br>

## Education & Certifications

| | |
|---|---|
| **Great Oak High School** | Expected Graduation: June 2026 |
| **AWS Cloud Practitioner (CLF-C02)** | In Progress |
| **Coursework** | AP Computer Science Principles, AP Calculus AB, AP Statistics, AP English Lit |
| **Cisco Mentorship Program** | Building monetizable projects & subscription-based businesses |

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
