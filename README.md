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

![Image Caption](./markdown%20images/reshuffle%20summary.png)
</br></br>
### DQN(Deep Q-Network) is applied to steel stockyard reshuffling problem

![Image Caption](./markdown%20images/RL%20reshuffling.png)
</br></br>

### State
1. For training the state of the steel stockyard is expressed in an array form and becomes the input data of the neural network
2. Number in each cells
   - 0: empty space, 1~3: release order
   - No priority with same release order
      - in case of release number 1, any one of 3 steels can be taken out first

![Image Caption](./markdown%20images/state%20sample.png)
</br></br>
### Terminal state

1. If release order in each stack is descending order from the top, than it's considered as terminal state
2. Various terminal state is possible as shown below
![](./markdown%20images/terminal%20state%20sample.png)
</br></br>
### Action
1. Action is moving steel from one stack to another
2. Impossible actions
   1. If there is no steel in stack, than withdrawl is impossible
   2. If stack has maximum number of steel, than stacking a steel is impossible
3. Solution
   1. The solution in steel reshuffling is reshuffling process
   2. Among solutions, the process of reshuffling by the minimum number of actions becomes optimal solution
![Image Caption](./markdown%20images/episode%20sample.png)
</br></br>
### Reward

1. The agent receive reward when it reaches the terminal state within a set number of actions
2. The agent receive penalty when the terminal state is not reached within a set number of actions
</br></br>
## Result








