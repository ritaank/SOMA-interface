## for SOMA
- clean up SOMA process TODOs
  - what does OC_05_G_03_real_000_synt_100 mean?
  - change cwd as needed
- set up soma-root so there is a template default set of mocaps which we can label and compare fiat labels to
- add bit about Mokka to visualize since normal visualization tools cannot process the c3d
- add a bit/script to move the files into the right place for mosh
  - or maybe we can automatically have the files save in the right place?
- find a way to log less info?
- test all the way through

## for MoSH
- what if our mocap is already labeled?
  - write a process to use exc3d to use a key to convert the label names to the ones used by the SuperSet
  - do the names even need to be converted? ie. does MoSH actually care about the names of each point? or does it just care about the continuity?
  - read the mosh paper / look thru the github fork to see if we can find the example of the guy who was adding keys
- can we re-verify that mosh manual goes down the same way as run_soma_on_multiple_settings?
- superset running on subset does have some degradation. for some of our labelling tasks, is there a model trained with less total points, that is still a superset of our training markerlayout? (we don't want to lose data, but we also want to limit the amount of ghost points that SOMA has to deal with)
  
## In general
- finish reading the soma paper
- likewise for mosh paper
- can we use parallel tools in python to parallelize the func(job) for loop that happens in parallel tools?
- can we use Numba to speed things up? do some tests on this?