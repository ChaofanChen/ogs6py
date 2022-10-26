# Changelog

All notable changes to **ogs6py** will be documented in this file.


## [0.370]

### Changes
* replacement method can be used together with writing files from scratch
* added direct setter for frqeuently used signle value properties
* added restart method

## [0.36]

### Changes
* minor bugfixes


## [0.35]

### Changes
* major update of the logfile parser which is now based on record
* script added for optimizing coupling parameter for staggered scheme
* added method for surface flux and robin BC

## [0.34]

### Changes
* Switch to turn off logging

## [0.33]

### Changes
* parse input if input is given (allows for execution of given file if no replace function is called)
* logparser can now output from staggered scheme
* OGS executables from a singularity container are now supported as well
* add argument for general wrapper for ogs

## [0.32]

### Changes
* added some tests for replace method
* add logfile parsing capabilities for output produced by PETSc
* add replace mesh function
* add compose from CSV tool
* add file include finction to outsource xmldata

### Bugfixes
* media are also recogniced if the id attribute is missing
* fix in log parser to recognise times in scientific format

## [0.31]

### Changes
* ogs6py uses now PEP8 naming convention for all ogs6py methods (lowercase with underscore separation)

### Bugfixes

### Additions

