## FROZEN LAKE

### Documentation:  
[Frozen Lake Environment Documentation](https://www.gymlibrary.dev/environments/toy_text/frozen_lake/)

### Frozen Lake Environment Overview

#### Observation Space:  

Consider a 4x4 grid for discussion purpose:  

<img src="https://github.com/user-attachments/assets/a8b10a1c-c9c2-4eac-9825-89a005c17324" alt="image" width="300" height="300">  

  
- **Observation space = Discrete(16)**  
- Each state is represented by a number ranging from 0 to 15.  
- A custom map can be defined, with each state labeled as S (Start), F (Frozen), H (Hole), or G (Goal).  
- In the default map, S is at 0 and G is at 15.

**For a general n x n grid:**  
State representation = `current_row * nrows + current_col`  
(Where rows and columns start from zero)

#### Action Space:  
The agent can take one of four possible actions:  
<!--- **0:** Left  
- **1:** Down  
- **2:** Right  
- **3:** Up  -->
| Value | Action     |
|-------|----------- |
| 0     | Turn Left  |
| 1     | Turn Down  |
| 2     | Turn Right |
| 3     | Turn Up    |
#### Rewards:  
- **1 :**  On Reaching the goal  
- **0 :**  Otherwise  
