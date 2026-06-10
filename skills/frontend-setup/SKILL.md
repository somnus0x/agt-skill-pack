---
name: frontend-setup
description: |
  Bootstrap Claude Code for React/Next.js repos: project context, conventions, and
  guardrails so it stops guessing and builds correctly from the first prompt. Use when
  setting up Claude Code in a frontend codebase.
---

# Frontend Setup — Claude Code × React/Next.js

You just installed Claude Code. Your frontend repo is React or Next.js. This skill gives Claude Code the context it needs to stop guessing and start building correctly from the first prompt.

## Why

Claude Code writes decent React out of the box. But "decent" means: wrong import paths, outdated patterns, components that don't match your structure, styles that fight your setup. You spend the first hour correcting things that should've been right from the start.

This skill front-loads the project context so Claude Code knows your stack before you ask it to build anything.

## When to use

Run once when setting up Claude Code on a frontend repo. Re-run when you change major dependencies (migration to App Router, new styling system, state management swap).

Say: "setup frontend", "configure for react", "frontend onboarding", or just paste this skill into your session.

## Step 1 — Detect your stack

Before writing any CLAUDE.md rules, tell Claude Code to scan your project:

```
Read my package.json, tsconfig, and project structure.
Tell me:
1. Framework (Next.js version? App Router or Pages?)
2. Styling (Tailwind? CSS Modules? styled-components? version?)
3. State management (Redux? Zustand? React Query? Context only?)
4. Testing (Vitest? Jest? Playwright? none?)
5. Component pattern (barrel exports? co-located files? flat?)
6. Linting/formatting (ESLint config? Prettier?)

Don't suggest changes. Just report what exists.
```

This gives you the facts before you write rules. Don't assume — detect.

## Step 2 — Generate your CLAUDE.md rules

Based on the scan, add these sections to your project's CLAUDE.md. Only include sections relevant to your stack.

### Component conventions

```markdown
## Component Rules

- Components live in `src/components/` grouped by feature, not by type
- One component per file. File name = component name (PascalCase)
- Co-locate styles, tests, and types with the component:
  ```
  components/
    MarketCard/
      MarketCard.tsx
      MarketCard.test.tsx
      types.ts
  ```
- No barrel exports (index.ts re-exports) unless the folder has 5+ files
- Props interface lives in the same file, named `{ComponentName}Props`
- Default export for page components, named export for everything else
```

Adapt to your actual structure. If your repo uses flat files — say flat files. If it uses barrel exports everywhere — say that. The point is to describe what IS, not what should be.

### Import rules

```markdown
## Import Rules

- Absolute imports from `@/` (mapped to `src/` in tsconfig)
- Import order: react → external libs → internal modules → relative files → styles
- No circular imports. If A imports B and B imports A — extract shared types to a third file
- Prefer named imports: `import { Button } from '@/components/ui/Button'`
```

### Styling

Pick your block based on what you use:

**Tailwind:**
```markdown
## Styling (Tailwind)

- Tailwind v4 with CSS-first config
- Use `cn()` utility for conditional classes (already in `lib/utils.ts`)
- No inline style objects. If Tailwind can't do it, add a CSS variable
- Color tokens: use semantic names (`text-primary`, `bg-surface`) not raw values
- Responsive: mobile-first. `sm:` `md:` `lg:` — no custom breakpoints
```

**CSS Modules:**
```markdown
## Styling (CSS Modules)

- One `.module.css` per component, co-located
- Class names: camelCase in JS, kebab-case in CSS
- No global styles except in `globals.css`
- CSS variables for colors and spacing — defined in `:root`
```

### Data fetching (Next.js App Router)

```markdown
## Data Fetching

- Server Components by default. Add 'use client' only when needed (state, effects, browser APIs)
- Fetch in Server Components or Route Handlers — not in client components
- Use React Server Actions for mutations
- Loading states: `loading.tsx` files, not manual isLoading booleans
- Error boundaries: `error.tsx` files at route level
```

### Data fetching (React SPA / Pages Router)

```markdown
## Data Fetching

- React Query (TanStack Query) for all server state
- Custom hooks in `hooks/` folder: `useMarkets()`, `useUser()`
- No raw fetch/axios in components — always wrap in a hook
- Loading/error states handled by React Query, not manual state
```

### State management

```markdown
## State

- Server state: React Query (or Server Components if Next.js App Router)
- Client state: Zustand for global, useState for local
- No prop drilling past 2 levels — extract to context or Zustand
- Form state: react-hook-form, not manual onChange handlers
```

### TypeScript

```markdown
## TypeScript

- Strict mode. No `any` unless you add a comment explaining why
- API response types in `types/api.ts`
- Component prop types co-located with component
- Use `satisfies` over `as` for type narrowing
- Enums → union types: `type Status = 'active' | 'pending' | 'closed'`
```

### Testing

```markdown
## Testing

- Unit tests: Vitest + React Testing Library
- Test file lives next to component: `Button.test.tsx`
- Test behavior, not implementation. Click the button, check the result
- No snapshot tests unless explicitly asked
- E2E: Playwright for critical flows only
```

## Step 3 — Add guardrails

These rules prevent Claude Code from doing things that break your project. Add to CLAUDE.md:

```markdown
## Don't

- Don't install new dependencies without asking first
- Don't create new top-level folders
- Don't refactor existing components unless I specifically ask
- Don't add error boundaries or loading states unless I ask for them
- Don't convert between CSS approaches (don't migrate Tailwind to CSS Modules)
- Don't add comments to code you didn't write
- Don't create utility functions for one-time operations
```

```markdown
## Before writing code

1. Check if a similar component already exists — don't duplicate
2. Follow the existing pattern in the nearest similar file
3. Run the dev server / type checker to verify your changes compile
```

## Step 4 — Verify

After setting up CLAUDE.md, test with a small task:

```
Create a simple card component that displays a title and description.
Follow existing project conventions.
```

Check:
- Did it put the file in the right place?
- Did it use the right styling approach?
- Did it follow your import pattern?
- Did it match existing component structure?

If it got any of these wrong, your CLAUDE.md is missing that rule. Add it.

## The principle

Claude Code with no context writes generic React. Claude Code with your CLAUDE.md writes **your** React. The gap between "works" and "fits" is 15 minutes of setup.

## Add to your CLAUDE.md

```markdown
### Frontend setup
Before building any new component, check:
1. Does a similar component already exist? Search first
2. What pattern does the nearest existing component follow? Match it
3. Where should this file live based on project structure?
Follow the component, import, and styling rules in this file exactly.
```

## Output discipline

When this skill is invoked:

1. Run the stack detection scan (Step 1)
2. Generate CLAUDE.md sections relevant to the detected stack
3. Include the guardrails section
4. Nothing else — no explanations of what React is, no best practices lectures

The output should be copy-pasteable into CLAUDE.md directly.
