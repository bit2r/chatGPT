# http://hbiostat.org/rflow

# 0. 패키지 ------------------------------------------------------------------

library(tidyverse)
library(Hmisc)
library(qreport)
library(palmerpenguins)
library(sparkline)

options(prType='html')
des <- describe(mtcars)
print(des, 'continuous')
