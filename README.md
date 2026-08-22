# APEX Templates

Official versioned template repository for the Apex Document Workbench.

This repository stores portable Template → Section → Function packages. Apex downloads a tagged repository version into its local `ApexTemplateRepo/examples/` directory, while user-authored packages remain separate under `ApexTemplateRepo/local/`.

## Branches

- `dev` — template/package development
- `main` — released repository content

## Repository layout

```text
repo.json
templates/
  basic-document/
    template.json
    template.jinja
    sections/
      body.jinja
    functions/
      heading.jinja
schema/
  template-package.schema.json
```

## Release model

Repository releases use semantic versions such as `v0.1.0`. `repo.json` declares the repository version, package format version, and the template packages included in that release.

Apex clones packages into SQLite with new private Workbench IDs. Repository packages never contain Apex resource IDs.
