#!/usr/bin/env python3
"""
FINAL ANALYSIS: ΞĐ Bloom Harmonic Signature vs Senouci Universal Template
=========================================================================
"""

import numpy as np
from scipy.interpolate import PchipInterpolator
import json, math

phi = (1 + math.sqrt(5)) / 2
G = 6.67430e-11; c = 2.99792458e8; c2 = c**2
hbar = 1.054571817e-34
l_P = math.sqrt(hbar * G / c**3); m_P = math.sqrt(hbar * c / G)
M_cell = (2 + phi) * m_P; l_cell = (2 + phi) * l_P

def senouci_pipeline(x_phys, y_phys, N=200, K=10):
    y_safe = np.maximum(y_phys, 1e-30)
    eps = 1e-6 * np.min(y_safe)
    log_x = np.nan_to_num(np.log10(x_phys), nan=-30, posinf=30, neginf=-30)
    log_y = np.nan_to_num(np.log10(y_safe + eps), nan=-30, posinf=30, neginf=-30)
    grid = np.linspace(log_x.min(), log_x.max(), N)
    y_grid = PchipInterpolator(log_x, log_y)(grid)
    y_centered = y_grid - np.mean(y_grid)
    fft = np.fft.rfft(y_centered)
    H = np.abs(fft)[1:K+1]
    H_norm = H / np.linalg.norm(H)
    ratios = H_norm[1:] / H_norm[0]
    return ratios, H_norm

# Senouci empirical template (Figure 6)
sen_med = np.array([0.56, 0.38, 0.28, 0.22, 0.18, 0.15, 0.12, 0.10, 0.09])
sen_lo = np.array([0.42, 0.30, 0.22, 0.17, 0.14, 0.11, 0.09, 0.07, 0.06])
sen_hi = np.array([0.65, 0.45, 0.34, 0.27, 0.22, 0.19, 0.16, 0.14, 0.12])

x = np.logspace(-2, 4, 10000)

# ═══════════════════════════════════════════════════════════════
# THE KEY PHYSICAL MODEL
# ═══════════════════════════════════════════════════════════════
# 
# The Bloom predicts that Energy distributes itself through a
# two-component structure everywhere:
#   1. Concentrated core (baryonic-scale, fraction f = 1/η)
#   2. Extended envelope (E-pool, fraction 1-f)
#
# At COSMIC scales (what Samir measures), the relevant η is NOT
# the galaxy-scale 5.3. The cosmic η includes:
#   - Dark matter ratio: ~5.3 (E-pool / baryons)
#   - Dark energy component: Λ ≈ 68% of total energy budget
#
# Total cosmic energy budget:
#   Baryons: 4.9%
#   E-pool (DM): 26.1%  (= 5.3 × 4.9%)
#   Background E (Λ): 68.9%
#
# The EFFECTIVE η for the cosmic energy distribution is:
#   η_cosmic = total / concentrated = (4.9 + 26.1 + 68.9) / 4.9 ≈ 20.4
#
# But wait — for the harmonic signature, what matters is the
# ratio of envelope scale to core scale. The E-pool extends to
# ~5.3× the baryonic scale. Dark energy extends to ~∞ (uniform).
# 
# The Bloom's prediction for the cosmic SED should therefore use
# a MULTI-SCALE bloom: baryonic core + DM envelope + Λ background
#

def bloom_cosmic(x, eta_dm=5.3, f_bar=0.049, f_dm=0.261, f_de=0.690):
    """
    Multi-scale Bloom for cosmic energy distribution.
    
    Three components reflecting the cosmic energy budget:
    1. Baryonic core: concentrated, scale ~ R
    2. E-pool (DM): extended, scale ~ η_dm × R  
    3. Background E (Λ): nearly uniform, scale >> η_dm × R
    
    The total SED shape is what generates the universal harmonic signature.
    """
    # Component 1: Baryonic core
    B_bar = f_bar / (1.0 + x**2)
    
    # Component 2: E-pool (dark matter equivalent)
    scale_dm = eta_dm
    B_dm = f_dm / (1.0 + (x / scale_dm)**2)
    
    # Component 3: Background E (dark energy equivalent)
    # Nearly uniform but with very gentle Bloom structure
    # Scale is ~100× the baryonic (Hubble scale / galaxy scale)
    scale_de = 100.0
    B_de = f_de / (1.0 + (x / scale_de)**2)
    
    return B_bar + B_dm + B_de


# ═══════════════════════════════════════════════════════════════
# SCAN: DE SCALE SENSITIVITY
# ═══════════════════════════════════════════════════════════════

print("=" * 70)
print("ΞĐ BLOOM COSMIC MODEL — Multi-Scale Harmonic Derivation")
print("=" * 70)
print(f"\nCosmological parameters (Planck 2018):")
print(f"  f_bar = 0.049, f_dm = 0.261, f_de = 0.690")
print(f"  η_dm = 5.3 (ΞĐ E-pooling ratio)")

# Test various DE scales
de_scales = [10, 30, 50, 100, 200, 500, 1000]
print(f"\nDE scale sensitivity:")
for s in de_scales:
    B_bar = 0.049 / (1.0 + x**2)
    B_dm = 0.261 / (1.0 + (x / 5.3)**2)
    B_de = 0.690 / (1.0 + (x / s)**2)
    y = B_bar + B_dm + B_de
    r, _ = senouci_pipeline(x, y)
    cos = np.dot(r, sen_med) / (np.linalg.norm(r) * np.linalg.norm(sen_med))
    within = sum(1 for i in range(len(r)) if sen_lo[i] <= r[i] <= sen_hi[i])
    print(f"  scale_de={s:5d}  cos={cos:.4f}  IQR={within}/9  R2={r[0]:.3f}")

# Now the full model with best physical parameters
print("\n" + "=" * 70)
print("FINAL RESULT: ΞĐ Cosmic Bloom (physical parameters)")
print("=" * 70)

# Physical model
B_bar = 0.049 / (1.0 + x**2)
B_dm = 0.261 / (1.0 + (x / 5.3)**2)
B_de = 0.690 / (1.0 + (x / 100)**2)
y_cosmic = B_bar + B_dm + B_de

r_cosmic, h_cosmic = senouci_pipeline(x, y_cosmic)
cos_cosmic = np.dot(r_cosmic, sen_med) / (np.linalg.norm(r_cosmic) * np.linalg.norm(sen_med))
within_cosmic = sum(1 for i in range(len(r_cosmic)) if sen_lo[i] <= r_cosmic[i] <= sen_hi[i])

print(f"\nBloom Cosmic Model: f_bar=0.049, f_dm=0.261(η=5.3), f_de=0.690")
print(f"Cosine similarity with Senouci: {cos_cosmic:.4f}")
print(f"(Senouci's cosmic coherence: 0.9931)")
print(f"\nWithin IQR: {within_cosmic}/9")

print(f"\n{'k':>3} {'Bloom':>10} {'Senouci':>10} {'IQR low':>10} {'IQR high':>10} {'Dev%':>8} {'':>6}")
print("-" * 60)
for i in range(len(r_cosmic)):
    k = i + 2
    dev = (r_cosmic[i] - sen_med[i]) / sen_med[i] * 100
    in_iqr = "✓" if sen_lo[i] <= r_cosmic[i] <= sen_hi[i] else "✗"
    print(f"  {k:2d}   {r_cosmic[i]:8.4f}   {sen_med[i]:8.4f}   {sen_lo[i]:8.4f}   {sen_hi[i]:8.4f}  {dev:+6.1f}%  {in_iqr}")

# ═══════════════════════════════════════════════════════════════
# ALSO: Simple two-component with effective cosmic η
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 70)
print("ALTERNATIVE: Two-component Bloom with effective cosmic η")
print("=" * 70)

# η_eff = total/baryonic = 1/0.049 ≈ 20.4
eta_eff = 1.0 / 0.049
print(f"  η_eff = 1/f_bar = {eta_eff:.1f}")

B_core = 0.049 / (1.0 + x**2)
B_envelope = 0.951 / (1.0 + (x / eta_eff)**2)
y_2comp = B_core + B_envelope

r_2comp, h_2comp = senouci_pipeline(x, y_2comp)
cos_2comp = np.dot(r_2comp, sen_med) / (np.linalg.norm(r_2comp) * np.linalg.norm(sen_med))
within_2comp = sum(1 for i in range(len(r_2comp)) if sen_lo[i] <= r_2comp[i] <= sen_hi[i])

print(f"  Cosine: {cos_2comp:.4f}")
print(f"  Within IQR: {within_2comp}/9")
print(f"  Ratios: {[f'{r:.3f}' for r in r_2comp]}")

# ═══════════════════════════════════════════════════════════════
# SAVE ALL RESULTS
# ═══════════════════════════════════════════════════════════════

# Also compute pure baselines for comparison
y_pure = 1.0 / (1.0 + x**2)
r_pure, _ = senouci_pipeline(x, y_pure)
cos_pure = np.dot(r_pure, sen_med) / (np.linalg.norm(r_pure) * np.linalg.norm(sen_med))

output = {
    'cosmic_3component': {
        'params': 'f_bar=0.049, f_dm=0.261(η=5.3), f_de=0.690(scale=100)',
        'ratios': r_cosmic.tolist(),
        'harmonics': h_cosmic.tolist(),
        'cosine': float(cos_cosmic),
        'within_iqr': within_cosmic,
    },
    'cosmic_2component': {
        'params': f'f_core=0.049, f_env=0.951, η_eff={eta_eff:.1f}',
        'ratios': r_2comp.tolist(),
        'harmonics': h_2comp.tolist(),
        'cosine': float(cos_2comp),
        'within_iqr': within_2comp,
    },
    'pure_smooth': {
        'params': '1/(1+x²) — no E-pooling',
        'ratios': r_pure.tolist(),
        'cosine': float(cos_pure),
    },
    'senouci': {
        'median': sen_med.tolist(),
        'iqr_low': sen_lo.tolist(),
        'iqr_high': sen_hi.tolist(),
    },
}

with open('/home/claude/bloom_final_data.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"\n{'='*70}")
print("SUMMARY")
print(f"{'='*70}")
print(f"  Pure 1/(1+x²):              cos = {cos_pure:.4f}")
print(f"  Bloom+DM (η=5.3):           cos = {cos_cosmic:.4f}  IQR={within_cosmic}/9")
print(f"  Bloom 2-comp (η_eff=20.4):  cos = {cos_2comp:.4f}  IQR={within_2comp}/9")
print(f"  Senouci cosmic coherence:          0.9931")
print(f"  Senouci global coherence:          0.9624")
