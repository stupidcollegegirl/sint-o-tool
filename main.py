import asyncio
from core.orchestrator import detect_type, get_scan_function
from utils.formatter import print_result, calculate_risk

async def main():
    target = input("Enter target: ")

    target_type = detect_type(target)
    print(f"[+] Detected type: {target_type}")

    scan_func = get_scan_function(target_type)

    result = await scan_func(target)

    print_result(result)

    score = calculate_risk(result)
    print(f"\n[!] Risk score: {score}")


if __name__ == "__main__":
    asyncio.run(main())
