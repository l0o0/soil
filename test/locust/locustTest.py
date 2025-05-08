from locust import FastHttpUser, task, between
from urllib.parse import quote
import random

class JournalUser(FastHttpUser):
    wait_time = between(1, 3)
    journal_names = ["园艺学报", "植物学报", "农业工程学报"]

    @task
    def get_journal(self):
        name = quote(random.choice(self.journal_names))
        response = self.client.get(
            f"/journals/{name}",
            headers={"pluginID": "thisisatest@zotero.org", "accept": "application/json"}
        )
        if response.status_code != 200:
            print(f"请求失败: {response.status_code}, {response.text}")

    def on_start(self):
        print("压力测试开始！")