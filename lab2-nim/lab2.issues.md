# Alexandro Buffa - S316999 - Lab 2 Reviews 
This is a collection of the Peer Review I've done for the Lab 2 of the Computational Intelligence course at Politecnico di Torino.

![Let's do this](https://media4.giphy.com/media/BpGWitbFZflfSUYuZ9/giphy.gif)

## Review 1 [(Open on Github)](https://github.com/vinz321/computational_intelligence_23_24/issues/2)
Issued to [Vincenzo Micciché - s316900](https://github.com/vinz321/computational_intelligence_23_24/blob/2a266ebdb14b920f9d5b60547b9dfe9f2c4c1a64/lab2-nim.ipynb), a friend of mine whom i have not worked with in this lab.

### Considerations
Hi Vinz 😊
I'll start off by complimenting you with how the code is well written and pretty straight forward, also nice approach with the `vinzgorithm` rule-based strategy.
I also have nothing to say about the Evolution-Strategy approach, if I had to name something I would say that you are training the individuals by playing always on the same side, with the same board size and with the same number of matches. This is not a problem per se, but it might be interesting to see how the individuals perform in different scenarios.  

I do have found though a couple of hiccups regarding the implementation, which I'll explain in the next section.

#### Problems with the implementation
- An oversight on the `tweak` function of the invidivual caused the program to never save the fitness value of the individual. This caused the program to always select the first individual as the best one.  
  ![Oopsie](https://media2.giphy.com/media/cE9GVwn2mJwoSvScrI/giphy.gif)
- Another problem I observed (because I've done the same mistake) is caused by applying softmax every time a new individual is created. This causes the probabilities to converge to $1/n$ where $n$ is the number of strategies used, e.g.
  ```python
  softmax(softmax(softmax(softmax(softmax([0.8, 0.1, 0.1])))))=array([0.33553626, 0.33223187, 0.33223187])
  ```
  I encountered the same problem in my implementation and I solved it by applying softmax only when the probabilities are used to select a strategy. Another approach would be to use a different normalization function, like dividing by their sum.

I ran your code with a combination of the above problem fixed and I got the following results:
- Results with nothing fixed, as a baseline (after only 50 epochs):
    ```python
    individual3.vec=array([0.24987535, 0.25108963, 0.25034635, 0.24868867]), mean=0.25, std=0.00087 # Caused by softmax
    individual3.fitness_value=0 # Caused by oversight
    evaluation=40.000%
    [('vinzgorithm', 0.2510896342022743),
    ('optimal', 0.2503463466419632),
    ('pure_random', 0.24987534537561654),
    ('gabriele', 0.24868867378014592)]
    ```

- Results with the oversight fixed (50 epochs):
   ```python
   individual3.vec=array([0.25074403, 0.25004322, 0.24976212, 0.24945063]), mean=0.25, std=0.00048 # Caused by softmax
    individual3.fitness_value=0.52 # Oversight fixed
    evaluation=39.000%
    [('pure_random', 0.2507440276099417),
    ('vinzgorithm', 0.2500432178488247),
    ('optimal', 0.24976211973159504),
    ('gabriele', 0.24945063480963853)]
   ```

- Results with oversight and softmax fixed (50 epochs):
    ```python
    individual3.vec=array([0.91646977, 1.81028982, 0.9667728 , 0.82709137]), mean=1.130155942697836, std=0.39585 # Fixed removing softmax
    individual3.fitness_value=0.6
    evaluation=40.000%
    # strategy name, softmax(vec)
    [('vinzgorithm', 0.4517941354717714), 
    ('optimal', 0.1943595129269683),
    ('pure_random', 0.1848244714173517),
    ('gabriele', 0.16902188018390876)]
    ```

Overall it seems that with the right amount of epochs and sigma it kind of converges to vinzgorithm, which is what we expect!  
![Bye bye](https://media4.giphy.com/media/p6P5KdqRljCrVoZj79/giphy.gif)

## Review 2 [(Open on Github)](https://github.com/AngeloIannielli/polito-computational-intelligence-23/issues/2)

Issued to [Angelo Iannelli - s317887](https://github.com/AngeloIannielli/polito-computational-intelligence-23/blob/a4dbb254077fdfd85c50b0e84765439962104c95/Lab2/Lab2.ipynb), picked random from the excel with random.org 😊.


### Considerations
Hi Angelo 😊, you've been picked randomly from random.org for my peer review, hope it will bring something useful to you!  
Your code is very well structured, well commented and very straight-forward to read and understand.
I also liked your approach on trying to find new strategies to compete against the `optimal` strategy, and thanks to your graphs it's easy to see that your results look promising.  

The only thing left for me to add is that you are using a $1+\lambda$ approach (instead of the $1,\lambda$ noted above the code), since you are appending the parent to the offspring and then picking the best individual (which could be the parent of the previous generation). This is not a problem per se, but it might be interesting to see how the results change with a $1,\lambda$ approach.  
Another twist that could spice things up is to try and train the individuals by playing different versions of the game (different sizes, with/without $k$-max pieces nimmable) and by playing different sides (first/second player).  
That said, I think you did a great job with this lab!  
![Bye bye](https://media2.giphy.com/media/ziWDuOipMj0BMrI540/giphy.gif)