import os
import socket
import re
import argparse
import SocketServer
import subprocess
import time
import sys


def commit_observe():
    parser = argparse.ArgumentParser()
    parser.add_argument("--forwarder-server",
                    help="forwarder ussage host:port, " \
                    "default is: localhost:8878",
                    default="localhost:8878",
                    action="store"
                    )
    parser.add_argument("repo", metavar="REPO", type=str,
                    help="path to the repo this will monitor")
    args = parser.parse_args()
    forwarder_host, forwaeder_post = args.forwarder_server.split(":")

    while True:
        try:
            subprocess.check_output(["./update_repo.sh", args.repo])
        except subprocess.CalledProcessError as e:
            raise Exception("not able to update and check the repo. " + \
                         "Reason: %s" % e.output)
