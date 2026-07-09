"""
Combine three separate ESC control technique figures into one figure* with subfigures,
converting all colors to black-and-white with unified formatting.
"""

import re, shutil, os

src = os.path.join(os.path.dirname(__file__), 'main.tex')
bak = src + '.bak_combine'
shutil.copy2(src, bak)
print(f"Backup saved to {bak}")

with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# NEW COMBINED FIGURE (all three as subfigures, B&W)
# ============================================================
NEW_FIGURE = r"""\begin{figure*}[t]
\centering
%------------------------------------------------------------
% (a) Technique 1: Direct-Input ESC Baseline
%------------------------------------------------------------
\begin{subfigure}[b]{\textwidth}
\centering
\begin{tikzpicture}[
    line cap=round,
    line join=round,
    >=Latex,
    every node/.style={font=\large},
    block/.style={
        draw,
        rectangle,
        fill=gray!12,
        minimum width=2.45cm,
        minimum height=1.30cm,
        align=center,
        font=\Large,
        line width=1.0pt
    },
    smallblock/.style={
        draw,
        rectangle,
        fill=gray!12,
        minimum width=1.50cm,
        minimum height=1.30cm,
        align=center,
        font=\Large,
        line width=1.0pt
    },
    sum/.style={
        draw,
        circle,
        minimum size=0.95cm,
        inner sep=0pt,
        font=\Large,
        line width=1.0pt
    },
    mult/.style={
        draw,
        circle,
        minimum size=0.95cm,
        inner sep=0pt,
        font=\Large,
        line width=1.0pt
    },
    signal/.style={
        ->,
        >=Latex,
        line width=1.05pt
    },
    wire/.style={
        line width=1.05pt
    },
    feedback/.style={
        ->,
        >=Latex,
        densely dashed,
        line width=0.85pt
    }
]

% ------------------------------------------------
% Main nodes
% ------------------------------------------------
\node[sum] (sum) at (0,0) {};
\node[block] (plant) at (2.70,0) {BCD\\System};
\node[circle, fill=black, inner sep=2.7pt] (branch) at (4.65,0) {};
\node[block] (hpf) at (6.65,0) {HPF\\$H_h(s)$};
\node[mult] (mult) at (8.75,0) {$\times$};
\node[block] (lpf) at (10.85,0) {LPF\\$H_l(s)$};
\node[smallblock] (int) at (13.35,0) {$k/s$};

\node[font=\Large] at ($(sum.center)+(-0.15,0.08)$) {$+$};
\node[font=\Large] at ($(sum.center)+(0.16,-0.19)$) {$+$};

% ------------------------------------------------
% Main signal path
% ------------------------------------------------
\draw[signal] (sum.east) -- node[above, font=\Large] {$u$} (plant.west);
\draw[wire] (plant.east) -- (branch.west);
\draw[signal] (branch.east) -- (hpf.west);
\draw[signal] (hpf.east) -- (mult.west);
\draw[signal] (mult.east) -- (lpf.west);
\draw[signal] (lpf.east) -- (int.west);

\draw[signal] ($(sum.north)+(0,1.55)$)
    node[above, font=\Large] {$a\sin\omega t$}
    -- (sum.north);

\draw[signal] ($(mult.north)+(0,1.55)$)
    node[above, font=\Large] {$\sin\omega t$}
    -- (mult.north);

\draw[signal] (branch.south) -- ++(0,-1.35)
    node[below, font=\LARGE] {$z$};

% ------------------------------------------------
% Feedback path
% ------------------------------------------------
\coordinate (fbRight) at ($(int.east)+(0.85,0)$);
\coordinate (fbBottomRight) at ($(fbRight)+(0,-2.55)$);
\coordinate (fbBottomLeft) at ($(sum.west)+(-1.00,-2.55)$);
\coordinate (fbLeft) at ($(sum.west)+(-1.00,0)$);

\draw[feedback]
    (int.east) -- (fbRight)
    -- (fbBottomRight)
    -- (fbBottomLeft)
    -- (fbLeft)
    -- (sum.west);

\node[left, font=\Large] at ($(fbLeft)!0.55!(fbBottomLeft)$) {$\hat{u}$};

\end{tikzpicture}
\caption{Control Technique 1: Direct-Input ESC Baseline}
\label{fig:control_technique_1}
\end{subfigure}

\vspace{1em}

%------------------------------------------------------------
% (b) Technique 2: ESC with Inner-Loop Actuator Stabilization
%------------------------------------------------------------
\begin{subfigure}[b]{\textwidth}
\centering
\resizebox{\textwidth}{!}{%
\begin{tikzpicture}[x=0.01cm, y=-0.01cm, line cap=round, line join=round]

    % Outer summing junction
    \draw[black, line width=1.4pt] (200,350) circle [radius=34];
    \node[font=\large] at (200,330) {$+$};
    \node[font=\large] at (178,352) {$+$};

    % Inner summing junction
    \draw[black, line width=1.4pt] (430,350) circle [radius=34];
    \node[font=\large] at (410,352) {$+$};
    \node[font=\large] at (432,370) {$-$};

    % PID block
    \draw[black, fill=gray!12, line width=1.4pt, rounded corners=8pt]
        (520,270) rectangle (720,430);
    \node[font=\Large] at (620,350) {PID};

    % BCD System block
    \draw[black, fill=gray!12, line width=1.4pt, rounded corners=8pt]
        (810,270) rectangle (1060,430);
    \node[align=center, font=\large] at (935,350) {BCD\\System};

    % HPF block
    \draw[black, fill=gray!12, line width=1.4pt, rounded corners=8pt]
        (1150,270) rectangle (1360,430);
    \node[align=center, font=\large] at (1255,345) {HPF\\$\frac{s}{s+\omega_h}$};

    % Multiplier (demodulator) circle
    \draw[black, line width=1.4pt] (1450,350) circle [radius=34];
    \node[font=\Large] at (1450,350) {$\times$};

    % LPF block
    \draw[black, fill=gray!12, line width=1.4pt, rounded corners=8pt]
        (1540,270) rectangle (1730,430);
    \node[align=center, font=\large] at (1635,345) {LPF\\$\frac{\omega_l}{s+\omega_l}$};

    % Integrator block
    \draw[black, fill=gray!12, line width=1.4pt, rounded corners=8pt]
        (1820,270) rectangle (1990,430);
    \node[font=\Large] at (1905,350) {$\frac{k}{s}$};

    % Outer -> inner (x_des)
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (234,350) -- (396,350);
    \node[anchor=south, font=\large] at (315,344) {$x_{\rm des}$};

    % Inner -> PID (e)
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (464,350) -- (520,350);
    \node[anchor=south, font=\large] at (492,344) {$e$};

    % PID -> BCD (u)
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (720,350) -- (810,350);
    \node[anchor=south, font=\large] at (765,344) {$u$};

    % BCD -> branch dot
    \draw[black, line width=1.2pt] (1060,350) -- (1100,350);
    \fill[black] (1100,350) circle [radius=8pt];

    % branch dot -> HPF
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (1100,350) -- (1150,350);

    % HPF -> demod
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (1360,350) -- (1416,350);

    % demod -> LPF
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (1484,350) -- (1540,350);

    % LPF -> integrator
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (1730,350) -- (1820,350);

    % a*sin(wt) -> outer sum
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (200,165) -- (200,316);
    \node[anchor=south, font=\large] at (200,165) {$a\sin\omega t$};

    % sin(wt) -> demod
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (1450,165) -- (1450,316);
    \node[anchor=south, font=\large] at (1450,165) {$\sin\omega t$};

    % z output
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (1100,350) -- (1100,540);
    \node[anchor=north, font=\large] at (1100,545) {$z$};

    % x inner feedback
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (935,430) -- (935,510) -- (430,510) -- (430,384);
    \node[anchor=north, font=\large] at (682,510) {$x$};

    % outer feedback (x_ref)
    \draw[black, line width=1.2pt]
        (1990,350) -- (2060,350) -- (2060,640) -- (100,640) -- (100,350);
    \draw[-{Triangle[length=9pt,width=8pt]}, black, line width=1.2pt]
        (100,350) -- (166,350);
    \node[anchor=west, font=\large] at (105,500) {$x_{\rm ref}$};

\end{tikzpicture}%
}% end \resizebox
\caption{Control Technique 2: ESC with Inner-Loop Actuator Stabilization}
\label{fig:control_technique_2}
\end{subfigure}

\vspace{1em}

%------------------------------------------------------------
% (c) Technique 3: Proposed ESC-Tuned PD Depth Controller
%------------------------------------------------------------
\begin{subfigure}[b]{\textwidth}
\centering
\resizebox{\textwidth}{!}{%
\begin{tikzpicture}[x=0.01cm, y=-0.01cm, line cap=round, line join=round]

    % Reference input
    \node[anchor=east, font=\LARGE] at (40,350) {$r$};

    % Depth error summing junction
    \draw[black, line width=1.5pt] (120,350) circle [radius=38];
    \node[font=\large] at (120,328) {$+$};
    \node[font=\large] at (99,353)  {$-$};

    % PD block
    \draw[black, fill=gray!12, line width=1.5pt, rounded corners=10pt]
        (220,265) rectangle (530,435);
    \node[align=center, font=\LARGE] at (375,345)
        {$K_p(r-z)$\\$-\,K_d\dot{z}$};

    % BCD System block
    \draw[black, fill=gray!12, line width=1.5pt, rounded corners=10pt]
        (630,265) rectangle (920,435);
    \node[align=center, font=\LARGE] at (775,350) {BCD\\System};

    % r -> sum
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (40,350) -- (82,350);

    % sum -> PD
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (158,350) -- (220,350);

    % PD -> BCD
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (530,350) -- (630,350);
    \node[anchor=south, font=\LARGE] at (580,344) {$u$};

    % BCD -> branch dot
    \draw[black, line width=1.3pt] (920,350) -- (980,350);
    \fill[black] (980,350) circle [radius=9pt];

    % z output
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (980,350) -- (980,570);
    \node[anchor=north, font=\LARGE] at (980,578) {$z$};

    % z feedback
    \draw[black, line width=1.3pt]
        (980,350) -- (980,490) -- (120,490) -- (120,388);
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (120,490) -- (120,388);
    \node[anchor=north, font=\LARGE] at (550,490) {$z$};

    % Cost J block
    \draw[black, fill=gray!12, line width=1.5pt, rounded corners=10pt]
        (1080,265) rectangle (1340,435);
    \node[align=center, font=\LARGE] at (1210,350) {$J$};

    % branch dot -> cost
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (980,350) -- (1080,350);

    % Dither for Kp
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (1210,50) -- (1210,265);
    \node[anchor=south, font=\LARGE] at (1210,50) {$a_p\!\sin\omega_p t$};

    % J branch dot
    \draw[black, line width=1.3pt] (1340,350) -- (1400,350);
    \fill[black] (1400,350) circle [radius=9pt];

    % upper branch: J -> ESC Kp
    \draw[black, line width=1.3pt] (1400,350) -- (1400,130);
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (1400,130) -- (1450,130);

    % ESC Kp block (darker gray to distinguish from plant blocks)
    \draw[black, fill=gray!25, line width=1.5pt, rounded corners=10pt]
        (1450,50) rectangle (1720,210);
    \node[align=center, font=\LARGE] at (1585,130) {ESC\\($K_p$ channel)};

    % Kp output -> PD block
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (1720,130) -- (1800,130) -- (1800,0) -- (375,0) -- (375,265);
    \node[anchor=south, font=\LARGE] at (1090,0) {$\hat{K}_p$};

    % Dither for Kd
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (1210,790) -- (1210,570);
    \node[anchor=north, font=\LARGE] at (1210,793) {$a_d\!\sin\omega_d t$};

    % lower branch: J -> ESC Kd
    \draw[black, line width=1.3pt] (1400,350) -- (1400,570);
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (1400,570) -- (1450,570);

    % ESC Kd block (darker gray to distinguish from plant blocks)
    \draw[black, fill=gray!25, line width=1.5pt, rounded corners=10pt]
        (1450,490) rectangle (1720,650);
    \node[align=center, font=\LARGE] at (1585,570) {ESC\\($K_d$ channel)};

    % Kd output -> PD block
    \draw[-{Triangle[length=10pt,width=9pt]}, black, line width=1.3pt]
        (1720,570) -- (1800,570) -- (1800,720) -- (375,720) -- (375,435);
    \node[anchor=north, font=\LARGE] at (1090,720) {$\hat{K}_d$};

\end{tikzpicture}%
}% end \resizebox
\caption{Control Technique 3: Proposed ESC-Tuned PD Depth Controller}
\label{fig:control_technique_3}
\end{subfigure}

\caption{Block diagrams of the three ESC-based control techniques.}
\label{fig:control_techniques_all}
\end{figure*}"""

# ============================================================
# 1. Replace the standalone Technique-1 figure* with the new combined figure
# ============================================================
# Unique start: \begin{figure*}[t]\n\centering\n\begin{tikzpicture}[
# Unique end: \end{figure*}
# We need to find the FIRST \begin{figure*}[t] in the file (which is T1).

t1_open  = r'\begin{figure*}[t]' + '\n'
t1_close = r'\end{figure*}' + '\n'

idx_start = content.find(t1_open)
if idx_start == -1:
    raise RuntimeError("Could not find start of Technique-1 figure*")

idx_end = content.find(t1_close, idx_start)
if idx_end == -1:
    raise RuntimeError("Could not find end of Technique-1 figure*")
idx_end += len(t1_close)

old_t1 = content[idx_start:idx_end]
print(f"T1 figure found: chars {idx_start}..{idx_end}  ({idx_end - idx_start} chars)")
content = content[:idx_start] + NEW_FIGURE + '\n' + content[idx_end:]
print("T1 replaced with combined figure.")

# ============================================================
# 2. Remove the standalone Technique-2 figure (single column)
#    Identified by: \begin{figure}[t] ... \definecolor{AC}{RGB}{20,20,100}
#    (no ESCGreen between BlockBlue and AC) ... \end{figure}
# ============================================================
# Find \begin{figure}[t] that is followed (within 600 chars) by
# \definecolor{BlockBlue} but NOT \definecolor{ESCGreen}

import re

# Pattern: \begin{figure}[t] ... \definecolor{BlockBlue}...{AC} (no ESCGreen) ... \end{figure}
# We match greedily up to the first \end{figure} after the BlockBlue definition w/o ESCGreen.
# Since T3 has ESCGreen, a pattern that requires NO ESCGreen uniquely identifies T2.

# Find all \begin{figure}[t]....\end{figure} blocks
fig_pattern = re.compile(
    r'\\begin\{figure\}\[t\].*?\\end\{figure\}',
    re.DOTALL
)

matches = list(fig_pattern.finditer(content))
print(f"Found {len(matches)} single-column figure environments.")

t2_match = None
t3_match = None
for m in matches:
    body = m.group(0)
    has_blockblue = 'BlockBlue' in body
    has_escgreen  = 'ESCGreen'  in body
    has_tech2_cap = 'Technique 2' in body or 'ESC block diagram: Technique 2' in body
    has_tech3_cap = 'Technique 3' in body or 'ESC block diagram: Technique 3' in body
    if has_blockblue and not has_escgreen and has_tech2_cap:
        t2_match = m
    if has_blockblue and has_escgreen and has_tech3_cap:
        t3_match = m

# Remove T3 first (it comes later in the file, so removing it won't shift T2's indices)
# Actually, after replacing T1, the positions have already shifted.
# We search in the updated content.

if t3_match:
    print(f"T3 figure found: chars {t3_match.start()}..{t3_match.end()}")
    # Remove it (replace with empty)
    content = content[:t3_match.start()] + content[t3_match.end():]
    print("T3 standalone figure removed.")
else:
    print("WARNING: T3 standalone figure NOT found – skipping.")

# Re-find T2 after T3 removal (positions changed)
matches2 = list(fig_pattern.finditer(content))
t2_match2 = None
for m in matches2:
    body = m.group(0)
    has_blockblue = 'BlockBlue' in body or 'gray!12' in body
    has_escgreen  = 'ESCGreen'  in body
    has_tech2_cap = ('Technique 2' in body or
                     'ESC block diagram: Technique 2' in body or
                     'definecolor{AC}' in body and not has_escgreen)
    # More reliable: check for AC definecolor without ESCGreen
    has_ac   = 'definecolor{AC}' in body
    has_blockblue_def = 'definecolor{BlockBlue}' in body
    if has_blockblue_def and has_ac and not has_escgreen:
        t2_match2 = m
        break

if t2_match2:
    print(f"T2 figure found (after T3 removal): chars {t2_match2.start()}..{t2_match2.end()}")
    content = content[:t2_match2.start()] + content[t2_match2.end():]
    print("T2 standalone figure removed.")
else:
    print("WARNING: T2 standalone figure NOT found – skipping.")

# ============================================================
# Write result
# ============================================================
with open(src, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone. main.tex updated ({len(content)} chars total).")
print(f"Backup at: {bak}")
