# Idea Eater

<img src="src/idea_eater/resources/idea_eater.png" width="100">

This application (supported primarily on MacOS) is designed to eat ideas so that you can get them out of your head when they might otherwise distract you.

If you've been puttering along, doing your work, and had a sudden idea about something unrelated - a task you need to do, a cool idea for a short story, the name of a song you've been trying to remember - you can feed it to the Idea Eating Monster, who will happily put it in a file called `ideas.txt` in your home directory for you.

At the end of your working period you can go and get all the ideas back out of the file and do whatever you want with them.

---

## How to build Idea Eater

Idea Eater requires **Python 3** and [Briefcase](https://github.com/beeware/briefcase).

If you want to build for platforms other than MacOS, please consult the [Briefcase docs](https://briefcase.readthedocs.io/en/latest/).

You can get started on MacOS by following these steps:

1) Clone this repo: `git clone git@github.com:attacus/idea-eater.git`
2) Create a Python virtual environment: `python3 -m venv beeware-venv`
3) Activate the virtual environment: `. beeware-venv/bin/activate`
4) Enter the project directory: `cd idea-eater/`
5) Install Briefcase in the virtual environment: `python -m pip install briefcase`
6) (If you want to do development work, you can run your project in a dev environment: `briefcase dev -d`)
7) Build the app: `briefcase build`
8) The standalone `Idea Eater.app` can now be found in `./macOS/app/Idea Eater/`
9) Om nom nom

---

## Notes for mouseless use

If you want to add notes without needing to use a mouse or trackpad to click the "Nom" button, there are two options:

1) In your Mac's settings, go to `Keyboard > Shortcuts` and check `Use keyboard navigation to move focus between controls`. This will allow you to enter an idea, press `Tab` to highlight the "Nom" button, then press `Space` to submit the idea
2) Help the [Toga](https://github.com/beeware/toga) project (which powers the Idea Eater GUI) by adding the feature that captures the Enter key in the input box. You can read about the issue at: [https://github.com/beeware/toga/issues/213](https://github.com/beeware/toga/issues/213)

---

## Optimistic future feature ideas (pull requests welcome)

- the ability to configure the destination file for ideas in the GUI
- enter-to-submit new ideas (see "Notes for mouseless use #2" above)
- make the UI prettier
- `.ico` files for the icons for Windows (about the only thing that means this isn't totally supported for Windows)

---

## About the developers

This app was developed by [Matt Cengia](https://blog.mattcen.com/about/) and [Lilly Ryan](https://twitter.com/attacus_au) and is in a vague alpha state. Please feel free to suggest improvements if you have them!

The Idea Eater would not exist without the work of [Russell Keith-Magee](https://twitter.com/freakboy3742) and the fine apiarists of [The BeeWare Project](https://beeware.org/) who gave us [Toga](https://github.com/beeware/toga) (a Python native, OS native GUI toolkit), and [Briefcase](https://github.com/beeware/briefcase) (a tool for converting Python projects into standalone native applications). If you want to see more tools like these, please
consider [becoming a financial member of BeeWare](https://beeware.org/contributing/membership).
