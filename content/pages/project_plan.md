Title: Project Plan
Date: 2016-1-21
Authors: Alex Schneider
Summary: Plan for the project

# High level Plan
Build a model and simulator for deployment rollout to many machines

Rollout occurs in two stages

1. Deployment to subset of total machines
2. Health checks which pauses the rollout to check for errors and build confidence in the deployment (potentially stopping or rolling back deployment)

Create a model that describes constraints and estimates total rollout time after plugging numbers into the model. Create a simulation that runs the model to get an idea of how it happens and visualize it.

# Model
The model will have to take into account several features, including:

* Constraints, e.g.:
  * Only 50% of the capacity can be upgraded at any one time
  * Certain parts of the domain can't be deployed at the same time
* Health checks
* Parallel deployment
* What sort of language should we use for models? Create a DSL?

# Simulation

* Failures
* Visualization (what sorts of things to visualize? Domains that are rolled out as they roll out? Failure rate? etc?)

#Data structure

Number of regions

number of data centers

clusters for given service

Set of racks

Servers

Upgrade domain

#Rollout plan

when start: start in x region with these machines

Start with a cluster - wait for a certain amount of time, I'm comfortable with the performance and that there are no bugs.

As confidence builds, parallelize (go to 2 clusters rather than 1 cluster)

I'm confident that we don't have any bugs and roll out into more regions


# Simulator

Probability that I'm going to find a bug (i.e. 0.2% probability at the first cluster, and a probability of 0.1% at the 2nd or 3rd cluster)

Build a graph from the nodes, connections, rollout plans - what's the probabilit that we'll hit a bug - how does the simulation let you find the bug best

What number of deployments will find bugs early, middle or late - find the bugs earlier while keeping the deployment going as fast as possible - what is the sweet spoil
