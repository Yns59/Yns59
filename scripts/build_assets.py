#!/usr/bin/env python3
"""Génère les visuels du profil GitHub.

  assets/banner.svg    bannière « terminal » animée
  assets/pipeline.svg  roadmap sous forme de pipeline CI, lue dans roadmap.yml

Usage : python scripts/build_assets.py
"""
from __future__ import annotations

import datetime as dt
from html import escape
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

# Palette : noir chaud + crème + ambre (volontairement loin du bleu/violet GitHub)
BG, PANEL, BORDER = "#14110f", "#1b1713", "#2b2520"
CREAM, DIM, MUTED, GREY = "#f2e8d5", "#b9ad98", "#8a7f70", "#4a4238"
AMBER, GREEN, RED = "#ffb454", "#8fd18f", "#ff6b5e"
FONT = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"


def svg_open(w: int, h: int, title: str, desc: str, css: str) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
        f'role="img" aria-labelledby="t d" font-family="{FONT}">'
        f'<title id="t">{escape(title)}</title><desc id="d">{escape(desc)}</desc>'
        f"<style>{css}</style>"
    )


# --------------------------------------------------------------------------- #
#  Bannière terminal
# --------------------------------------------------------------------------- #

BANNER_CSS = """
.cover{animation-name:reveal;animation-fill-mode:backwards}
@keyframes reveal{from{transform:translateX(calc(var(--w) * -1))}}
.fade{animation:fade .7s ease-out backwards}
@keyframes fade{from{opacity:0;transform:translateY(6px)}}
.blink{animation:blink 1.05s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.pulse{animation:pulse 1.6s ease-in-out infinite}
@keyframes pulse{50%{opacity:.35}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
"""


def typed(x, y, size, parts, delay, cps=34):
    """Ligne tapée au clavier : un cache de la couleur du fond glisse de gauche à droite."""
    n = sum(len(t) for t, _ in parts)
    w = round(n * size * 0.6, 1)
    spans = "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in parts)
    dur = round(n / cps, 2)
    svg = (
        f'<text x="{x}" y="{y}" font-size="{size}" textLength="{w}" lengthAdjust="spacing" '
        f'xml:space="preserve">{spans}</text>'
        f'<rect class="cover" x="{x + w}" y="{y - size * 1.05:.1f}" width="{w}" height="{size * 1.5:.1f}" '
        f'fill="{BG}" style="--w:{w}px;animation-duration:{dur}s;animation-delay:{delay}s;'
        f'animation-timing-function:steps({n},end)"/>'
    )
    return svg, round(delay + dur, 2)


def build_banner() -> str:
    W, H, X = 900, 350, 44
    body: list[str] = []
    t = 0.4

    def line(y, size, parts, gap=0.25):
        nonlocal t
        svg, end = typed(X, y, size, parts, t)
        body.append(svg)
        t = round(end + gap, 2)

    line(84, 14, [("$ ", AMBER), ("whoami", CREAM)])

    body.append(
        f'<g class="fade" style="animation-delay:{t}s">'
        f'<text x="{X}" y="154" font-size="84" font-weight="800" fill="{AMBER}" opacity=".45" '
        f'filter="url(#glow)" textLength="300" lengthAdjust="spacing">YOUNES</text>'
        f'<text x="{X}" y="154" font-size="84" font-weight="800" fill="{CREAM}" '
        f'textLength="300" lengthAdjust="spacing">YOUNES</text>'
        f'<rect class="blink" x="{X + 322}" y="98" width="28" height="56" fill="{AMBER}"/></g>'
    )
    t = round(t + 0.6, 2)

    line(186, 15, [("étudiant en bachelor informatique · enigma · lille", DIM)])
    line(228, 14, [("$ ", AMBER), ("cat mission.txt", CREAM)])
    line(254, 16, [("devenir la meilleure version de moi-même.", AMBER)])
    line(296, 14, [("$ ", AMBER), ("./roadmap --now", CREAM)])
    line(
        322,
        14,
        [
            ("dev web ", CREAM),
            ("+", AMBER),
            (" devops  ·  ", CREAM),
            ("typescript → react → next.js", GREEN),
        ],
    )

    # Panneau status.json
    px, py, pw, ph = 568, 62, 288, 268
    K, S, P = AMBER, GREEN, DIM
    json_lines = [
        [("{", P)],
        [("  ", P), ('"stage"', K), (": ", P), ('"moderne"', S), (",", P)],
        [("  ", P), ('"maintenant"', K), (": ", P), ('"terraform"', S), (",", P)],
        [("  ", P), ('"ensuite"', K), (": [", P), ('"Ansible"', S), (", ", P), ('"Kubernetes"', S), ("],", P)],
        [("  ", P), ('"homelab"', K), (": ", P), ("true", AMBER), (",", P)],
        [("  ", P), ('"alternance"', K), (": ", P), ('"recherche active"', S)],
        [("}", P)],
    ]
    panel = [
        f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="10" fill="{PANEL}" stroke="{BORDER}"/>',
        f'<text x="{px + 18}" y="{py + 26}" font-size="11" fill="{MUTED}">status.json</text>',
        f'<line x1="{px}" y1="{py + 38}" x2="{px + pw}" y2="{py + 38}" stroke="{BORDER}"/>',
    ]
    for i, parts in enumerate(json_lines):
        spans = "".join(f'<tspan fill="{c}">{escape(s)}</tspan>' for s, c in parts)
        panel.append(
            f'<text class="fade" style="animation-delay:{round(1.0 + i * 0.2, 2)}s" x="{px + 18}" '
            f'y="{py + 70 + i * 26}" font-size="12" xml:space="preserve">{spans}</text>'
        )
    panel.append(f'<circle class="pulse" cx="{px + 24}" cy="{py + ph - 26}" r="4" fill="{AMBER}"/>')
    panel.append(
        f'<text x="{px + 38}" y="{py + ph - 22}" font-size="11" fill="{MUTED}">build en cours</text>'
    )

    out = [
        svg_open(
            W,
            H,
            "Younes, terminal",
            "Terminal animé : whoami, Younes, étudiant en Bachelor Informatique à Enigma à Lille. "
            "Mission : devenir la meilleure version de moi-même. Maintenant TypeScript, ensuite "
            "React et Next.js. Recherche une alternance.",
            BANNER_CSS,
        ),
        "<defs>"
        '<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="7"/></filter>'
        '<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">'
        '<rect width="4" height="1" fill="#000" opacity=".1"/></pattern>'
        '<radialGradient id="vig" cx="50%" cy="50%" r="75%">'
        '<stop offset="60%" stop-color="#000" stop-opacity="0"/>'
        '<stop offset="100%" stop-color="#000" stop-opacity=".45"/></radialGradient>'
        "</defs>",
        f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="{BG}" stroke="{BORDER}"/>',
        f'<path d="M1 14A13 13 0 0 1 14 1H{W - 14}A13 13 0 0 1 {W - 1} 14V38H1Z" fill="{PANEL}"/>',
        f'<line x1="1" y1="38" x2="{W - 1}" y2="38" stroke="{BORDER}"/>',
        f'<circle cx="24" cy="19" r="5.5" fill="{RED}" opacity=".85"/>',
        f'<circle cx="44" cy="19" r="5.5" fill="{AMBER}" opacity=".85"/>',
        f'<circle cx="64" cy="19" r="5.5" fill="{GREEN}" opacity=".85"/>',
        f'<text x="{W // 2}" y="23" font-size="12" fill="{MUTED}" text-anchor="middle">younes@lille: ~/profil</text>',
        f'<circle class="pulse" cx="{W - 140}" cy="19" r="3.5" fill="{AMBER}"/>',
        f'<text x="{W - 24}" y="23" font-size="11" fill="{AMBER}" text-anchor="end">pipeline en cours</text>',
        *body,
        *panel,
        f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="url(#scan)" pointer-events="none"/>',
        f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="14" fill="url(#vig)" pointer-events="none"/>',
        "</svg>",
    ]
    return "".join(out)


# --------------------------------------------------------------------------- #
#  Pipeline (roadmap.yml)
# --------------------------------------------------------------------------- #

PIPELINE_CSS = """
.pill{animation:rise .6s cubic-bezier(.2,.7,.2,1) backwards}
@keyframes rise{from{opacity:0;transform:translateY(8px)}}
.bar{transform-box:fill-box;transform-origin:0 50%;animation:grow 1.1s cubic-bezier(.2,.7,.2,1) backwards}
@keyframes grow{from{transform:scaleX(0)}}
.flow{stroke-dasharray:5 5;animation:flow .9s linear infinite}
@keyframes flow{to{stroke-dashoffset:-10}}
.pulse{animation:pulse 1.8s ease-in-out infinite}
@keyframes pulse{50%{opacity:.45}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
"""

COLOR = {"passed": GREEN, "running": AMBER, "next": AMBER, "pending": GREY}
LABEL = {"passed": "acquis", "running": "en cours", "next": "prochain", "pending": "à venir"}


def icon(status: str, cx: float, cy: float, r: float = 6) -> str:
    g = f'<g transform="translate({cx:.1f} {cy:.1f})">'
    if status == "passed":
        return (
            f'{g}<circle r="{r}" fill="{GREEN}"/>'
            f'<path d="M-2.6 0.2L-0.8 2.1L2.8 -2.2" fill="none" stroke="{BG}" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round"/></g>'
        )
    rr = r - 0.5
    if status == "running":
        return (
            f'{g}<circle r="{rr}" fill="none" stroke="{GREY}" stroke-width="1.8"/>'
            f'<g><path d="M0 {-rr}A{rr} {rr} 0 0 1 {rr} 0" fill="none" stroke="{AMBER}" '
            f'stroke-width="1.8" stroke-linecap="round"/>'
            f'<animateTransform attributeName="transform" type="rotate" from="0" to="360" '
            f'dur="1s" repeatCount="indefinite"/></g></g>'
        )
    if status == "next":
        return (
            f'{g}<circle r="{rr}" fill="none" stroke="{AMBER}" stroke-width="1.4" stroke-dasharray="2 2"/>'
            f'<circle r="1.8" fill="{AMBER}"/></g>'
        )
    return f'{g}<circle r="{rr}" fill="none" stroke="{GREY}" stroke-width="1.5"/></g>'


def job_status(job: dict, thr: int) -> str:
    forced = job.get("status")
    if forced in COLOR:
        return forced
    p = job["progress"]
    if p >= thr:
        return "passed"
    return "running" if p > 0 else "pending"


def stage_status(statuses: list[str]) -> str:
    if all(s == "passed" for s in statuses):
        return "passed"
    if all(s in ("pending", "next") for s in statuses):
        return "pending"
    return "running"


def build_pipeline() -> str:
    cfg = yaml.safe_load((ROOT / "roadmap.yml").read_text(encoding="utf-8"))
    thr = int(cfg.get("seuil_acquis", 80))
    stages = cfg["stages"]
    n = len(stages)

    # Une colonne par étape : garder une largeur lisible même avec 8 étapes.
    # Le SVG peut être affiché à une taille réduite dans GitHub, tout en restant lisible
    # lorsqu'il est ouvert seul.
    PAD, GAPX, MIN_COLW = 24, 14, 142
    W = max(900, 2 * PAD + n * MIN_COLW + GAPX * (n - 1))
    colw = (W - 2 * PAD - GAPX * (n - 1)) / n
    PH, GAPY, TOP, RAIL = 36, 6, 166, 148
    max_jobs = max(len(s["jobs"]) for s in stages)
    H = TOP + max_jobs * (PH + GAPY) - GAPY + 62
    today = dt.date.today().isoformat()

    info = []
    all_progress: list[float] = []
    for st in stages:
        sts = [job_status(j, thr) for j in st["jobs"]]
        prog = [float(j["progress"]) for j in st["jobs"]]
        all_progress += prog
        info.append(
            {
                "status": stage_status(sts),
                "avg": round(sum(prog) / len(prog)),
                "jobs": [(j["name"], int(j["progress"]), s) for j, s in zip(st["jobs"], sts)],
            }
        )
    overall = round(sum(all_progress) / len(all_progress))
    xs = [PAD + i * (colw + GAPX) for i in range(n)]

    out = [
        svg_open(
            W,
            H,
            "Roadmap Dev vers DevOps",
            f"Pipeline de progression généré depuis roadmap.yml, avancement global {overall} pour cent. "
            + " ; ".join(
                f"{s['label']} : {info[i]['avg']} pour cent" for i, s in enumerate(stages)
            ),
            PIPELINE_CSS,
        ),
        f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="{BG}" stroke="{BORDER}"/>',
        f'<text x="{PAD}" y="36" font-size="15" font-weight="700" fill="{CREAM}">{escape(cfg.get("titre", "ROADMAP"))}</text>',
        f'<text x="{PAD}" y="54" font-size="10.5" fill="{MUTED}">roadmap.yml → GitHub Actions → ce visuel</text>',
        f'<text x="{W - PAD}" y="44" font-size="30" font-weight="700" fill="{AMBER}" text-anchor="end">{overall}%</text>',
        f'<text x="{W - PAD}" y="60" font-size="10" fill="{MUTED}" text-anchor="end">progression globale</text>',
        f'<rect x="{PAD}" y="70" width="{W - 2 * PAD}" height="4" rx="2" fill="{BORDER}"/>',
        f'<rect class="bar" x="{PAD}" y="70" width="{(W - 2 * PAD) * overall / 100:.1f}" height="4" rx="2" fill="{AMBER}"/>',
    ]

    # Colonne « focus »
    for i, st in enumerate(stages):
        if st.get("focus"):
            hl_h = TOP + max_jobs * (PH + GAPY) - GAPY + 10 - 84
            out.append(
                f'<rect x="{xs[i] - 7:.1f}" y="84" width="{colw + 14:.1f}" height="{hl_h}" rx="10" '
                f'fill="{AMBER}" fill-opacity=".045" stroke="{AMBER}" stroke-opacity=".3" stroke-dasharray="3 4"/>'
            )
            out.append(
                f'<text x="{xs[i]:.1f}" y="97" font-size="9" font-weight="700" letter-spacing="1.2" '
                f'fill="{AMBER}">▼ FOCUS ACTUEL</text>'
            )

    # Rail entre les étapes
    for i in range(n - 1):
        x1, x2 = xs[i] + 13 + 8, xs[i + 1] + 13 - 8
        s = info[i]["status"]
        if s == "passed":
            out.append(f'<line x1="{x1:.1f}" y1="{RAIL}" x2="{x2:.1f}" y2="{RAIL}" stroke="{GREEN}" stroke-width="2"/>')
        elif s == "running":
            out.append(f'<line class="flow" x1="{x1:.1f}" y1="{RAIL}" x2="{x2:.1f}" y2="{RAIL}" stroke="{AMBER}" stroke-width="2"/>')
        else:
            out.append(
                f'<line x1="{x1:.1f}" y1="{RAIL}" x2="{x2:.1f}" y2="{RAIL}" stroke="{GREY}" '
                f'stroke-width="2" stroke-dasharray="2 5"/>'
            )

    # Étapes + jobs
    for si, st in enumerate(stages):
        x, d = xs[si], info[si]
        color = COLOR[d["status"]]
        stage_label = str(st["label"])
        stage_font = min(10.5, max(7.5, 150 / max(len(stage_label), 1)))
        out.append(
            f'<text x="{x:.1f}" y="114" font-size="{stage_font:.1f}" font-weight="700" fill="{CREAM}">'
            f'{si + 1:02d} · {escape(stage_label)}</text>'
        )
        out.append(
            f'<text x="{x:.1f}" y="129" font-size="10" fill="{MUTED}">'
            f'<tspan fill="{color}">{LABEL[d["status"]]}</tspan> · {d["avg"]}%</text>'
        )
        out.append(icon(d["status"], x + 13, RAIL, 7))
        out.append(
            f'<line x1="{x + 13:.1f}" y1="{RAIL + 8}" x2="{x + 13:.1f}" y2="{TOP}" stroke="{color}" '
            f'stroke-width="1.5" stroke-opacity=".5"/>'
        )

        for k, (name, prog, status) in enumerate(d["jobs"]):
            y = TOP + k * (PH + GAPY)
            c = COLOR[status]
            delay = round(0.15 + si * 0.12 + k * 0.05, 2)
            stroke = {
                "passed": f'stroke="{GREEN}" stroke-opacity=".45"',
                "running": f'stroke="{AMBER}" stroke-opacity=".75"',
                "next": f'stroke="{AMBER}" stroke-opacity=".55" stroke-dasharray="3 3"',
                "pending": f'stroke="{BORDER}"',
            }[status]
            cls = ' class="pulse"' if status == "running" else ""
            bw = colw - 26 - 34
            fill_w = bw * prog / 100
            bar = (
                f'<rect class="bar" x="{x + 26:.1f}" y="{y + 24}" width="{fill_w:.1f}" height="4" rx="2" '
                f'fill="{c}" style="animation-delay:{delay + 0.2}s"/>'
                if prog > 0
                else ""
            )
            # Éviter que les noms longs débordent sur le pourcentage dans les colonnes étroites.
            name_text = str(name)
            max_chars = max(7, int((colw - 66) / 6.2))
            if len(name_text) > max_chars:
                name_text = name_text[: max_chars - 1] + "…"
            out.append(
                f'<g class="pill" style="animation-delay:{delay}s">'
                f'<rect{cls} x="{x:.1f}" y="{y}" width="{colw:.1f}" height="{PH}" rx="8" fill="{PANEL}" {stroke}/>'
                f"{icon(status, x + 13, y + 14)}"
                f'<text x="{x + 26:.1f}" y="{y + 16}" font-size="11.5" '
                f'fill="{MUTED if status == "pending" else CREAM}">{escape(name_text)}</text>'
                f'<rect x="{x + 26:.1f}" y="{y + 24}" width="{bw:.1f}" height="4" rx="2" fill="{BORDER}"/>'
                f"{bar}"
                f'<text x="{x + colw - 8:.1f}" y="{y + 29}" font-size="9" fill="{MUTED}" text-anchor="end">{prog}%</text>'
                f"</g>"
            )

    # Légende
    fy = H - 26
    lx = PAD
    for status, label in [
        ("passed", "acquis"),
        ("running", "en cours"),
        ("next", "prochain objectif"),
        ("pending", "plus tard"),
    ]:
        out.append(icon(status, lx + 6, fy))
        out.append(f'<text x="{lx + 18}" y="{fy + 4}" font-size="10" fill="{MUTED}">{label}</text>')
        lx += 18 + len(label) * 6.1 + 22
    out.append(
        f'<text x="{W - PAD}" y="{fy + 4}" font-size="10" fill="{MUTED}" text-anchor="end">'
        f"généré le {today} depuis roadmap.yml</text>"
    )
    out.append("</svg>")
    return "".join(out)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "banner.svg").write_text(build_banner(), encoding="utf-8")
    (ASSETS / "pipeline.svg").write_text(build_pipeline(), encoding="utf-8")
    print("OK -> assets/banner.svg, assets/pipeline.svg")


if __name__ == "__main__":
    main()
