# ResBaz24Python

![ResBazLogo](https://resbaz.auckland.ac.nz/img/resbaz_logos/ResBaz_transparent_cropped.png)

> [!NOTE] 
> this is the REAMDE that is **exclusive** to the `dev` branch!

In a nutshell: 
- participants use `StartHere_ResBaz24Python.ipynb` in `main`
- presenters see answers in `All_Answers_ResBaz24Python.ipynb`
- presenters can see the results of feedback in `plot_answers.ipynb`

Letting participants know to push the Colab button ![Colab](https://colab.research.google.com/assets/colab-badge.svg) is of high importance.

## Overview of Core components
> [!IMPORTANT]
> make sure you read the details below

- Component A: the filled-out notebook to be used in the workshop (`All_Answers_ResBaz24Python.ipynb`)
- Component B: the feedback functionality
  - you can run the `plot_answers.ipynb` ipynb and in the session
- Component C: the *run sheet*
- Component D: server setup


## Component A: the filled-out notebook to be used in the workshop

- The filled-out notebook is `All_Answers_ResBaz24Python.ipynb`
- This notebook is for the presenter to use during the workshop
- most content that isn't vital is stripped from this notebook; some headlines, etc. are left in there to make it easier to navigate in the live coding session

## Component B: the feedback functionality


- the `plot_answers.ipynb` file is used to plot the feedback from the participants
- to gather this feedback in a *Pythonian* way asks you to run this Jupyter notebook in either another Google Colab session (this might be challenging if Google cuts down the number of concurrent sessions) or on your local machine (e.g. in VSC) and by pushing the relevant cell's play button repeatedly, the latest answers can be pulled

> [!IMPORTANT]
> make sure that you adjust the data in that notebook, so we can keep track of the feedback across multiple runs1

## Component C: the *run sheet*

Part 1 - Introduction
- presenter A (estimation was 30min, first run took 45min)
  - From:  Introduction
  - To end of: variables and data types
  - BREAK ☕️ 3min or so
- presenter B (estimation was 30min, first run took 45min)
  - From: More complex data types
  - To end of: Functions

BREAK ☕️ 5-10min

Part 2 - Math Problem - Option A
- presenter A (estimation was)
  - all of: A1
  - BREAK ☕️ 3min or so
- presenter B 
  - all of: A2
- only if time: A3

BREAK ☕️ 5-10min

Part 3 - Waiter and Tips - Option B
- presenter A (estimation was 30min, first run took 35min)
  - all of: B1 up to including B3
- presenter B 
  - all of B4 (estimation was 30min, first run took 30min)

## Component D: server setup

- currently, there is a Nectar VM running FastAPI (as configured in the `API.py`) file
- the steps to set this up are detailed in the table below
- longer-term we might want to move this to a more robust solution, e.g. a Docker container

| Command                                                                 | Description                                                                  |
|-------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `git clone https://github.com/UoA-eResearch/ResBaz24Python.git`         | clone the repo to the VM                                                     |
| `cd ResBaz24Python/`                                                    | go in that directory                                                         |
| `git checkout 'dev'`                                                    | make sure we are on the right branch (not main which is mainly for participants) |
| `cat API.py`                                                            | see the content of the API script on the commandline                         |
| `vim .ssh/authorized_keys`                                              | add other people's ssh keys if needed                                        |
| `sudo apt update`                                                       | get latest update                                                            |
| `sudo apt install python3-pip`                                          | install pip                                                                  |
| `sudo apt install python-is-python3`                                     | install workaround not having to type python3 all the time (Ubuntu exclusive) |
| `sudo pip install pandas --break-system-packages`                       | install packages required to run this 'backend'                              |
| `sudo pip install fastapi --break-system-packages`                      | install packages required to run this 'backend'                              |
| `pip install ipykernel --break-system-packages`                         | install packages required to run this 'backend'                              |
| `pip install nbdime --break-system-packages`                            | install packages required to run this 'backend'                              |
| `sudo fastapi dev API.py --host 0.0.0.0 --port 80`                      | run the fastapi server                                                       |
| `crontab -e`                                                            | add this line "@reboot cd ResBaz24Python && sudo fastapi run API.py --port 80 &> fastapi.log" |
| `cp answers.csv answers.csv.bak`                                        | backup answers                                                               |
