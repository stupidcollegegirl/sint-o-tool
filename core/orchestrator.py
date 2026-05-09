import validators
import re

def detect_type(target: str) -> str:
   
    target = target.strip()
    
    
    clean = ''.join(filter(str.isdigit, target))
    if len(clean) >= 10 and len(clean) <= 15:
        return "phone"
    
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", target) or ":" in target:
        return "ip"
    
 
    if validators.email(target):
        return "email"
    

    if validators.domain(target) or "." in target and not target[0].isdigit():
        return "domain"
    
    return "username"


def get_scan_function(target_type: str):
    
    if target_type == "ip":
        from core.scanner import run_ip_scan
        return run_ip_scan
    elif target_type == "email":
        from core.scanner import run_email_scan
        return run_email_scan
    elif target_type == "domain":
        from core.scanner import run_domain_scan
        return run_domain_scan
    elif target_type == "phone":
        from core.scanner import run_phone_scan
        return run_phone_scan
    else:  # username
        from core.scanner import run_username_scan
        return run_username_scan
