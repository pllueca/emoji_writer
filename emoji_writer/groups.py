""" Groups of emojis """

import os
from functools import cache

import emoji


@cache
def get_emoji_list_names(emoji_source: str) -> list:
    """get list of emoji name based on specified type"""
    if emoji_source not in emoji_groups:
        raise KeyError(f"Unsupported emoji group {emoji_source}")
    return emoji_groups[emoji_source]


@cache
def get_emoji_list_pairs() -> list[tuple[str, str]]:
    return [
        (name[1:-1], label)
        for name, label in emoji.get_emoji_unicode_dict("en").items()
    ]


@cache
def get_emoji_dict() -> dict[str, str]:
    return {
        name[1:-1]: label for name, label in emoji.get_emoji_unicode_dict("en").items()
    }


def is_emoji(s: str) -> bool:
    """return true if the passed string is an emoji. will return false if has
    more characters:
    '⏫' => True
    'x: ⏫' => False
    """
    return s in emoji.get_emoji_unicode_dict("en").values()


# emojis representing a flag
FLAGS = [
    "flag_for_Afghanistan",
    "flag_for_Albania",
    "flag_for_Algeria",
    "flag_for_American_Samoa",
    "flag_for_Andorra",
    "flag_for_Angola",
    "flag_for_Anguilla",
    "flag_for_Antarctica",
    "flag_for_Antigua_&_Barbuda",
    "flag_for_Argentina",
    "flag_for_Armenia",
    "flag_for_Aruba",
    "flag_for_Ascension_Island",
    "flag_for_Australia",
    "flag_for_Austria",
    "flag_for_Azerbaijan",
    "flag_for_Bahamas",
    "flag_for_Bahrain",
    "flag_for_Bangladesh",
    "flag_for_Barbados",
    "flag_for_Belarus",
    "flag_for_Belgium",
    "flag_for_Belize",
    "flag_for_Benin",
    "flag_for_Bermuda",
    "flag_for_Bhutan",
    "flag_for_Bolivia",
    "flag_for_Bosnia_&_Herzegovina",
    "flag_for_Botswana",
    "flag_for_Bouvet_Island",
    "flag_for_Brazil",
    "flag_for_British_Indian_Ocean_Territory",
    "flag_for_British_Virgin_Islands",
    "flag_for_Brunei",
    "flag_for_Bulgaria",
    "flag_for_Burkina_Faso",
    "flag_for_Burundi",
    "flag_for_Cambodia",
    "flag_for_Cameroon",
    "flag_for_Canada",
    "flag_for_Canary_Islands",
    "flag_for_Cape_Verde",
    "flag_for_Caribbean_Netherlands",
    "flag_for_Cayman_Islands",
    "flag_for_Central_African_Republic",
    "flag_for_Ceuta_&_Melilla",
    "flag_for_Chad",
    "flag_for_Chile",
    "flag_for_China",
    "flag_for_Christmas_Island",
    "flag_for_Clipperton_Island",
    "flag_for_Cocos__Islands",
    "flag_for_Colombia",
    "flag_for_Comoros",
    "flag_for_Congo____Brazzaville",
    "flag_for_Congo____Kinshasa",
    "flag_for_Cook_Islands",
    "flag_for_Costa_Rica",
    "flag_for_Croatia",
    "flag_for_Cuba",
    "flag_for_Curaçao",
    "flag_for_Cyprus",
    "flag_for_Czech_Republic",
    "flag_for_Côte_d’Ivoire",
    "flag_for_Denmark",
    "flag_for_Diego_Garcia",
    "flag_for_Djibouti",
    "flag_for_Dominica",
    "flag_for_Dominican_Republic",
    "flag_for_Ecuador",
    "flag_for_Egypt",
    "flag_for_El_Salvador",
    "flag_for_Equatorial_Guinea",
    "flag_for_Eritrea",
    "flag_for_Estonia",
    "flag_for_Ethiopia",
    "flag_for_European_Union",
    "flag_for_Falkland_Islands",
    "flag_for_Faroe_Islands",
    "flag_for_Fiji",
    "flag_for_Finland",
    "flag_for_France",
    "flag_for_French_Guiana",
    "flag_for_French_Polynesia",
    "flag_for_French_Southern_Territories",
    "flag_for_Gabon",
    "flag_for_Gambia",
    "flag_for_Georgia",
    "flag_for_Germany",
    "flag_for_Ghana",
    "flag_for_Gibraltar",
    "flag_for_Greece",
    "flag_for_Greenland",
    "flag_for_Grenada",
    "flag_for_Guadeloupe",
    "flag_for_Guam",
    "flag_for_Guatemala",
    "flag_for_Guernsey",
    "flag_for_Guinea",
    "flag_for_Guinea__Bissau",
    "flag_for_Guyana",
    "flag_for_Haiti",
    "flag_for_Heard_&_McDonald_Islands",
    "flag_for_Honduras",
    "flag_for_Hong_Kong",
    "flag_for_Hungary",
    "flag_for_Iceland",
    "flag_for_India",
    "flag_for_Indonesia",
    "flag_for_Iran",
    "flag_for_Iraq",
    "flag_for_Ireland",
    "flag_for_Isle_of_Man",
    "flag_for_Israel",
    "flag_for_Italy",
    "flag_for_Jamaica",
    "flag_for_Japan",
    "flag_for_Jersey",
    "flag_for_Jordan",
    "flag_for_Kazakhstan",
    "flag_for_Kenya",
    "flag_for_Kiribati",
    "flag_for_Kosovo",
    "flag_for_Kuwait",
    "flag_for_Kyrgyzstan",
    "flag_for_Laos",
    "flag_for_Latvia",
    "flag_for_Lebanon",
    "flag_for_Lesotho",
    "flag_for_Liberia",
    "flag_for_Libya",
    "flag_for_Liechtenstein",
    "flag_for_Lithuania",
    "flag_for_Luxembourg",
    "flag_for_Macau",
    "flag_for_Macedonia",
    "flag_for_Madagascar",
    "flag_for_Malawi",
    "flag_for_Malaysia",
    "flag_for_Maldives",
    "flag_for_Mali",
    "flag_for_Malta",
    "flag_for_Marshall_Islands",
    "flag_for_Martinique",
    "flag_for_Mauritania",
    "flag_for_Mauritius",
    "flag_for_Mayotte",
    "flag_for_Mexico",
    "flag_for_Micronesia",
    "flag_for_Moldova",
    "flag_for_Monaco",
    "flag_for_Mongolia",
    "flag_for_Montenegro",
    "flag_for_Montserrat",
    "flag_for_Morocco",
    "flag_for_Mozambique",
    "flag_for_Myanmar",
    "flag_for_Namibia",
    "flag_for_Nauru",
    "flag_for_Nepal",
    "flag_for_Netherlands",
    "flag_for_New_Caledonia",
    "flag_for_New_Zealand",
    "flag_for_Nicaragua",
    "flag_for_Niger",
    "flag_for_Nigeria",
    "flag_for_Niue",
    "flag_for_Norfolk_Island",
    "flag_for_North_Korea",
    "flag_for_Northern_Mariana_Islands",
    "flag_for_Norway",
    "flag_for_Oman",
    "flag_for_Pakistan",
    "flag_for_Palau",
    "flag_for_Palestinian_Territories",
    "flag_for_Panama",
    "flag_for_Papua_New_Guinea",
    "flag_for_Paraguay",
    "flag_for_Peru",
    "flag_for_Philippines",
    "flag_for_Pitcairn_Islands",
    "flag_for_Poland",
    "flag_for_Portugal",
    "flag_for_Puerto_Rico",
    "flag_for_Qatar",
    "flag_for_Romania",
    "flag_for_Russia",
    "flag_for_Rwanda",
    "flag_for_Réunion",
    "flag_for_Samoa",
    "flag_for_San_Marino",
    "flag_for_Saudi_Arabia",
    "flag_for_Senegal",
    "flag_for_Serbia",
    "flag_for_Seychelles",
    "flag_for_Sierra_Leone",
    "flag_for_Singapore",
    "flag_for_Sint_Maarten",
    "flag_for_Slovakia",
    "flag_for_Slovenia",
    "flag_for_Solomon_Islands",
    "flag_for_Somalia",
    "flag_for_South_Africa",
    "flag_for_South_Georgia_&_South_Sandwich_Islands",
    "flag_for_South_Korea",
    "flag_for_South_Sudan",
    "flag_for_Spain",
    "flag_for_Sri_Lanka",
    "flag_for_St._Barthélemy",
    "flag_for_St._Helena",
    "flag_for_St._Kitts_&_Nevis",
    "flag_for_St._Lucia",
    "flag_for_St._Martin",
    "flag_for_St._Pierre_&_Miquelon",
    "flag_for_St._Vincent_&_Grenadines",
    "flag_for_Sudan",
    "flag_for_Suriname",
    "flag_for_Svalbard_&_Jan_Mayen",
    "flag_for_Swaziland",
    "flag_for_Sweden",
    "flag_for_Switzerland",
    "flag_for_Syria",
    "flag_for_São_Tomé_&_Príncipe",
    "flag_for_Taiwan",
    "flag_for_Tajikistan",
    "flag_for_Tanzania",
    "flag_for_Thailand",
    "flag_for_Timor__Leste",
    "flag_for_Togo",
    "flag_for_Tokelau",
    "flag_for_Tonga",
    "flag_for_Trinidad_&_Tobago",
    "flag_for_Tristan_da_Cunha",
    "flag_for_Tunisia",
    "flag_for_Turkey",
    "flag_for_Turkmenistan",
    "flag_for_Turks_&_Caicos_Islands",
    "flag_for_Tuvalu",
    "flag_for_U.S._Outlying_Islands",
    "flag_for_U.S._Virgin_Islands",
    "flag_for_Uganda",
    "flag_for_Ukraine",
    "flag_for_United_Arab_Emirates",
    "flag_for_United_Kingdom",
    "flag_for_United_States",
    "flag_for_Uruguay",
    "flag_for_Uzbekistan",
    "flag_for_Vanuatu",
    "flag_for_Vatican_City",
    "flag_for_Venezuela",
    "flag_for_Vietnam",
    "flag_for_Wallis_&_Futuna",
    "flag_for_Western_Sahara",
    "flag_for_Yemen",
    "flag_for_Zambia",
    "flag_for_Zimbabwe",
    "flag_for_Åland_Islands",
]

FACES = []
all_emojis = list(emoji.get_emoji_unicode_dict("en").keys())

short_emojis = [k for k, v in emoji.get_emoji_unicode_dict("en").items() if len(v) == 1]


medium_emojis = [
    k for k, v in emoji.get_emoji_unicode_dict("en").items() if len(v) == 2
]

long_emojis = [k for k, v in emoji.get_emoji_unicode_dict("en").items() if len(v) >= 2]


SLACK_EMOJIS_FILENAME = "./slack_emoji_list.txt"

slack_emojis = []
if os.path.isfile(SLACK_EMOJIS_FILENAME):
    with open(SLACK_EMOJIS_FILENAME, "r") as f:
        slack_emojis = [f.read().splitlines()]

emoji_groups: dict[str, list[str]] = {
    "flags": FLAGS,
    "short": short_emojis,
    "medium": medium_emojis,
    "long": long_emojis,
    "all": all_emojis,
    "slack": slack_emojis,
}
