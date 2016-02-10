Title: Requirements
Date: 2016-1-18
Authors: Alex Schneider
Summary: Define deployment simulator requirements

#5 Requirements
## 5.1 Introduction
The project involves a model and simulator for a deployment to many (on the order of millions) of machines. Rolling out involves deployment to an increasingly larger subset of machines, with pauses between stages to see if errors occur, and if not, building confidence in the release before going forward or rolling back. The project will accurately describe constraints and estimate total rollout time based on certain variables such as the rollout time per domain, delay times, number of domains, and number of regions.
## 5.2 Functional Requirements
### 5.2.1 Graphical User interface

|   |   |
| ---:|:--- |
| 5.2.1.1 | The graphical user interface shall provide a widget to select the model to run the simulation on |
| 5.2.1.2 | The graphical user interface shall provide several configuration options to manipulate the simulation |
| 5.2.1.3 | The graphical user interface may provide an interface to build the models |
| 5.2.1.4 | The graphical user interface shall provide a manner in which to view the results in an intuitive fashion |

### 5.2.2 Model language
|   |   |
| ---:|:--- |
| 5.2.2.1 | The modeling language will allow the user to define the deployment model in clear, easily readable terms |
| 5.2.2.2 | The modeling language shall provide a manner in to define the deployment space down to the individual server, while preventing the need for tediously needing to define every single server |
| 5.2.2.3 | The modeling language shall allow the user to define a deployment strategy and specify the constraints under which the program must optimize |

### 5.2.3 Simulator
|   |   |
| ---:|:--- |
| 5.2.3.1 | The simulator shall take the metadata from the model and run deployment simulations on it |
| 5.2.3.2 | The simulator shall find the combination of variables that lead to the minimum combined risk and deployment time required |
| 5.2.3.3 | The simulator shall update the GUI with the progress and partial results of the simulation |

## 5.3 Performance Requirements
### 5.3.1 Simulator
|   |   |
| ---:|:--- |
| 5.3.1.1 | The simulator shall return the results within a reasonable timeframe (on the order of minutes) |

### 5.3.2 Graphical User Interface
|   |   |
| ---:|:--- |
| 5.3.2.1 | The graphical user interface shall not lock up and fail to respond in any phase of the application's runtime |
| 5.3.2.2 | The graphical user interface shall be fluid and usable even when simulations are ongoing |

## 5.4 Environment Requirement
### 5.4.1 Development Environment
#### 5.4.1.1 Hardware Requirements
|   |   |
| ---:|:--- |
| **Category** | **Requirement** |
| Computer | AMD64/x86_64 compatible computer |

#### 5.4.1.2 Software Requirements
|   |   |
| ---:|:--- |
| **Category** | **Requirement** |
| Runtime | Python 3.5+ |
| Operating System | Windows or Unix based |

### 5.4.2 Deployment Environment
#### 5.4.2.1 Hardware Requirements
|   |   |
| ---:|:--- |
| **Category** | **Requirement** |
| Computer | AMD64/x86_64 compatible computer |

#### 5.4.2.2 Software Requirements
|   |   |
| ---:|:--- |
| **Category** | **Requirement** |
| Runtime | Python 3.5+ |
| Operating System | One each of Windows, Mac, BSD, or GNU/Linux |
| Deployment Software | PyInstaller |

### 5.4.3 Production Requirements
#### 5.4.3.1 Hardware Requirements
|   |   |
| ---:|:--- |
| **Category** | **Requirement** |
| Computer | AMD64/x86_64 compatible computer |

#### 5.4.3.2 Software Requirements
|   |   |
| ---:|:--- |
| **Category** | **Requirement** |
| Operating System | Windows, Mac, BSD, or GNU/Linux |
