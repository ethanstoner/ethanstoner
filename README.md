<div align="center">

# Ethan Stoner

**Software Engineer · Cloud, Backend & AI Systems**

I build and deploy software, cloud infrastructure, and applied AI systems.

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

### GenAI Gateway on AWS — cloud deployment &nbsp; [![Terraform](https://img.shields.io/badge/IaC-Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)](https://github.com/aws-solutions-library-samples/guidance-for-multi-provider-generative-ai-gateway-on-aws)

Took AWS's multi-provider GenAI gateway from an empty repository to a working, TLS-secured endpoint, with **~120 AWS resources provisioned with Terraform**. It was stood up end to end and then torn down, not left running as a service. LiteLLM fronts Amazon Bedrock behind one OpenAI-compatible endpoint; VPC, ECS Fargate, ALB, RDS, ElastiCache, WAF, Secrets Manager and Bedrock VPC endpoints, with a remote S3 state backend, Route 53 + ACM, least-privilege IAM and per-key cost observability. Bedrock Guardrails plus a Presidio PII-masking sidecar — where I traced a masking defect to a dependency version and fixed it with a controlled upgrade and regression testing.

**Scope and credit:** the architecture is AWS's own [reference design](https://github.com/aws-solutions-library-samples/guidance-for-multi-provider-generative-ai-gateway-on-aws), not mine. My work was the deployment, a task set by Cisco professionals at Riffyx Labs.

`AWS` · `Terraform` · `ECS Fargate` · `Bedrock` · `RDS` · `ElastiCache` · `Docker` · `LiteLLM`

---

### Local LLM Lab — measuring and speeding up a 7B model on one GPU &nbsp; [![Tests](https://img.shields.io/badge/tests-173%20passing-brightgreen?style=flat-square)](https://github.com/ethanstoner/local-llm-lab) [![Repo](https://img.shields.io/badge/code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/local-llm-lab)

A measurement framework run on **Qwen2.5-7B-Instruct** and an RTX 4090, asking where inference time goes, how close it runs to what the hardware allows, and whether refusal runs through one direction inside the network. A roofline built from measured ceilings (947 GB/s, 157.5 TFLOP/s) with no fitted parameters showed the old attention path copying the KV cache seven times per layer; the replacement reads each cached key and value once and decodes **1.57x faster at 16k context** and **1.65x at batch 32**, with no measurable fidelity loss against an FP32-attention reference. Removing one residual-stream direction takes refusal on harmful prompts from **95% to 0-2.5%**, adding it makes the model refuse 100% of harmless ones, and random directions do nothing. Paired ABBA benchmarks, held-out splits and random controls; every headline number comes from a recorded run stored with its hardware, versions and commit. **173 tests.**

`Python` · `PyTorch` · `Transformers` · `CUDA` · `Roofline` · `Interpretability`

---

### aibackflip — a humanoid that learns to backflip &nbsp; [![Tests](https://img.shields.io/badge/tests-303%20passing-brightgreen?style=flat-square)](https://github.com/ethanstoner/aibackflip) [![Repo](https://img.shields.io/badge/code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/aibackflip)

No physics library, no animation playback, no inverse kinematics, no scripted trajectory. A neural network reads joint angles and foot contacts at 60 Hz and writes twelve motor targets, and a hand-written rigid-body solver does the rest. Both halves are the project: a 2D sequential-impulse constraint solver in **C++** — warm starting, speculative contacts, a Coulomb friction cone, a dedicated position solver — and **PPO written from scratch** in PyTorch with GAE, advantage normalisation and a KL-estimator early stop.

The trained policy completes **24 of 24** backflips at 358 degrees mean rotation and 0.71 s airborne, and still lands 83% of them when shoved with 200 N·s mid-flight. Every figure in the repository is produced by a command in it, against a checkpoint committed alongside — including the training snapshots where success rate goes *backwards* before recovering. Sixty-four environments share one UDP datagram per control step, with C++ telling Python its observation and action shapes so neither side hardcodes them. **303 automated tests** — 214 C++, 89 Python. Two dependencies: GLFW and PyTorch.

`C++` · `Python` · `PyTorch` · `PPO` · `OpenGL`

---

### kvstore — Redis-compatible database engine &nbsp; [![Tests](https://img.shields.io/badge/tests-209%20passing-brightgreen?style=flat-square)](https://github.com/ethanstoner/kvstore) [![Repo](https://img.shields.io/badge/code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/kvstore)

Written from scratch in **Java 21** rather than wrapped around an existing engine. The storage layer is the same shape as LevelDB and RocksDB — write-ahead log, in-memory memtable, sorted on-disk SSTables, leveled compaction, bloom filters — behind a TCP server speaking Redis's **RESP** protocol, so `redis-cli`, `redis-py` and `Jedis` connect unmodified. TLS, multi-user auth, pub/sub and snapshots. **~100K writes/s and ~130K reads/s** single-threaded (JMH), with bloom filters answering missing keys ~90x faster. **209 automated tests**, ~5,200 lines.

`Java 21` · `LSM-Tree` · `RESP` · `TLS` · `Concurrency`

---

### strata — zero-setup DICOM viewer &nbsp; [![Tests](https://img.shields.io/badge/tests-125%20passing-brightgreen?style=flat-square)](https://github.com/ethanstoner/strata) [![Repo](https://img.shields.io/badge/code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/strata)

Point one binary at a folder of CT or MRI files and get a viewer in the browser: scroll the slice stack, window the Hounsfield range, or raymarch the whole study in 3D on the GPU. No DICOMweb server to stand up, no import step, no multi-gigabyte desktop install.

The interesting problem here is not rendering, it is the ways a viewer can be confidently and silently wrong. Slices stacked in the wrong order still render perfectly, with no crash and no warning, and simply show anatomy that does not exist. So the stacking order is derived from each file's own `ImagePositionPatient` projected onto the slice normal, never from `InstanceNumber`, which lies in real data — and a regression test shuffles the instance numbers to prove it holds.

Indexing reads headers only and never pixel data, so a 1026-slice study indexes in **97.8 ms**. The volume renderer is hand-written **WebGL2** with a resolution pyramid, so a modest laptop loads 1 MB instead of 64 MB. A bundled script pulls a real study from the public NCI archive, so it runs end to end without an account. **125 tests** — 65 in Rust and 60 in the browser client — plus 7 more that run against a real downloaded study. MIT.

`Rust` · `WebGL2` · `axum` · `SQLite` · `TypeScript`

---

### Heart Disease Audit — a reproducibility audit of a popular ML dataset &nbsp; [![Tests](https://img.shields.io/badge/tests-77%20passing-brightgreen?style=flat-square)](https://github.com/ethanstoner/heart-disease-audit) [![Repo](https://img.shields.io/badge/code-GitHub-181717?style=flat-square&logo=github)](https://github.com/ethanstoner/heart-disease-audit)

Traces the Kaggle Heart Failure Prediction CSV back to its four UCI hospital sources. Every value missing at the source was filled in, and in four columns the filled value matches the diagnosis perfectly: every filled `ST_Slope` is `Flat` for a patient with heart disease (111 of 111) and `Up` for one without (191 of 191). Undoing the fill drops the typical published pipeline from **86.4% to 79.3%** median accuracy over 1,000 paired splits, and a pre-registered survey of 30 public notebooks found **0 of 30** mention it. Trained on three hospitals and tested on the fourth, the honest AUC is about **0.83**. Every experiment's prediction was committed before it ran; 14 of 15 held up.

`Python` · `pandas` · `scikit-learn` · `SciPy` · `pytest`


<br>

## Open Source

**48 pull requests merged into 31 repositories totalling 475,000+ stars.** Fixes in codebases I do not maintain — found by reading unfamiliar code, diagnosed by measurement, and defended in review. The ten largest repositories:

| Repo | ★ | Merged | What it fixed |
|---|---|---|---|
| [withastro/astro](https://github.com/withastro/astro/pull/17861) | 62.8k | 1 | Fallback route generation swapped the locale as a substring, corrupting any path segment that merely started with the locale code. |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas/pull/67406) | 49.8k | 1 | `qcut` never validated `q`: a bad bin count raised the wrong error, or none at all. |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view/pulls?q=is%3Apr+author%3Aethanstoner+is%3Amerged) | 42.8k | 3 | Kept `node:fs` out of the browser build, fixed 25 tests that failed on every Windows clone, and bounded CCTV media downloads with an idle deadline. |
| [psf/black](https://github.com/psf/black/pull/5411) | 41.9k | 1 | Formatting from a notebook crashed because it assumed every stdout has a `.buffer`. |
| [raysan5/raylib](https://github.com/raysan5/raylib/pull/6187) | 34.9k | 1 | `MatrixCompose()` read back vector components it had just overwritten, so most rotations produced a wrong matrix. |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading/pulls?q=is%3Apr+author%3Aethanstoner+is%3Amerged) | 34.0k | 3 | Reference links that resolve on GitHub and for the agent, and "newest first" history that really is, fixing three tests already failing on `main`. |
| [fmtlib/fmt](https://github.com/fmtlib/fmt/pull/4919) | 25.8k | 1 | A test target built from `format.cc` never inherited the library's `/utf-8`, so the pedantic build did not compile under MSVC. |
| [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect/pull/22980) | 23.9k | 1 | Jitter was drawn around the base interval instead of the backed-off one, so every caller silently lost its retry backoff. |
| [kivy/kivy](https://github.com/kivy/kivy/pulls?q=is%3Apr+author%3Aethanstoner+is%3Amerged) | 19.0k | 2 | KV bindings queued during `Builder.sync` were dropped, silently and forever. |
| [pyinstaller/pyinstaller](https://github.com/pyinstaller/pyinstaller/pull/9521) | 13.1k | 1 | The icon suffix was checked case-sensitively, so `MyApp.ICO` was rejected or silently re-encoded. |

Plus 33 more merges across OpenLayers, kornia, Unciv, node-gyp, Terser, SwiftFormat, Luau, MockK, OpenBot and 12 other repositories — [full list on ethanstoner.dev](https://ethanstoner.dev/open-source).

<sub>Two worth reading in full: <a href="https://github.com/elie222/rakazo/pull/322">rakazo #322</a>, where the reporter wrote "I cannot explain the root cause" and I narrowed it by elimination; and <a href="https://github.com/truefoundry/trueforge/pull/464">trueforge #464</a>, where a reviewer questioned whether an abort was needed and I measured it rather than argued it — <code>Promise.race</code> frees the caller but leaves the socket open.</sub>

<br>

## More Work

| Project | What it does | Stack |
|---|---|---|
| [Universe Simulator](https://github.com/ethanstoner/universe-simulator-cpp) | Newtonian N-body gravity in C++20 and OpenGL 3.3 from real astronomical data — four integrators, Barnes-Hut or exact summation, live energy and momentum diagnostics. 141 unit tests; builds warning-free on four toolchains, and CI runs the OpenGL self-test headlessly through Mesa, 41,005 checks. | `C++20` `OpenGL` `CMake` |
| Pincer <sub>(private)</sub> | Closed-loop agent driving physical Android phones over ADB: a fine-tuned YOLO11 detector finds on-screen targets, and the agent labels its own training data through a self-supervised flywheel. Per-frame capture from ~600 ms to ~1.3 ms. 127 tests. | `Python` `PyTorch` `YOLO11` `ONNX` |
| [Qorlyt](https://github.com/ethanstoner/3d-generator) | One image becomes a textured `.glb` in about 90 seconds on a local ComfyUI + Hunyuan3D 2.1 GPU pipeline, behind a FastAPI backend with WebSocket progress and an async job queue. | `Python` `FastAPI` `ComfyUI` `GPU` |
| [CSUSM Campus Monitor](https://github.com/ethanstoner/csusm-monitor) | Counts people on live campus HLS streams using NVIDIA's LocateAnything-3B open-vocabulary grounding model, falling back to YOLOv8n when the GPU service is unreachable. CI-tested FastAPI dashboard. | `Python` `FastAPI` `OpenCV` `Docker` |
| Automated 3D Asset Pipeline | Unattended ComfyUI + Hunyuan3D GPU pipeline, built and run end to end. **15,200+ sales and 344k Robux (~$1.3k at the DevEx rate) in the past year.** | `Python` `ComfyUI` `GPU` |
| [yt2tiktok](https://github.com/ethanstoner/yt2tiktok) | Turns a YouTube video into scheduled, captioned vertical clips — NVENC encoding with CPU fallback, hybrid transcription. | `Python` `ffmpeg` `Whisper` |
| [Lyric Generator](https://github.com/ethanstoner/lyric-generator) | Spotify link in, lyric video out — Whisper word-level timing, Pillow rendering, ffmpeg mux. | `Python` `FastAPI` `Whisper` |
| [Hunyuan3D-2.1 Install Guide](https://github.com/ethanstoner/Hunyuan3D-2.1-Complete-Install-Guide) | Step-by-step install for Hunyuan3D-2.1 + ComfyUI on Windows. My most-starred repo. | `Docs` |

<br>

## Experience

**Landed** — Founder & Solo Engineer · 2026 – Present
> Built a card-pricing product end to end as sole engineer — product, infrastructure and testing. Deployed and live at [landedcards.com](https://landedcards.com); auth and billing are wired but not yet running in production.

**Roblox UGC** — Independent Creator · 2025 – Present
> Design and sell 3D avatar accessories made with a local-GPU generation pipeline: **15,200+ sales and 344k Robux (~$1.3k at the DevEx rate) over the past year.**

**Riffyx Labs** — Engineering Mentee · 2025 – 2026
> Deployed a multi-provider GenAI gateway on AWS end to end, provisioning ~120 resources with Terraform across ECS Fargate, RDS, ALB, WAF and Bedrock, with Guardrails and PII masking. A task set by Cisco professionals, completed end to end.

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
