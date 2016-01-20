Title: Proposal
Date: 2016-1-18
Authors: Alex Schneider
Summary: Propose deployment simulator project.

#Title
##Project Name
DepSim

##Author
Alex Schneider

#Project Description
The project involves a model and simulator for a deployment to many (on the order of millions) of machines. Rolling out involves deployment to an increasingly larger subset of machines, with pauses between stages to see if errors occur, and if not, building confidence in the release before going forward or rolling back. The project will accurately describe constraints and estimate total rollout time based on certain variables such as the rollout time per domain, delay times, number of domains, and number of regions.

#Justification
The simulator can be used for modeling deployment at large scales to see if certain deployment strategies and models work. It would also work on optimizing the deployment model, sequence, and strategy to get the best possible deployment within the given constraints (e.g. risk).

In addition to the business implications of the project, this will help me learn about modeling, simulation, and distributed systems, something I don't have much experience in. The project will also help me learn skills useful to my career that I'm starting.

#User's point of view
The user point of view is to develop a model with constraints for the simulator to run. The simulator will then return the data and visualize it in an intuitive way for the user. Ideally, there will be a way to graphically design and develop a model, but that may not be possible within the timeframe the project must be developed within.

#Operations Description
The application will run entirely locally on a system and have no external network access or requests. The user will double click on the application, which will launch an interface that allows them to run the simulation. It will be entirely self contained using PyInstaller, allowing users to easily download and use the application.

Since the application runs locally and makes no network connections, there are no security concern. 

#Technologies
* Python
  * Bokeh
  * PyD3
  * matplotlib
  * NumPy/SciPy/SymPy
  * SimPy
  * PyWebkit
  * PyInstaller
* JavaScript
  * D3.js

All of these libraries are open source and have licenses which permit me to use them.

#Other Information
## People Involved
* Mike Andrews (Microsoft)
* Dondi

#Preliminary Development Schedule
## Milestones
1. Get all the moving parts working together, SimPy, Bokkeh or D3, PyWebkit, etc. Use sample data for this.
2. Develop a simplistic model and simulation that doesn't take into account additional constraints. Figure out visualization
3. Develop more complex models and simulations that allow constraints.
4. Provide a graphical tool for designing models for simulation.
5. Automatically optimize the model

Timeline:

1. 2nd week
2. 4th week
3. 8th week
4. 10th week
5. Time left

# Questions?
