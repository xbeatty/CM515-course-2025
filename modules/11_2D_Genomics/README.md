# Module 11 2D Genomics

## Introduction

Methods for analyzing and visualizing next-generation sequencing experiments (such as DNA-seq, RNA-seq) require High Performance Computing (HPC), which requires linux, and often involve the suite of programs provided by deeptools.


## What we're doing this week

- Monday
    - Overview of HPC, getting started on Alpine Web Interface
    - Review command line and linux from previous modules
    - Run setup code on Alpine using Jupyter BASH notebooks 
       - Troubleshoot if necessary

- Wednesday
    - Sarah Swygert: Deeptools analysis and Exercises

---


## Background 

[Why biologists need high performance computing (HPC) (video)](https://youtu.be/eQ660XXG9MI?si=taE-LA_GYI7DF5ue)


## Alpine Overview (from DSCI510)

**Supercomputers** in the crudest terms are basically what happens if
you glued 100\'s or 1000\'s of individual computers together. You end up
making a giant computer with more functionality.

The supercomputer we\'ll be using is **ALPINE** and it lives on CU
Boulder campus. ALPINE is a joint venture between Colorado State
University and CU Boulder and is sponsored by those institutes and by a
grant from the National Science Foundation. **ALPINE** is shared between
CU Boulder, Colorado State University, CU Anschutz, and RMACC (Rocky
Mountain Advanced Computing Consortium, a network of \>20 other academic
institutions in Colorado, Arizona, Idaho, Montana, and New Mexico).

There is a list of the [Top 500 biggest
supercomputers](https://www.top500.org/lists/top500/list/2023/06/) on
the planet (as of June 2023). According to this list, the largest
supercomputer is **FRONTIER** located at Oak Ridge National Labs in
Tennessee and run by the DOE (US Department of Energy).

How do these supercomputer systems compare to our laptops?


  |**Typical laptop**                 | **Alpine Supercomputer**  |  **FRONTIER Supercomputer**|
  |-----------------------------------|---------------------------|---------------------------|
  |0.1 - 10 teraFLOPS                 |450 teraFLOPS              |1,102,000 teraFLOPS        |
  |1 - 4 cores organized onto 1 node  |>15,500 cores on 458 nodes |    8,730,112 cores        |
  

-   FLOPS: a measure of how many floating point operations a computer
    can do per second. So it\'s a measure of calculations a second
-   Node: Like a miniature computer within the cluster
-   Core: Independent processing unit on a CPU (central processing unit)

**A *cluster* of nodes**

<figure>
    <img src="setup/img/cluster.png" alt="cluster diagram" width="534" height="395">
    <figcaption>https://www.hpc2n.umu.se/documentation/guides/beginner-guide</figcaption>
</figure>

Within each node is the set of resources- CPUs, memory, motherboard, cooling system.

**A compute node (blade)**

<figure>
    <img src="setup/img/ACTblade-side.png" alt="Compute node (blade)">
    <figcaption>ACT blade from https://www.advancedclustering.com</figcaption>
</figure>

------------------------------------------------------------------------

### What are the benefits and drawbacks of using a supercomputer?

**Benefits**

-   power, efficiency, and speed!!!
-   team of professionals to help set up the system and provide user
    support
-   allows for collaboration with other users

**Drawbacks**

-   There is a learning curve
-   Multi-user platform requires job-sharing - there is usually a queue
    to execute your code
-   May not have architecture specialized for your task.


### Video: Logging on to Alpine Web Interface

[CU Research computing (video) - logging on with Open OnDemand](https://www.youtube.com/watch?v=cP6lfRWywk0)

<img src="setup/img/exclaim.svg" height="17px" width="17px"> **EXERCISE**: Let\'s connect to ALPINE using OnDemand but with changes for CSU:

-   Navigate to [https://ondemand-rmacc.rc.colorado.edu](https://ondemand-rmacc.rc.colorado.edu) in a new tab
    or window
    -   For me, I right click on the above link and select **Open Linkin New Window**
    -   You will be asked to select an identity provider using a
        pull-down menu. Select on the pull-down menu (it may say
        **ORCID**). Start typing **Colorado State University**. Click on
        **Remember** and log in. It should look like this

![](setup/img/screen_shot_2023-08-28_at_12.37.17_pm.png)


### Video: Alpine File Organization

[CU Research computing (video) - File system](https://www.youtube.com/watch?v=xfeRDnZQrJ4&t=18s)


---

<img src="setup/img/exclaim.svg" height="17px" width="17px"> **EXERCISE**: Using the file navigator, browse to the files we cloned from the class repository.

Using the *Files* pull down menu, go to your /projects directory as below:

<figure>
    <img src="setup/img/OnDemand-Files.png" width="461" height="198">
    <figcaption>Screen image caught mid-file navigation</figcaption>  
</figure>
<br>
<br>
<figure>
    <img src="setup/img/ondemand-repo-dirview.png" width="800" height="311">
    <figcaption>File browser showing <i>/projects/dcking@colostate.edu/CM515-course-2025</i></figcaption>
</figure>
<br>
<figure>
    <img src="setup/img/repo-09Deeptools-hover-setup.png" width="833" height="300">
    <figcaption>File browser showing <i>/projects/dcking@colostate.edu/CM515-course-2025/modules/09_Deeptools</i> hovering on <b><i>setup</i></b>
    </figcaption>
</figure>

### Time to run JupyterLab in a job

Jupyterlab is like RStudio- it is an integrated environment with many different tools, especially the ability to run Jupyter notebooks, which are in turn like RMarkdown. They are documents that can run embedded code.

#### Interactive Apps -> Servers -> Jupyter Session (Presets)

<img src="setup/img/InteractiveAppsHoverJupyter.png">

#### Jupyter launch page

<img src="setup/img/JupyterSessionLaunchScreen.png">

To continue: Hit Launch

- wait for job to start
- launch jupyterlab
- explore
- navigate to  modules / 11_2D_Genomics / setup
- open DEEPTOOLS-KERNEL.ipynb
- Run code cells.


