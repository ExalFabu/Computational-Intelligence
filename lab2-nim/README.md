# Lab 2: Nim - ES
## Description
This lab requested us to build an evolutionary-based agent able to play a Nim game.  
We started by defining a (*expert*) rule-based agent, which was able to play the game with a certain level of success.
We then tried (really hard) to come up with an evolutionary-based agent and we came up with the following parameters to be trained:
 - **Phase Thresholds**: the thresholds for the phases of the game (early, mid, late)  
      We measure the phase of the game by the number of theoretical moves left to end the game over the total number of moves (it thus depends on both size of the board and k-limit): $p\in [0,1]$  
      The thresholds are thus $t_{1}, t_{2} \in [0,1]$ and the phase is defined as follows:  
      - Late phase: $t_{2} < p\ < 1$
      - Mid  phase: $t_{1} < p \leq t_{2}$
      - Early phase: $0 \leq\ p \leq t_{1}$
 - **Strategy Probabilities**: the probabilities of the strategies to be used in each phase, the strategies he can use are: [expert, pure_random, gabriele, optimal]  
  *Note*: We initially thought of saving this as probabilities (thus summing up to 1 for each phase), but the results were not satisfactory (due to the fact that we were often applying softmax, who would *flatten* them up to $1/n$), so we decided to save them as weights, and then normalize them (w/ softmax) when picking the strategy to use.   
  *TL;DR*: these values do not represents probabilities, but weights.  
  *Example*: 
    ```python
    [[0.7, 0.2, 0.0, 0.1], # early phase  
     [0.7, 0.4, 0.01, 0.0], # mid phase  
     [0.7, 0.1, 0.1, 0.1]]  # late phase  
    ```
   
Each Individual, for every Nim board, will have a probability to use each strategy (depending on the phase the board is), and the strategy that will be played will be picked with the aforementioned probabilities.

The fitness of an individual is the average of the accuracy of the games played against the *expert* rule-based agent.

A good Individual will be able to play the game with a high accuracy, and will be able to adapt to different board sizes and k-limits.
We believe that the Individual should converge to be playing always the *expert* strategy, thus achieving a fitness of 50%, and a fitness above that would mean that the Individual is better than the *expert*.

## Collaborations
- I worked with (Davide Vitabile - S330509)[https://github.com/Vitabile] and (Davide Sferrazza - S326619)[https://github.com/FarInHeight], used their rule-based agent (tried to implement a rule for the k-limit variant, with not much success) and we developed the evolutionary agent together.

## Sources
- [Nim Game](https://en.wikipedia.org/wiki/Nim)
- [How to Win at Nim](https://www.archimedes-lab.org/How_to_Solve/Win_at_Nim.html)