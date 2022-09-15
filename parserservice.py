from bs4 import BeautifulSoup


class ParserService:

    def get_containers(self, html):
        soup = BeautifulSoup(html, 'html.parser')

        if not soup.find('table', id='tracing_by_booking_f:hl27'):
            return []

        containers_line = soup.find('table', id='tracing_by_booking_f:hl27').find('tbody').find_all('tr')
        containers = []
        for container_line in containers_line:
            container_data = container_line.findAll('td')

            if not(len(container_data) >= 2):
                continue

            containers.append(container_data[2].text)

        return containers
