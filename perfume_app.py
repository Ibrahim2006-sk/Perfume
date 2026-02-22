"""Perfume recommendation app.

A simple command-line app that recommends perfume styles
based on weather and user preference (male/female).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class PerfumeRecommendation:
    name: str
    notes: str
    reason: str


RECOMMENDATIONS: Dict[str, Dict[str, List[PerfumeRecommendation]]] = {
    "male": {
        "hot": [
            PerfumeRecommendation(
                name="Dior Homme Cologne",
                notes="citrus, musky",
                reason="Fresh citrus profiles feel clean and light in high heat.",
            ),
            PerfumeRecommendation(
                name="Acqua di Gio",
                notes="marine, citrus, aromatic",
                reason="Aquatic notes are refreshing and not too heavy for warm days.",
            ),
        ],
        "mild": [
            PerfumeRecommendation(
                name="Bleu de Chanel",
                notes="grapefruit, incense, woody",
                reason="Balanced woody-citrus profile works across spring/autumn weather.",
            ),
            PerfumeRecommendation(
                name="Prada Luna Rossa Carbon",
                notes="lavender, metallic, ambroxan",
                reason="A versatile aromatic scent for moderate temperatures.",
            ),
        ],
        "cold": [
            PerfumeRecommendation(
                name="Tom Ford Noir Extreme",
                notes="amber, vanilla, spices",
                reason="Richer sweet-spicy scents project better in cold air.",
            ),
            PerfumeRecommendation(
                name="Spicebomb Extreme",
                notes="tobacco, cinnamon, vanilla",
                reason="Warm spicy profiles are cozy and long-lasting in winter.",
            ),
        ],
        "rainy": [
            PerfumeRecommendation(
                name="Terre d'Hermès",
                notes="orange, vetiver, patchouli",
                reason="Earthy-citrus notes pair well with damp, rainy conditions.",
            ),
            PerfumeRecommendation(
                name="Montblanc Explorer",
                notes="bergamot, vetiver, ambroxan",
                reason="Woody fresh profile remains elegant in humid/rainy weather.",
            ),
        ],
    },
    "female": {
        "hot": [
            PerfumeRecommendation(
                name="Dolce & Gabbana Light Blue",
                notes="lemon, apple, cedar",
                reason="Bright fruity-citrus scents feel airy in summer heat.",
            ),
            PerfumeRecommendation(
                name="Versace Bright Crystal",
                notes="pomegranate, peony, musk",
                reason="Soft floral freshness is comfortable in warm climates.",
            ),
        ],
        "mild": [
            PerfumeRecommendation(
                name="Chanel Chance Eau Tendre",
                notes="grapefruit, jasmine, white musk",
                reason="Clean floral-fruity scents fit changing temperatures.",
            ),
            PerfumeRecommendation(
                name="YSL Libre",
                notes="lavender, orange blossom, vanilla",
                reason="A balanced floral with slight warmth for daily wear.",
            ),
        ],
        "cold": [
            PerfumeRecommendation(
                name="YSL Black Opium",
                notes="coffee, vanilla, white flowers",
                reason="Sweet warm perfumes bloom beautifully in cold weather.",
            ),
            PerfumeRecommendation(
                name="Lancôme La Vie Est Belle",
                notes="iris, praline, patchouli",
                reason="Richer gourmand notes provide depth in winter.",
            ),
        ],
        "rainy": [
            PerfumeRecommendation(
                name="Narciso Rodriguez For Her",
                notes="rose, peach, musk",
                reason="Musky florals feel elegant and comforting on rainy days.",
            ),
            PerfumeRecommendation(
                name="Jo Malone Wood Sage & Sea Salt",
                notes="sea salt, sage, ambrette",
                reason="Mineral-aromatic freshness pairs nicely with damp weather.",
            ),
        ],
    },
}


def normalize_gender(value: str) -> str:
    value = value.strip().lower()
    aliases = {
        "m": "male",
        "man": "male",
        "male": "male",
        "f": "female",
        "woman": "female",
        "female": "female",
    }
    if value not in aliases:
        raise ValueError("Gender must be male or female.")
    return aliases[value]


def weather_from_temperature(temp_c: float, rainy: bool = False) -> str:
    if rainy:
        return "rainy"
    if temp_c >= 30:
        return "hot"
    if temp_c <= 12:
        return "cold"
    return "mild"


def recommend(gender: str, temp_c: float, rainy: bool = False) -> List[PerfumeRecommendation]:
    normalized_gender = normalize_gender(gender)
    weather = weather_from_temperature(temp_c=temp_c, rainy=rainy)
    return RECOMMENDATIONS[normalized_gender][weather]


def run_cli() -> None:
    print("=== Perfume Weather Helper ===")
    print("Find which perfume style to wear in current weather (male/female).\n")

    gender = input("Enter gender (male/female): ").strip()
    temp_input = input("Enter temperature in °C (example 22): ").strip()
    rainy_input = input("Is it rainy? (yes/no): ").strip().lower()

    try:
        temp_c = float(temp_input)
        rainy = rainy_input in {"yes", "y", "true", "1"}
        picks = recommend(gender=gender, temp_c=temp_c, rainy=rainy)
        weather = weather_from_temperature(temp_c, rainy)

        print(f"\nWeather category: {weather}")
        print("Recommended perfumes:")
        for idx, perfume in enumerate(picks, start=1):
            print(f"{idx}. {perfume.name}")
            print(f"   Notes : {perfume.notes}")
            print(f"   Why   : {perfume.reason}")
    except ValueError as exc:
        print(f"Input error: {exc}")


if __name__ == "__main__":
    run_cli()
