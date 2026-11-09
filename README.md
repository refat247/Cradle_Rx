# Cradle Rx — Pregnancy & Lactation Reader

This repository keeps three **separately versioned artifacts**. They are not interchangeable, and publishing a review artifact does **not** release clinical guidance.

| Artifact | Version | Location | Role |
| --- | --- | --- | --- |
| Original maintenance skill | **1.0.0** | [pregnancy-lactation-reader-1.0.0.zip](pregnancy-lactation-reader-1.0.0.zip) | Original portable skill, scripts, template and frozen baseline metadata (preserved) |
| Compiled offline study Reader | **1.3.0** | [Open the original HTML](reader/releases/v1.3.0/Pregnancy_Lactation_Therapeutic_Classes_1.3.0.html) | Exact immutable user-supplied compiled HTML; no source content edits |
| Illustrated UI/UX decision Atlas | **0.2.0** | [Open Atlas HTML](atlas/reviews/v0.2.0/index.html) | Nonclinical decision/review aid; **not** an updated production Reader |

## How to open

To use the HTML files, open the respective file on GitHub, select **Download raw file**, then open the downloaded HTML locally in Chrome or another modern browser. The Atlas works offline and includes its preview screenshots inline; it is **not** hosted as a live website by this repository.

## Integrity

| File | SHA-256 |
| --- | --- |
| Original ZIP `pregnancy-lactation-reader-1.0.0.zip` | `705f65193c5912a87ee1974e71fcf66c28156c5b04478e370e808a2642174b46` |
| Reader v1.3.0 HTML | `085b5c6ea0c1233b86e42ae90c234b911cb86830a2bbae5f22b1d06fc8f95e4f` |
| Atlas v0.2.0 HTML | `b490bc9ccbee34dda37f132f9eeb9c03ca86b24605f1890f49c9cd61fd8563fa` |

Run `python3 scripts/verify_artifacts.py` to verify the checked-in bytes. A GitHub Actions integrity-only check is included. The original Reader checksum matches `references/baseline.json` inside the untouched original skill ZIP.

## Safety and release boundaries

- Reader v1.3.0 reproduces supplied pregnancy/lactation source assessments for **study**, not as independently medically validated prescribing advice.
- The Atlas visualizes 50 UI + 50 UX proposals and 72 declared dependencies. Eight examples are isolated browser previews using original Reader components; the remaining 92 are context illustrations / audit pending. Illustrated conditions such as gesture bars and keyboard visibility are simulations, not evidence of a verified device bug.
- Feature decision status does not constitute approval to implement, promote clinical content or release.
- Neither the underlying original skill (v1.0.0) nor the frozen compiled Reader (v1.3.0) receives a version bump from adding this documentation/review aid.
- GitHub PR merge, on-device testing, independent clinical validation and real app deployment are separate gates.

## Governance

For future changes, follow the existing [version-manager/SKILL.md](https://github.com/refat247/medical-cdss-skills/blob/main/version-manager/SKILL.md): inspect → classify SemVer → synchronize declarations → verify/test → focused PR → owner-controlled merge. Keep skill, Reader, and Atlas versions distinct.
