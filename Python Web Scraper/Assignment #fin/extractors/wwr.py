from bs4 import BeautifulSoup
import requests


def extract_wwr_jobs(term):
  url = f"https://weworkremotely.com/remote-jobs/search?term={term}"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  results = []

  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all('section', class_='jobs')
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:
        anchor = post.find_all('a')[1]
        link = anchor['href']
        company, kind, location = post.find_all('span', class_='company')
        position = post.find('span', class_='title')
        job_data = {
            'link': f"https://remoteok.com{link}",
            'position': position.string,
            'company': company.string,
            'location': location.string
        }
        results.append(job_data)
  else:
    print("Can't get jobs.")

  return results
