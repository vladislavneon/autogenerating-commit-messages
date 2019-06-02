# Autogenerating commit messages

## Motivation

Every developer makes many commits and often these commits are for some not really interesting or for some repeated work. Also, 
there are a lot of devs in the world for whom English is not native. We want to help people in all these cases by developing a 
model for autogenerating commit messages using commit diffs.

## Previous work

The approach using neural machine translation is described in paper of Siyuan Jiang, Ameer Armaly and Collin McMillan: 
https://arxiv.org/abs/1708.09492

They reported that their method reaches a BLEU-4 score about 32, which is considered good on the first sight.

However, in 2018 Zhongxin Liu, Xin Xia, Ahmed E. Hassan, David Lo, Zhenchang Xing, and Xinyu Wang investigated
(https://doi.org/10.1145/3238147.3238190) reasons of such 
good performance of NMT model and concluded that one can obtain similar results using really simple methods like kNN. They proposed 
new method called NNGen, which performed better than NMT on the same dataset resulting in score about 38. Moreover, NNGen was 
many times faster and didn't take time for training.

Also, authors cleaned original dataset from trivial messages which resulted in decreasing score of both methods to about 16.

## Reproduction

After reproduction we approved these results on given dataset. Next we wanted to apply this approach to our data, which was exactly 
Intellij community repository (https://github.com/JetBrains/intellij-community). And that is where we had to stop and think a lot.
On our data approach took score of only 4, which is really low. After some investigation we found out that original data cannot be
considered good at all. The biggest issue is data shuffling by time - in real world we want to learn from past and predict future, 
however, messages for train dataset were chosen randomly in NMT dataset.

## Research of applicability

When we retained only short messages from our data, we could increase score to 9, which was significantly higher, but we still wasn't
satisfied. We decided to solve a simpler problem. Now we wanted to predict a commit tag. 

After small changes, the same approach could solve this problem quite good. We aimed to minimize I type error, and could reach
accuracy of 0.7, and did just 0.03 of totally wrong predictions.
