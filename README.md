<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This repository contains a collection of scrapers designed to extract open source dependencies from various websites and platforms. The goal of the project is to provide a tool for analyzing the dependencies of different software projects, helping developers and researchers gain insights into the usage of open source libraries and frameworks.

The scrapers are developed using a combination of web scraping techniques and data extraction methods. They are capable of extracting information such as package names, versions from websites and platforms commonly used for software development.

By utilizing these scrapers, users can retrieve valuable data about the dependencies of specific companies, packages, or projects. This information can be used for various purposes, including identifying common dependencies among companies, tracking the usage of specific packages across different projects, and exploring the relationships between different open source libraries.

We have the following Scrapers:

1. Slack
2. Spotify
3. Cisco
4. Samsung
5. Porsche
6. Discord
7. Broadcom
8. Confluent
9. Adlock
10. Apple Maps
11. Bocada
12. Bosch
13. Genesis
14. Veertu
15. Smartsheet
16. Spark
17. Camunda
18. Oracle Fusion Platform
19. Box
20. Parasoft Enterprise
21. Clue.io
22. Cognition
23. Nvidia
24. Shoott

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.com]][Python-url]
* [![Beautiful Soup][Beautifulsoup.com]][Beautifulsoup-url]
* [![Flask][Flask.com]][Flask-url]
* [![Docker][Docker.com]][Docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Before running the project, make sure you have the following prerequisites installed:

* [Python 3](https://www.python.org/doc/): You should have Python 3 installed in order to run the project.
* [Docker](https://www.docker.com/): Docker is required to run the project. You can download and install Docker from the official website.

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/FOSSRIT/FOCUSED-Web-Scraper.git
   ```

2. Run docker compose

   ```sh
    cd FOCUSED-Web-Scraper
    docker-compose build
    docker-compose up
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

There are 4 GET API calls to get the data

    To get all the dependencies

  ```sh
   http://127.0.0.1:4000/dependencies  
  ```

     To get all the dependencies of a company along with shared authors of a dependency

  ```sh
   http://127.0.0.1:4000/dependencies/company/<CompanyName>
   # example
   http://127.0.0.1:4000/dependencies/company/slack 
  ```

     To get the list of companies which share that particular dependency

  ```sh
   http://127.0.0.1:4000/dependencies/<Company>/<Package>
   # example
   http://127.0.0.1:4000/dependencies/slack/buffer
  ```

    To get the list of companies which share that particular dependency

  ```sh
   http://127.0.0.1:4000/dependencies/package/<Package>
   # example
   http://127.0.0.1:4000/dependencies/package/react
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

If you have any questions, suggestions, or encounter any issues while using the scrapers, please don't hesitate to contact us.

Team at Open@RIT

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python.com]: https://img.shields.io/badge/Python-0769AD?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/doc/
[Beautifulsoup.com]: https://img.shields.io/badge/BeautifulSoup-DD0031?style=for-the-badge&logo=beautifulsoup&logoColor=white
[Beautifulsoup-url]: https://pypi.org/project/beautifulsoup4/
[Flask.com]: https://img.shields.io/badge/Flask-4E4A56?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.3.x/
[Docker.com]: https://img.shields.io/badge/Docker-4F4B55?style=for-the-badge&logo=docker&logoColor=FF3E00
[Docker-url]: https://www.docker.com/
