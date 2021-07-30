# HomeAutomation

Monitoring the temperature of the room and setting accordingly either heater or Ac

module_1

1.Generating the random value as temp sensor 

2.serialize the data

3.interfacing through the socket and transfer data to the slave periodically 

module_2

1.Receiving the data from module_1 deserialize the data

2.continously writing data to the file eg:-logfile with appropriate printing msg

3.serialize the data usually acts as interface b/w module_1 and module_3

4.which in turn transfer the data to the master module_3

module_3

1.Received data should be deserialize

2.filter out the unwanted data thus increases the throughput and speed

3.In case the master finds the sensor data not within the normal range 

  then it should send the connection request to slave where the master would request the slave to

  increase the throughput(reducing the amount of time) of its data so that the master becomes sure that the temperature 

  is not within the normal range and its time to alert(printing the msg) the maintenance and call appropiate function to get the work done

4.serailize the data and send to the server for further processing 

module_4

1.deserialize the data and writing the data to the files( when returning need to be int casting)which include all warnings and error

2.https://docs.python.org/3/library/logging.handlers.html#filehandler

3.plot the graph using matplotlib

