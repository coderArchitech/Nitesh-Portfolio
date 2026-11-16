# Blended version: Engineering Manager first, backed by Staff-level technical depth.
# Every number here comes from the original résumé or the public project repos.
# **text** marks bold.
from content import NAME, CONTACT, EDUCATION, EARLIER

HEADLINE = "Engineering Leader | People Manager & Hands-on Architect | Platform, Developer Productivity & AI"

SUMMARY = (
    "Engineering leader with **10+ years** in customer-facing platforms and distributed systems, including "
    "**4+ years managing teams** while staying hands-on in architecture. Lead **8 engineers** at Jazzx.ai (grown from 2) "
    "and previously led a **7-engineer** web and mobile team, owning hiring, performance, promotions, delivery and "
    "production reliability. Known for raising team speed and quality together: **daily zero-downtime releases**, "
    "**~40% faster PR turnaround**, **99.99% uptime** at **50K+ DAU**, and a measured rollout of AI-assisted engineering. "
    "Seeking **Engineering Manager** roles leading product or platform teams."
)

HIGHLIGHTS = [
    ("Team building", "grew a team **2 → 8 engineers**; **3 engineers promoted** to senior"),
    ("Reliability", "**99.99% uptime** for **50K+ DAU**; owned on-call, SLAs and post-incident reviews"),
    ("Delivery speed", "**daily zero-downtime releases**; **~40% faster** PR turnaround"),
    ("Backend scale", "**10M rows per run** through a RabbitMQ microservices pipeline; REST APIs for **100K peak users**"),
    ("Distributed systems", "BFF services over **gRPC** with **Kafka**; notification microservice for **100K users**"),
    ("Automation", "**12 workflows** automated (Node.js, BPMN): **90% faster** processing, **$200K/yr** saved"),
    ("AI platform", "RAG over **150,000 documents** for **~500 users**, with no model retraining"),
    ("Frontend platform", "**100+ component** design system (**60% faster** feature work); **45% faster** page load"),
]

SKILLS = [
    ("Leadership", "Hiring & Interviewing, Performance Management, Career Development & Promotions, 1:1 Coaching, "
                   "OKRs & Goal-Setting, Technical Strategy, Stakeholder & Vendor Management"),
    ("Delivery & Operations", "Agile/Scrum, Delivery & Capacity Planning, RFCs & Technical Design Documents, SLAs, "
                              "On-call & Incident Management, Post-incident Reviews, DORA Metrics"),
    ("Architecture", "Distributed Systems, Microservices, Event-Driven Architecture, BFF, REST, GraphQL, gRPC, Kafka, RabbitMQ"),
    ("Cloud & DevOps", "AWS (Lambda, ECS, RDS/Aurora, API Gateway, CloudFront, SQS/SNS), Docker, Kubernetes, Terraform, GitHub Actions"),
    ("AI / LLM", "RAG, LangChain, LangGraph, Vector Databases (Pinecone, Milvus, AWS Kendra), Claude Code, OpenAI Codex, "
                 "GitHub Copilot, LLM-assisted Code Review"),
    ("Stack & Quality", "TypeScript, Node.js, Python, React, React Native, Next.js; PostgreSQL, MongoDB, Redis, DynamoDB; "
                        "New Relic, Sentry, OpenTelemetry; TDD, Jest, Cypress, WCAG 2.1"),
]

ROLES = [
    {
        "title": "Staff Software Engineer", "company": "Jazzx.ai",
        "where": "Bengaluru, India", "when": "September 2025 – Present",
        "scope": "People manager and technical lead for 8 engineers, owning architecture, delivery and SLAs for a "
                 "customer-facing mortgage-origination platform built with US-based engineering and Platform teams.",
        "groups": [
            ("Leadership & Delivery", [
                "Own **hiring end to end** and ran hiring drives that **grew the team from 2 to 8 engineers**.",
                "Own **performance reviews and career development**; run structured 1:1s that moved junior developers "
                "to independent feature ownership.",
                "Set **quarterly OKRs** with Product; run sprint planning, grooming and retrospectives to keep delivery predictable.",
                "Coordinate ownership and handoffs across **US–India teams** for continuous delivery and production support across time zones.",
                "Own **platform-level SLAs** and **lead post-incident reviews**, driving corrective actions that reduced recurring production issues.",
            ]),
            ("Architecture & Engineering", [
                "Own **end-to-end architecture** of the React/TypeScript platform; set standards through **RFCs**, a shared "
                "component architecture and design tokens.",
                "Built test-scaffolding tooling and a **TDD-first GitHub Actions pipeline**: **~40% faster PR turnaround** "
                "and **daily zero-downtime releases**.",
                "Led the rollout of **AI-assisted and agentic workflows** (Claude Code, Codex, Copilot, LLM-assisted PR review), "
                "measuring quality and productivity before scaling team-wide.",
                "Architected a **RAG platform** for real-time Q&A across **150,000 private mortgage documents** for **~500 users**, "
                "with no model retraining.",
                "Led the team to **cut initial page-load time by 45%** through code splitting, lazy loading and bundle optimization.",
            ]),
        ],
    },
    {
        "title": "Lead Software Engineer", "company": "Hella Infra Market",
        "where": "Bengaluru, India", "when": "January 2022 – August 2025",
        "scope": "People manager and technical lead for a 7-engineer web and mobile team building customer-facing B2B "
                 "platforms serving 50K+ daily active users.",
        "groups": [
            ("Leadership & Delivery", [
                "Owned **hiring, onboarding, performance and mentoring**; **3 engineers promoted to senior**.",
                "Led technical planning with engineering and business stakeholders, balancing scope, architecture, quality and capacity.",
                "**Owned the production on-call rotation** and incident response for platforms running at **99.99% uptime**.",
                "Partnered with the Director of Engineering to **introduce DORA metrics**; ran the company **Hackathon and Bugathon**.",
                "Co-led **Shalimar Experts**, a B2B loyalty platform for painters: **15K MAU** (target 500K), "
                "**₹2 Cr+ in rewards per quarter**.",
            ]),
            ("Architecture & Engineering", [
                "Architected a **React/React Native platform**: **50K+ DAU**, **99.99% uptime**, Lighthouse **95+**.",
                "Designed **BFF services over gRPC** with **Kafka** for asynchronous messaging and third-party integrations.",
                "Led the team to build a **100+ component TypeScript/Storybook design system**, cutting feature development time by **60%**.",
                "Established **TDD (85%+ frontend coverage)** and observability with New Relic and Sentry; the team cut "
                "**bundle size by 50%** and **load time by 40%**.",
                "Led the replacement of a third-party support tool (Zuper) with an **in-house platform**, projected to "
                "**cut support-team workload by 75%**.",
            ]),
        ],
    },
    {
        "title": "Senior Software Engineer", "company": "Simpplr",
        "where": "Gurgaon, India", "when": "May 2021 – November 2021",
        "groups": [(None, [
            "Designed a **notification microservice** and scheduled newsletter workflows (daily, weekly, monthly) for "
            "**100K users**; authored the technical design documents.",
        ])],
    },
    {
        "title": "Senior Consultant", "company": "Xebia IT Architects",
        "where": "Gurgaon, India", "when": "August 2020 – May 2021",
        "groups": [(None, [
            "Partnered with **U.A.E. government stakeholders** on platforms serving **1M+ MAU**; automated **12 manual workflows** "
            "with Node.js and BPMN, cutting processing time by **90%** and saving **$200K a year**.",
        ])],
    },
]

PROJECTS = [
    ("Sidekick", "github.com/coderArchitech/Sidekick", "https://github.com/coderArchitech/Sidekick",
     "Private, real-time AI meeting copilot (**Rust, Tauri 2, React 19**): live transcription, question detection and "
     "cited answers via hybrid retrieval. Run like a team product: PRD, **15 ADRs**, a **15-crate** Rust workspace, CI on **3 OSes**."),
    ("Flipbook", "github.com/coderArchitech/flipbook", "https://github.com/coderArchitech/flipbook",
     "Self-hosted publishing studio (**Node.js 24, React 19, Three.js, SQLite**): visual editor, WebGL page-turn reader and "
     "a background PDF-export worker; PRD, HLD/LLD and Playwright tests on desktop and mobile."),
]
