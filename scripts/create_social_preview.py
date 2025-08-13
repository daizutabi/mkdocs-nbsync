from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

# Create figure for social preview - modern design
fig, ax = plt.subplots(figsize=(12, 6.3))
fig.patch.set_facecolor("#0d1117")
ax.set_facecolor("#0d1117")

# Remove axes - expanded vertical space for better layout
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

# Background gradient effect (subtle)
gradient = Rectangle((0, 0), 10, 6, facecolor="#161b22", alpha=0.3)
ax.add_patch(gradient)

# Main title with modern styling - moved up for more space
ax.text(
    5,
    5.2,
    "mkdocs-nbsync",
    fontsize=42,
    fontweight="bold",
    ha="center",
    va="center",
    color="#58a6ff",
)

# Tagline - more spacing
ax.text(
    5,
    4.6,
    "Jupyter ↔ MkDocs Sync Made Simple",
    fontsize=16,
    ha="center",
    va="center",
    color="#f0f6fc",
    style="italic",
)

# Problem statement box - repositioned with more space
problem_box = FancyBboxPatch(
    (0.5, 2.8),
    4,
    1.4,
    boxstyle="round,pad=0.15",
    facecolor="#21262d",
    edgecolor="#f85149",
    linewidth=2,
)
ax.add_patch(problem_box)

ax.text(
    2.5,
    3.9,
    "THE PROBLEM",
    fontsize=13,
    fontweight="bold",
    ha="center",
    color="#f85149",
)
ax.text(
    2.5,
    3.5,
    "✗ Screenshots break",
    fontsize=12,
    ha="center",
    color="#f0f6fc",
)
ax.text(2.5, 3.2, "✗ Exports forgotten", fontsize=12, ha="center", color="#f0f6fc")
ax.text(2.5, 2.9, "✗ Docs out of sync", fontsize=12, ha="center", color="#f0f6fc")

# Solution box - repositioned with matching spacing
solution_box = FancyBboxPatch(
    (5.5, 2.8),
    4,
    1.4,
    boxstyle="round,pad=0.15",
    facecolor="#0d4429",
    edgecolor="#3fb950",
    linewidth=2,
)
ax.add_patch(solution_box)

ax.text(
    7.5,
    3.9,
    "THE SOLUTION",
    fontsize=13,
    fontweight="bold",
    ha="center",
    color="#3fb950",
)
ax.text(7.5, 3.5, "✓ Auto-sync everything", fontsize=12, ha="center", color="#f0f6fc")
ax.text(7.5, 3.2, "✓ One simple syntax", fontsize=12, ha="center", color="#f0f6fc")
ax.text(7.5, 2.9, "✓ Always up to date", fontsize=12, ha="center", color="#f0f6fc")

# Code example with enhanced styling - moved down with more space
code_bg = FancyBboxPatch(
    (0.8, 1.4),
    8.4,
    0.9,
    boxstyle="round,pad=0.15",
    facecolor="#161b22",
    edgecolor="#30363d",
    linewidth=1,
)
ax.add_patch(code_bg)

# Code label
ax.text(1.2, 2.1, "SYNTAX:", fontsize=11, fontweight="bold", color="#8b949e", ha="left")

# Code text
ax.text(
    5,
    1.8,
    "![My visualization](analysis.ipynb){#my-plot}",
    fontsize=17,
    fontfamily="monospace",
    ha="center",
    va="center",
    color="#79c0ff",
    bbox={"boxstyle": "round,pad=0.3", "facecolor": "#21262d", "alpha": 0.8},
)

# Call to action - moved down
ax.text(
    5,
    0.9,
    "pip install mkdocs-nbsync",
    fontsize=14,
    fontfamily="monospace",
    ha="center",
    va="center",
    color="#f0f6fc",
    bbox={"boxstyle": "round,pad=0.4", "facecolor": "#238636", "alpha": 0.9},
)

# GitHub link - moved down
ax.text(
    9.2,
    0.4,
    "github.com/daizutabi/mkdocs-nbsync",
    fontsize=11,
    ha="right",
    va="center",
    color="#58a6ff",
)

plt.tight_layout()
plt.savefig(
    Path(__file__).parent / "social-preview.png",
    dpi=150,
    bbox_inches="tight",
    facecolor="#0d1117",
    edgecolor="none",
)

print("✅ Social preview created: social-preview.png")
print("📐 Size: 1280x640 pixels (GitHub recommended)")
print("🎨 Modern design with problem/solution layout")
print()
print("📝 To use:")
print("1. Go to GitHub repo settings")
print("2. General > Social Preview")
print("3. Upload social-preview.png")
