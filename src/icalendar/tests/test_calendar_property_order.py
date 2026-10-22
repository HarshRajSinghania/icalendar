"""Tests for Calendar property sorting order."""

from icalendar import Calendar


def test_calendar_property_order_with_url_and_xwr():
    """URL and standard properties should appear before X-WR- properties in sorted output."""
    cal = Calendar()
    cal.add("X-WR-CALNAME", "Test")
    cal.add("X-WR-TIMEZONE", "America/New_York")
    cal.add("URL", "https://example.com")
    cal.add("NAME", "Test Calendar")

    ical = cal.to_ical().decode()
    lines = [line for line in ical.splitlines() if line and not line.startswith(("BEGIN", "END"))]

    # Extract property names in order
    prop_names = [line.split(":")[0] for line in lines]

    # URL should come before X-WR-TIMEZONE
    assert prop_names.index("URL") < prop_names.index("X-WR-TIMEZONE")
    # NAME should come before X-WR-CALNAME
    assert prop_names.index("NAME") < prop_names.index("X-WR-CALNAME")
    # Standard properties before remaining X-WR
    assert "URL" in prop_names
    assert "X-WR-TIMEZONE" in prop_names
