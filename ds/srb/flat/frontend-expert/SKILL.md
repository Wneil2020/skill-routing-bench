---
name: frontend-expert
description: "Use when Review and improve React component architecture, Vite build performance, Core Web Vitals, and testing strategy. Use when the user asks about: covers frontend, expert, 프론트엔드, 감사, vitals"
metadata:
  holon-triggers: |
    component refactoring
    bundle optimization
---

---
name: frontend-expert
description: >-
  Review and improve React component architecture, Vite build performance, Core
  Web Vitals, and testing strategy. Use when the user asks about frontend code
  review, component refactoring, bundle optimization, or frontend testing gaps.
  Do NOT use for building new UI from scratch (use frontend-design), UX audits
  or accessibility evaluation (use ux-expert), or writing Playwright E2E tests
  (use e2e-testing). Korean triggers: "프론트엔드", "감사", "리뷰", "테스트".
metadata:
  version: "1.0.0"
  category: "review"
  author: "thaki"
---
# Frontend Expert

Specialist for the React 18 + TypeScript + Vite 6 + Tailwind CSS frontend at `frontend/`.

## Key Directories

- `frontend/src/components/` — Reusable UI components
- `frontend/src/features/` — Feature modules (admin, auth, call, chatbot, dashboard, knowledge, summary)
- `frontend/src/hooks/` — Custom React hooks
- `frontend/src/stores/` — Zustand state stores (authStore, callStore, chatStore)
- `frontend/src/config/` — API clients, env config
- `frontend/src/lib/` — Utilities (api.ts, cn.ts)
- `frontend/src/i18n/` — Internationalization (react-i18next)
- `frontend/src/test/` — Test setup and helpers

## Component Architecture Review

### Checklist

- [ ] Components follow single-responsibility principle
- [ ] Presentational vs container separation is clear
- [ ] Props are typed with TypeScript interfaces (not `any`)
- [ ] Zustand stores are scoped (no god-store)
- [ ] React Query used for server state, Zustand for client state
- [ ] Custom hooks extract reusable logic from components
- [ ] `React.memo` / `useMemo` / `useCallback` used only where profiling justifies
- [ ] Error boundaries wrap feature-level components
- [ ] Lazy loading via `React.lazy` + `Suspense` for route-level code splitting

### Anti-patterns to Flag

- Prop drilling beyond 2 levels (use Zustand or context)
- Side effects in render (move to `useEffect` or React Query)
- Inline styles or raw CSS instead of Tai
