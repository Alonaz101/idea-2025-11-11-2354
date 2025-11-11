# Project Overview

This repository implements the meal recommendation application with features defined in Jira issues SCRUM-302 to SCRUM-309, including:

- **SCRUM-302:** MVP Architecture and Core Components including backend API and OAuth authentication.
- **SCRUM-303:** Data Models for User, Mood, Recipe, UserMoodEntry, RecipeRating.
- **SCRUM-304:** API endpoints for mood entry, recipe retrieval, rating submission, mood history.
- **SCRUM-305:** Security, privacy, and compliance features such as OAuth 2.0, role-based access, GDPR and CCPA considerations.
- **SCRUM-306:** Performance and scalability via Redis caching, DB indexing preparation, and cloud deployment readiness.
- **SCRUM-307:** Testing framework with unit and integration tests covering API and recommendation logic.
- **SCRUM-308:** Post-MVP features and analytics including user feedback data model, feedback APIs, analytics dashboards (planned).
- **SCRUM-309:** Future expansions including AI mood detection, smart device integration, collaborative meal planning service (planned).

The backend is implemented in Python using Flask and SQLAlchemy for ORM. OAuth 2.0 is stubbed for authentication.

Caching uses Redis for scalability. Testing uses unittest framework.

Further enhancements will be added as per the post-MVP and future phase issues.
