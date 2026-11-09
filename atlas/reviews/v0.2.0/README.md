# Cradle Rx actual-Reader UI/UX Visual Atlas — review v0.2.0

**Artifact:** `index.html`  
**SHA-256:** `b490bc9ccbee34dda37f132f9eeb9c03ca86b24605f1890f49c9cd61fd8563fa`  
**Baseline Reader:** [v1.3.0](../../../reader/releases/v1.3.0/Pregnancy_Lactation_Therapeutic_Classes_1.3.0.html), SHA-256 `085b5c6ea0c1233b86e42ae90c234b911cb86830a2bbae5f22b1d06fc8f95e4f`.

This is a **self-contained offline HTML review tool**, not production Reader code. Download raw `index.html` and open it locally. It covers **50 UI + 50 UX proposals**, their **72 declared direct ID dependency links**, owner-selected statuses (**35 APPLY, 42 HOLD, 22 LATER, 1 REJECT**) and reversible, nonpersistent WHAT-IF simulation.

### Visual evidence
- **8 isolated proposal previews:** `UI01`, `UI02`, `UI04`, `UI07`, `UI10`, `UI31`, `UX01`, `UX50`. They use screenshots of the real compiled Reader and limited browser-memory DOM/CSS changes; these are demonstrations, **not changes** to v1.3.0.
- **Remaining 92:** actual Reader context screens without a fabricated “After” claim. They still need independent feature-specific visual fidelity review.
- **UI04:** safe-area/gesture-zone overlay is simulated; actual phone-level defect is **not verified**.
- **UI03 / UI06:** 44px targets and keyboard focus outlines have already been found in the Reader; these are not blanket absent features.
- **UI04 source status vs permission:** source Google Doc may show bold APPLY, but owner has not approved implementation. The Atlas simulation cannot override this.

### Scope and QA
- Source HTML checksum and 100/72 dependency data validated.
- Previous browser QA at 1280px and 390px simulated viewports reported no JS errors or horizontal overflow.
- **Not run:** native Android/iOS device QA, independent clinical evidence review, full semantic review of all 100 visual changes, clinical release.
- Original Reader, original ZIP and clinical text remain unchanged.

### Versioning
The Atlas's `0.2.0` is a **review artifact version**. It is not a new release of Reader v1.3.0 or maintenance skill v1.0.0.
