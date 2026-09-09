# JAW Templates

Official versioned template repository for the JAW Document Workbench.

This repository stores portable Template → Section → Function packages. JAW downloads the newest compatible tagged repository release into its local `JAWTemplateRepo/examples/` directory, while user-authored packages remain separate under `JAWTemplateRepo/local/`.

## Included templates

- **Document Tour** — guided deterministic tour of Documents and Workbench composition.
- **JAW Object Examples** — direct examples of `user`, `job_ref`, `work_exp`, `cap`, `system`, and runtime helpers; no AI required.
- **Cover Letter** — deterministic cover-letter example.
- **Cover Letter - AI** — job-aware cover letter with an AI-generated body using the active JAW document-generation provider.

## Repository layout

```text
releases.json
repo.json
templates/
  document-tour/
  jaw-object-examples/
  cover-letter/
  cover-letter-ai/
schema/
  template-package.schema.json
```

Each package contains `template.json`, a Template source file, and optional Section/Function source files. Packages never contain JAW resource or reference JIDs; JAW creates private Workbench identities when a package is cloned.

## Version contracts

JAW and this repository use separate version numbers and compatibility contracts:

- **JAW version** — application release, for example `0.1.0`.
- **Repository version** — content release for this repository, for example `0.1.1`.
- **Template API** — runtime contract exposed to templates. Bump this when a JAW change is not backward compatible with existing template behavior, such as removing or changing JAW Objects, helpers, generation-block syntax, or rendering semantics.
- **Package format** — structure of `repo.json`, `template.json`, and packaged resources. Bump this only when the package/file format itself changes incompatibly.

A repository content update can therefore ship without requiring a JAW code release as long as its Template API, package format, and JAW compatibility range remain compatible.

## Release registry

`releases.json` is the release channel registry. JAW reads it and chooses the newest release compatible with the running JAW version, its supported Template APIs, and its supported package format.

Example:

```json
{
  "registry_format": 1,
  "releases": [
    {
      "version": "0.1.0",
      "ref": "v0.1.0",
      "template_api": 1,
      "package_format": 1,
      "jaw": ">=0.1.0,<0.2.0"
    }
  ]
}
```

Tagged releases are immutable snapshots. Keep old entries in `releases.json` so older JAW releases can continue resolving their newest compatible template release.

## Publishing a template release

1. Update templates and make `repo.json` match the exact packages being released.
2. Increment `repo_version` when publishing new template content.
3. Keep `template_api` unchanged for backward-compatible runtime behavior; increment it for a breaking template-runtime contract.
4. Commit the release contents.
5. Create an immutable tag such as `v0.1.1` at that commit.
6. Add the tagged release to `releases.json` with its JAW compatibility range.
7. Commit the registry update on `main`.

JAW's normal **Download** action resolves `releases.json` at download time. The development channel is separate and downloads the `dev` branch directly for the JAW `Dev` user.
