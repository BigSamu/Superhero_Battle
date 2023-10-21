<a name="back-to-top"></a>

# SuperhereoAPI Simulation

<!-- *********************************************************************** -->
<!-- I) ABOUT THE PROJECT -->
<!-- *********************************************************************** -->

## About The Project

A simple program that simulates a series of fights between superheroes and villains 💥🦸‍♂️🆚🦹‍♀️💥. The script connects to the Superhero API and forms two teams, each consisting of five members. It then simulates the fights round by round and provides the final results. All the fight status information is displayed in the console, and a summary can be sent by email 📧 if an address is provided.

Get ready for an epic battle! 🥊🔥 Brace yourself as superheroes clash with villains in an ultimate showdown! 💪💥 May the best team emerge victorious! 🏆✨

---

<!-- *********************************************************************** -->
<!-- II) TECHNOLOGIES -->
<!-- *********************************************************************** -->

## Technologies

The following technologies are used for the implementation of this project:

![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![PyPI Badge](https://img.shields.io/badge/PyPI-3775A9?logo=pypi&logoColor=fff&style=for-the-badge)
![Mailgun Badge](https://img.shields.io/badge/Mailgun-F06B66?logo=mailgun&logoColor=fff&style=for-the-badge)

<p align="right">(<a href="#back-to-top">back to top</a>)</p>

---

<!-- *********************************************************************** -->
<!-- III) GETTING STARTED -->
<!-- *********************************************************************** -->

## Getting Started

<!-- ----------------------------------------------------------------------- -->
<!-- 3.1) Prerequisites -->
<!-- ----------------------------------------------------------------------- -->

### Prerequisites

`Python3` and a `pip3` are required for the setup of this simulation.

For easy management of packages and environments `pipenv` is used. For installing this tool globally run:

```sh
pip3 install pipenv
```

> **NOTE:** At the time of the implementation of this project, `Python v3.10.11`, `pip v23.0` and `pipenv v2023.2.4` were used.

<!-- 3.2) Installation -->
<!-- ----------------------------------------------------------------------- -->

### Installation

To get a copy of this project and run it in your local environment, follow the steps listed below.

1. Clone the repo
   ```sh
   git clone git@github.com:BigSamu/SuperhereoAPI_Simulation.git
   ```
2. Go into the repository
   ```sh
   cd SuperhereoAPI_Simulation
   ```
3. Install required pyhon packages or dependencies
   ```sh
   pipenv install
   ```
4. Create a .env file and add the following related API Keys and Domains

   ```sh
   SUPERHERO_API_KEY=[YOUR_SUPERHERO_API_KEY]
   MAILGUN_API_KEY=[YOUR_MAILGUN_API_KEY]
   MAILGUN_DOMAIN_NAME=[YOUR_MAILGUN_DOMAIN_NAME]
   ```
5. Activate virtual environemnt
   ```sh
   pipenv shell
   ```

6. Run application
   ```sh
   python -m app.main [-email <email address>]
   ```

<p align="right">(<a href="#back-to-top">back to top</a>)</p>

<!-- ----------------------------------------------------------------------- -->
<!-- 3.3) Usage -->
<!-- ----------------------------------------------------------------------- -->

### Usage

After successful installation and execution, you will be able to experience the simulation in your terminal. If an email address is provided, you will receive the results of the simulation in your email.

> **NOTE:** The email address provided has to be registered in your domain in Mailgun API, so the script can send the results of the simulation that particular email.

<p align="right">(<a href="#back-to-top">back to top</a>)</p>

---

<!-- *********************************************************************** -->
<!-- VIII) FOOTER -->
<!-- *********************************************************************** -->

<p align="center">
Developed with ❤️ in Chile 🇨🇱
</p>
