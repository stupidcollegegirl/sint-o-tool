import validators


def detect_type(target: str) -> str:
    if validators.email(target):
        return "email"
    elif validators.domain(target):
        return "domain"
    else:
        return "username"


def get_scan_function(target_type: str):
    if target_type == "email":
        from core.scanner import run_email_scan
        return run_email_scan
    elif target_type == "domain":
        from core.scanner import run_domain_scan
        return run_domain_scan
    else:
        from core.scanner import run_username_scan
        return run_username_scan
