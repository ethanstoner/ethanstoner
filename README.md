<div align="center">

# Ethan Stoner

**Software Engineer · Cloud, Backend & AI Systems**

I build and operate production software, cloud infrastructure, and applied AI systems.

[![Portfolio](https://img.shields.io/badge/Portfolio-ethanstoner.dev-0A0A0A?style=for-the-badge&logo=googlechrome&logoColor=white)](https://ethanstoner.dev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-eastoner-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/eastoner)
[![Email](https://img.shields.io/badge/Email-ethanstoner08-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ethanstoner08@gmail.com)

</div>

<br>

## About

Computer Science student at **Cal State San Marcos**, working across cloud infrastructure, backend applications, computer vision, and GPU inference. I like owning things end to end — application code, the infrastructure under it, deployment, testing, and keeping it running. Open to software engineering internships and part-time development work.

<br>

## Selected Work

### Landed — pricing for card shops &nbsp; [![Live](https://img.shields.io/badge/live-landedcards.com-00C853?style=flat-square&logo=googlechrome&logoColor=white)](https://landedcards.com) ![Tests](https://img.shields.io/badge/tests-371%20passing-brightgreen?style=flat-square)

Paste a TCGplayer link, get a sticker price for every condition — Near Mint through Damaged — as whole dollars. The figure is what the card actually costs a buyer online *including shipping*, so a customer walking out with it today is not paying more than they would waiting a week for the mail. Sole engineer across product, infrastructure and testing.

The pricing engine is written **twice on purpose** — a Python reference and the TypeScript port that actually runs — with golden tests asserting the port reproduces the reference byte for byte from shared fixtures. **371 automated tests** across both.

Built and deployed, not yet in service: auth and billing are wired against Clerk and Stripe in test mode rather than running in production.

`TypeScript` · `Cloudflare Workers` · `D1` · `KV` · `Clerk` · `Stripe` · `Python`

---

### GenAI Gateway on AWS — production deployment &nbsp; [![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)](https://github.com/aws-solutions-library-samples/guidance-for-multi-provider-generative-ai-gateway-on-aws)

Took AWS's multi-provider GenAI gateway from an empty repository to a live, TLS-secured production endpoint — **~120 AWS resources provisioned with Terraform**, and ownership of the deployment lifecycle after it was running. LiteLLM fronts Amazon Bedrock behind one OpenAI-compatible endpoint; VPC, ECS Fargate, ALB, RDS, ElastiCache, WAF, Secrets Manager and Bedrock VPC endpoints, with a remote S3 state backend, Route 53 + ACM, least-privilege IAM and per-key cost observability. Bedrock Guardrails plus a Presidio PII-masking sidecar — where I traced a masking defect to a dependency version and fixed it with a controlled upgrade and regression testing.

**Scope and credit:** the architecture is AWS's own [reference design](https://github.com/aws-solutions-library-samples/guidance-for-multi-provider-generative-ai-gateway-on-aws), not mine. My work was the deployment and the operation of it — a real production task set by Cisco professionals at Riffyx Labs.

`AWS` · `Terraform` · `ECS Fargate` · `Bedrock` · `RDS` · `ElastiCache` · `Docker` · `LiteLLM`

---

### Pincer — real-time computer-vision agent &nbsp; ![Tests](https://img.shields.io/badge/tests-127%20passing-brightgreen?style=flat-square) ![Private](https://img.shields.io/badge/repo-private-6E7681?style=flat-square&logo=github&logoColor=white)

A closed loop against real hardware: capture an Android device's screen over ADB, locate the target with a fine-tuned **YOLO11** detector, decide, and actuate a gesture back to the phone. A self-supervised flywheel has the running agent label its own training data (**5,400+ frames**), corrected through a human review UI and fed back through a train → validation-gate → ship pipeline with ONNX export. Per-frame capture taken from **~600 ms to ~1.3 ms**, each tap from ~200 ms to ~20 ms, with multi-device orchestration and self-healing recovery. **127 automated tests.**

`Python` · `PyTorch` · `YOLO11` · `OpenCV` · `ONNX` · `adb`

<sub>Source is private — happy to walk through the architecture and the training pipeline.</sub>

---

### aibackflip — a humanoid that learns to backflip &nbsp; [![Tests](https://img.shields.io/badge/tests-303%20passing-brightgreen?style=flat-square)](https://github.com/ethanstoner/aibackflip) [![Repo](https://img.shields.io/badge/code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/aibackflip)

No physics library, no animation playback, no inverse kinematics, no scripted trajectory. A neural network reads joint angles and foot contacts at 60 Hz and writes twelve motor targets, and a hand-written rigid-body solver does the rest. Both halves are the project: a 2D sequential-impulse constraint solver in **C++** — warm starting, speculative contacts, a Coulomb friction cone, a dedicated position solver — and **PPO written from scratch** in PyTorch with GAE, advantage normalisation and a KL-estimator early stop.

The trained policy completes **24 of 24** backflips at 358 degrees mean rotation and 0.71 s airborne, and still lands 83% of them when shoved with 200 N·s mid-flight. Every figure in the repository is produced by a command in it, against a checkpoint committed alongside — including the training snapshots where success rate goes *backwards* before recovering. Sixty-four environments share one UDP datagram per control step, with C++ telling Python its observation and action shapes so neither side hardcodes them. **303 automated tests** — 214 C++, 89 Python. Two dependencies: GLFW and PyTorch.

`C++` · `Python` · `PyTorch` · `PPO` · `OpenGL`

---

### kvstore — Redis-compatible database engine &nbsp; [![Tests](https://img.shields.io/badge/tests-209%20passing-brightgreen?style=flat-square)](https://github.com/ethanstoner/kvstore) [![Repo](https://img.shields.io/badge/code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/kvstore)

Written from scratch in **Java 21** rather than wrapped around an existing engine. The storage layer is the same shape as LevelDB and RocksDB — write-ahead log, in-memory memtable, sorted on-disk SSTables, leveled compaction, bloom filters — behind a TCP server speaking Redis's **RESP** protocol, so `redis-cli`, `redis-py` and `Jedis` connect unmodified. TLS, multi-user auth, pub/sub and snapshots. **209 automated tests**, ~5,200 lines.

`Java 21` · `LSM-Tree` · `RESP` · `TLS` · `Concurrency`

---

### strata — zero-setup DICOM viewer &nbsp; [![Tests](https://img.shields.io/badge/tests-125%20passing-brightgreen?style=flat-square)](https://github.com/ethanstoner/strata) [![Repo](https://img.shields.io/badge/code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/strata)

Point one binary at a folder of CT or MRI files and get a viewer in the browser: scroll the slice stack, window the Hounsfield range, or raymarch the whole study in 3D on the GPU. No DICOMweb server to stand up, no import step, no multi-gigabyte desktop install.

The interesting problem here is not rendering, it is the ways a viewer can be confidently and silently wrong. Slices stacked in the wrong order still render perfectly, with no crash and no warning, and simply show anatomy that does not exist. So the stacking order is derived from each file's own `ImagePositionPatient` projected onto the slice normal, never from `InstanceNumber`, which lies in real data — and a regression test shuffles the instance numbers to prove it holds.

Indexing reads headers only and never pixel data, so a 1026-slice study indexes in **97.8 ms**. The volume renderer is hand-written **WebGL2** with a resolution pyramid, so a modest laptop loads 1 MB instead of 64 MB. A bundled script pulls a real study from the public NCI archive, so it runs end to end without an account. **125 tests** — 65 in Rust and 60 in the browser client — plus 7 more that run against a real downloaded study. MIT.

`Rust` · `WebGL2` · `axum` · `SQLite` · `TypeScript`

<br>

## Open Source

**22 pull requests merged into repositories totalling 234,000+ stars.** Fixes in codebases I do not maintain — found by reading unfamiliar code, diagnosed by measurement, and defended in review.

| Repo | ★ | Merged | What it fixed |
|---|---|---|---|
| [withastro/astro](https://github.com/withastro/astro/pull/17861) | 62.5k | [#17861](https://github.com/withastro/astro/pull/17861) | Fallback route generation swapped the locale as a substring, so it corrupted any path segment that merely started with the locale code. |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading/pull/1347) | 33.2k | [#1347](https://github.com/HKUDS/Vibe-Trading/pull/1347) | Three "newest first" queries had no tiebreaker, so records sharing a timestamp came back oldest first. Three tests were already failing on `main`. |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading/pull/1328) | 33.2k | [#1328](https://github.com/HKUDS/Vibe-Trading/pull/1328) | Dropped the skill-name prefix from reference links, so they resolve on GitHub and not only for the agent. |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading/pull/1252) | 33.2k | [#1252](https://github.com/HKUDS/Vibe-Trading/pull/1252) | `read_file` now resolves a skill-relative reference link, so a bundled path works for the agent *and* for a human reading it on GitHub. |
| [fmtlib/fmt](https://github.com/fmtlib/fmt/pull/4919) | 25.7k | [#4919](https://github.com/fmtlib/fmt/pull/4919) | A test target built from `format.cc` directly never inherited the `/utf-8` the library sets, so the pedantic build did not compile under MSVC. CI never saw it because only the Linux and macOS jobs enable that flag. |
| [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect/pull/22980) | 23.8k | [#22980](https://github.com/PrefectHQ/prefect/pull/22980) | Jitter was drawn around the base interval instead of the backed-off one, so every caller in the repo silently lost the retry backoff the loop documents. |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view/pull/83) | 23.0k | [#83](https://github.com/bilawalsidhu/gods-eye-view/pull/83) | Kept `node:fs` out of the browser build, where Vite only warns and the boundary rested entirely on one runtime guard being right. |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view/pull/81) | 23.0k | [#81](https://github.com/bilawalsidhu/gods-eye-view/pull/81) | Added `.gitattributes` so text files check out as LF, fixing 25 tests that failed on every Windows clone. |
| [pyinstaller/pyinstaller](https://github.com/pyinstaller/pyinstaller/pull/9521) | 13.1k | [#9521](https://github.com/pyinstaller/pyinstaller/pull/9521) | The icon suffix was compared against a lower-case allowlist without being lower-cased, so `MyApp.ICO` was either rejected outright or silently re-encoded through Pillow, replacing hand-made frames with resampled ones. |
| [openlayers/openlayers](https://github.com/openlayers/openlayers/pull/17614) | 12.6k | [#17614](https://github.com/openlayers/openlayers/pull/17614) | `deflateCoordinate` took a `stride` but looped over the coordinate's length, leaving `Point` and `Circle` with a stride and layout that no longer described their own data. |
| [kornia/kornia](https://github.com/kornia/kornia/pull/4305) | 11.4k | [#4305](https://github.com/kornia/kornia/pull/4305) | `float16` gradients came back NaN: the forward pass divides by a Hessian determinant near 1e-4, and the backward scales by its square, which is below `float16`'s smallest normal. |
| [nodejs/node-gyp](https://github.com/nodejs/node-gyp/pull/3364) | 10.7k | [#3364](https://github.com/nodejs/node-gyp/pull/3364) | `--msvs_version` is documented in three places in the README, but the option is declared and read under the dash spelling, so nopt filed the value somewhere nothing looks at and the flag did nothing on the command line. The environment variable always worked, which is why it went unnoticed. |
| [truefoundry/trueforge](https://github.com/truefoundry/trueforge/pull/477) | 5.4k | [#477](https://github.com/truefoundry/trueforge/pull/477) | Split 401 from 403, so a valid key missing one permission stopped being reported as a bad key. |
| [truefoundry/trueforge](https://github.com/truefoundry/trueforge/pull/464) | 5.4k | [#464](https://github.com/truefoundry/trueforge/pull/464) | Bounded third-party calls that could hold a request open for minutes. |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot/pull/268) | 4.6k | [#268](https://github.com/CopilotKit/OpenBot/pull/268) | Fixed a truthiness check that silently discarded every token on Responses-API models. |
| [JetBrains/go-modern-guidelines](https://github.com/JetBrains/go-modern-guidelines/pull/22) | 3.4k | [#22](https://github.com/JetBrains/go-modern-guidelines/pull/22) | A `go.mod` with no `go` directive fell through to the local toolchain, so the CLI recommended language features the go command then refused to compile — it reads such a module as go1.16. |
| [tobi/walgit](https://github.com/tobi/walgit/pull/18) | 2.5k | [#18](https://github.com/tobi/walgit/pull/18) | No S3 operation could return a retryable error, so the manifest CAS — the repo's only commit point — gave up on transient faults the GCS backend retried. |
| [elie222/rakazo](https://github.com/elie222/rakazo/pull/322) | 2.2k | [#322](https://github.com/elie222/rakazo/pull/322) | Diagnosed a Windows-only startup hang: `tsx watch`'s stdin listener never resolves under turbo. |
| [User0332/rewards-farmer](https://github.com/User0332/rewards-farmer/pull/81) | 848 | [#81](https://github.com/User0332/rewards-farmer/pull/81) | Cleanup after a failed task closed the Rewards tab it was meant to keep, because "the tab to keep" defaulted to whichever one had focus. Every later task then failed, and the rest of the run was silently skipped. |
| [User0332/rewards-farmer](https://github.com/User0332/rewards-farmer/pull/36) | 848 | [#36](https://github.com/User0332/rewards-farmer/pull/36) | Structured logging, a query source that needs no LLM, multi-account runs and a Docker image. |
| [User0332/rewards-farmer](https://github.com/User0332/rewards-farmer/pull/33) | 848 | [#33](https://github.com/User0332/rewards-farmer/pull/33) | Waited on the panel's content rather than its container, fixing a flaky scrape. |
| [User0332/rewards-farmer](https://github.com/User0332/rewards-farmer/pull/32) | 848 | [#32](https://github.com/User0332/rewards-farmer/pull/32) | Lowered the Python floor to widen platform support. |

<sub>Two worth reading in full: <a href="https://github.com/elie222/rakazo/pull/322">rakazo #322</a>, where the reporter wrote "I cannot explain the root cause" and I narrowed it by elimination; and <a href="https://github.com/truefoundry/trueforge/pull/464">trueforge #464</a>, where a reviewer questioned whether an abort was needed and I measured it rather than argued it — <code>Promise.race</code> frees the caller but leaves the socket open.</sub>

<br>

## More Work

| Project | What it does | Stack |
|---|---|---|
| [Universe Simulator](https://github.com/ethanstoner/universe-simulator-cpp) | Newtonian N-body gravity in C++20 and OpenGL 3.3 from real astronomical data — four integrators, Barnes-Hut or exact summation, live energy and momentum diagnostics. 141 unit tests; builds warning-free on four toolchains, and CI runs the OpenGL self-test headlessly through Mesa, 41,005 checks. | `C++20` `OpenGL` `CMake` |
| [Qorlyt](https://github.com/ethanstoner/3d-generator) | One image becomes a textured `.glb` in about 90 seconds on a local ComfyUI + Hunyuan3D 2.1 GPU pipeline, behind a FastAPI backend with WebSocket progress and an async job queue. | `Python` `FastAPI` `ComfyUI` `GPU` |
| [CSUSM Campus Monitor](https://github.com/ethanstoner/csusm-monitor) | Counts people on live campus HLS streams using NVIDIA's LocateAnything-3B open-vocabulary grounding model, falling back to YOLOv8n when the GPU service is unreachable. CI-tested FastAPI dashboard. | `Python` `FastAPI` `OpenCV` `Docker` |
| Automated 3D Asset Pipeline | Unattended ComfyUI + Hunyuan3D GPU pipeline, built and run end to end. **11,000+ AI-generated 3D assets sold.** | `Python` `ComfyUI` `GPU` |
| [yt2tiktok](https://github.com/ethanstoner/yt2tiktok) | Turns a YouTube video into scheduled, captioned vertical clips — NVENC encoding with CPU fallback, hybrid transcription. | `Python` `ffmpeg` `Whisper` |
| [Lyric Generator](https://github.com/ethanstoner/lyric-generator) | Spotify link in, lyric video out — Whisper word-level timing, Pillow rendering, ffmpeg mux. | `Python` `FastAPI` `Whisper` |
| [Hunyuan3D-2.1 Install Guide](https://github.com/ethanstoner/Hunyuan3D-2.1-Complete-Install-Guide) | Step-by-step install for Hunyuan3D-2.1 + ComfyUI on Windows. My most-starred repo. | `Docs` |

<br>

## Experience

**Landed** — Founder & Solo Engineer · 2026 – Present
> Built a card-pricing product end to end as sole engineer — product, infrastructure and testing. Deployed and live at [landedcards.com](https://landedcards.com); auth and billing are wired but not yet running in production.

**Riffyx Labs** — Engineering Mentee · 2025 – 2026
> Deployed and operated a multi-provider GenAI gateway on AWS, provisioning ~120 resources with Terraform across ECS Fargate, RDS, ALB, WAF and Bedrock, with Guardrails and PII masking. Given a real production task by Cisco professionals and completed it end to end.

**Freelance Web Developer** — Self-Employed · 2024 – Present
> Build, deploy and maintain production sites for small-business clients, owning deployment, DNS and hosting.

<br>

## Education & Certifications

| | |
|---|---|
| **Cal State San Marcos** — B.S. Computer Science | Fall 2026 – 2030 (expected) |
| **Great Oak High School** | Graduated June 2026 |
| **Anthropic** | Claude API, Amazon Bedrock, Vertex AI, Model Context Protocol (Advanced), Claude Code — [all certificates](https://ethanstoner.dev/certifications) |
| **OpenAI Academy** | Agents & Workflows, AI Foundations, Applied AI Foundations |
| **AWS Certified Cloud Practitioner (CLF-C02)** | Exam in progress |

<br>

---

<div align="center">

[![Portfolio](https://img.shields.io/badge/ethanstoner.dev-000?style=for-the-badge&logo=googlechrome&logoColor=white)](https://ethanstoner.dev)

</div>
