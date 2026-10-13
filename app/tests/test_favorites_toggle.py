"""Regression tests for the favorites HTMX toggle contract.

The favorite button is rendered inside ``partials/result_card.html`` by the
``/converter/convert`` endpoint. It carries its payload in an ``hx-vals``
attribute that htmx turns into the POST body for ``/favorites/toggle``.

If the convert endpoint forgets to pass ``category``/``from_unit``/``to_unit``
into the template context, Jinja renders them as empty strings, htmx sends no
usable fields, and FastAPI's required ``Form(...)`` validation answers 422.

These tests exercise the real UI contract instead of posting a hand-written
body, so the regression cannot silently come back.
"""
from __future__ import annotations

import json
import re

RESULT_BUTTON_RE = re.compile(r"hx-vals='([^']*)'")


def _favorite_button_hx_vals(html: str) -> dict[str, str]:
    """Extract the parsed hx-vals payload from the rendered favorite button."""
    match = RESULT_BUTTON_RE.search(html)
    assert match is not None, "favorite button hx-vals not found in result card"
    return json.loads(match.group(1))


def _convert(client, **overrides):
    data = {
        "category": "length",
        "value": "12",
        "from_unit": "meter",
        "to_unit": "foot",
        "precision": "4",
    }
    data.update(overrides)
    return client.post("/converter/convert", data=data)


def test_result_card_favorite_button_carries_real_values(client):
    """The button must advertise the actual pair, not empty strings."""
    r = _convert(client)
    assert r.status_code == 200

    vals = _favorite_button_hx_vals(r.text)
    assert vals == {
        "category": "length",
        "from_unit": "meter",
        "to_unit": "foot",
    }


def test_favorites_toggle_using_rendered_hx_vals(client):
    """Replay exactly what the browser would POST from that button."""
    r = _convert(client)
    assert r.status_code == 200
    vals = _favorite_button_hx_vals(r.text)

    toggle = client.post("/favorites/toggle", data=vals)
    assert toggle.status_code == 200
    assert "Favorited" in toggle.text

    # The response is a standalone button partial, ready for hx-swap="outerHTML".
    assert "hx-post=\"/favorites/toggle\"" in toggle.text
    assert "<html" not in toggle.text

    # Toggling again removes it (FavoriteService.toggle is a flip).
    untoggle = client.post("/favorites/toggle", data=vals)
    assert untoggle.status_code == 200
    assert "Add to favorites" in untoggle.text
