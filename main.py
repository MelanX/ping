import csv
import json
import os
import time

from pythonping import ping
from datetime import datetime

RETRY_TIMER = 10
MAIN_TEST_URL = 'versatel.de'


def done():
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write("\n")


def log(text):
    with open('log.txt', 'a', encoding='utf-8') as f:
        logging_text = f"{datetime.now()}: {text}"
        f.write(logging_text + "\n")
        print(logging_text)


def write_stats(now: datetime, success: bool):
    if not os.path.exists('stats.json'):
        with open('stats.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps({
                "total_failed": 0,
                "total_success": 0,
                "total_tests": 0,
                "last_failed": None,
                "all_failed_times": []
            }))

    with open('stats.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        data["total_tests"] = data["total_tests"] + 1
        if success:
            data["total_success"] = data["total_success"] + 1
        else:
            data["total_failed"] = data["total_failed"] + 1
            data["last_failed"] = str(now)
            data["all_failed_times"].append(str(now))

    with open('stats.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))


def test_dns_servers():
    ips = [
        '8.8.8.8', '8.8.4.4',  # Google Public DNS
        '208.67.222.222', '208.67.220.220',  # Cisco OpenDNS
        '1.1.1.1', '1.0.0.1',  # Cloudflare
        '9.9.9.9', '149.112.112.112'  # Quad9
    ]
    for ip in ips:
        add_resp = ping(ip)
        if not os.path.exists('fails.csv'):
            with open('fails.csv', 'w', encoding='utf-8') as f:
                f.write('time,ip,failed\n')

        with open('fails.csv', 'a+', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([datetime.now(), ip, not add_resp.success()])
            if add_resp.success():
                log('Internet is working, something else messed up')
                return True

    return False


def test_ping(domain):
    log(f"Pinging {domain}")
    now = datetime.now()
    response = ping(domain, verbose=True)
    log(f"Average reply time: {f'%.2f' % (response.rtt_avg * 1000)}ms")
    log(f"{response.stats_packets_returned}/{response.stats_packets_sent} packets returned")
    success = response.success()
    if success:
        log("Internet is working")
    else:
        log("Internet is missing, logging to extra file")
        success = test_dns_servers()

    write_stats(now, success)
    done()


def main():
    while True:
        if ping('fritz.box').success():
            break

        log(f'No connection to router, try again in {RETRY_TIMER} seconds.')
        time.sleep(RETRY_TIMER)

    test_ping(MAIN_TEST_URL)


if __name__ == '__main__':
    main()
