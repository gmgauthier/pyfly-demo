import os
from subprocess import Popen, PIPE
import requests
from hoverpy import capture


class TestUsingHoverpy:

    def setup_class(self):
        # startup the simple server (only needed for this example)
        Popen("sh pipenv run python app/simple.py", shell=True, stdout=PIPE, stderr=PIPE)

    def teardown_class(self):
        # deletes the captured session
        os.remove("tests/test_version_call.db")

    @capture("tests/test_version_call.db", recordMode="once")
    def test_version_call(self):
        resp = requests.get("http://127.0.0.1:5000/version")
        assert resp.json()['version'] == 0.1

    # FROM THE DEMO:
    # @capture("tests/test_time2.db", recordMode="once")
    # def test_time3(self):
    #     time = requests.get("http://time.jsontest.com")
    #     assert list(time.json().keys()).index('time') > 0
