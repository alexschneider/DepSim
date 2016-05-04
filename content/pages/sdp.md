Title: Software Development Plan
Date: 2016-3-7
Authors: Alex Schneider
Summary: Define software development plan

#4 Software Development Plan
##4.1 Plan Introduction
The project involves a model and simulator for a deployment to many (on the order of millions) of machines. Rolling out involves deployment to an increasingly larger subset of machines, with pauses between stages to see if errors occur, and if not, building confidence in the release before going forward or rolling back. The project will accurately describe constraints and estimate total rollout time based on certain variables such as the rollout time per domain, delay times, number of domains, and number of regions.

The development of the software takes place in three main stages, developing the model, the simulation, and the graphical interface. The milestones are as follows:

1. Get all the moving parts working together, SimPy, Bokkeh or D3, PyWebkit, etc. Use sample data for this. 2nd week
2. Develop a simplistic model and simulation that doesn't take into account additional constraints. Figure out visualization. 4th week
3. Develop more complex models and simulations that allow constraints. 8th week
4. Provide a graphical tool for designing models for simulation. 10th week
5. Automatically optimize the model. Time left

###4.1.1 Project Deliverables
* Proposal
* Requirements
* Software Development Plan
* Demonstration Presentations
* Packaged Software System

##4.2 Project resources
The application is fairly simple without many requirements needed to utilize it.

###4.2.1 Hardware resources
Since the application is locally hosted, only a single computer capable of running a modern x86 or x86_64 operating system is required. An example of one might be an Intel Core i3, 4 GB of memory, 1 GB of hard drive space, and some GPU capable of outputting a normal window to the screen (integrated GPUs work excellently).

###4.2.2 Software resources
The application comes packaged with all libraries required to run it. The computer need only have software capable of launching executables in a directory. A file manager such as Thunar or a terminal such as xterm will do.

It is expected that the operating system is fully updated (Linux 4.4, Mac OSX 10.11, or Windows 10). Other versions or systems may work, but no guarantees are provided.

For developing, Python 3.5.1 is used with the NeoVim editor. The following plugins are used in varying capacities during development:

* Vim sensible
* Vim slueth
* Vim fugitive
* Vim surround
* Vim speeddating
* Vim Repeat
* NERDTree
* Deoplete (and deoplete-jedi for Python code completion)
* Unite.Vim
* Vim airline
* Tagbar
* Syntastic
* Vim gitgutter

In addition, the PyPI is used to fetch libraries, so the development machine must have PIP installed. Virtualenv is recommended (though not required) to manage differing versions of dependencies.

##4.3

The major functions are the simulation backend and the display frontend. These can be developed more or less separately, as connecting the two should be trivial.

The graphical frontend is a lower priority for the project's success, since it is more important for it to function properly than to look good.

The priority should be focused on ensuring the model definition is easy to read and write, and the simulation is performed in an adequate manner. The majority of development time is likely going to be spent on doing so.

The frontend, on the other hand, if it were a group project could be developed by a separate team independently of the backend. A minimum viable product for the frontend can likely be developed in two weeks or so, with additional time to make it nicer. 

##4.4.1 GANTT/PERT Chart

###[GANTT]({filename}/images/gantt.png) 
(This is too wide to embed)

###Pert
![PERT]({filename}/images/pert.png)
