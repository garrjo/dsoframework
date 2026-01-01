# E is Prime

## The Drag-Scale-Object (DSO) Framework

**A foundational framework proposing that Energy (E) is the sole fundamental constituent of physical reality.**

> *"E is prime. Everything else is measurement."*

---

## Core Thesis

**E = DC²**

Einstein's E = mc² inverted: Mass (Drag) is not fundamental—it is how we *detect* concentrated Energy. What we call "dark matter" is Energy detected gravitationally but not baryonically.

This isn't new physics. It's physics taking seriously what it already established:
- Energy is conserved (it persists through all transformations)
- E = mc² (mass and energy are equivalent)
- Quantum fields (particles are energy excitations)

DSO simply uses Energy as the foundation instead of the footnote.

---

## Key Results

| Validation | Result |
|------------|--------|
| SPARC galaxies tested | 175 |
| DSO outperforms baryons-only | 56% |
| Mean improvement factor | 11.7× |
| CMB Ω_dm prediction | 0.261 |
| Planck measured Ω_dm | 0.265 |
| **Agreement** | **98.6%** |

The cosmic E-pooling/baryon ratio (5.3) derived from galaxy rotation curves *predicts* the CMB dark matter density—without fitting.

---

## Papers

| Document | Description |
|----------|-------------|
| [E_is_Prime_Complete.docx](E_is_Prime_Complete.docx) | **Main paper**: Full theoretical framework, derivations, and validation |
| [DSO_Framework_Paper_v2.docx](DSO_Framework_Paper_v2.docx) | Technical paper focused on galaxy validation |

---

## Theoretical Framework

### The Detection Hierarchy

| Detection Mode | What It Measures | Coverage |
|----------------|------------------|----------|
| Gravitational | Total E field | 100% |
| Baryonic | High E concentration | ~16% |
| Electromagnetic | E oscillations | Frequency-dependent |

**"Dark matter" = E detected gravitationally but not baryonically.**

### The Acceleration Threshold

**g† = 1.2 × 10⁻¹⁰ m/s²**

This is the E-detection boundary. Above it, baryons dominate. Below it, E-pooling dominates. This produces the Radial Acceleration Relation (RAR):

```
g_obs = g_bar / [1 - exp(-√(g_bar/g†))]
```

### The Cosmic Ratio

```
E-pooling / Baryon = 5.3
Ω_E-pooling = 0.0493 × 5.3 = 0.261
Planck Ω_dm = 0.265
Agreement: 98.6%
```

---

## Unique Predictions (vs ΛCDM)

| # | Prediction | ΛCDM Says | DSO Says |
|---|------------|-----------|----------|
| 1 | Dark matter particles | Should exist | Will never be found |
| 2 | Cluster galaxies | Less DM (tidal stripping) | More E-pooling (clustering) |
| 3 | Density profiles | Cuspy (NFW) | Cored |
| 4 | RAR | Emergent | Fundamental |
| 5 | Post-merger curves | Smooth | E-wave interference |
| 6 | BTFR scatter | Secondary correlations | None |
| 7 | E-ratio | Varies by scale | Universal (5.3) |

---

## Repository Structure

```
dso_framework/
├── README.md                    # This file
├── E_is_Prime_Complete.docx     # Main theoretical paper
├── DSO_Framework_Paper_v2.docx  # Technical validation paper
│
├── code/
│   ├── dso_rar_physics.py       # RAR derivation + SPARC validation
│   ├── dso_sparc_validation.py  # Alternative validation approach
│   ├── dso_cmb.py               # CMB power spectrum prediction
│   └── dso_local_group.py       # MW, M31, M33 detailed analysis
│
├── data/
│   ├── sparc/                   # 175 SPARC rotation curves
│   │   ├── NGC3198_rotmod.dat
│   │   ├── NGC2841_rotmod.dat
│   │   └── ... (175 files)
│   └── dso_sparc_results.csv    # Validation results for all galaxies
│
└── figures/
    └── dso_rar_validation.png   # Key validation figure
```

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/garrjo/dsoframework.git
cd dso_framework

# Run SPARC validation
python code/dso_rar_physics.py

# Run CMB prediction
python code/dso_cmb.py

# Run Local Group analysis
python code/dso_local_group.py
```

**Requirements:** Python 3.x, NumPy, Matplotlib, SciPy

---

## Validation Data

This framework is validated against the [SPARC database](http://astroweb.cwru.edu/SPARC/) (Lelli, McGaugh & Schombert 2016):
- 175 disk galaxies
- Spitzer 3.6μm photometry
- High-quality HI/Hα rotation curves
- Mass range: 10⁷ to 10¹² L☉

---

## Citation

```bibtex
@article{garrett2026eprime,
  author  = {Garrett, Joe William},
  title   = {E is Prime: A Foundational Framework for Physics},
  year    = {2026},
  note    = {The Drag-Scale-Object (DSO) Model with validation 
             across 175 galaxies and the Cosmic Microwave Background}
}
```

### SPARC Data Citation

```bibtex
@article{lelli2016sparc,
  author  = {Lelli, F. and McGaugh, S. S. and Schombert, J. M.},
  title   = {SPARC: Mass Models for 175 Disk Galaxies with Spitzer 
             Photometry and Accurate Rotation Curves},
  journal = {AJ},
  volume  = {152},
  pages   = {157},
  year    = {2016}
}
```

---

## Author

**Joe William Garrett**  
VaultSync Solutions Inc.  
joegarrett@outlook.com

---

## License

This work is presented for scientific evaluation. Independent validation by the astrophysics community is welcomed and encouraged.

---

*January 2026*
