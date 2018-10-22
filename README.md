# Implementation of Bittorent-like algorithem Using UDP with Reliability and Congestion Control

## Introduction
BitTorrent, one of the most widespread file sharing P2P applications, has recently been updated to eliminate use of TCP by introducing an application-level congestion control protocol. 
This new protocol aims to efficiently use the available link capacity while avoiding interference with other user traffic (e.g., Web, VoIP, and gaming) sharing the same access link.
In this project, we are aimed to simulate this protocal in a virtual network environment. Because of the high complexity of Bittorrent, we decide not to fully implement the algorithm; instead,
we decide to implement a Bittorrent-like protocol to demonstrate its functionality. 

## Implementation and Methods
A virtual network condition will be created and all the network information will be stored inside a configuration file. The configuration file is available at <a href="https://github.com/NIICKK/CongestionControl/blob/master/config.yml"> config.yaml </a>. The protocal will sense the network condition by accessing the configuration file.
A mutex-like mechanism will be used in case multiple processes access this file at the same time and try to modify it. 

Rather than use the AIMD method adopted in TCP, we plan to fully use the network capacity at the beginning and adjust it when more network loads are expected.


## Performance

## Conclusion

## Reference  
