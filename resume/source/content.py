# Résumé content, shared by the HTML/PDF and DOCX builders.
# **text** marks bold.

NAME = "Nitesh Kumar"
HEADLINE = "Engineering Leader | People Management, Platform Engineering & Distributed Systems"
CONTACT = [
    ("Bengaluru, India", None),
    ("+91-7042512363", "tel:+917042512363"),
    ("nitesh.kumar07091993@gmail.com", "mailto:nitesh.kumar07091993@gmail.com"),
    ("linkedin.com/in/nitesh-kumar-architect", "https://linkedin.com/in/nitesh-kumar-architect"),
    ("github.com/coderArchitech", "https://github.com/coderArchitech"),
]

SUMMARY = (
    "Engineering leader with **10+ years** building customer-facing platforms and distributed systems, "
    "including **4+ years leading teams** with full people-management responsibility. Currently lead a team of "
    "**8 engineers** at Jazzx.ai (grown from 2), owning hiring, performance, career growth, architecture and delivery. "
    "Track record of team outcomes: **3 engineers promoted to senior**, **99.99% uptime** at 50K+ DAU, "
    "**daily zero-downtime releases** and **~40% faster PR turnaround** through TDD, observability and AI-assisted "
    "workflows. Experienced running on-call, post-incident reviews and delivery across **US–India** time zones."
)

SKILLS = [
    ("Leadership", "Hiring & Interviewing, Performance Management, Career Development & Promotions, 1:1 Coaching, "
                   "OKRs & Goal-Setting, Technical Strategy, Stakeholder Management, Vendor Management"),
    ("Delivery & Operations", "Agile/Scrum, Delivery & Capacity Planning, RFCs & Technical Design Documents, SLAs, "
                              "On-call & Incident Management, Post-incident Reviews, DORA Metrics"),
    ("Architecture", "Distributed Systems, Microservices, Event-Driven Architecture, BFF, REST, GraphQL, gRPC, Kafka, RabbitMQ"),
    ("Cloud & DevOps", "AWS (Lambda, ECS, RDS/Aurora, API Gateway, CloudFront, SQS/SNS), Docker, Kubernetes, Terraform, "
                       "GitHub Actions, GoCD, Jenkins"),
    ("Observability & Quality", "New Relic, Sentry, CloudWatch, OpenTelemetry, TDD, BDD, Jest, React Testing Library, "
                                "Cypress, WCAG 2.1, OWASP"),
    ("Languages & Data", "TypeScript, JavaScript, Python, Node.js, React, React Native, Next.js; "
                         "PostgreSQL, MongoDB, Redis, DynamoDB"),
    ("AI / LLM", "RAG, LangChain, LangGraph, Claude Code, OpenAI Codex, GitHub Copilot, LLM-assisted Code Review, "
                 "Vector Databases (Pinecone, Milvus, AWS Kendra)"),
]

# Each role: title, company, location, dates, scope line, list of (group heading or None, bullets)
ROLES = [
    {
        "title": "Staff Software Engineer", "company": "Jazzx.ai",
        "where": "Bengaluru, India", "when": "September 2025 – Present",
        "scope": "Lead a team of 8 engineers with full people-management responsibility, building a customer-facing "
                 "mortgage-origination platform with US-based engineering and Platform teams.",
        "groups": [
            ("Team & Delivery Leadership", [
                "Own **hiring end to end** (sourcing, interviews, assessment, onboarding) and ran hiring drives that "
                "**grew the team from 2 to 8 engineers**.",
                "Own **performance reviews and career development**; run structured 1:1s that moved junior developers "
                "toward independent feature ownership.",
                "Set **quarterly OKRs** with Product and run sprint planning, grooming and retrospectives to keep delivery predictable.",
                "Coordinate ownership and handoffs across **US–India teams**, enabling continuous delivery and production support across time zones.",
                "Own **platform-level SLAs** for the mortgage application and **lead post-incident reviews**, driving "
                "corrective actions that reduced recurring production issues.",
            ]),
            ("Engineering & Platform", [
                "Own **end-to-end architecture** of the React/TypeScript platform; set engineering standards through "
                "**RFCs**, a shared component architecture and design tokens.",
                "Led the rollout of **AI-assisted and agentic workflows** (Claude Code, OpenAI Codex, GitHub Copilot, "
                "LLM-assisted PR review), measuring quality and productivity before scaling them team-wide.",
                "Introduced test-scaffolding tooling and a **TDD-first GitHub Actions pipeline**; the team cut average "
                "**PR turnaround by ~40%** and now ships **daily zero-downtime releases**.",
                "Led the team to **cut initial page-load time by 45%** through code splitting, lazy loading and bundle optimization.",
                "Architected a **RAG platform** for real-time Q&A across **150,000 private mortgage documents** for ~500 users, without model retraining.",
            ]),
        ],
    },
    {
        "title": "Lead Software Engineer", "company": "Hella Infra Market",
        "where": "Bengaluru, India", "when": "January 2022 – August 2025",
        "scope": "Led a 7-engineer web and mobile team with people-management responsibility, building customer-facing "
                 "B2B platforms serving 50K+ daily active users.",
        "groups": [
            ("Team & Delivery Leadership", [
                "Owned **hiring, onboarding, performance and mentoring** for the team; **3 engineers promoted to senior**.",
                "Led technical planning with engineering and business stakeholders, balancing product scope, architecture, quality and team capacity.",
                "**Owned the production on-call rotation** and incident response for customer-facing platforms running at **99.99% uptime**.",
                "Partnered with the Director of Engineering to **introduce DORA metrics**, and **ran the company Hackathon and Bugathon**.",
                "Co-led **Shalimar Experts**, a B2B loyalty platform for painters with **15K MAU**, supporting **₹2 Cr+ in rewards per quarter**.",
            ]),
            ("Engineering & Platform", [
                "Architected a React/React Native platform serving **50K+ DAU at 99.99% uptime** with Lighthouse scores of 95+.",
                "Led the team to build a **100+ component TypeScript/Storybook design system**, cutting feature development time by **60%**.",
                "Established a **TDD-first culture (85%+ frontend coverage)** and production observability with New Relic and Sentry; "
                "the team cut bundle size by **50%** and load time by **40%**.",
                "Designed **BFF services over gRPC** with **Kafka** for asynchronous messaging and third-party integrations.",
                "Led the replacement of a third-party support tool (Zuper) with an in-house platform, projected to "
                "**reduce support-team workload by 75%**.",
            ]),
        ],
    },
    {
        "title": "Senior Software Engineer", "company": "Simpplr",
        "where": "Gurgaon, India", "when": "May 2021 – November 2021",
        "groups": [(None, [
            "Designed a **notification microservice** and scheduled newsletter workflows (daily, weekly, monthly) for "
            "**100K users**; authored the technical design documents that guided implementation.",
        ])],
    },
    {
        "title": "Senior Consultant", "company": "Xebia IT Architects",
        "where": "Gurgaon, India", "when": "August 2020 – May 2021",
        "groups": [(None, [
            "Partnered with **U.A.E. government stakeholders** to digitize platforms serving **1M+ MAU**; automated "
            "**12 manual workflows** with Node.js and BPMN, cutting processing time by **90%** and saving **$200K a year**.",
        ])],
    },
]

EARLIER = [
    ("Senior Software Engineer, To The New", "Noida | Jan 2020 – Jul 2020",
     "High-throughput tax-processing backend handling **10M rows per run** with RabbitMQ and asynchronous microservices."),
    ("Software Engineer, ThinkSys", "Noida | Apr 2018 – Jan 2020",
     "REST APIs and Stripe payments; real-time features with Socket.IO and Redis; shared backend libraries."),
    ("Software Engineer, Infogain", "Noida | Jan 2016 – Apr 2018",
     "REST APIs for up to **100K peak users**; modernized a legacy codebase; authored technical design documents."),
]

PROJECTS = [
    ("Sidekick", "github.com/coderArchitech/Sidekick", "https://github.com/coderArchitech/Sidekick",
     "Private, real-time AI meeting copilot (Rust, Tauri 2, React): live transcription, question detection and "
     "cited answers from your documents. Built like a team product: PRD, 15 ADRs, a 15-crate Rust workspace and CI on 3 OSes."),
    ("Flipbook", "github.com/coderArchitech/flipbook", "https://github.com/coderArchitech/flipbook",
     "Self-hosted publishing studio (Node.js, React, Three.js, SQLite): visual editor, WebGL page-turn reader and a "
     "background PDF-export worker, with PRD, HLD/LLD and Playwright tests on desktop and mobile."),
]

EDUCATION = ("Bachelor of Engineering, Computer Science", "Panjab University (PUSSGRC)", "2012 – 2016")
