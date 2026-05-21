"""Small Python helpers exposed as Robot keywords."""

from datetime import datetime

from robot.api.deco import keyword


@keyword("Get Run Timestamp")
def get_run_timestamp() -> str:
    """Return current time for logs and reports."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
