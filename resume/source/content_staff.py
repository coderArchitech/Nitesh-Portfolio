# Staff Engineer / Tech Lead Manager version: engineering first, leadership second.
# **text** marks bold.
from content import NAME, CONTACT, EDUCATION

HEADLINE = "Staff Software Engineer / Tech Lead Manager | Platform Architecture, Distributed Systems & AI"

SUMMARY = (
    "Staff-level engineer and tech lead manager with **10+ years** designing and shipping customer-facing platforms "
    "and distributed systems. Own architecture end to end, from React/TypeScript front ends and BFF services to "
    "event-driven backends on AWS, while leading teams of up to **8 engineers**. Recent work: a **RAG platform** over "
    "**150,000 documents**, **daily zero-downtime releases**, **~40% faster PR turnaround** through AI-assisted "
    "workflows, and a **50K+ DAU** platform at **99.99% uptime**. Comfortable moving between deep technical work "
    "and running a team across **US–India** time zones."
)

SKILLS = [
    ("Architecture", "Distributed Systems, Microservices, Event-Driven Architecture, BFF, REST, GraphQL, gRPC, Kafka, "
                     "RabbitMQ, Design Systems, Web Performance"),
    ("Languages & Frameworks", "TypeScript, JavaScript, Python, Node.js, Express.js, React, React Native, Next.js, "
                               "Redux Toolkit, Apollo Client"),
    ("Cloud & DevOps", "AWS (Lambda, ECS, RDS/Aurora, API Gateway, CloudFront, S3, SQS/SNS), Docker, Kubernetes, "
                       "Terraform, GitHub Actions, GoCD, Jenkins"),
    ("AI / LLM", "RAG, LangChain, LangGraph, Vector Databases (Pinecone, Milvus, AWS Kendra), Claude Code, OpenAI Codex, "
                 "GitHub Copilot, LLM-assisted Code Review, Automated Test Generation"),
    ("Data", "PostgreSQL, MongoDB, Redis, DynamoDB"),
    ("Reliability & Quality", "New Relic, Sentry, CloudWatch, OpenTelemetry, SLAs, Incident Response, TDD, BDD, Jest, "
                              "React Testing Library, Cypress, WCAG 2.1, OWASP"),
    ("Technical Leadership", "RFCs & Technical Design Documents, Technical Strategy, Code Review, Mentoring, Hiring, "
                             "Performance Management, OKRs, Agile/Scrum, Stakeholder Management"),
]

ROLES = [
    {
        "title": "Staff Software Engineer", "company": "Jazzx.ai",
        "where": "Bengaluru, India", "when": "September 2025 – Present",
        "scope": "Technical lead and people manager for a team of 8 engineers, owning the architecture of a "
                 "customer-facing mortgage-origination platform built with US-based teams.",
        "groups": [
            ("Architecture & Engineering", [
                "Own **end-to-end architecture** of the React/TypeScript mortgage-origination platform; defined "
                "standards through **RFCs**, a shared component architecture and **design tokens**.",
                "Architected a **RAG platform** for real-time Q&A across **150,000 private mortgage documents** and "
                "internal knowledge bases for ~500 users, without model retraining.",
                "Built tooling that **auto-generates unit-test scaffolding** and a **TDD-first GitHub Actions pipeline**, "
                "cutting average **PR turnaround by ~40%** and enabling **daily zero-downtime releases**.",
                "Cut **initial page-load time by 45%** through code splitting, lazy loading and Webpack bundle optimization.",
                "Evaluated and rolled out **agentic engineering workflows** (Claude Code, OpenAI Codex, GitHub Copilot, "
                "LLM-assisted PR review), measuring quality and productivity before scaling them.",
            ]),
            ("Technical Leadership", [
                "Own hiring, performance reviews and mentoring; **grew the team from 2 to 8 engineers**.",
                "Own **platform-level SLAs** with Platform and infrastructure teams and **lead post-incident reviews**, "
                "driving fixes that reduced recurring production issues.",
                "Set **quarterly OKRs** with Product and coordinate handoffs across **US–India teams** for continuous delivery.",
            ]),
        ],
    },
    {
        "title": "Lead Software Engineer", "company": "Hella Infra Market",
        "where": "Bengaluru, India", "when": "January 2022 – August 2025",
        "scope": "Technical lead and people manager for a 7-engineer web and mobile team building customer-facing "
                 "B2B platforms serving 50K+ daily active users.",
        "groups": [
            ("Architecture & Engineering", [
                "Architected a **React/React Native platform** serving **50K+ DAU at 99.99% uptime** with Lighthouse scores of **95+**.",
                "Designed **BFF services** communicating with downstream microservices over **gRPC**, with **Kafka** for "
                "asynchronous messaging and third-party integrations.",
                "Built a **100+ component TypeScript/Storybook design system**, cutting feature development time by **60%**.",
                "Cut **bundle size by 50%** and **load time by 40%** through Webpack optimization and caching; "
                "established **85%+ frontend test coverage** with TDD.",
                "Set up production observability with **New Relic and Sentry**, improving system-health visibility and incident response.",
                "Led the replacement of a third-party support tool (Zuper) with an **in-house platform**, projected to "
                "**reduce support-team workload by 75%**.",
            ]),
            ("Technical Leadership", [
                "Owned hiring, onboarding and mentoring for the team; **3 engineers promoted to senior**.",
                "**Owned the production on-call rotation**, partnered with the Director to **introduce DORA metrics**, "
                "and ran the company **Hackathon and Bugathon**.",
                "Co-led **Shalimar Experts**, a B2B loyalty platform with **15K MAU** supporting **₹2 Cr+ in rewards per quarter**.",
            ]),
        ],
    },
    {
        "title": "Senior Software Engineer", "company": "Simpplr",
        "where": "Gurgaon, India", "when": "May 2021 – November 2021",
        "groups": [(None, [
            "Designed and built a **notification microservice** for scalability and reliability, plus scheduled newsletter "
            "workflows (daily, weekly, monthly) serving **100K users**; authored the technical design documents.",
        ])],
    },
    {
        "title": "Senior Consultant", "company": "Xebia IT Architects",
        "where": "Gurgaon, India", "when": "August 2020 – May 2021",
        "groups": [(None, [
            "Automated **12 manual workflows** with Node.js and BPMN for U.A.E. government platforms serving **1M+ MAU**, "
            "cutting processing time by **90%** and saving **$200K a year**.",
        ])],
    },
]

EARLIER = [
    ("Senior Software Engineer, To The New", "Noida | Jan 2020 – Jul 2020",
     "High-throughput tax-processing backend handling **10M rows per run**; asynchronous microservices over RabbitMQ."),
    ("Software Engineer, ThinkSys", "Noida | Apr 2018 – Jan 2020",
     "REST APIs and Stripe payments; scalable real-time features with **Socket.IO and Redis**; reusable backend libraries."),
    ("Software Engineer, Infogain", "Noida | Jan 2016 – Apr 2018",
     "REST APIs for up to **100K peak users**; modernized a legacy codebase; authored technical design documents."),
]

PROJECTS = [
    ("Sidekick", "github.com/coderArchitech/Sidekick", "https://github.com/coderArchitech/Sidekick",
     "Private, real-time AI meeting copilot. **Rust (15-crate Cargo workspace), Tauri 2, React 19**, SQLite with "
     "sqlite-vec and SQLCipher; hybrid vector + keyword retrieval with cited answers; pluggable speech-to-text and LLM "
     "providers (Claude, OpenAI, Gemini, Ollama); 15 ADRs; CI on Windows, macOS and Linux."),
    ("Flipbook", "github.com/coderArchitech/flipbook", "https://github.com/coderArchitech/flipbook",
     "Self-hosted publishing studio. **Node.js 24, Express 5, React 19, Three.js**, node:sqlite with a durable job "
     "queue; WebGL page-turn reader and a background PDF-export worker with no headless browser; Playwright, Vitest "
     "and integration tests."),
]
