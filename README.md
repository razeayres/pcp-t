# pcp-t - precipitation tester for SWAT models
###### *Rodrigo de Queiroga Miranda*

###### Contact: rodrigo.qmiranda@gmail.com

### About
pcp-t is a recursive selector for SWAT rainfall stations. It removes stations from the pcp files, run the SWAT model, and validate results with observed data. The process is repeated unitl the best combination of rainfall stations is reached. The scripts were developed for the interpreter Python 3.6.9.

### Package usage

A new interface is being developed, however it can be already used by modyfing this [line](https://github.com/razeayres/pcp-t/blob/a6fdfacd2db9e6ddab7c9336af182f63299d9790/main.py#L10) in the [main.py](https://github.com/razeayres/pcp-t/blob/master/main.py).
