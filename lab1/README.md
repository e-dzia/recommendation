# Lab1 - Simple recommender systems

Our simple implementation includes content-based filtering and collaborative filtering (SVD, KNN), as well as hybrid model.

### Collaborative filtering 

&#10004; No much data needed - only ratings (or some other measure)   
&#10004; There are a lot of different methods  
&#10004; User gets more diverse and personalized recommendations  
&#10007; Assumption that taste doesn't change  
&#10007; Much data needed (on the other hand &#128513;): user-item matrix can't be too sparse  
&#10007; *Cold-start* problem


### Content-based filtering 

&#10004; No *cold-start* problem - easy recommendation for new users   
&#10004; Works even for few users  
&#10007; Needs a lot of information about items  
&#10007; Isn't diverse  


### Hybrid model

&#10004; Combines advantages of both content-based filtering and collaborative filtering  
&#10007; Is usually more complicated 




## Implementation

Implementation uses benchmark MovieLens dataset - 100K ratings for about 700 users and 9000 movies 
([data can be found here](https://drive.google.com/drive/folders/1JnQXDCsGAb75I4PRRMDHUO0WxmXT-usv)).  

**Collaborative filtering**  
- SVD
- KNN (cosine similarity, euclidean distance)
- ratings counted based on similar users (Pearson correlation - script)

**Content-based filtering**
- budget
- popularity
- date
- duration
- average rating

**Hybrid method**
1. Content-based filtering
2. Collaborative filtering (SVD)


## Summary
- cosine similarity is better than euclidean distance
- hybrid model comes across as the best
