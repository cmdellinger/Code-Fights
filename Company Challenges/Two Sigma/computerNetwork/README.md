# computerNetwork
You know what they say: "time is money." In today's markets, the price of a stock that you see on your computer might not be the price that you end-up trading at, since by the time your request reaches the exchange the price might have changed. Therefore, the quicker you can get your order to the exchange, the better the chances that you will trade at your expected price.

Picture a peer-to-peer computer network of n nodes that's supposed to route your request from your computer to a computer where the trade is actually registered. Let's assume that the network is not optimized yet, so it's your task to implement an algorithm that computes the shortest path from the source at index 1 (your computer) to the destination at index n.

#### Example:
For `n = 4` and
```network = [[1, 4, 200],
            [1, 2, 5], 
            [1, 3, 10], 
            [2, 3, 4], 
            [2, 4, 150], 
            [3, 4, 100]]
```
the output should be
`computerNetwork(n, network) = 109`.

The shortest path is `1 -> 2 -> 3 -> 4`.
