library(tidyverse)
library(readxl)

survey_26 <- read_excel("data/(붙임) 경기도청 챗GPT 직원직무 교육신청 명단(취합).xlsx", sheet = '4.26.(수)', skip =2) %>%
  mutate(날짜 = "2023-04-26")
survey_27 <- read_excel("data/(붙임) 경기도청 챗GPT 직원직무 교육신청 명단(취합).xlsx", sheet = '4.27.(목)', skip =2) %>%
  mutate(날짜 = "2023-04-27")
survey_28 <- read_excel("data/(붙임) 경기도청 챗GPT 직원직무 교육신청 명단(취합).xlsx", sheet = '4.28.(금)', skip =2) %>%
  mutate(날짜 = "2023-04-28")

survey <- bind_rows(survey_26, survey_27) %>%
  bind_rows(survey_28) %>%
  janitor::clean_names(ascii = FALSE) %>%
  set_names(c("연번", "실국", "소속", "직위", "성명", "프롬프트", "API", "성취목표", "날짜")) %>%
  mutate(실국 = ifelse(is.na(실국), "직속", 실국))


student_26 <- survey %>%
  filter(날짜 == "2023-04-26") %>%
  pull(성명)

student_27 <- survey %>%
  filter(날짜 == "2023-04-27") %>%
  pull(성명)

student_28 <- survey %>%
  filter(날짜 == "2023-04-28") %>%
  pull(성명)

assign_team <- function(students) {
  # 무작위로 섞어 줍니다.
  students_shuffled <- sample(students)

  # 6개 팀으로 나눕니다.
  teams <- split(students_shuffled, ceiling(seq_along(students_shuffled)/4))

  # 결과를 출력합니다.
  return(teams)
}

assign_team(student_26)

assign_team(student_27)

assign_team(student_28)
