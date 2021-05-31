# Appling Reinforcement Learning to steel stockyard reshuffling problem in ship building company

### steel stockyards steel storage and release process

1. Warehousing steel plate
   - Steel is ordered from various steel mills and received randomly without special rules
2. Piling steel plate
   - It is piled in the stockyard in order as it is received regardless of the process(cutting) schedule of the steel
3. Steel cutting schedule confirmed
4. Reshuffle steel plate 
   - Need to reshuffle the randomly stacked steel for fast release
   - If the steel that should be released out first is underneath, change the stacking order by using a crane, etc
   - In this Code, Reinforcement Learning is applied to reshuffling operations
5. Release steel plate

![Reshuffle summary](https://user-images.githubusercontent.com/43307537/120211724-3700fc00-c26c-11eb-8a39-910c029a4247.png){: width="100%" height="100%"}
</br></br>
### DQN(Deep Q-Network) is applied to steel stockyard reshuffling problem

![RL reshuffling](https://user-images.githubusercontent.com/43307537/120211837-5009ad00-c26c-11eb-8dff-104aaec46d75.png){: width="100%" height="100%"}

</br></br>

### State
1. For training the state of the steel stockyard is expressed in an array form and becomes the input data of the neural network
2. Number in each cells
   - 0: empty space, 1~3: release order
   - No priority with same release order
      - in case of release number 1, any one of 3 steels can be taken out first

![state sample](https://user-images.githubusercontent.com/43307537/120211893-5b5cd880-c26c-11eb-9d5c-4d691d1904eb.png){: width="70%" height="70%"}
</br></br>
### Terminal state

1. If release order in each stack is descending order from the top, than it's considered as terminal state
2. Various terminal state is possible as shown below
![terminal state sample](https://user-images.githubusercontent.com/43307537/120211943-644daa00-c26c-11eb-9b0e-53dabe1963b3.png){: width="80%" height="80%"}
</br></br>
### Action
1. Action is moving steel from one stack to another
2. Impossible actions
   1. If there is no steel in stack, than withdrawl is impossible
   2. If stack has maximum number of steel, than stacking a steel is impossible
3. Solution
   1. The solution in steel reshuffling is reshuffling process
   2. Among solutions, the process of reshuffling by the minimum number of actions becomes optimal solution
![episode sample](https://user-images.githubusercontent.com/43307537/120211975-6b74b800-c26c-11eb-8d97-207176585920.png){: width="100%" height="100%"}
</br></br>
### Reward

1. The agent receive reward when it reaches the terminal state within a set number of actions
2. The agent receive penalty when the terminal state is not reached within a set number of actions
</br></br>
## Result








