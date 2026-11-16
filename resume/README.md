# Résumé: review guide

This folder holds your résumé in three versions. Read this before you send any of them.

## Files

| File | Use it for |
|---|---|
| `Nitesh-Kumar-Resume.pdf` / `.docx` | **Main version (recommended).** Engineering Manager first, backed by Staff-level technical depth. Use for most EM applications. The website's download button serves this one. |
| `Nitesh-Kumar-Resume-EM.pdf` / `.docx` | Conventional EM version. Its Key Impact block holds only the four backend items (Backend scale, Distributed systems, Automation, AI platform); leadership results are carried by the summary and the bullets. Use it if a recruiter asks for something more conventional. |
| `Nitesh-Kumar-Resume-Staff-TLM.pdf` / `.docx` | Engineering-first version for Staff Engineer, Tech Lead Manager and AI engineering-lead roles. |
| `source/` | The text and build scripts that generate all three (see "Editing and rebuilding" below). |

All versions are 2 pages, use the same titles and dates, and contain **no invented numbers**.

## Which version to send

| Role you're applying for | Send |
|---|---|
| Engineering Manager at a startup or scale-up | Main |
| EM for a backend, platform or distributed-systems team | Main: four Key Impact lines are backend (Backend scale, Distributed systems, Automation, AI platform) |
| EM, Developer Productivity / Platform / DevEx | Main, unchanged: Delivery speed and Frontend platform are already in Key Impact |
| India engineering centre of a US company (fintech, lending) | Main |
| Engineering Manager at a large company with a strict format | EM |
| Staff Engineer, Tech Lead Manager, Engineering Lead | Staff/TLM |
| AI / LLM engineering lead | Staff/TLM |

## Why the main version is built for EM shortlists

No résumé guarantees a job, but this one is shaped around how EM candidates are screened.

1. **The 6-second scan.** Recruiters read the headline, the first summary sentence and the top of the first job.
   - The headline says *People Manager*.
   - The summary says *4+ years managing teams* and ends with *Seeking Engineering Manager roles*.
   - Key Impact puts eight results with numbers above the fold, balanced across leadership, backend, AI and frontend.
2. **Keyword searches.** Recruiters and applicant-tracking systems search for "Engineering Manager", "people manager", "hiring", "performance management", "OKRs", "on-call", "SLA" and "DORA". All of these appear in the text.
3. **Titles vs scope.** Your titles are Staff Software Engineer and Lead Software Engineer. Each role opens with a scope line ("People manager and technical lead for 8 engineers…") so readers see management responsibility straight away.
4. **Management first, then engineering.** In both recent roles, *Leadership & Delivery* comes before *Architecture & Engineering*. This shows you can lead people and still go deep technically, which is what most EM interview loops test.
5. **Results, not activities.** Bullets end in outcomes: team growth, promotions, uptime, release frequency, PR turnaround.
6. **Two pages, nothing repeated.** Earlier roles are compressed, and there is no repeated bullet across jobs.

## Every number, and where it came from

You should be able to explain each of these in an interview. All of them come from your original résumé, except the project numbers, which come from the public GitHub repos.

| Number | Where it appears | Source |
|---|---|---|
| 10+ years experience, 4+ years managing teams | Summary | Résumé dates (2016 →; leading teams since Jan 2022) |
| Team grown 2 → 8 engineers | Summary, Key Impact, Jazzx.ai | Original résumé |
| 7-engineer team; 3 promoted to senior | Summary, Key Impact, Hella | Original résumé |
| 99.99% uptime, 50K+ DAU, Lighthouse 95+ | Summary, Key Impact, Hella | Original résumé |
| Daily zero-downtime releases; ~40% faster PR turnaround | Summary, Key Impact, Jazzx.ai | Original résumé |
| 45% faster initial page load | Key Impact (Frontend platform), Jazzx.ai | Original résumé |
| 150,000 documents, ~500 users (RAG) | Key Impact, Jazzx.ai | Original résumé |
| 100+ components, 60% faster feature development | Key Impact (Frontend platform), Hella | Original résumé |
| 85%+ test coverage; 50% smaller bundle; 40% faster load | Hella | Original résumé |
| 75% support-workload reduction (projected) | Hella | Original résumé |
| Shalimar Experts: 15K MAU (target 500K), ₹2 Cr+ rewards per quarter | Hella | Original résumé |
| 100K users (Simpplr notification microservice) | Key Impact (Distributed systems), Simpplr | Original résumé |
| 1M+ MAU, 12 workflows, 90% faster, $200K/yr (Xebia) | Key Impact (Automation), Xebia | Original résumé |
| 10M rows per run (To The New); 100K peak users (Infogain) | Key Impact (Backend scale), Earlier Experience | Original résumé |
| BFF over gRPC with Kafka | Key Impact (Distributed systems), Hella | Original résumé |
| 15 ADRs, 15-crate Rust workspace, CI on 3 OSes | Projects | Sidekick repo |

## Prepare a story for each Key Impact line

Interviewers will pick from the Key Impact block. Have a 2-minute answer ready for each (situation, what *you* did, result, what you'd do differently):

- **Team building (2 → 8, 3 promotions):** how you ran hiring, what you looked for, how you built promotion cases.
- **Reliability (99.99%, on-call, SLAs):** a real incident, the post-incident review, and the fix that stopped it recurring.
- **Delivery speed (daily releases, ~40% faster PRs):** what was slow before, what you changed, how you measured it.
- **Backend scale (10M rows per run):** how the RabbitMQ pipeline handled throughput, retries and failures.
- **Distributed systems (BFF, gRPC, Kafka):** why a BFF, why gRPC between services, and how you handled consistency and message failures.
- **Automation ($200K/yr, 90% faster):** how you picked which workflows to automate and how you measured the savings.
- **AI platform (RAG, 150,000 docs):** retrieval design and evaluation, and how you decided what to measure before rolling AI tools out to the team.
- **Frontend platform (design system, 45% faster load):** how you got the design system adopted across teams and kept performance from regressing.

## Before you send: checklist

- [ ] **Jazzx.ai start date:** the résumé says September 2025. Your old website said November 2025. Use the date on your offer letter.
- [ ] **OKRs:** listed under Jazzx.ai. Move the bullet if you ran OKRs at Hella instead.
- [ ] **Titles match your records:** Staff Software Engineer (Jazzx.ai) and Lead Software Engineer (Hella Infra Market) should match LinkedIn and your relieving letters.
- [ ] **LinkedIn headline** matches the résumé headline, and your experience entries have the same scope lines.
- [ ] **File name** when uploading: `Nitesh-Kumar-Resume.pdf` (already set).
- [ ] **Per-application tweak:** reorder Key Impact so the most relevant line for that job comes first.

## Numbers that would make it stronger

These are the most common questions in EM interviews. None are in the résumé because I don't have the numbers. If you have any, add them where shown:

| Add | Where | Example wording |
|---|---|---|
| Sprint predictability | Jazzx.ai, OKRs bullet | "…keeping delivery predictable (**[X]%** of committed scope delivered per sprint)." |
| Hiring speed or quality | Jazzx.ai, hiring bullet | "…grew the team from 2 to 8 engineers in **[N] months** with **[X]%** offer acceptance." |
| Retention | Summary or Jazzx.ai | "…with **no regretted attrition**." (only if true) |
| Incident trend | Jazzx.ai, SLA bullet | "…reduced repeat P1 incidents by **[X]%** / MTTR from **[A]** to **[B]**." |
| DORA before/after | Hella, DORA bullet | "…deployment frequency from **[weekly]** to **[daily]**." |
| Actual support savings | Hella, Zuper bullet | Replace "projected to cut… by 75%" with the measured figure. |
| OKR results | Jazzx.ai, OKRs bullet | "…delivered **[N] of [M]** key results last quarter." |

Even two of these noticeably strengthen an EM application.

## Editing and rebuilding

- **Quick edits:** open the `.docx` in Word or Google Docs, edit, and export to PDF. Keep it to 2 pages.
- **Rebuild all versions** (keeps them consistent; the text lives in `source/content*.py`):

```bash
cd resume/source
```

```bash
python3 build.py content_blend out Nitesh-Kumar-Resume && node print.js out Nitesh-Kumar-Resume
```

```bash
python3 build.py content_em out Nitesh-Kumar-Resume-EM && node print.js out Nitesh-Kumar-Resume-EM
```

```bash
python3 build.py content_staff out Nitesh-Kumar-Resume-Staff-TLM && node print.js out Nitesh-Kumar-Resume-Staff-TLM
```

The build needs Python with `python-docx`, Node.js with Playwright and Chromium, and the Carlito or Calibri font.
