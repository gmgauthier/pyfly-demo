import json
from app import simple


class TestSimple:

    def setup(self):
        self.app = simple.app.test_client()

    def teardown(self):
        pass

    def test_version(self):
        resp = self.app.get('/version')
        rjson = json.loads(resp.data)
        assert rjson['version'] == 0.1

    def test_random_numbers(self):
        resp = self.app.get('/randoms')
        rjson = json.loads(resp.data)
        assert rjson['number'] <= 80

    def test_random_string(self):
        resp = self.app.get('/randoms')
        rjson = json.loads(resp.data)
        assert len(rjson['string']) <= 80
