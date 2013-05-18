# Async Consumer

Often an application will need to retrieve data from a third-party service, 
and transform that data so it conforms to a reliable structure. This is usually 
straightforward, however services are not always responsive, and, depending on the 
data, processing it can start to be expensive. For these reasons it's often 
helpful to consume third-party data using a standalone service (as opposed to 
the core application responsible for responding to client requests). 

Hence this project.

This leverages an actor model based on [gevent](https://github.com/surfly/gevent) 
to allow a number of consumers retrieve and process data asynchronously. 

* Note that you'll need libev in order for gevent to install successfully.

* On Linx: apt-get install libev-dev
* On Mac: brew install libevent
