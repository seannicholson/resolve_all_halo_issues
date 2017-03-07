#! /usr/local/bin/python

# Author: Sean Nicholson
# Script for resolving all Halo issues. This script is intended to clear out
# data related to Halo testing and issues created from a PoC


import json, io, requests
import cloudpassage
import yaml



def create_api_session(session):
    config_file_loc = "cloudpassage.yml"
    config_info = cloudpassage.ApiKeyManager(config_file=config_file_loc)
    session = cloudpassage.HaloSession(config_info.key_id, config_info.secret_key)
    return session


def resolve_issues(session):
    issues= cloudpassage.HttpHelper(session)
    list_of_issues_json = issues.get("/v2/issues")
    body = {"status": "resolved",}
    #loop list of issues and resolve them
    list_of_issues = list_of_issues_json['issues']
    for issue in list_of_issues:
        issueID = issue['id']
        issue_to_resolve = cloudpassage.HttpHelper(session)
        list_of_issues_json = issue_to_resolve.get("/v2/issues")
        reply = issue_to_resolve.put("/v2/issues/" + issueID, body)





def main():
    api_session = None
    api_session = create_api_session(api_session)
    resolve_issues(api_session)

if __name__ == "__main__":
        main()
