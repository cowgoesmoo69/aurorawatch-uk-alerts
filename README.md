# Acknowledgements
[<img src="assets/aw-logo_w_300.jpg">](https://aurorawatch.lancs.ac.uk)

This project uses data that is made available by the [Aurorawatch UK](https://aurorawatch.lancs.ac.uk) project based at [Lancaster University](https://www.lancs.ac.uk). Neither [the author](https://github.com/cowgoesmoo69), nor this project, are in any way associated with or endorsed by Aurorawatch UK.

The data from Aurorawatch UK is made available under CC BY-NC-SA 3.0 Attribution-NonCommercial-ShareAlike 3.0 Unported. Accordingly, this project is licensed under CC BY-NC-SA 4.0 Attribution-NonCommercial-ShareAlike 4.0 International. See [LICENSE](./LICENSE) for further details.

# aurorawatch-uk
Retrieves status information from Aurorawatch UK and sends an alert using [Pushover](https://pushover.net/) if all sites are reporting [red](https://aurorawatch.lancs.ac.uk/alerts/).

This project is intended to be run as a background systemd service in a Linux environment. The pre-requisites and installation instructions are provided on that basis.

# Pre-requisites
- A system running a Linux distribution that uses systemd, e.g. [Debian](https://www.debian.org/), and sudo access.
- [git](https://git-scm.com/). Install with `sudo apt install git`.
- [Python 3](https://www.python.org/). This project is currently developed using [Python 3.14.2](https://www.python.org/downloads/release/python-3142/). It will probably work ok with most earlier versions, but YMMV.
- Some Python libraries. Dependent upon which Linux distribution you're using some/all of these may already be present.
  - [Requests HTTP library](https://pypi.org/project/requests/). Dependent upon which Linux distribution you're using this can either be installed by running

    `python3 -m pip install requests` or

    `sudo apt install python3-requests` from the command line.
  - [lxml library](https://pypi.org/project/lxml/). Dependent upon which Linux distribution you're using this can either be installed by running

    `python3 -m pip install lxml` or

    `sudo apt install python3-lxml` from the command line.
- A [Pushover](https://pushover.net/) account.

# Installation
These instructions assume you are either logged in at a physical terminal, or connecting over SSH etc.

These instructions are written primarily with Debian in mind, but they will probably work without modification on most Linux systems.
1. Create a new, minimal user account for the project to run under, e.g. aurora:

    ```sudo adduser aurora --no-create-home --disabled-password```. Enter whatever you like for name etc. when prompted.
1. Clone the project repository:

    `git clone https://github.com/cowgoesmoo69/aurorawatch-uk-alerts.git`.
1. Change ownership of the directory and its contents:

    `sudo chown -R aurora: aurorawatch-uk-alerts`.
1. Update permissions of the directory and its contents:

    `sudo chmod -R 755 aurorawatch-uk-alerts`.
1. Move the directory into /opt:

    `sudo mv aurorawatch-uk-alerts /opt`.
1. Create a directory to hold an environment file:

    `sudo mkdir /etc/opt/aurorawatch-uk-alerts`.
1. [Log in](https://pushover.net/login) to your Pushover account.
1. [Create a new app](https://pushover.net/apps/build).
1. Fill in the name, description etc., agree to terms and click Create Application.
1. Copy the API token into a note-taking app.
1. Go back to your Pushover [account page](https://pushover.net/).