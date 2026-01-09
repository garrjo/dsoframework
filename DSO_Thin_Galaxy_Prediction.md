# DSO Prediction: Why Thin Galaxies Stay Thin

**A Testable Formula from the Drag-Scale-Object Framework**

Joe William Garrett | VaultSync Solutions Inc. | January 2026

---

## The Problem

Low surface brightness dwarf galaxies are observed to be extremely thin (q < 0.2 for ~40% of dwarfs). ΛCDM simulations produce almost none. Newtonian dynamics with spherical dark matter halos predicts thick disks at low surface density because the vertical restoring force is weak.

MOND resolves this by boosting the vertical restoring force in the low-acceleration regime. DSO provides the same prediction with an explicit threshold.

---

## DSO Derivation

### Newtonian Vertical Dynamics

For a self-gravitating disk with surface density Σ:

**g_z(bar) = 2πGΣ**

Vertical scale height relates to velocity dispersion:

**z_0 = σ_z² / g_z**

Disk thickness:

**q = z_0 / R_d**

### DSO Enhancement

In DSO, E-pooling follows baryonic geometry. The effective vertical acceleration becomes:

**g_z(DSO) = g_z(bar) × ν(g_z(bar) / g†)**

where the interpolation function:

**ν(x) = 1 / (1 − exp(−√x))**

and g† = 1.236 × 10⁻¹⁰ m/s² (derived from 2/φ × 10⁻¹⁰)

### Thickness Prediction

**q(DSO) = q(Newton) × [1 − exp(−√(2πGΣ / g†))]**

This single equation predicts disk thickness from surface density with zero free parameters.

---

## Critical Surface Density

The transition occurs at:

**Σ_crit = g† / (2πG) = 2.9 M☉/pc²**

| Regime | Condition | Result |
|--------|-----------|--------|
| High Σ | Σ >> Σ_crit | Newtonian (ν → 1) |
| Low Σ | Σ << Σ_crit | Enhanced restoring force (ν > 1) |

---

## Test Case: UGC 7321

Matthews (2000) data:
- Central surface brightness: μ_0 = 23.4 mag/arcsec² (B-band)
- Observed thickness: q = 0.07 (14:1 axis ratio)
- Classification: Superthin, low surface brightness, no bulge

Estimated surface density: Σ ≈ 50-100 M☉/pc²

**Calculation:**

2πGΣ ≈ 2-4 × 10⁻¹¹ m/s²

Ratio: 2πGΣ / g† ≈ 0.16-0.32

ν(0.16) ≈ 1.7
ν(0.32) ≈ 1.5

**Result:** Vertical restoring force boosted by factor ~1.5-2×

This allows thin disk stability without fine-tuning velocity dispersion.

---

## Testable Predictions

### Against Benevides et al. (2025) data:

1. **q vs Σ correlation**: Thinnest galaxies (lowest q) should cluster at Σ < 10 M☉/pc²

2. **Transition at Σ_crit**: Sharp increase in typical q above ~3 M☉/pc²

3. **40% thin dwarfs explained**: Low-Σ dwarfs naturally maintain q < 0.2

4. **No thin high-Σ disks**: Unless dynamically very cold (low σ_z)

### Falsification:

- Thin galaxies (q < 0.2) with high Σ (> 100 M☉/pc²) and normal σ_z would falsify DSO
- q distribution inconsistent with ν(2πGΣ/g†) scaling would falsify DSO

---

## Comparison

| Framework | Thin dwarfs? | Mechanism | Free parameters |
|-----------|--------------|-----------|-----------------|
| Newton + spherical halo | No | Halo doesn't contribute to g_z | Halo shape |
| ΛCDM simulations | ~0% | Mergers heat disks | Many |
| MOND | Yes | Modified gravity boosts g_z | a_0 (fitted) |
| **DSO** | **Yes** | **E-pooling follows disk** | **g† = 2/φ × 10⁻¹⁰ (derived)** |

---

## The Formula

For any disk galaxy with measured surface density Σ and scale length R_d:

```
q_predicted = (σ_z² / 2πGΣR_d) × [1 − exp(−√(2πGΣ / 1.236×10⁻¹⁰))]
```

This is checkable in an afternoon against existing catalogs.

---

## References

- McGaugh, S.S. (2026). "Very thin galaxies." Triton Station, January 2.
- Benevides et al. (2025). Dwarf galaxy thickness distribution.
- Matthews, L.D. (2000). UGC 7321 analysis.
- Garrett, J.W. (2026). DSO Framework. Zenodo DOI: 10.5281/zenodo.18118894

---

*E-pooling follows baryons. The "dark matter" is in the plane, not around it. Thin disks stay thin.*
