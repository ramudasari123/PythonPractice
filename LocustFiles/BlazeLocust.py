import re
from locust import HttpLocust, TaskSet, task


class BrowseDocumentation(TaskSet):
    HOME_PAGE_TITLE_REGEX = re.compile(".*Welcome to the Simple Travel Agency!.*")

    @task(1)
    def index_page_with_regex_assertion(self):
        r = self.client.get("/")
        assert self.HOME_PAGE_TITLE_REGEX.search(r.text) is not None, \
            "Expected title has not been found!" \

    @task(2)
    def SearchFlight(self):
        r = self.client.post('/reserve.php',{'fromPort':'Paris','toPort':'Berlin'})
        headers = {'Referer': 'http://blazedemo.com/'}

    @task(3)
    def PurchaseFlight(self):
        r= self.client.post('/purchase.php',{'flight':234,'price':432.98,'airline':'United Airlines','fromPort':'Paris',"":'Berlin'})
        headers={'Referer': 'http://blazedemo.com/'}

class AwesomeUser(HttpLocust):
    task_set = BrowseDocumentation
    host = "http://blazedemo.com"
    min_wait = 1 * 1000
    max_wait = 2 * 1000