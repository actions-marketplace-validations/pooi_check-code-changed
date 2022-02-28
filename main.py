#!/usr/bin/env python3

import sys

import requests


def get_pull_request_files():
    api_headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': f"token {github_token}"
    }

    response = requests.get(
        f"{pull_request_url}/files?per_page=100",
        headers=api_headers
    )

    if response.ok:
        return [file['filename'] for file in response.json()]
    else:
        print(f"GET-PULL-REQUEST-FILED-ERROR, code={response.status_code}, body={response.json()}")
        return []


def main():
    changed_files = get_pull_request_files()
    for changed_file in changed_files:
        if changed_file.startswith(target_path):
            print("::set-output name=changed::true")
            return
    print("::set-output name=changed::false")


if __name__ == '__main__':
    assert len(sys.argv) > 3

    github_token = sys.argv[1]
    pull_request_url = sys.argv[2]
    target_path = sys.argv[3]

    main()
