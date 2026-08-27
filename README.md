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

I'm a cloud and automation-focused engineer with hands-on experience building computer vision systems, self-hosting production web applications, running AI inference workloads on local GPU hardware, and managing deployment infrastructure end-to-end. Recent **Great Oak High School** graduate (June 2026), heading to **Cal State San Marcos** for a B.S. in Computer Science (Fall 2026), and pursuing the **AWS Certified Cloud Practitioner (CLF-C02)**. Open to internships and part-time roles.

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
<img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white">
<img src="https://img.shields.io/badge/Cloudflare_Workers-F38020?style=flat-square&logo=cloudflareworkers&logoColor=white">
<img src="https://img.shields.io/badge/Self--Hosted-333?style=flat-square&logo=serverfault&logoColor=white">
</td>
</tr>
<tr>
<td><b>AI & CV</b></td>
<td>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white">
<img src="https://img.shields.io/badge/YOLOv8_%2F_YOLO11-111?style=flat-square&logo=yolo&logoColor=00FFFF">
<img src="https://img.shields.io/badge/ONNX-005CED?style=flat-square&logo=onnx&logoColor=white">
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
<img src="https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white">
<img src="https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white">
<img src="https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white">
</td>
</tr>
<tr>
<td><b>Backend & Data</b></td>
<td>
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white">
<img src="https://img.shields.io/badge/WebSockets-333?style=flat-square&logo=socketdotio&logoColor=white">
<img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white">
<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white">
<img src="https://img.shields.io/badge/Redis_%2F_RESP-DC382D?style=flat-square&logo=redis&logoColor=white">
<img src="https://img.shields.io/badge/Stripe-635BFF?style=flat-square&logo=stripe&logoColor=white">
<img src="https://img.shields.io/badge/Clerk-6C47FF?style=flat-square&logo=clerk&logoColor=white">
<img src="https://img.shields.io/badge/MQTT-660066?style=flat-square&logo=eclipsemosquitto&logoColor=white">
<img src="https://img.shields.io/badge/ffmpeg-007808?style=flat-square&logo=ffmpeg&logoColor=white">
</td>
</tr>
<tr>
<td><b>Testing & QA</b></td>
<td>
<img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white">
<img src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white">
<img src="https://img.shields.io/badge/JUnit-25A162?style=flat-square&logo=junit5&logoColor=white">
</td>
</tr>
</table>

<br>

# Flagship Projects

## Landed — Pricing Platform for Card Shops &nbsp; [![Live](https://img.shields.io/badge/Live-landedcards.com-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://landedcards.com) [![Tests](https://img.shields.io/badge/tests-359%20passing-brightgreen?style=flat-square)](https://landedcards.com)

> **Live subscription product** at **[landedcards.com](https://landedcards.com)**, in production use by two card shops. Paste a card, get a whole-dollar price for all five conditions — priced on **landed cost** (item + shipping), so buying it in the case beats waiting a week for the mail — with the evidence behind every number shown beside it. Sole engineer across product, infrastructure, billing and support: **Cloudflare Workers + D1 + KV** at the edge, **Clerk** auth with per-organization roles, **Stripe** subscription billing with plan entitlements and trials, and an hourly cron sweep that re-prices inventory and flags stickers that have drifted. The pricing engine is implemented **twice on purpose** — a Python reference and the TypeScript port that actually runs — with golden tests asserting the port reproduces the reference byte-for-byte from shared fixtures. **359 automated tests** across both.
>
> A companion intake tool scans a stack of cards on a flatbed and identifies each one **by artwork** rather than by name (ORB keypoint matching), grades it from edge, corner and centering defects measured in OpenCV, and routes it to a human review queue before anything is listed.

`TypeScript` · `Cloudflare Workers` · `D1` · `KV` · `Stripe` · `Clerk` · `Python` · `OpenCV`

---

## GenAI Gateway on AWS — Production Deployment &nbsp; [![AWS](https://img.shields.io/badge/AWS-Production%20Deployment-FF9900?style=flat-square)](https://github.com/aws-solutions-library-samples/guidance-for-multi-provider-generative-ai-gateway-on-aws) [![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)](https://github.com/aws-solutions-library-samples/guidance-for-multi-provider-generative-ai-gateway-on-aws)

> **Deployed & operated** AWS's multi-provider Generative AI gateway from an empty repo to a live, **TLS-secured production endpoint** — provisioning **~120 AWS resources with Terraform** and owning the full deployment lifecycle. An OpenAI-compatible API layer (**LiteLLM**) fronts **Amazon Bedrock**, exposing Amazon Nova and Anthropic Claude through one endpoint with usage-based routing and automatic fallbacks. Provisioned VPC, **ECS Fargate**, ALB, **PostgreSQL on RDS**, **Redis on ElastiCache**, WAF, Secrets Manager, and Bedrock VPC endpoints via Terraform with a remote **S3 state backend**; custom domain on **Route 53** + a DNS-validated **ACM** certificate; horizontal autoscaling, least-privilege IAM, Redis caching, and per-key cost/token observability. Layered **Bedrock Guardrails** + a **Microsoft Presidio** PII-masking sidecar — then traced a masking defect to a dependency version and fixed it via a controlled upgrade and regression testing. Built one-command spin-up / spin-down cost controls and rebuilt the entire stack from Terraform state to verify it.
>
> **Scope & credit:** a real production cloud/DevOps task set by **Cisco professionals at Riffyx Labs** and completed end to end — hands-on *deployment and operation* of AWS's official [Guidance for Multi-Provider Generative AI Gateway on AWS](https://github.com/aws-solutions-library-samples/guidance-for-multi-provider-generative-ai-gateway-on-aws) reference architecture, not original authorship of the codebase.

`Client → Route 53 + ACM (TLS) → ALB + WAF → ECS Fargate (LiteLLM + Presidio) → Amazon Bedrock (Nova / Claude)` · `RDS` · `ElastiCache` · `Secrets Manager`

`AWS` · `Terraform` · `ECS Fargate` · `Amazon Bedrock` · `RDS` · `ElastiCache` · `Route 53` · `ACM` · `Docker` · `LiteLLM`

---

## Pincer — Real-Time Computer-Vision Agent &nbsp; ![Tests](https://img.shields.io/badge/tests-127%20passing-brightgreen?style=flat-square) ![Private](https://img.shields.io/badge/repo-private-6E7681?style=flat-square&logo=github&logoColor=white)

> A real-time **computer-vision agent** that drives physical **Android** phones autonomously to play a mobile game. It streams live video off each device over USB, locates targets with a fine-tuned **YOLO11** detector, and executes the on-screen gestures to act on them — closing the perception → decision → actuation loop end to end. A **self-supervised data flywheel** has the running agent label its own training data (**5,400+ frames**), corrected through a human-in-the-loop review UI and fed back through a train → validation-gate → ship pipeline with **ONNX** export. Latency engineered to the floor — per-frame capture **~600ms → ~1.3ms**, each tap **~200ms → ~20ms** — with multi-device orchestration, self-healing recovery, and a live MJPEG dashboard. Structural safety invariants enforced in code and tests; **127 automated tests**.

`Python` · `PyTorch` · `YOLO11` · `OpenCV` · `ONNX` · `Computer Vision` · `adb`

<sub>Source is private — happy to walk through the architecture and the training pipeline in an interview.</sub>

---

## Qorlyt — Image-to-3D Generator &nbsp; [![Repo](https://img.shields.io/badge/Code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/3d-generator)

<p align="center">
  <img src="https://raw.githubusercontent.com/ethanstoner/3d-generator/main/docs/screenshots/main-app.png" width="640" alt="Qorlyt 3D generator app">
</p>

> **Self-hosted product.** Upload a single image, get a textured `.glb` 3D model back in ~80 seconds via a local **ComfyUI + Hunyuan3D 2.1** GPU pipeline. A persistent **WebSocket** to ComfyUI maps per-node progress back to each user in real time, an **async job queue** serializes GPU work with live queue position + ETA, and every generation is stored with an in-browser 3D viewer. Shared-password auth, GPU health pings, persistent history.

`Python` · `FastAPI` · `WebSockets` · `ComfyUI` · `Hunyuan3D 2.1` · `GPU Inference` · `Self-Hosted`

---

## kvstore — Redis-Compatible Database &nbsp; [![Tests](https://img.shields.io/badge/tests-203%20passing-brightgreen?style=flat-square)](https://github.com/ethanstoner/kvstore) [![Repo](https://img.shields.io/badge/Code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/kvstore)

> Persistent, Redis-compatible key-value database written from scratch in **Java 21**. An **LSM-tree** storage engine — write-ahead log, leveled compaction, bloom filters, concurrent flush — behind a TCP server speaking the Redis **RESP** protocol, so standard Redis clients connect directly. TLS, multi-user auth, pub/sub, and snapshots, all backed by **203 automated tests**.

`Java 21` · `LSM-Tree` · `RESP` · `TLS` · `Concurrency`

<br>

# Open-Source Contributions

Merged fixes in other people's production codebases — found by reading unfamiliar code, diagnosed by measurement, and defended in review.

## rakazo &nbsp; [![PR #322](https://img.shields.io/badge/PR%20%23322-merged-8957E5?style=flat-square&logo=github&logoColor=white)](https://github.com/elie222/rakazo/pull/322) [![Stars](https://img.shields.io/badge/upstream-1.4k%20stars-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/elie222/rakazo)

> Three services silently failed to start on Windows under `turbo` — no output, no port, no error. The reporter could reproduce it but wrote *"I cannot explain the root cause."* I narrowed it by elimination: a trivial script under turbo worked while the real app did not; redirecting the child's stdout to a file still hung, ruling out pipe blocking; a 160-second wait proved a hang rather than slowness. The cause was `tsx watch`'s press-Return-to-restart **stdin listener** — under turbo on Windows that inherited handle never delivers and never closes, so the process never reaches its entrypoint. Fixed with a small cross-platform runner that detaches stdin while preserving output and signal semantics.

`Node.js` · `TypeScript` · `turbo` · `Windows` · `Process I/O`

---

## TrueForge &nbsp; [![PR #464](https://img.shields.io/badge/PR%20%23464-merged-8957E5?style=flat-square&logo=github&logoColor=white)](https://github.com/truefoundry/trueforge/pull/464) [![Stars](https://img.shields.io/badge/upstream-4.7k%20stars-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/truefoundry/trueforge)

> A sandbox status refresh called a third-party API with **no timeout** from three request-handling paths, so a stalled provider could hold API requests open until the HTTP client's multi-minute default. Added a timeout budget and an abort on the request itself. When a reviewer questioned whether the abort was necessary, I measured it rather than argued it: `Promise.race` frees the caller but leaves the socket open — demonstrated with socket-close events. Merged after a changes-requested review round.

`TypeScript` · `Node.js` · `Timeouts` · `AbortSignal` · `Code Review`

<br>

## More Featured Work

### CSUSM Campus Monitor &nbsp; [![Tests](https://github.com/ethanstoner/csusm-monitor/actions/workflows/ci.yml/badge.svg)](https://github.com/ethanstoner/csusm-monitor/actions/workflows/ci.yml)
> Real-time occupancy tracker for campus locations using computer vision — live HLS stream capture, YOLOv8 person detection with custom false-positive filtering, dashboard with live counts, weekly heatmaps, and best-times recommendations. Dual backend (local YOLO + Frigate NVR via MQTT), full CI pipeline.

`Python` `FastAPI` `YOLOv8` `OpenCV` `SQLite` `MQTT` `Docker` | [View Repo](https://github.com/ethanstoner/csusm-monitor)

### yt2tiktok &nbsp; [![Repo](https://img.shields.io/badge/Code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/yt2tiktok)
> Desktop app that turns any YouTube video into scheduled, captioned TikTok clips. Splits into 60–70s vertical segments (silence-based or LLM cliffhanger cuts), burns in word-by-word karaoke captions, and uploads on a schedule. **NVENC GPU encoding** with CPU fallback and hybrid transcription — YouTube captions with local Whisper fill-in.

`Python` `CustomTkinter` `ffmpeg / NVENC` `faster-whisper` | [View Repo](https://github.com/ethanstoner/yt2tiktok)

<br>

## Client / Freelance Work

### GSI Sand & Gravel
> Designed, built, and deployed a production marketing website for **GSI Sand & Gravel**, a Southern California sand & gravel supplier serving the region for 30+ years. Responsive Next.js site presenting the company's services, coverage area, and contact funnel — shipped for a real business.

`Next.js` `React` `Responsive` `Deployed`

<br>

<details>
<summary><b>More Projects</b></summary>

<br>

| Project | What it does | Stack | Link |
|---------|-------------|-------|------|
| **Hunyuan3D-2.1 Install Guide** ⭐13 | Comprehensive step-by-step guide for installing Hunyuan3D-2.1 + ComfyUI on Windows — my most-starred repo | Docs | [Repo](https://github.com/ethanstoner/Hunyuan3D-2.1-Complete-Install-Guide) |
| **Lyric Generator** | Spotify link in, brat-style lyric video out — Whisper word-level timing, Pillow rendering, ffmpeg mux, CI-tested | Python, FastAPI, Whisper | [Repo](https://github.com/ethanstoner/lyric-generator) |

</details>

<br>

## Work Experience

**Mentee** &nbsp;&middot;&nbsp; Riffyx Labs Mentorship &nbsp;|&nbsp; 2025 – 2026 &nbsp;&middot;&nbsp; 1 yr
> Given a real production task by **Cisco professionals** at Riffyx Labs and completed it end to end — deployed and operated a production **Generative AI gateway on AWS**, provisioning ~120 resources with **Terraform** (ECS Fargate, RDS, ALB, WAF, Bedrock) with Guardrails and PII masking. Worked through Git-based workflows (branches, commits, pull requests) and hands-on production debugging — building troubleshooting, release discipline, and real infrastructure ownership. *(See the GenAI Gateway flagship above.)*

**Co-Founder** &nbsp;&middot;&nbsp; TrashCan Powerwashing &nbsp;|&nbsp; Aug 2025 – Oct 2025 &nbsp;&middot;&nbsp; 3 mos
> Co-founded a residential trash-can power-washing business, working directly with customers from scheduling through service completion. Managed scheduling, customer communication, and cash handling while tracking income and expenses. Delivered services reliably, building hands-on experience with responsibility, time management, and client-facing work.

**Member** &nbsp;&middot;&nbsp; Cheryl's Caramels &nbsp;|&nbsp; 2022 – 2025 &nbsp;&middot;&nbsp; 3 yrs &nbsp;|&nbsp; Oceanside, CA
> Represented the company at markets and events, engaging customers and resolving product questions on the spot. Tested Stripe payment flows for the Cheryl's Caramels e-commerce site before release to verify checkout and payment reliability. Processed cash and digital transactions accurately while maintaining inventory and display readiness. Took ownership of assigned responsibilities, consistently meeting expectations with minimal oversight, and communicated professionally in fast-paced, high-traffic environments.

<br>

## Education & Certifications

| | |
|---|---|
| **Cal State San Marcos** — B.S. Computer Science | Starting Fall 2026 |
| **Great Oak High School** | Graduated June 2026 |
| **Anthropic** — [21 Certificates of Completion](https://ethanstoner.github.io/certs) | Anthropic API, Amazon Bedrock, Google Vertex AI, Code in Action, Code 101, Model Context Protocol (MCP) + Advanced, Agent Skills, Subagents, AI Fluency (Builders / Framework / Students / Educators / K-12 / Nonprofits / Small Businesses / Teaching / Capabilities & Limitations), Platform 101, Claude 101 & Cowork |
| **OpenAI** — [Agents and Workflows](https://academy.openai.com/public/certificate/2b0iq3mrzx), [AI Foundations](https://academy.openai.com/public/certificate/v0uhjoyeu3) & [Applied AI Foundations](https://academy.openai.com/public/certificate/zl8falk765) | OpenAI Academy — AI agents & workflows, plus AI foundations and applied practice |
| **AWS Cloud Practitioner (CLF-C02)** | In Progress |
| **HS Coursework** | AP Computer Science A, AP Computer Science Principles, AP Calculus AB, AP Statistics, AP English Lit |

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
