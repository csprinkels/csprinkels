"""Build the SVG assets used by the GitHub-rendered profile concept.

This script uses only Python's standard library. The supplied header artwork is
embedded in the hero SVG so GitHub can render it without loading remote assets.
"""

from base64 import b64encode
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
HEADER_ART = ROOT.parent / "assets" / "hawaii-header.jpg"


def write_svg(name: str, content: str) -> None:
    (ASSETS / name).write_text(content.strip() + "\n", encoding="utf-8")


def build_header() -> None:
    encoded_art = b64encode(HEADER_ART.read_bytes()).decode("ascii")
    write_svg(
        "profile-header.svg",
        f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="560" viewBox="0 0 1200 560" role="img" aria-labelledby="title desc">
  <title id="title">Aloha, I'm Christian</title>
  <desc id="desc">Christian Sprinkel builds resilient digital products for Hawaiʻi and beyond. An ʻio soars over the Hawaiian Islands.</desc>
  <defs>
    <clipPath id="frame"><rect width="1200" height="560" rx="28"/></clipPath>
    <linearGradient id="shade" x1="0" x2="1">
      <stop offset="0" stop-color="#082F3C" stop-opacity=".97"/>
      <stop offset=".48" stop-color="#0A3E4C" stop-opacity=".78"/>
      <stop offset=".78" stop-color="#0A3E4C" stop-opacity=".12"/>
      <stop offset="1" stop-color="#0A3E4C" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="bottom" x1="0" y1="0" x2="0" y2="1">
      <stop offset=".45" stop-color="#082F3C" stop-opacity="0"/>
      <stop offset="1" stop-color="#082F3C" stop-opacity=".7"/>
    </linearGradient>
  </defs>

  <g clip-path="url(#frame)">
    <image href="data:image/jpeg;base64,{encoded_art}" width="1200" height="800" y="0" preserveAspectRatio="xMidYMin slice"/>
    <rect width="1200" height="560" fill="url(#shade)"/>
    <rect width="1200" height="560" fill="url(#bottom)"/>

    <g fill="none" stroke="#7CDCE2" stroke-opacity=".22">
      <path d="M-20 488 C100 430 185 535 305 475 S520 430 650 490 870 535 1010 470 1160 435 1240 475" stroke-width="3"/>
      <path d="M-20 510 C100 452 185 557 305 497 S520 452 650 512 870 557 1010 492 1160 457 1240 497" stroke-width="2"/>
      <path d="M-20 532 C100 474 185 579 305 519 S520 474 650 534 870 579 1010 514 1160 479 1240 519" stroke-width="1.5"/>
    </g>

    <g font-family="Inter, Segoe UI, Arial, sans-serif">
      <text x="68" y="108" fill="#F5B54C" font-size="23" font-weight="700" letter-spacing="5">ALOHA, I'M CHRISTIAN</text>
      <text x="64" y="190" fill="#FFFFFF" font-size="66" font-weight="800">Building resilient</text>
      <text x="64" y="264" fill="#FFFFFF" font-size="66" font-weight="800">digital products.</text>
      <text x="68" y="316" fill="#B8F0EE" font-size="25">For Hawaiʻi and beyond.</text>

      <rect x="66" y="362" width="568" height="58" rx="29" fill="#082F3C" fill-opacity=".72" stroke="#7CDCE2" stroke-opacity=".7"/>
      <circle cx="101" cy="391" r="8" fill="#F07855"/>
      <text x="126" y="400" fill="#FFFFFF" font-size="18" font-weight="600" letter-spacing="1.4">SOFTWARE · IT · PRODUCT</text>
    </g>
  </g>
  <rect x="1.5" y="1.5" width="1197" height="557" rx="27" fill="none" stroke="#D9A441" stroke-width="3" stroke-opacity=".7"/>
</svg>
""",
    )


def build_impact_strip() -> None:
    write_svg(
        "impact-strip.svg",
        """
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="210" viewBox="0 0 1200 210" role="img" aria-labelledby="title desc">
  <title id="title">Impact at a glance</title>
  <desc id="desc">Five plus years of experience, twelve plus emergency feeds, 177 practice questions, and work across web, mobile, cloud, and IT.</desc>
  <rect width="1200" height="210" rx="24" fill="#082F3C"/>
  <path d="M0 18Q0 0 18 0h264v7H0z" fill="#F07855"/>
  <path d="M306 0h282v7H306z" fill="#55C9CD"/>
  <path d="M612 0h282v7H612z" fill="#F5B54C"/>
  <path d="M918 0h264q18 0 18 18v-11H918z" fill="#55C9CD"/>
  <g stroke="#356370" stroke-width="1">
    <path d="M300 28v154"/><path d="M606 28v154"/><path d="M912 28v154"/>
  </g>
  <g font-family="Inter, Segoe UI, Arial, sans-serif" text-anchor="middle">
    <g transform="translate(150)">
      <path d="M-30 74q15-22 30 0t30 0M-30 88q15-22 30 0t30 0" fill="none" stroke="#7CDCE2" stroke-width="5" stroke-linecap="round"/>
      <text y="137" fill="#FFFFFF" font-size="42" font-weight="800">5+</text>
      <text y="169" fill="#B8D9DD" font-size="17" font-weight="600">YEARS EXPERIENCE</text>
    </g>
    <g transform="translate(456)">
      <path d="M0 54v38M-18 70a25 25 0 0 1 36 0M-30 58a41 41 0 0 1 60 0" fill="none" stroke="#F07855" stroke-width="5" stroke-linecap="round"/>
      <circle cy="93" r="7" fill="#F07855"/>
      <text y="137" fill="#FFFFFF" font-size="42" font-weight="800">12+</text>
      <text y="169" fill="#B8D9DD" font-size="17" font-weight="600">EMERGENCY FEEDS</text>
    </g>
    <g transform="translate(762)">
      <path d="M-28 55h20q8 0 8 8v34q0-8-10-8h-18zM28 55H8q-8 0-8 8v34q0-8 10-8h18z" fill="none" stroke="#F5B54C" stroke-width="5" stroke-linejoin="round"/>
      <text y="137" fill="#FFFFFF" font-size="42" font-weight="800">177</text>
      <text y="169" fill="#B8D9DD" font-size="17" font-weight="600">PRACTICE QUESTIONS</text>
    </g>
    <g transform="translate(1056)">
      <circle cx="-30" cy="73" r="13" fill="none" stroke="#7CDCE2" stroke-width="4"/>
      <rect x="-8" y="60" width="26" height="26" rx="5" fill="none" stroke="#7CDCE2" stroke-width="4"/>
      <path d="M42 59l15 9v18l-15 9-15-9V68z" fill="none" stroke="#7CDCE2" stroke-width="4"/>
      <text y="133" fill="#FFFFFF" font-size="27" font-weight="800">WEB · MOBILE</text>
      <text y="164" fill="#FFFFFF" font-size="27" font-weight="800">CLOUD · IT</text>
    </g>
  </g>
</svg>
""",
    )


def placeholder_svg(
    *,
    title: str,
    subtitle: str,
    start: str,
    end: str,
    accent: str,
    illustration: str,
) -> str:
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="560" height="350" viewBox="0 0 560 350" role="img" aria-label="Temporary image slot for {title}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop stop-color="{start}"/><stop offset="1" stop-color="{end}"/>
    </linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="#FFFFFF" stroke-opacity=".08"/>
    </pattern>
  </defs>
  <rect width="560" height="350" rx="22" fill="url(#bg)"/>
  <rect width="560" height="350" rx="22" fill="url(#grid)"/>
{illustration.strip()}
  <rect x="28" y="28" width="154" height="34" rx="17" fill="#082F3C" fill-opacity=".78" stroke="{accent}"/>
  <text x="105" y="50" fill="#FFFFFF" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="13" font-weight="700" text-anchor="middle" letter-spacing="1.5">IMAGE SLOT</text>
  <text x="30" y="284" fill="#FFFFFF" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="32" font-weight="800">{title}</text>
  <text x="30" y="317" fill="#FFFFFF" fill-opacity=".8" font-family="Inter, Segoe UI, Arial, sans-serif" font-size="16">{subtitle}</text>
  <rect x="1.5" y="1.5" width="557" height="347" rx="21" fill="none" stroke="{accent}" stroke-width="3" stroke-opacity=".8"/>
</svg>
"""


def build_placeholders() -> None:
    write_svg(
        "kilo-placeholder.svg",
        placeholder_svg(
            title="Kilo",
            subtitle="Replace with product screenshot",
            start="#082F3C",
            end="#086F78",
            accent="#F07855",
            illustration="""
  <g transform="translate(300 140)">
    <path d="M-105 18l25-19 31 6 21-23 31 11 19 28-31 10-17 31-38-10-25 8z" fill="#2CA6A4" stroke="#9DE3DE" stroke-width="3"/>
    <path d="M34-32l24-14 30 13 10 25-27 12-30-11zM105 28l17-12 24 8 7 22-24 9-21-10z" fill="#2CA6A4" stroke="#9DE3DE" stroke-width="3"/>
    <circle cx="-15" cy="4" r="28" fill="#F07855" fill-opacity=".2"/>
    <path d="M-15-18a20 20 0 0 0-20 20c0 17 20 38 20 38S5 19 5 2a20 20 0 0 0-20-20z" fill="#F07855"/>
    <circle cx="-15" cy="2" r="7" fill="#FFFFFF"/>
  </g>
""",
        ),
    )
    write_svg(
        "aloha-permits-placeholder.svg",
        placeholder_svg(
            title="Aloha Permits",
            subtitle="Replace with App Store screenshot",
            start="#D85D45",
            end="#E6A33D",
            accent="#7CDCE2",
            illustration="""
  <g transform="translate(280 138)">
    <rect x="-58" y="-92" width="116" height="184" rx="23" fill="#082F3C" stroke="#FFFFFF" stroke-width="5"/>
    <rect x="-43" y="-66" width="86" height="128" rx="6" fill="#F6F0E5"/>
    <rect x="-18" y="-82" width="36" height="5" rx="2.5" fill="#7CDCE2"/>
    <path d="M0-45l33 33L0 21l-33-33z" fill="#F5B54C" stroke="#082F3C" stroke-width="4"/>
    <path d="M-11-22q22 7 13 28M2 6l-8-8M2 6l9-6" fill="none" stroke="#082F3C" stroke-width="5" stroke-linecap="round"/>
    <circle cy="76" r="7" fill="#7CDCE2"/>
  </g>
""",
        ),
    )
    write_svg(
        "portfolio-placeholder.svg",
        placeholder_svg(
            title="csprinkels.com",
            subtitle="Replace with 3D portfolio screenshot",
            start="#0A3947",
            end="#176D78",
            accent="#F5B54C",
            illustration="""
  <g transform="translate(280 150)" fill="none" stroke-linejoin="round">
    <path d="M-154 55L-62-45 2 18 66-73 157 55z" fill="#0D515D" stroke="#7CDCE2" stroke-width="3"/>
    <path d="M-154 55L-35 75 2 18 74 79 157 55M-62-45L-35 75M66-73L74 79M-62-45L2 18M66-73L2 18" stroke="#7CDCE2" stroke-opacity=".65" stroke-width="2"/>
    <circle cx="66" cy="-73" r="24" fill="#F5B54C" fill-opacity=".18" stroke="#F5B54C" stroke-width="3"/>
    <path d="M-185 91q80-34 160 0t160 0 95 0" stroke="#F5B54C" stroke-width="4"/>
  </g>
""",
        ),
    )


if __name__ == "__main__":
    ASSETS.mkdir(parents=True, exist_ok=True)
    build_header()
    build_impact_strip()
    build_placeholders()
