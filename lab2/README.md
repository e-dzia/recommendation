# Lab2 - Advanced problems of recommendation systems

Our implementation includes clustering recommendation and sequential approaches 
based on personalized Markov chains, association rules, RNN and prod2vec. 

## Theory

### Partitioning / hierarchical clustering

- main idea: 
    - dispose items between clusters, 
    - assign new item to the one of existing clusters
    - recommend item based on user items in clusters
- not used as autonomic system but rather as its part
- low computational complexity 

Worth reading: [link](https://towardsdatascience.com/build-your-own-clustering-based-recommendation-engine-in-15-minutes-bdddd591d394)

### Association rules

- uses association between items
- frequent item sets
- works only with well thought rules
- can be created f. e. on base of user basket or activity during one session

Worth reading: [link](https://towardsdatascience.com/association-rules-2-aa9a77241654)

### Complexity of user actions

- general positive relationship between viewing time of an item or item description and preference for (propensity to consume) that item
- 90% of the data behaviors are implicit feedback which are much more important but complicated

Worth reading: [Using Viewing Time to Infer User Preference in Recommender Systems](https://pdfs.semanticscholar.org/e100/b0a6d20db67b5b89be0944a776bf17b15209.pdf)

### Sequence-aware systems

- frequently based on implicit evaluation
- subcategory of context-aware recommender systems
- implementation depends on what is recommended
- not equal to time-aware recommender systems

Worth reading: [Sequence-Aware Recommender Systems](https://arxiv.org/pdf/1802.08452.pdf)

### Embedding

- based on word2vec
- items instead of words
- can be applied to sequences as well as sets
- ex. item2vec, prod2vec

Worth reading: [item2vec](https://arxiv.org/vc/arxiv/papers/1603/1603.04259v2.pdf)

### Deep learning

- possibility to find non-linear dependencies
- reduces the efforts in hand-craft feature design
- heterogeneous content information: text, images, audio, etc.
- RNN -> sequential pattern mining
- a lot of tools and libraries to implement
- many different types used

Worth reading: [link](https://towardsdatascience.com/recommendation-system-series-part-2-the-10-categories-of-deep-recommendation-systems-that-189d60287b58)

### Context-aware recommendation

- takes context into consideration, f. e.:
    - season while buying clothes
    - company while choosing a movie
    - mood while listening to music
- context - information that describes event/situation/environment
- context acquisition: explicitly, implicitly, inferring
- types: pre-filtering, post-filtering, contextual modelling

Worth reading: [Context based Recommendation Methods: A Brief Review](https://research.ijcaonline.org/icke2016/number1/icke2016008.pdf)

## Implementation

### Dataset

**30Music** - sequences of songs listened by users
- Number of songs: 1000
- Number of users: 4165
- Number of sessions: 6766 (4-5 songs average, 1-13 sessions per user)
- Other data about: artists, albums, tags 

### Evaluation

- Precision
- Recall
- MRR - Mean Reciprocal Rank
- Calinski-Harabasz (clustering)
- Davies-Bouldin (clustering)

### Methods

#### Sequential

- FPMC - personalized Markov chains for next-basket recommendation
- FSC - association rules 
- RNN with GRU 
- prod2vec

#### Clustering

- K-means

## Summary

- clustering can be used as a part of larger systems for pre-processing to cut computational complexity, not effective as autonomous system
- sequence-awareness is very important in recommendation
- prod2vec is worth using - good results
- measures seem low, but they describe the ability to predict the next specific song - perhaps another song (or songs in a different order) would also please the user
