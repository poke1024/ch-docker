#!/bin/Rscript

install.packages(
   c(
     'devtools', 
      'rlang',
      'uuid', 
      'digest', 
      'callr', 
      'tidyverse', 
      'dplyr',
      'devtools',
      'formatR', 
      'remotes', 
      'selectr', 
      'caTools', 
      'stringi', 
      'tidyverse', 
      'rlang'
     ),
     repos='http://cran.us.r-project.org' 
     )

 install.packages(
     c(
       'curl',
       'openssl',
       'git2r',
       'httr',
       'gh',
       'usethis',
       'devtools',
       'shiny'
       ),
       repos='http://cran.us.r-project.org' 
       )

devtools::install_github("IRkernel/IRkernel")
IRkernel::installspec(user = FALSE)
