
# 거대언어모형 ------------------------------------------------------------------

# 거대언어모형(LLM) - A Survey of Large Language Models

# 00. packages ------------------------------------------------------------
library(tidyverse)
library(docxtractr)
library(readxl)
library(janitor)
library(ggrepel)
extrafont::loadfonts()

# 01. dataset -------------------------------------------------------------

raw_data <- read_excel("data/LLMs.xlsx")


# 02. data munging --------------------------------------------------------

llm_tbl <- raw_data %>%
  janitor::clean_names() %>%
  slice(2:n()) %>%
  select(type, model, release, size) %>%
  mutate(출시월 = excel_numeric_to_date(as.numeric(as.character(release)), date_system = "modern") + 14 ) %>%
  mutate(구분 = if_else(str_detect(type, "Open"), "공개", "비공개")) %>%
  mutate(모형 = str_remove(model, "\\[\\d+\\]") %>% str_trim) %>%
  mutate(크기 = parse_number(size)*10) %>%
  select(matches("[가-힣]"))

# 03. visualization -------------------------------------------------------

llm_g <- llm_tbl %>%
  ggplot(aes(x = 출시월, y = 크기, color = 구분)) +
    geom_point() +
    geom_text_repel(aes(label = 모형), show_guide = F) +
    scale_y_continuous(label = scales::comma) +
    # scale_y_log10(label = scales::comma) +
    theme_bw(base_family = "NanumBarunpen") +
    theme(legend.position = "top") +
    labs(x = "",
         y = "모형크기 (억)",
         title = "(패러미터 수가 10억 이상) 거대언어모형 추세",
         subtitle = "GPT-4는 모형크기가 비공개로 제외됨") +
    scale_color_manual(values = c("공개" = "blue", "비공개" = "red"))


# ragg always works for mac
ragg::agg_png("images/llm_g.png", width = 297,
              height = 210,
              units = "mm", res = 300)
llm_g
dev.off()




# 04. table -------------------------------------------------------

llm_tbl %>%
  filter(str_detect(모형, "GPT"))

