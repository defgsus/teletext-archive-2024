import re
import urllib.parse
from typing import Generator, Tuple, Union, Any

import bs4

from ..scraper import Scraper
from ..teletext import Teletext, TeletextPage
from src.teletext.unico import G0_TO_UNICODE_MAPPING

CUSTOM_G0_MAPPING = G0_TO_UNICODE_MAPPING.copy()
CUSTOM_G0_MAPPING.update({
    0xdf: ord("ß"),
    0xd6: ord("Ö"),
    0xf6: ord("ö"),
    0xdc: ord("Ü"),
    0xfc: ord("ü"),
    0xc4: ord("Ä"),
    0xe4: ord("ä"),
    0xb0: ord("°"),
    0xa7: ord("§"),
})

from .zdf import ZDFBase


class DreiSAT(ZDFBase):
    ABSTRACT = False
    NAME = "3sat"
    ZDF_MANDANT = "3sat"

    PAGE_CATEGORIES = {
        100: "index",
        111: "news",
        160: "stocks",
        180: "undefined",
        200: "sport",
        280: "lotto",
        300: "program",
        400: "index",
        401: "weather",
        450: "traffic",
        500: "culture",
        600: "index",
        601: "internal",
    }
