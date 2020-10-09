import os
from subprocess import Popen, PIPE
import requests
from hoverpy import capture


class TestUsingHoverpy:

    root_url = "http://127.0.0.1:5000"

    def setup_class(self):
        # startup the simple server (only needed for this example)
        # This will get destroyed automatically, when the tests end
        Popen("sh pipenv run python app/simple.py", shell=True, stdout=PIPE, stderr=PIPE)

    def teardown_class(self):
        # deletes the captured sessions
        os.remove("tests/test_version_call.db")
        os.remove("tests/test_random_numbers.db")
        os.remove("tests/test_random_string.db")
        os.remove("tests/test_hashname.db")

    @capture("tests/test_version_call.db", recordMode="once")
    def test_version_call(self):
        resp = requests.get(self.root_url + "/version")
        assert resp.json()['version'] == 0.1

    @capture("tests/test_random_numbers.db", recordMode="once")
    def test_random_numbers(self):
        resp = requests.get(self.root_url + "/randoms")
        assert resp.json()['number'] <= 80

    @capture("tests/test_random_string.db", recordMode="once")
    def test_random_string(self):
        resp = requests.get(self.root_url + "/randoms")
        assert len(resp.json()['string']) <= 80

    @capture("tests/test_hashname.db", recordMode="once")
    def test_hashname(self):
        req_body = {
            "name": "Frootloops Johnson"
        }
        resp = requests.post(self.root_url + "/hashname", json=req_body)
        assert resp.json()['name'] == "Frootloops Johnson"
