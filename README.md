## My_first_robot

Control SW for wheeled mobile robot based on ROS2 Architecture.

## goals

- Create control SW for movement, preception and control based on sensor fusion (first iteration camera, sonar sensor,
  lidar and maybe radar will follow)
- simultanously create a digital twin of HW, on which the SW will be tested in virutal environment

## Install

''' Bash
python -m venv .venv_bot
source .venv_bot/bin/activate

pip install -r Requirements.txt
'''

## Run

'''Bash
python main.py
'''

## Project structure

```my_first_robot
├── data/
├── docs/
├── src/
├── tests/
├── requirements.txt
├── README.md
└── main.py
```
## Safety architecture

#Fail-safe method

If secure movement is not assured, robot has to proceed to safer state:

- robot will use simple state machine with three basic states
	- STOPPED - motors of robot are disabled and motion is forbidden
	- EMERGENCY - same as STOPPED  + robot has to be restarted to go to STOPPED state (EMERGENCY → reset() → STOPPED → start() → RUNNING). 
	  Robot is not allowed to go to RUNNING state directly from EMERGENCY state.
	- RUNNING - engines are enabled, robot can move. Only possible from STOPPED state

- sensor error or fail value must not be interpreted as "go". in case of failed value, robot state is changed to EMERGENCY

# Speed limiter

- function calculate_speed(distance) defines safe speed based on distance from obstacle


# Safety invariant

state != RUNNING -> motors stopped

motors must not be enabled in any other state, than RUNNING

EMERGENCY stata has higher priority in architecture, than movement commands
