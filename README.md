# JAW Templates

Official versioned template repository for the JAW Document Workbench.

This repository stores portable Template → Section → Function packages. JAW downloads a tagged repository version into its local `JAWTemplateRepo/examples/` directory, while user-authored packages remain separate under `JAWTemplateRepo/local/`.

## Included templates

- **Basic Document** — minimal Template → Section → Function example.
- **Document Tour** — guided deterministic tour of Documents and Workbench composition.
- **JAW Object Examples** — direct examples of `user`, `job_ref`, `work_exp`, `cap`, `system`, and runtime helpers; no AI required.
- **Cover Letter** — job-aware cover letter whose body uses the active JAW AI provider.

## Repository layout

```text
repo.json
templates/
  basic-document/
  document-tour/
  jaw-object-examples/
  cover-letter/
schema/
  template-package.schema.json
```

Each package contains `template.json`, a Template source file, and optional Section/Function source files. Packages never contain JAW resource or reference JIDs; JAW creates private Workbench identities when a package is cloned.

## Release model

Repository releases use semantic versions such as `v0.1.0`. `repo.json` declares the repository version, package format version, minimum JAW version, and the packages included in that release.
