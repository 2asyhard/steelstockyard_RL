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
</br>
<img src="https://user-images.githubusercontent.com/43307537/122550967-5327da00-d06f-11eb-9c2a-e5dab913a3bc.png">

</br></br>
### DQN(Deep Q-Network) is applied to steel stockyard reshuffling problem</br>

<img src="https://user-images.githubusercontent.com/43307537/122551129-8c604a00-d06f-11eb-8a8f-1a222beb38a0.png">

</br></br>

### State
1. For training the state of the steel stockyard is expressed in an array form and becomes the input data of the neural network
2. Number in each cells
   - 0: empty space, 1~3: release order
   - No priority with same release order
      - in case of release number 1, any one of 3 steels can be taken out first
</br>
<img src="https://user-images.githubusercontent.com/43307537/122551241-ad289f80-d06f-11eb-9067-504baf5fefc1.png">
</br></br>

### Terminal state

1. If release order in each stack is descending order from the top, than it's considered as terminal state
2. Various terminal state is possible as shown below
</br>

<img src="https://user-images.githubusercontent.com/43307537/122551288-b9146180-d06f-11eb-8ea3-a15b34a35d40.png">
</br></br>

### Action
1. Action is moving steel from one stack to another
2. Impossible actions
   1. If there is no steel in stack, than withdrawl is impossible
   2. If stack has maximum number of steel, than stacking a steel is impossible
3. Solution
   1. The solution in steel reshuffling is reshuffling process
   2. Among solutions, the process of reshuffling by the minimum number of actions becomes optimal solution
</br>
<img src="https://user-images.githubusercontent.com/43307537/122551315-c598ba00-d06f-11eb-9881-3e449cc89611.png">
</br></br>

### Reward

- The agent receive reward when it reaches the terminal state within a set number of actions

</br></br>

---

## Problem with applying Reinforcement Learning

### Sparse reward
- Terminal states ratio gets smaller when total number of states increases

|Total number of states|Terminal states ratio|
|----------------------|---------------------|
|200|0.275|
|900|0.147|
|1800|0.115|
|3600|0.09|
|7200|0.071|
<br/>
- An example of an environment with 200 states

|0|0|0|
|---|---|---|
|1|1|1|
|2|2|2|

- An example of an environment with 7200 states

|0|0|0|
|---|---|---|
|1|2|3|
|4|5|6|
<br/>

- When the total number of states increases, the proportion of terminal states decreases

- Therefore, it is expected that the ratio of terminal states will be very small in an environment where the total number of states is larger

- For this reason, a sparse reward problem arises in which rewards are not received in a complex environment




