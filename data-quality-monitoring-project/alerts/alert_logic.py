def trigger_alert(alert_type: str, details):
    """
    Simple alert simulation.
    In production, this could send Slack, email, PagerDuty, etc.
    """
    print("=" * 60)
    print(f"[ALERT] {alert_type}")
    print("Details:")
    print(details)
    print("=" * 60)