# Anomaly Detection in Traffic Scene Videos using Self-Supervised Learning

LaTeX source code for the master's thesis at FER Zagreb, 2026.

**Author:** Dominik Barukčić  
**Mentor:** Prof. Tomislav Hrkać  
**Institution:** Faculty of Electrical Engineering and Computing, University of Zagreb

## 📄 PDF

The compiled thesis is available at: [diplomski_rad.pdf](diplomski_rad.pdf)

## Compilation

```bash
pdflatex diplomski_rad.tex
bibtex diplomski_rad
pdflatex diplomski_rad.tex
pdflatex diplomski_rad.tex
```

Or with latexmk:

```bash
latexmk -pdf diplomski_rad.tex
```

## Final version for FERWeb upload

Change the documentclass option in `diplomski_rad.tex`:

```latex
\documentclass[diplomskirad,upload]{fer}
```

Then recompile.

## Project Structure

```
master-thesis-traffic-anomaly-ssl/
├── Figures/
│   ├── cityscapes/          # Cityscapes dataset figures
│   ├── deeplab/             # DeepLabV3+ architecture figures
│   ├── kvalitativno/        # Qualitative results
│   ├── loss/                # Training curves
│   ├── metodologija/        # Pipeline diagram
│   ├── moco/                # MoCo comparison figure
│   ├── resnet/              # ResNet architecture figures
│   └── smiyc/               # SMIYC benchmark figures
├── diplomski_rad.tex        # Main document
├── literatura.bib           # Bibliography
├── fer.cls                  # FER thesis class
├── fer_IEEEtran_EN.bst      # Bibliography style (IEEE, English)
├── fer_IEEEtran_HR.bst      # Bibliography style (IEEE, Croatian)
├── fer_plainnat_EN.bst      # Bibliography style (plainnat, English)
├── fer_plainnat_HR.bst      # Bibliography style (plainnat, Croatian)
├── hr_0036538320_94.pdf     # Thesis assignment
├── LICENSE
└── README.md
```

## Related

- **Implementation:** [traffic-anomaly-ssl](https://github.com/doms911/traffic-anomaly-ssl)