# Threat Intelligence Dashboard

A lightweight web dashboard for visualizing Open Source Intelligence (OSINT) findings, Indicators of Compromise (IOCs), and threat actor patterns. Built with Python Flask and designed for SOC analyst workflows.

## Purpose

During my internship, I observed analysts manually reviewing text-based OSINT reports. This dashboard transforms raw intelligence into actionable visualizations for faster decision-making.

## Features

- **IOC Management**: Track and categorize IPs, domains, hashes, and emails
- **Threat Actor Profiles**: Visualize TTPs (Tactics, Techniques, Procedures)
- **Timeline View**: Chronological attack progression
- **Risk Scoring**: Automated severity assessment
- **Export**: Generate incident response briefings

## Tech Stack

- Python 3.10+
- Flask (web framework)
- SQLite (database)
- Chart.js (visualizations)
- Bootstrap 5 (UI)

## Installation

```bash
git clone https://github.com/ZeakMeadows/threat-intel-dashboard.git
cd threat-intel-dashboard
pip install -r requirements.txt
python app.py
```
## What I Learned

- Full-stack web application development
- Database design for security data
- Threat intelligence lifecycle (collection to analysis to dissemination)
- Secure coding practices for web applications

## Future Improvements

- [ ] Integrate with MISP threat sharing platform
- [ ] Add MITRE ATT&CK matrix mapping
- [ ] Implement user authentication and RBAC
- [ ] Deploy to AWS with HTTPS
