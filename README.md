<div align="center">

# Ethan Stoner

**Software Engineer · Cloud, Backend & AI Systems**<br>CS at Cal State San Marcos · open to SWE internships and part-time work

[![Portfolio](https://img.shields.io/badge/Portfolio-111111?style=for-the-badge&logo=googlechrome&logoColor=white)](https://ethanstoner.dev)&nbsp;[![Resume](https://img.shields.io/badge/Resume-1b3a72?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xNCAySDZhMiAyIDAgMCAwLTIgMnYxNmEyIDIgMCAwIDAgMiAyaDEyYTIgMiAwIDAgMCAyLTJWOGwtNi02em0tMSA3VjMuNUwxOC41IDlIMTN6TTggMTNoOHYySDh2LTJ6bTAgNGg4djJIOHYtMnoiLz48L3N2Zz4%3D)](https://ethanstoner.dev/Ethan_Stoner_Resume.pdf)&nbsp;[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0yMC40NSAyMC40NWgtMy41NnYtNS41N2MwLTEuMzMtLjAzLTMuMDQtMS44NS0zLjA0LTEuODUgMC0yLjE0IDEuNDUtMi4xNCAyLjk0djUuNjdIOS4zNVY5aDMuNDF2MS41NmguMDVjLjQ4LS45IDEuNjQtMS44NSAzLjM3LTEuODUgMy42IDAgNC4yNyAyLjM3IDQuMjcgNS40NnY2LjI4ek01LjM0IDcuNDNhMi4wNiAyLjA2IDAgMSAxIDAtNC4xMyAyLjA2IDIuMDYgMCAwIDEgMCA0LjEzek03LjEyIDIwLjQ1SDMuNTZWOWgzLjU2djExLjQ1ek0yMi4yMiAwSDEuNzdDLjc5IDAgMCAuNzcgMCAxLjczdjIwLjU0QzAgMjMuMjMuNzkgMjQgMS43NyAyNGgyMC40NWMuOTggMCAxLjc4LS43NyAxLjc4LTEuNzNWMS43M0MyNCAuNzcgMjMuMiAwIDIyLjIyIDB6Ii8%2BPC9zdmc%2B)](https://linkedin.com/in/eastoner)&nbsp;[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ethanstoner08@gmail.com)

</div>

### Highlights

- **54 pull requests merged into 34 open-source repositories totalling 511,000+ stars**, including Astro, pandas, Black, raylib and Prefect.
- **15,200+ sales and 344k Robux (~$1.3k at the DevEx rate) in the past year** from 3D accessories made on my own local-GPU generation pipeline.
- **1.57x faster LLM decoding at 16k context** on an RTX 4090, found with a roofline built from measured hardware ceilings.
- **~120 AWS resources provisioned with Terraform** to deploy a multi-provider GenAI gateway end to end.
- **A Redis-compatible database engine from scratch** in Java 21: ~100K writes/s and ~130K reads/s single-threaded.

### Tech Stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=py,ts,js,java,cpp,rust,react,nextjs,fastapi,nodejs&perline=10" alt="Python, TypeScript, JavaScript, Java, C++, Rust, React, Next.js, FastAPI, Node.js" height="48"><br>
  <img src="https://skillicons.dev/icons?i=pytorch,aws,terraform,docker,cloudflare,postgres,sqlite,linux,githubactions,git&perline=10" alt="PyTorch, AWS, Terraform, Docker, Cloudflare, PostgreSQL, SQLite, Linux, GitHub Actions, Git" height="48">
</p>

---

## Selected Projects

<img align="right" width="300" src="https://ethanstoner.dev/media/local-llm-lab-768.webp?v=1" alt="">

### [Local LLM Lab](https://github.com/ethanstoner/local-llm-lab): making a 7B model faster on one GPU, then taking it apart

A measurement framework for Qwen2.5-7B-Instruct on an RTX 4090. It finds where inference time goes, fixes the bottleneck, and tests how refusal works inside the network.

- Built a roofline from measured ceilings (947 GB/s, 157.5 TFLOP/s) with no fitted parameters. It showed the attention path copying the KV cache seven times per layer.
- Wrote a grouped-query decode path that reads each cached key and value once: **1.57x faster at 16k context, 1.65x at batch 32**, with no measurable fidelity loss against an FP32 reference.
- Removing one residual-stream direction takes refusal on harmful prompts from **95% to 0-2.5%**. Random directions of the same size do nothing.
- Paired ABBA benchmarks, and every headline number is a recorded run stored with its hardware, versions and commit. **173 tests.**

`Python` · `PyTorch` · `Transformers` · `CUDA`
<br clear="right">

<img align="right" width="300" src="https://ethanstoner.dev/media/kvstore-768.webp?v=1" alt="">

### [kvstore](https://github.com/ethanstoner/kvstore): a Redis-compatible database engine

An LSM-tree key-value store written from scratch in Java 21. `redis-cli`, `redis-py` and Jedis connect to it unmodified.

- Storage engine shaped like LevelDB/RocksDB: write-ahead log, memtable, sorted SSTables, leveled compaction and bloom filters.
- **~100K writes/s and ~130K reads/s** single-threaded (JMH, 100K keys). Bloom filters answer missing keys **~90x faster** by skipping the disk.
- Speaks Redis's RESP protocol over TCP, with TLS, multi-user auth, pub/sub and snapshots.
- **209 tests**, about 3,800 lines of Java plus 3,300 of tests.

`Java 21` · `LSM-Tree` · `RESP` · `Concurrency`
<br clear="right">

<img align="right" width="300" src="https://ethanstoner.dev/media/tempo-768.webp?v=1" alt="">

### [Tempo](https://github.com/ethanstoner/tempo-chess): a neural-network chess engine <sub>([live on Lichess](https://lichess.org/@/prospedplayer))</sub>

A chess engine written from scratch in C++20, with an NNUE evaluation trained in PyTorch on its own self-play games.

- Rated **2976 (95% CI 2933-3019)** from 300 games against Stockfish 19 capped at 2800-3190, on Stockfish's own scale at 10s + 0.1s. The first version rated 2688.
- The network trained on **120M self-play positions** beat the hand-written evaluation by **+175 ± 32 Elo**, and every retrain after it had to pass an SPRT match to ship.
- Lazy SMP search gains **+269 Elo** at 8 threads. Move generation matches all 32 published perft counts (610M nodes, ~113M nodes/s).
- Plays rated blitz on Lichess as a BOT account, currently around 2600.

`C++20` · `PyTorch` · `NNUE` · `CMake`
<br clear="right">

<img align="right" width="300" src="https://ethanstoner.dev/media/bytepair-768.webp?v=1" alt="">

### [bytepair](https://github.com/ethanstoner/bytepair): GPT-4's tokenizer, rebuilt in Rust

A byte-level BPE tokenizer with a Rust engine behind PyO3 bindings, and a pure-Python reference kept alongside it as the oracle.

- **1.6-2.2x faster than tiktoken** on one thread, with **zero mismatches** over 7.46M tokens on cl100k and o200k, plus a 1M-string fuzz.
- Trains a vocabulary **3.2-4.9x faster than Hugging Face tokenizers**, with merges identical to the Python reference.
- Hand-written pre-tokenizer splitters replace the regex engine and run **15.5-20x faster** than it.
- Refuses a literal `<|endoftext|>` in user text, which Hugging Face's GPT-4 port turns into the special token. **151 tests** (138 Python, 13 Rust), CI green.

`Rust` · `Python` · `PyO3` · `maturin`
<br clear="right">

<img align="right" width="300" src="https://ethanstoner.dev/media/heart-disease-audit-768.webp?v=1" alt="">

### [Heart Disease Audit](https://github.com/ethanstoner/heart-disease-audit): a reproducibility audit of a popular ML dataset

Traces the Kaggle Heart Failure Prediction CSV back to its four UCI hospital sources and measures what that changes.

- Found that the filled-in missing values encode the diagnosis: every filled `ST_Slope` is `Flat` for heart disease (111 of 111) and `Up` without it (191 of 191).
- Undoing the fill drops the typical pipeline's median accuracy from **86.4% to 79.3%** over 1,000 paired splits.
- A pre-registered survey of 30 public notebooks found **0 of 30** mention it. Every prediction was committed before its experiment ran, and 14 of 15 held up.
- Leave-one-hospital-out AUC is about **0.83**. **77 tests**, and all five notebooks run in CI.

`Python` · `pandas` · `scikit-learn` · `pytest`
<br clear="right">

<img align="right" width="300" src="https://ethanstoner.dev/media/landed-768.webp?v=1" alt="">

### [Landed](https://landedcards.com): pricing for card shops

Paste a TCGplayer link and get a whole-dollar sticker price for every condition, matched to what a buyer would pay online including shipping. I'm the sole engineer.

- Full stack on Cloudflare Workers, D1 and KV, with an hourly cron keeping prices current.
- Pricing engine written **twice on purpose**: a Python reference and the production TypeScript port, with golden tests asserting they match byte for byte.
- **371 automated tests.** Deployed but not yet in service: Clerk auth and Stripe billing are wired in test mode.

`TypeScript` · `Cloudflare Workers` · `D1` · `Stripe` · `Python`
<br clear="right">

<img align="right" width="300" src="https://ethanstoner.dev/media/genai-gateway-696.webp?v=1" alt="">

### GenAI Gateway on AWS: cloud deployment

Deployed AWS's [multi-provider GenAI gateway reference design](https://github.com/aws-solutions-library-samples/guidance-for-multi-provider-generative-ai-gateway-on-aws) from an empty repository to a working, TLS-secured endpoint, as a task set by Cisco professionals at Riffyx Labs. The architecture is AWS's; the deployment was mine. It was stood up end to end and then torn down.

- **~120 AWS resources in Terraform**: VPC, ECS Fargate, ALB, RDS, ElastiCache, WAF, Secrets Manager, Route 53 + ACM, remote S3 state.
- LiteLLM in front of Amazon Bedrock behind one OpenAI-compatible endpoint, with least-privilege IAM and per-key cost tracking.
- Traced a PII-masking defect in the Presidio sidecar to a dependency version, and fixed it with a controlled upgrade and regression tests.

`AWS` · `Terraform` · `ECS Fargate` · `Bedrock` · `LiteLLM`
<br clear="right">

---

## Open Source

**54 pull requests merged into 34 repositories totalling 511,000+ stars.** These are fixes in codebases I don't maintain, found by reading unfamiliar code, diagnosed by measurement and defended in review. The ten largest repositories:

| Repo | ★ | Merged | What it fixed |
|---|---|---|---|
| [withastro/astro](https://github.com/withastro/astro/pull/17861) | 62.9k | 1 | Fallback route generation swapped the locale as a substring, corrupting any path segment that merely started with the locale code. |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas/pull/67406) | 49.9k | 1 | `qcut` never validated `q`: a bad bin count raised the wrong error, or none at all. |
| [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view/pulls?q=is%3Apr+author%3Aethanstoner+is%3Amerged) | 44.3k | 3 | Kept `node:fs` out of the browser build, fixed 25 tests that failed on every Windows clone, and bounded CCTV media downloads with an idle deadline. |
| [psf/black](https://github.com/psf/black/pull/5411) | 41.9k | 1 | Formatting from a notebook crashed because it assumed every stdout has a `.buffer`. |
| [raysan5/raylib](https://github.com/raysan5/raylib/pull/6187) | 34.9k | 1 | `MatrixCompose()` read back vector components it had just overwritten, so most rotations produced a wrong matrix. |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading/pulls?q=is%3Apr+author%3Aethanstoner+is%3Amerged) | 34.2k | 3 | Reference links that resolve on GitHub and for the agent, and "newest first" history that really is, fixing three tests already failing on `main`. |
| [fmtlib/fmt](https://github.com/fmtlib/fmt/pull/4919) | 25.8k | 1 | A test target built from `format.cc` never inherited the library's `/utf-8`, so the pedantic build did not compile under MSVC. |
| [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect/pull/22980) | 23.9k | 1 | Jitter was drawn around the base interval instead of the backed-off one, so every caller silently lost its retry backoff. |
| [kivy/kivy](https://github.com/kivy/kivy/pulls?q=is%3Apr+author%3Aethanstoner+is%3Amerged) | 19.0k | 2 | KV bindings queued during `Builder.sync` were dropped, silently and forever. |
| [FreshRSS/FreshRSS](https://github.com/FreshRSS/FreshRSS/pull/9343) | 16.2k | 1 | The feed preview page skipped the URL-rewriting hook that subscribing ran, so extensions like RSS-Bridge were bypassed on the page that confirms a subscription. |

Plus 39 more merges across PyInstaller, OpenLayers, Simon Willison's llm, kornia, Unciv, node-gyp, Terser, SwiftFormat, Puma and 15 other repositories: [full list on ethanstoner.dev](https://ethanstoner.dev/open-source).

Two worth reading in full: [rakazo #322](https://github.com/elie222/rakazo/pull/322), where the reporter wrote "I cannot explain the root cause" and I narrowed it down by elimination, and [trueforge #464](https://github.com/truefoundry/trueforge/pull/464), where a reviewer asked whether an abort was needed and I measured it instead of arguing: `Promise.race` frees the caller but leaves the socket open.

---

## Experience

**Landed**, Founder & Solo Engineer · 2026 – Present<br>
Built and deployed a card-pricing tool as sole engineer across product, infrastructure and testing. 371 automated tests; billing wired in test mode, not yet in service.

**Roblox UGC**, Independent Creator · 2025 – Present<br>
Design and sell 3D avatar accessories made with a local-GPU generation pipeline: **15,200+ sales and 344k Robux (~$1.3k at the DevEx rate) in the past year.**

**Riffyx Labs**, Engineering Mentee · 2025 – 2026<br>
Deployed a multi-provider GenAI gateway on AWS end to end, provisioning ~120 resources with Terraform across ECS Fargate, RDS, ALB, WAF and Bedrock, with Guardrails and PII masking.

---

## More Work

| Project | What it does | Stack |
|---|---|---|
| [aibackflip](https://github.com/ethanstoner/aibackflip) | A humanoid learns to backflip on a 2D physics engine and PPO both written from scratch: 24 of 24 flips land, and 83% still land when shoved mid-flight. 313 tests. | `C++` `Python` `PyTorch` |
| [strata](https://github.com/ethanstoner/strata) | One Rust binary turns a folder of CT or MRI files into a browser viewer with hand-written WebGL2 volume rendering, ordering slices by scanner geometry rather than file index. 127 tests. | `Rust` `WebGL2` `TypeScript` |
| [Universe Simulator](https://github.com/ethanstoner/universe-simulator-cpp) | Newtonian N-body gravity from real astronomical data, with four integrators, Barnes-Hut or exact summation, and live energy diagnostics. 160 unit tests; CI runs the OpenGL self-test headlessly (41,005 checks). | `C++20` `OpenGL` `CMake` |
| [NeuroRacer](https://github.com/ethanstoner/neuro-racer) | Neuroevolution racing cars as a generalisation lab, with every claim pre-registered in git. The champion laps 43/43 clockwise test tracks and 0/42 counter-clockwise; training both ways makes 5/5 seeds lap all 100 in both directions. Includes a TypeScript track editor parity-tested against the trainer's NumPy checks, [live in the browser](https://neuroracer.ethanstoner.dev). | `Python` `NumPy` `TypeScript` |
| [RAG From Scratch](https://github.com/ethanstoner/rag-from-scratch) | 18 RAG techniques in plain Python, scored on 300 MultiHop-RAG queries with paired bootstrap CIs. A reranker lifts exact match from 0.563 to 0.667; CRAG and Self-RAG both hurt. | `Python` `Ollama` `pytest` |
| Pincer <sub>(private)</sub> | Closed-loop agent driving physical Android phones over ADB with a fine-tuned YOLO11 detector that labels its own training data. | `Python` `PyTorch` `YOLO11` |
| [Qorlyt](https://github.com/ethanstoner/3d-generator) | One image becomes a textured 3D model in under two minutes (median 107 s over 102 runs) on a local ComfyUI + Hunyuan3D 2.1 pipeline, behind FastAPI with live progress. | `Python` `FastAPI` `ComfyUI` |
| [CSUSM Campus Monitor](https://github.com/ethanstoner/csusm-monitor) | Counts people on live campus camera streams with an open-vocabulary grounding model, falling back to YOLOv8n without a GPU. 133 tests. | `Python` `FastAPI` `OpenCV` |
| [Lyric Generator](https://github.com/ethanstoner/lyric-generator) | Spotify link in, lyric video out, with Whisper word-level timing. | `Python` `FastAPI` `Whisper` |
| [Hunyuan3D-2.1 Install Guide](https://github.com/ethanstoner/Hunyuan3D-2.1-Complete-Install-Guide) | Step-by-step Windows install for Hunyuan3D-2.1 + ComfyUI. My most-starred repo. | `Docs` |

---

## Education & Certifications

- **Cal State San Marcos**, B.S. Computer Science · Fall 2026 – 2030 (expected)
- **Great Oak High School**, Temecula, CA, Diploma · June 2026
- **Anthropic:** Claude API, Amazon Bedrock, Vertex AI, Model Context Protocol (Advanced), Agent Skills, Claude Code ([all certificates](https://ethanstoner.dev/certifications))
- **OpenAI Academy:** Agents & Workflows, AI Foundations, Applied AI Foundations
- **AWS Certified Cloud Practitioner (CLF-C02):** exam in progress
